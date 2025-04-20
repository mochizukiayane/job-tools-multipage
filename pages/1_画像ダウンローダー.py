import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import base64

st.set_page_config(page_title="画像ダウンローダー")

st.title("🖼️ 画像ダウンローダー")

url = st.text_input("画像を取得したいWebページのURLを入力してください")

if url:
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        images = soup.find_all("img")

        image_urls = []
        for img in images:
            src = img.get("src")
            if src:
                full_url = urljoin(url, src)
                image_urls.append(full_url)

        st.write(f"画像数：{len(image_urls)}枚")

        for i, img_url in enumerate(image_urls):
            try:
                img_data = requests.get(img_url).content
                b64 = base64.b64encode(img_data).decode()
                href = f'<a href="data:image/jpeg;base64,{b64}" download="image_{i}.jpg">📥 画像{i+1} をダウンロード</a>'
                st.image(img_url, width=200)
                st.markdown(href, unsafe_allow_html=True)
                st.markdown("---")
            except:
                st.warning(f"画像{i+1}の取得に失敗しました")

    except Exception as e:
        st.error("画像の取得中にエラーが発生しました")
        st.error(e)
