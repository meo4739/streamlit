# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')

# markdown 연습하기
st.header("Header:데이터 분석 표현")
st.subheader("Subheader: 스트림릿")
st.text("Text: this is the Streamlit")
st.caption("Caption: Streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹 어플리케이션이다.")

# # Latex & Code 연습하기
# st.markdown('## Code & Latex')
st.code ("x=1234")
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1}ar^k = a \left(\frac{1-r^{n}}{1-r}\right) ''')

# # write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
st.latex(r''' a + ar + a r^2 + a r^3''')
df = pd.DataFrame({'이름': ['홍길동','김사랑','일지매','이루리'],'수준': ['금','동','은','은']})
st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서',df,'스트림릿의 write 함수로 표현')

# # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text.py