import streamlit as st
st.caption('참조사이트: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app')

def main_page(): # 페이지 선언 (🎈 ❄️ 🎉)
    st.title('Main page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    st.title('Page 2 ❄️')
    st.sidebar.title('side 2 ❄️')

def page3():
    st.title('Page3 🎉')
    st.sidebar.title('side 3 🎉')

page_names_to_funcs = {'Main Page': main_page, 'Page 2': page2, 'Page 3': page3} # 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }

selected_page = st.sidebar.selectbox( 'Select a page', page_names_to_funcs.keys()  ) # 사이드 바에서 selectbox 선언 & 선택 결과 저장 # page_names_to_funcs의 키값들이 들어간다. ('Main Page','Page 2','Page 3')
  
page_names_to_funcs[selected_page ]() # 해당 페이지 부르기 # selected_page에서 누른 값이 들어가며 value 값을 부른다. # 딕셔너리 구조이므로 키값이 들어가면 value가 튀어나온다.

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-2.layouts.py