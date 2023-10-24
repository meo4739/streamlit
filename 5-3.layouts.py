import streamlit as st
import pandas as pd


# Iris 사진 나타하기 - https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 나타내기 

def main_page(): # 메인페이지 
    st.header('Main Page')
    st.image("https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200")
    iris = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv')
    st.write(iris)
    
    
def page2(): # 2페이지: 세 개의 columns으로 나누어 꽃 이름과 사진 나타내기
    st.header('Page 2')    
    tab1, tab2, tab3 = st.columns(3) # 칼럼 3개
    with tab1:
        st.text('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg')
    with tab2:
        st.text('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg')
    with tab3:
        st.text('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg')


def page3(): # 3페이지: 세 개의 tab을 사용하여 iris 3가지 꽃 나타내기 (width=500)
    st.header('Page 3')
    tab1 ,tab2, tab3 = st.tabs(['Setosa','Versicolor','Virginica'])  # 세 개의 tab
    with tab1:
        st.text('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg', width = 500)
    with tab2:
        st.text('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg', width = 500)
    with tab3:
        st.text('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg', width = 500)

page_names_to_funcs = {'Main page':main_page, 'Page 2' :page2, 'Page 3':page3} # 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }

selected_page =  st.sidebar.selectbox( 'Select a page',page_names_to_funcs.keys()) # 사이드 바에서 selectbox 선언 & 선택 결과 저장

page_names_to_funcs[selected_page]() # 해당 페이지 부르기

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-3.layouts.py