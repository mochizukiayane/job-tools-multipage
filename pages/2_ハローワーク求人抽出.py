import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="ハローワーク求人抽出")

st.title("🗂️ ハローワーク求人抽出ツール")

url = st.text_input("求人詳細ページのURLを入力してください（ハローワーク）")

if url:
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        job_info = soup.get_text()
        st.text_area("抽出された求人情報（プレーンテキスト）", value=job_info, height=400)
    except Exception as e:
        st.error("データの取得に失敗しました")
        st.error(e)
