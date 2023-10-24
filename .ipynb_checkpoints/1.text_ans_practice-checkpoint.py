import streamlit as st # streamlit, pandas 라이브러리 불러오기 
import pandas as pd

st.title('Text elements') # header, subheader, text, caption 연습하기
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
st.header('Header: 데이터 분석 표현')
st.subheader('Subheader: 스트림릿')
st.text('Text: this is the Streamlit')
st.caption('Caption: Streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹어플리케이션이다.')

st.markdown('# Markdown 1st') # markdown 연습하기
st.markdown('## Markdown 2nd')
st.markdown('### Markdown 3rd')
st.markdown('**_Markdown 진하고 기울임_**')
st.markdown('- Markdown 글머리 기호')

st.markdown('## Code & Latex')# Latex & Code 연습하기
st.code('a + ar + a r^2 + a r^3')
st.latex(r''' a + ar + a r^2 + a r^3''')
    
st.markdown('# write')# write 연습하기
df = pd.DataFrame({'이름':['홍길동','김사랑','일지매','이루리'],'수준':['금','동','은','은']})
st.write('아래 딕셔너리를 판다스 데이터프레임으로 변경', df, '스트림릿의 write 함수로 표현')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text_ans.py