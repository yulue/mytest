import streamlit as st

# 配置页面基础信息：标题、图标、布局
st.set_page_config(page_title='广西职业师范学院',page_icon='📝',layout='wide')
st.title('广西职业师范学院')
# 创建选项卡
tab1, tab2, tab3 , tab4, tab5, tab6= st.tabs(["数字档案", "南宁美食数据", "相册","音乐播放器",  "视频播放器", "个人简历生成器"])

# 在第一个选项卡中添加内容
with tab1:
    #数字档案代码
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

# 在第二个选项卡中添加内容
with tab2:
    #南宁美食数据代码
    import streamlit as st
    import pandas as pd
    import numpy as np

    # 餐厅数据
    restaurants_data = {
        "餐厅": ['星艺荟肯德基', '蛙小侠', '必胜客', '好友缘', '蚂蚁洞'],
        "类型": ['快餐', '中餐', '快餐', '自助餐', '烤肉'],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "latitude": [22.854016, 22.814051, 22.838049, 22.812196, 22.813766],
        "longitude": [108.222592, 108.321394, 108.262899, 108.397716, 108.385751]
    }
    #价格数据
    Price_data={
        '月份':['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
        '星艺荟肯德基':[58,75,66,69,75,59,77,67,59,68,71,70],
        '蛙小侠':[158,175,166,169,175,159,177,167,159,168,171,170],
        '必胜客':[79,159,136,124,136,79,139,135,149,159,144,156],
        '好友缘':[158,136,159,139,159,144,167,175,158,177,164,158],
        '蚂蚁洞':[188,172,158,167,155,144,159,143,165,135,152,155],
    }
    #时间数据
    time_data={
        '时间':['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00'],
        '星艺荟肯德基':[18,25,36,19,7,5,7,36,29,18,11,8],
        '蛙小侠':[0,17,66,39,15,1,17,67,59,28,11,2],
        '必胜客':[0,15,36,24,36,7,13,15,19,10,14,6],
        '好友缘':[2,36,59,39,19,14,17,55,58,17,16,15],
        '蚂蚁洞':[1,12,28,27,15,14,9,33,45,25,22,15],
    }
    # 根据上面创建的data，创建数据框
    df=pd.DataFrame(restaurants_data)   #餐厅数据
    jg=pd.DataFrame(Price_data)         #价格数据
    sj=pd.DataFrame(time_data)          #时间数据
    #地图
    st.header('🌍餐厅位置')  #标题
    mp_df=pd.DataFrame(df)   
    st.map(mp_df)   #显示地图

    st.header('⭐餐厅评分')   #标题
    #条形图，定义x轴和y轴
    st.bar_chart(df,x='餐厅',y='评分')

    st.header('💰餐厅价格')   #标题
    #折线图，定义x轴
    st.line_chart(jg,x='月份')

    st.header('🕚用餐的高峰时段')   #标题
    #面积图，定义x轴
    st.area_chart(sj,x='时间')

# 在第三个选项卡中添加内容
with tab3:
    #相册代码
    import streamlit as st


    st.title('相册')

    #把索引存储在ind变量中
    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    #图片链接
    images=[
        {
            'url':"https://picx.zhimg.com/v2-4a5363d925731a7ad7b061da48f71d38_r.jpg?source=172ae18b",
            'text':"柴犬"
        },{
            'url':"https://img.keaitupian.cn/uploads/2020/10/03/5f62f5a39a4e1.jpg",
            'text':"柯基"
        },{
            'url':"https://ts4.tc.mm.bing.net/th/id/OIP-C.GCBMejD3rtPzAr4bjLKIkgHaEo?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
            'text':"萨摩耶"
        }

        ]
    #url：图片的地址 caption：图片注释
    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])
    #上一页
    def prevImg():
         st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
    #下一页
    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)

    c1,c2=st.columns(2)
    #按钮
    with c1:
        st.button('上一张',on_click=prevImg,use_container_width=True)

    with c2:
        st.button('下一张',on_click=nextImg,use_container_width=True)

