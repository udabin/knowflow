import streamlit as st
import requests

st.set_page_config(page_title="KnowFlow Assistant", layout="wide")
st.title("KnowFlow - Internal Knowledge Assistant")

query = st.text_input("질문을 입력하세요:")

if query:
    with st.spinner("에이전트 응답 생성 중 ..."):
        res = requests.post(
            "http://localhost:8000/query",
            json={"query":query}
        )
        if res.status_code == 200:
            result = res.json()
            st.success("응답 완료!")
            st.json(result)
        else:
            st.error(f"에러 발생: {res.status_code}")