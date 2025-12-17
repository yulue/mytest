import streamlit as st     # 导入Streamlit并用st代表它
import pandas as pd

st.title("🕶学生 小语-数字档案")   #标题
st.header("🔑基础信息")            #章节
st.markdown("**学生ID：** NEO-2022-008")
st.markdown("**注册时间：** :orange[2022-09-01 08:30:16] **| 精神状态：✅正常**")   #加粗字体加橙色字体
st.markdown("**当前教室：** :orange[实训楼108] |**安全等级：🔐:orange[绝密]**")

st.header("📊技能矩阵")
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言",help='C语言', value="95%", delta="2%")
c2.metric(label="Python",help='Python', value="87%", delta="-1%")
c3.metric(label="Java", help='Java',value="68%", delta="-10")

st.subheader("Streamlit课程进度")
st.text("Streamlit课程进度")
# 设置进度值（范围0~1，示例为50%进度）
progress = 0.5

# 渲染进度条
st.progress(progress)

st.header("📝任务日志")
#创建表格
data = {
    '日期':['2023-10-01','2023-10-05','2023-10-12'],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['✅完成','🕗进行中','❌未完成'],
    '难度':['⭐⭐⛤⛤⛤','⭐⛤⛤⛤⛤','⭐⭐⭐⛤⛤'],
}
index = pd.Series(['0','1', '2'], name='序号')    #表格索引
df = pd.DataFrame(data, index=index)      # 根据上面创建的data和index，创建数据框
st.dataframe(df, width=500, height=150)    #显示表格并设置表格宽高

# 创建一个代码块
st.header("🔔最新结果代码")
# 创建要显示的Java代码块的内容
python_code='''def matrix_breach():
  while True:
     if detrct_vulnerability():
         exploit()
         return"ACCESS GRANTED"
     else:
         stealth_evade'''
#用于展示python_code的内容
st.code(python_code)

st.markdown('***')  #分割线
st.markdown(':green[>> SYSTEM MESSAGE：]下一个任务目标已解锁...')   #输出绿色和普通文本
st.markdown(':green[>> TGARGET：]课程管理系统')
st.markdown(':green[>> COUNTDOW：]2025-06-03 15:24:58')
st.text('系统状态：在线   连接状态：已加密')     #输出文本
