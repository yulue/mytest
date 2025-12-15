import streamlit as st
from datetime import datetime

# 配置页面基础信息：标题、图标、布局
st.set_page_config(page_title='个人简历生成器',page_icon='📝',layout='wide')

# 设置页面主标题和副标题
st.title('🎨个人简历生成器')
st.text('使用Streamlit创建您的个性化简历')

# 分割页面为两列，比例1:2
c1,c2=st.columns([1,2])
#左侧表单
with c1:
    st.markdown('<h4> 个人信息表单</h4>',unsafe_allow_html=True)   #标题
    st.markdown('***')
    user_name=st.text_input('姓名')         # 文本输入框：姓名
    user_age=st.slider('年龄',0,100,20)     # 滑块组件：年龄（范围0-100，默认值20）
    user_job=st.text_input('职位')          # 文本输入框：应聘职位
    user_num=st.text_input('电话')          # 文本输入框：电话号码
    user_email=st.text_input('邮箱')        # 文本输入框：邮箱
    #日期选择器
    min_birth_date = datetime(1980, 1, 1)
    max_birth_date = datetime.now()
    user_date=st.date_input('出生日期',min_value=min_birth_date,max_value=max_birth_date)
    # 性别选择
    user_gender=st.radio('性别',options=['男','女'],horizontal=True)
     # 学历下拉选择
    user_edu=st.selectbox('学历',options=['高中','专科','本科','硕士','博士'])
    
    # 语言能力下拉
    user_lang=st.multiselect('语言能力(可多选)',['中文', '英语', '法语', '德语', '意大利语'])
    
    # 技能多选
    user_skill=st.multiselect('技能（可多选）',options=['Python','Java','PS','HTML/CSS','数据库', 'C++', 'Linux'])
    user_work=st.slider('工作经验（年）',0,30,0)
    user_salary=st.slider('期望薪资（元）',2000,20000,2000)
    user_intro=st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点')
    contact_time=st.selectbox(label='每日最佳联系时段',options=[f'{h:02d}:{m:02d}' for h in range(8,24) for m in [0,30]])  # 8:00-23:30的半小时间隔选项
    user_photo=st.file_uploader(
        label='上传个人照片',
        type=['jpg','jpeg','png'],
        help='支持 JPG、JPEG、PNG 格式，文件不超过20MB')
    
#左侧表单
with c2:
    st.markdown('<h4>简历实时预览</h4>', unsafe_allow_html=True)
    st.markdown('***')
    #把左侧表单分为3列
    c3,c4,c5=st.columns(3)
    #头像、姓名（没有值为默认）
    with c3:
        # 显示头像（上传/默认）
        if user_photo:
            st.image(user_photo, width=150)
        else:
            st.image("https://pic4.zhimg.com/50/v2-6afa72220d29f045c15217aa6b275808_hd.jpg?source=1940ef5c", width=150,caption='请上传图片')
        # 显示姓名（上传/默认）
        if user_name:
            st.header(user_name)
        else:
            st.header('姓名')
    with c4:
        st.text(f'📆年龄：{user_age}')
        st.write(f"📞电话: {user_num}")
        st.write(f"💼职位: {user_job}")
        st.write(f'📩邮箱：<a href="mailto:{user_email}">{user_email}</a>', unsafe_allow_html=True)
        st.write(f"🎂出生日期: {user_date}")

    with c5:
        st.write(f"⚥性别: {user_gender}")
        st.write(f"🎓学历: {user_edu}")
        st.write(f"💻工作经验: {user_work}年")
        st.write(f"💰期望薪资: {user_salary}元")
        st.write(f"🕘最佳联系时间: {contact_time}")

    st.markdown('***')
    
     # 个人简介模块
    st.markdown('<h4>个人简介</h4>', unsafe_allow_html=True)
    st.write(user_intro if user_intro else "这个人很神秘，没有留下任何介绍。")
        
    # 专业技能、语言能力模块
    c6,c7=st.columns(2)
    with c6:
        st.markdown('<h4>专业技能</h4>', unsafe_allow_html=True)
        # 技能列表（每行展示）
        for skill in user_skill:
            st.write(f"• {skill}")
    with c7:
        #语言能力
        st.markdown('<h4>语言能力</h4>', unsafe_allow_html=True)
        st.write(f"{'、 '.join(user_lang)}") 
