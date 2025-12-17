import streamlit as st

#修改标签页的文字和图标
st.set_page_config(page_title='音乐',page_icon='🎵')

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
