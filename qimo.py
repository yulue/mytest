import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 设置页面基本配置，包括标题、图标和布局
st.set_page_config(
    page_title="学生成绩分析和预测系统",  # 页面标题
    page_icon="🎓",                        # 页面图标
    layout="wide"                          # 宽布局
)

def load_all_data():
       # 加载学生原始数据
    df_student = pd.read_csv("student_data_adjusted_rounded.csv", encoding='utf-8-sig')
    # 重命名列名
    df_student.columns = ["学号", "性别", "专业", "每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率", "期末考试分数"]
    
    # 预处理：按专业分组
    df_prof_summary = df_student.groupby("专业").agg(
        每周平均学时=("每周学习时长（小时）", "mean"),          # 计算各专业每周平均学习时长
        期中考试平均分=("期中考试分数", "mean"),                # 计算各专业期中考试平均分
        期末考试平均分=("期末考试分数", "mean"),                # 计算各专业期末考试平均分
        平均上课出勤率=("上课出勤率", lambda x: round(x.mean() * 100, 2))  		# 出勤率转百分比并保留2位小数
    )
    
    # 统计各专业性别比例
    gender_count = df_student.groupby(["专业", "性别"]).size().unstack(fill_value=0)  	# 按专业+性别统计人数
    gender_count["总人数"] = gender_count.sum(axis=1)                                			# 计算各专业总人数
    gender_count["男性比例"] = round((gender_count.get("男", 0) / gender_count["总人数"]) * 100, 2)  # 男性比例
    gender_count["女性比例"] = round((gender_count.get("女", 0) / gender_count["总人数"]) * 100, 2)  # 女性比例
    gender_summary = gender_count[["男性比例", "女性比例"]].reset_index()            # 重置索引
    
    # 合并核心指标和性别比例数据，填充缺失值
    df_summary = df_prof_summary.merge(gender_summary, on="专业", how="left").fillna(0)
    
    # 加载成绩预测模型
    with open('student_score_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # 加载专业列表
    with open('majors_list.pkl', 'rb') as f:
        majors = pickle.load(f)
    
    # 返回所有加载的数据和模型
    return df_student, df_summary, model, majors

# 提前加载所有数据和模型
df_student, df_summary, model, majors = load_all_data()
# 获取模型训练时的特征名称
feature_names = model.feature_names_in_

#  侧边栏导航
with st.sidebar:
    st.title("🎯 功能导航")          # 侧边栏标题
    
    # 侧边栏单选框：实现三个页面的切换导航
    nav_option = st.radio(
        "选择功能模块",                # 单选框标题
        options=["项目介绍", "专业数据分析", "成绩预测"],  	# 三个页面选项
        index=0                        # 默认选中第一个页面（项目介绍）
    )
    st.sidebar.success("单击☝️所需功能模块")

   # 页面1：项目介绍
if nav_option == "项目介绍":
    st.title("🎓 学生成绩分析和预测系统")  # 页面主标题
    st.markdown("***")                     # 分隔线
    
    # 项目概述：分两列布局（文字+图片）
    c1, c2 = st.columns(2)  # 第一列宽度是第二列的2倍
    with c1:
        st.header("📋 项目概述")  # 二级标题
        st.markdown("""
        本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，
        帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。
        """)
        # 项目主要特点
        st.markdown('<h4>主要特点：</h4>', unsafe_allow_html=True)
        st.markdown("**📊 数据可视化：** 多维度展示学生学业数据")
        st.markdown("**🔍 专业分析：** 按专业分类的详细统计分析")
        st.markdown("**👀 智能预测：** 基于机器学习模型的成绩预测")
        st.markdown("**❗ 学习建议：** 根据预测结果提供个性化反馈")
    
    with c2:
        # 展示项目相关图片
        st.image(
            'img/1.png',
            use_container_width=True  	# 自适应列宽
        )
    
    st.markdown("***")  	# 分隔线
    
    # 项目目标：分三列布局
    st.header("🚀 项目目标")
    c3, c4, c5 = st.columns(3)  	# 三个列布局
    with c3:
        st.markdown('<h4>🎯 目标一：</h4>', unsafe_allow_html=True)
        st.markdown('''
            分析影响因素
            - 识别关键学习指标
            - 探索成绩相关因素
            - 提供数据支持决策
        ''')
    with c4:
        st.markdown('<h4>🎯 目标二：</h4>', unsafe_allow_html=True)
        st.markdown('''
            可视化展示
            - 专业对比分析
            - 性别差异研究
            - 学习模式识别
        ''')
    with c5:
        st.markdown('<h4>🎯 目标三：</h4>', unsafe_allow_html=True)
        st.markdown('''
            成绩预测
            - 机器学习模型
            - 个性化预测
            - 及时干预预警
        ''')
    
    st.markdown("***")  # 分隔线
    
    # 技术架构：分四列布局，展示项目使用的核心技术栈
    st.header("🔧 技术架构")
    m1, m2, m3, m4 = st.columns(4)  # 四个列布局
    with m1:
        st.markdown("**前端框架**")
        st.code("Streamlit", language=None)  	# 代码样式展示技术名称
    with m2:
        st.markdown("**数据处理**")
        st.code("Pandas\nNumPy", language=None)		# 代码样式展示技术名称
    with m3:
        st.markdown("**可视化**")
        st.code("Plotly\nMatplotlib", language=None)		# 代码样式展示技术名称
    with m4:
        st.markdown("**机器学习**")
        st.code("Scikit-learn", language=None)		# 代码样式展示技术名称

#  页面2：专业数据分析
elif nav_option == "专业数据分析":
    st.title("📊 课程学生成绩分析平台")  # 页面主标题
    st.markdown("***")                     # 分隔线
    
    # 1. 各专业核心指标统计：展示关键学习数据表格
    st.header("1. 各专业核心指标统计")
    # 选择需要展示的列，确保表格简洁清晰
    table_cols = ["专业", "每周平均学时", "期中考试平均分", "期末考试平均分", "平均上课出勤率"]
    # 展示数据表格，自适应容器宽度
    st.dataframe(df_summary[table_cols], use_container_width=True)
    
    st.markdown("***")  # 分隔线
    
    # 2. 各专业男女性别比例：图表+表格双展示
    st.header("2. 各专业男女性别比例")
    c1, c2 = st.columns(2)  # 两列布局
    with c1:
        # 创建性别比例柱状图（Plotly图表，支持交互）
        fig_gender = go.Figure()
        fig_gender.add_trace(go.Bar(x=df_summary["专业"], y=df_summary["男性比例"], name="男"))
        fig_gender.add_trace(go.Bar(x=df_summary["专业"], y=df_summary["女性比例"], name="女"))
        # 图表布局配置
        fig_gender.update_layout(
            barmode="group",                # 分组柱状图
            title="各专业男女性别分布",      # 图表标题
            xaxis_title="专业",              # X轴标题
            yaxis_title="比例(%)",           # Y轴标题
            height=400                      # 图表高度
        )
        # 展示图表，自适应容器宽度
        st.plotly_chart(fig_gender, use_container_width=True)
    with c2:
        # 展示性别比例详细数据表格，隐藏索引列更整洁
        st.dataframe(
            df_summary[["专业", "男性比例", "女性比例"]],
            use_container_width=True,
            hide_index=True
        )
    
    st.markdown("***")  # 分隔线
    
    # 3. 各专业学习指标对比（期中/期末分数+学时）：双Y轴图表+数据表格
    st.header("3. 各专业学习指标对比")
    c3, c4 = st.columns([2, 1])  # 第一列宽度是第二列的2倍
    with c3:
        # 创建双Y轴图表，同时展示柱状图和折线图
        fig_scores = go.Figure()
        # 每周平均学时（柱状图，对应左侧Y轴）
        fig_scores.add_trace(go.Bar(
            x=df_summary["专业"], y=df_summary["每周平均学时"],
            name="每周平均学时", yaxis="y1"
        ))
        # 期中考试分数（折线图，对应右侧Y轴）
        fig_scores.add_trace(go.Scatter(
            x=df_summary["专业"], y=df_summary["期中考试平均分"],
            name="期中考试分数", mode="lines+markers", line=dict(width=3), yaxis="y2"
        ))
        # 期末考试分数（折线图，对应右侧Y轴）
        fig_scores.add_trace(go.Scatter(
            x=df_summary["专业"], y=df_summary["期末考试平均分"],
            name="期末考试分数", mode="lines+markers", line=dict(width=3), yaxis="y2"
        ))
        # 双Y轴布局配置
        fig_scores.update_layout(
            title="各专业学习指标对比",    # 图表标题
            xaxis_title="专业",            # X轴标题
            yaxis=dict(title="每周平均学时", side="left"),  # 左侧Y轴（学时）
            yaxis2=dict(title="考试分数", side="right", overlaying="y"),  # 右侧Y轴（分数，叠加左侧Y轴）
            height=400                    # 图表高度
        )
        # 展示图表
        st.plotly_chart(fig_scores, use_container_width=True)
    with c4:
        st.subheader("详细数据")  # 三级标题
        # 展示学习指标详细数据
        st.dataframe(
            df_summary[["专业", "每周平均学时", "期中考试平均分", "期末考试平均分"]],
            use_container_width=True,
            hide_index=True
        )
    
    st.markdown("***")  # 分隔线
    
    # 4. 各专业平均上课出勤率：柱状图+数据表格
    st.header("4. 各专业平均上课出勤率")
    c5, c6 = st.columns([2, 1])  # 第一列宽度是第二列的2倍
    with c5:
        # 创建出勤率柱状图（Plotly Express，简洁易用）
        fig_attendance = px.bar(
            df_summary,
            x="专业",
            y="平均上课出勤率",
            title="各专业平均出勤率分布",
            labels={"平均上课出勤率": "出勤率(%)"}  # 轴标签重命名
        )
        # 展示图表
        st.plotly_chart(fig_attendance, use_container_width=True)
    with c6:
        # 展示出勤率详细数据
        st.dataframe(
            df_summary[["专业", "平均上课出勤率"]],
            use_container_width=True,
            hide_index=True
        )
    
    st.markdown("***")  # 分隔线
    
    # 5. 大数据管理专业专项分析：针对特定专业的深度分析
    st.header("5. 大数据管理专业专项分析")
    # 筛选大数据管理专业的数据
    bigdata_prof = df_summary[df_summary["专业"] == "大数据管理"]
    if not bigdata_prof.empty:  # 若存在该专业数据
        col1, col2 = st.columns(2)  # 两列布局
        with col1:
            # 展示出勤率指标（Metric组件，突出显示关键数据）
            st.metric("平均上课出勤率", f"{bigdata_prof['平均上课出勤率'].values[0]}%")
        with col2:
            # 展示期末平均分指标
            st.metric("期末考试平均分", round(bigdata_prof["期末考试平均分"].values[0], 2))
        
        # 创建大数据管理专业核心指标柱状图
        fig_bigdata = go.Figure(go.Bar(
            x=["平均出勤率(%)", "期末平均分"],
            y=[
                bigdata_prof["平均上课出勤率"].values[0],
                bigdata_prof["期末考试平均分"].values[0]
            ],
            textposition="auto"  # 自动显示数值标签
        ))
        # 图表布局配置
        fig_bigdata.update_layout(title="大数据管理专业核心指标", height=300)
        # 展示图表
        st.plotly_chart(fig_bigdata, use_container_width=True)
    else:  # 若不存在该专业数据，显示警告提示
        st.warning("未找到「大数据管理」专业的数据")

#  页面3：成绩预测
elif nav_option == "成绩预测":
    st.title("🔮 期末成绩预测")  # 页面主标题
    st.markdown("***")           # 分隔线
    # 信息提示：引导用户输入数据
    st.info("请输入学生的学习信息，系统将预测期末成绩并提供学习建议")
    
    # 表单容器：包裹所有输入组件，统一提交
    with st.form('student_score_pred_form', clear_on_submit=False):
        # 第一行：学号、性别、专业（两列布局）
        c1, c2 = st.columns(2)
        with c1:
            # 学号输入框（必填）
            student_id = st.text_input("学号", placeholder="如：22331331")
            # 性别下拉选择框
            gender = st.selectbox("性别", options=["男", "女"], index=0)
            # 专业下拉选择框（选项来自加载的专业列表）
            major = st.selectbox("专业", options=majors, index=0)
        
        with c2:
            # 每周学习时长滑块：范围0-50小时，步长0.5，默认0.0
            study_hours = st.slider(
                "每周学习时长（小时）",
                min_value=0.0,
                max_value=50.0,
                step=0.5,
                value=0.0,
                format="%.1f"  # 显示1位小数
            )
            
            # 上课出勤率滑块：范围0-100%，步长0.1，默认0.0
            attendance = st.slider(
                "上课出勤率（%）",
                min_value=0.0,
                max_value=100.0,
                step=0.1,
                value=0.0,
                format="%.1f"
            )
            
            # 期中考试分数滑块：范围0-100分，步长0.5，默认0.0
            midterm_score = st.slider(
                "期中考试分数（0-100）",
                min_value=0.0,
                max_value=100.0,
                step=0.5,
                value=0.0,
                format="%.1f"
            )
            
            # 作业完成率滑块：范围0-100%，步长0.1，默认0.0
            homework_rate = st.slider(
                "作业完成率（%）",
                min_value=0.0,
                max_value=100.0,
                step=0.1,
                value=0.0,
                format="%.1f"
            )
        
        # 表单提交按钮（主样式，蓝色突出显示）
        submitted = st.form_submit_button("预测期末成绩", type="primary")
    
    # 提交后处理逻辑：仅在点击提交按钮后执行
    if submitted:
        # 输入验证：学号不能为空
        if not student_id:
            st.error("❌ 学号不能为空！")  # 错误提示
            st.stop()  # 停止后续代码执行
        
        # 数据预处理：出勤率和作业完成率转小数（模型训练时用小数格式）
        attendance = attendance / 100.0
        homework_rate = homework_rate / 100.0
        
        # 特征编码：对分类特征（性别、专业）进行独热编码（与模型训练时保持一致）
        # 性别编码：生成性别对应的独热编码字典
        gender_encoded = {f'性别_{g}': 0 for g in ["男", "女"]}
        gender_encoded[f'性别_{gender}'] = 1  # 选中的性别设为1，其余为0
        # 专业编码：生成专业对应的独热编码字典
        major_encoded = {f'专业_{m}': 0 for m in majors}
        major_encoded[f'专业_{major}'] = 1  # 选中的专业设为1，其余为0
        
        # 整理输入特征：按模型训练时的特征顺序排列
        input_data = []
        for feat in feature_names:
            if feat == '每周学习时长（小时）':
                input_data.append(study_hours)
            elif feat == '上课出勤率':
                input_data.append(attendance)
            elif feat == '期中考试分数':
                input_data.append(midterm_score)
            elif feat == '作业完成率':
                input_data.append(homework_rate)
            elif feat in gender_encoded:
                input_data.append(gender_encoded[feat])
            elif feat in major_encoded:
                input_data.append(major_encoded[feat])
        
        # 模型预测：将输入特征转为DataFrame，传入模型进行预测
        final_score = model.predict(pd.DataFrame([input_data], columns=feature_names))[0]
        final_score = round(final_score, 1)  # 预测结果保留1位小数
        
        # 结果展示：突出显示预测分数
        st.subheader("预测结果")
        st.info(f"预测期末考试成绩：**{final_score} 分**")
        
        # 分数段细分展示：根据不同分数段给出对应的反馈和建议
        if final_score >= 90:
            # 90分及以上：优秀
            st.image('img/2.jpg', width=300)
            st.success("🏆 太棒了！预测成绩达到优秀（90分及以上）")
            st.warning("你展现了极高的学习水平，继续保持精益求精的态度，期末考试有望冲击满分！")
        elif 80 <= final_score < 90:
            # 80-90分：优秀
            st.image('img/4.jpg', width=300)
            st.success("🌟 优秀！预测成绩在80-90分段")
            st.warning("你的学习效果显著，只需针对性弥补个别知识漏洞，即可向90分以上冲刺。")
        elif 70 <= final_score < 80:
            # 70-80分：良好
            st.image('img/5.jpg', width=300)
            st.success("👍 良好！预测成绩在70-80分段")
            st.warning("你的学习基础扎实，若能增加学习时长、强化难点复习，可稳步提升至80分以上。")
        elif 60 <= final_score < 70:
            # 60-70分：及格
            st.image('img/3.jpeg', width=300)
            st.success("✅ 恭喜！预测成绩及格（60-70分段）")
            st.warning("你已达到合格标准，建议重点巩固基础知识，优化学习方法，争取提升至更高分数段。")
        else:
            # 60分以下：未及格
            st.image('img/6.jpg', width=300)
            st.warning("💪 加油！预测成绩暂未及格（60分以下）")
            st.warning("建议：1. 增加每周学习时长；2. 提高上课出勤率；3. 重点复习期中考试薄弱环节；4. 确保作业按时完成。")