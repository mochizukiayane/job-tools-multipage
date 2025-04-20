import streamlit as st

st.set_page_config(page_title="求人掲載ツール", layout="centered")

st.markdown("""
    <h1 style="color: #8b0000; text-align: center;">📚 求人掲載ツール</h1>
    <p style="text-align: center; font-size: 18px;">
        求人情報の取得・管理に役立つツールを<br>
        ひとつにまとめたポータルページです。
    </p>
    <hr style="margin-top: 30px; margin-bottom: 30px;">
""", unsafe_allow_html=True)

st.subheader("▶ 左のサイドバーからツールを選んでください")
st.info("現在、「画像ダウンローダー」「ハローワーク求人抽出」が利用可能です。")
