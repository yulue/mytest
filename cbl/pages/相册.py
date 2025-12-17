import streamlit as st

#修改标签页的文字和图标
st.set_page_config(page_title='相册',page_icon='⭐')

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
