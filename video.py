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



        