# 在第四个选项卡中添加内容
with tab4:
    #音乐播放器代码
    import streamlit as st


    st.title('🎧音乐播放器')   #标题
    st.text('使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制')   #说明文本

    #把索引存储在ind变量中
    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    #音乐链接、封面和相关信息
    musics=[
        {
            'url':"https://music.163.com/song/media/outer/url?id=2704864872.mp3",
            'name':"浆果",
            'cover': "http://p1.music.126.net/BQAY8w9XzOj_j1wZgIsczQ==/109951168247366566.jpg?param=130y130",  
            'singer': "SPIDERUNIVERSAL",
            'duration': "4:34"
        },{
            'url':"https://music.163.com/song/media/outer/url?id=1855555967.mp3",
            'name':"陪你看星星",
            'cover': "http://p2.music.126.net/8ydKseCBBBojILcvPGRK0A==/109951166112752604.jpg?param=130y130",  
            'singer': "Yan.",
            'duration': "3:15"
        },{
            'url':"https://music.163.com/song/media/outer/url?id=2756031693.mp3",
            'name':"几分之几",
            'cover': "http://p1.music.126.net/tUW_svaKt1hM84mJxulSpQ==/109951172157224890.jpg?param=130y130", 
            'singer': "刘可以",
            'duration': "3:53"
        }]

    current_music = musics[st.session_state['ind']]

    #上一页
    def prevmusic():
         st.session_state['ind'] = (st.session_state['ind']-1) % len(musics)
    #下一页
    def nextmusic():
        st.session_state['ind']=(st.session_state['ind']+1)%len(musics)
    
    #摆放位置，封面1/3，其他2/3
    c1,c2=st.columns([1,2])
    with c1:
        st.image(current_music['cover'], caption="专辑封面", use_container_width=True)

    with c2:
        st.subheader(current_music['name'])
        st.write(f"歌手: {current_music['singer']}")
        st.write(f"时长: {current_music['duration']}")
        #按钮
        b1,b2=st.columns([1,1])
        with b1:
            st.button('⏮上一首',on_click=prevmusic,use_container_width=True)
        with b2:
            st.button('下一首⏭',on_click=nextmusic,use_container_width=True)
    
    #显示播放器
    st.audio(current_music['url'])


