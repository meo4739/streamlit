# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd



# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')

st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header('1. Metric')
st.metric(label = 'Temperature', value = '30.5°C', delta = '2.5°C')
st.metric(label = 'Temperature', value = '28°C', delta = '-2.5°C')

st.header('2. Columns')
col1, col2, col3 = st.columns(3)
col1.metric("기온",'30.5°C', '2.5°C')
col1.metric('풍속','9 mph','-8%')
col1.metric('습도','86%','4%')

st.header('3. Dataframe 조회하기')
st.markdown('- st.dataframe(상위 15행)')
st.dataframe(titanic.head(15))

st.write(titanic.head(15))

st.table(titanic.head(15))

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\3.data_ans.py