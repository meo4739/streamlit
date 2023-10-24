# streamlit 라이브러리 불러오기 
import streamlit as st

# 이미지 주소: https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80
# 오디오 주소: streamlit\MusicSample.mp3
# 비디오 주소: streamlit\VideoSample.mp4

st.title('Unit 2. Media elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/media')

st.header('1. Image')
st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80')
st.header('2. Audio')
st.audio('streamlit\MusicSample.mp3')
st.header('3. Video')
st.video('streamlit\VideoSample.mp4')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\2.media_ans.py