# 在第五个选项卡中添加内容
with tab5:
    #视频播放器代码
    import streamlit as st

    st.title('📺视频播放器')   #标题

    # 视频数据，包含每集视频的链接、标题、集数和剧情简介
    video_arr=[
        {
            'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/48/40/27183154048/27183154048-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&mid=0&uipk=5&trid=62fc0aa5808442e9930b6feb7357404O&deadline=1765769914&nbs=1&oi=2067284620&gen=playurlv3&os=08cbv&og=hw&upsig=402c82cf828080338953e7263ff9364b&uparams=e,platform,mid,uipk,trid,deadline,nbs,oi,gen,os,og&bvc=vod&nettype=1&bw=696348&build=7330300&dl=0&f=O_0_0&agrr=1&buvid=&orderid=0,3',
            'title':'星游记-第1集：风筝见证 我要去彩虹海',
            'episode':1,
            'text':'不允许任何人飞行的地球上，终于出现了唯一一艘飞船，却被银河眼的大头钉部队夺走。为了前往传说中的彩虹海，麦当与飞船的主人咕咚决定挑战银河眼'
            },{
            'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/84/56/27183285684/27183285684-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&gen=playurlv3&trid=a430dbfb73db4024a9d7ff42ae1d9a0O&mid=0&deadline=1765770060&nbs=1&os=estgcos&og=hw&platform=html5&uipk=5&oi=1385955528&upsig=02c31d50720a0fb317460d9326fe5717&uparams=e,gen,trid,mid,deadline,nbs,os,og,platform,uipk,oi&bvc=vod&nettype=1&bw=644396&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
            'title':'星游记-第2集：争夺战 地球上唯一的飞船',
            'episode':2,
            'text':'由于银河眼经理人——赛璐珞的阻止，已经近在眼前的飞船被送到了飞船坟场，无穷无尽的龟龟熊，彻底挡住了麦当面前的道路'
            },{
            'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/90/27189579018/27189579018-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&platform=html5&mid=0&gen=playurlv3&os=zosbv&trid=b68ccb134aaa4bfd8597b3c8061fa6aO&oi=1385955528&deadline=1765770139&og=hw&nbs=1&upsig=2a5758766188f89863227f468c1dedb1&uparams=e,uipk,platform,mid,gen,os,trid,oi,deadline,og,nbs&bvc=vod&nettype=1&bw=703919&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
            'title':'星游记-第3集：倒计时 无法停止的吞噬',
            'episode':3,
            'text':'借助龟龟熊的能力，麦当终于赶到了飞船坟场。但唯一能够制止飞船进入焚毁炉的遥控器，却装在了破坏力巨大的碎渣机器人头部..'
            },{
            'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/83/75/27189707583/27189707583-1-192.mp4?e=ig8euxZM2rNcNbRVhbdVhwdlhWdghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1765770187&platform=html5&os=estgoss&og=ali&trid=4317f350e3a641b88bc1763a3b59baeO&mid=0&nbs=1&uipk=5&oi=144233936&gen=playurlv3&upsig=9409510cd536f8a13006f17639680022&uparams=e,deadline,platform,os,og,trid,mid,nbs,uipk,oi,gen&bvc=vod&nettype=1&bw=821847&f=O_0_0&agrr=1&buvid=&build=7330300&dl=0&orderid=0,3',
            'title':'星游记-第4集：碾碎的翅膀 我曾经相信的你',
            'episode':4,
            'text':'坟场主人的真实身份，居然是飞船制造师哈雷的孪生弟弟--哈马。梦想破灭的怨恨，驱使哈马不惜一切去毁掉每一艘飞船。'
            },{
            'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/40/16/27196981640/27196981640-1-192.mp4?e=ig8euxZM2rNcNbRV7zdVhwdlhWdahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1765770234&nbs=1&uipk=5&gen=playurlv3&os=estgcos&trid=d62161fc49ad4836ab08efb8c4d80fdO&oi=144233936&platform=html5&mid=0&og=cos&upsig=eec02831280b12386efc7609a049bc63&uparams=e,deadline,nbs,uipk,gen,os,trid,oi,platform,mid,og&bvc=vod&nettype=1&bw=861543&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
            'title':'星游记-第5集：大傻瓜',
            'episode':5,
            'text':'看到哥哥留下的飞船，哈马终于承认了自己仍然想飞的梦想。麦当不顾一切冲向布满电网的天空，最后在熊猫阿姨出人意料的帮助下，飞出了地球，开始了迈向彩虹海的第一步'
            }]

    # 演员表，包含角色图片、姓名和角色介绍
    performer=[
        {
            'img':'http://img2.a0bi.com/upload/ttq/20150214/1423886042217.jpg',
            'name':'麦当',
             'sf':'红魔鬼麦林的儿子，是一名拥有彩虹石的“自由者”性格超级自信乐观，且体力超群，热爱美食（本身就是一名厨师）'
         },{
             'img':'https://ts1.tc.mm.bing.net/th/id/R-C.1654deee2bf1db85f486206244b9fb48?rik=CfxSgPwrYXePXQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10100%2f374%2fw640h534%2f20191212%2f1633-ikrsesr7779992.png&ehk=P2pm%2bGlT4rJHmJfZuOk%2bmq2fOedQoiPDvj21DJZlPaU%3d&risl=&pid=ImgRaw&r=0',
             'name':'咕咚·萌西',
             'sf':'亚亚罗星球的国王，父母是居住在这个星球里，被人们奉为“英雄”的人，所以因父母的关系，被星球里掌握实权的大臣约士亚尊为“国王”，将王冠戴到了他的头上。'
         },{
             'img':'https://ts2.tc.mm.bing.net/th/id/OIP-C.NimX0jPrwlwKjal3cpaQhQHaFi?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3',
             'name':'笛亚',
             'sf':'著名星学会会长盖亚的孙女，星学会唯一幸存者，是彩虹石的自由者，守护着银河眼费尽心机寻找的神秘装置——“黄金魔方”'
         },{
             'img':'https://gss0.baidu.com/-4o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/09fa513d269759eef1e60924b9fb43166c22dfaf.jpg',
             'name':'红眼罗曼',
             'sf':'银河眼最强的五个经理人五色眼之一。受某人的委托来阻止麦当去彩虹海。是个亦正亦邪的角色。认路能力极差。可实力极强。'
         },{
             'img':'https://ts4.tc.mm.bing.net/th/id/OIP-C.92S2yV5l9QgF2vqEOlq9EwHaJP?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3',
             'name':'克拉',
             'sf':'克拉，银河眼干部，隶属于专门负责战争的特攻部门，五色眼之一蓝眼的手下，曾作为代表出席星际联盟会议。性格冷血好战，杀人如麻。'
         }]

    # 如果'ind'键不存在，设置初始值为0
    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    # 获取当前播放的视频信息
    current_video = video_arr[st.session_state['ind']]
    # 在视频上方显示当前集数标题
    st.header(f'{current_video['title']}')

    #显示视频
    st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

    # 显示当前集数的简介
    st.markdown('<h6>📝 剧情简介</h6>',unsafe_allow_html=True)
    st.write(f'> {current_video['text']}')
    st.markdown('***')  #分割线

    #播放函数
    def play(i):
        st.session_state['ind']=int(i)
    #选集标题
    st.markdown('<h4>选集</h4>',unsafe_allow_html=True)
    #用于横向排列选集按钮
    cols=st.columns(len(video_arr))
    #为每一集创建一个按钮
    for i,col in enumerate(cols):
        with col:
            st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))
    st.markdown('***')
    st.markdown('<h5>🕶 星游记演员表</h5>',unsafe_allow_html=True)

    # 循环展示每个演员的卡片
    for p in performer:
        # 用列布局;图片+文字
        actor_col1, actor_col2 = st.columns([1, 3])
        with actor_col1:
            st.image(p['img'])  #显示图片
        with actor_col2:
            st.markdown(f"**{p['name']}**")
            st.write(p['sf'])
        st.markdown('---')  # 每个演员之间加分隔线


# 在第六个选项卡中添加内容
with tab6:
    #个人简历生成器
    import streamlit as st
    from datetime import datetime


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
