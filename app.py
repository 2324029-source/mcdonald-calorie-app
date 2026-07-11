import streamlit as st

import pandas as pd

# ページ設定

st.set_page_config(

    page_title="マクドナルド カロリー計算アプリ",

    page_icon="🍔",

    layout="wide"

)

st.title("🍔 マクドナルド カロリー計算アプリ")

st.write("マクドナルド公式サイトの栄養情報をもとに作成")

# CSV読み込み

df = pd.read_csv("mcdonald_calorie.csv")

# カテゴリー一覧を取得

categories = sorted(df["カテゴリー"].unique())

# カテゴリー選択

category = st.selectbox(

    "カテゴリーを選択してください",

    categories

)

# 選択したカテゴリーの商品だけ表示

category_df = df[df["カテゴリー"] == category]

# 商品選択

selected = st.multiselect(

    "商品を選択してください",

    options=category_df["商品名"]

)

# 選択した商品のデータ

if selected:

    result = df[df["商品名"].isin(selected)]

    st.subheader("選択した商品")

    st.dataframe(result, use_container_width=True)

    total = result["カロリー(kcal)"].sum()

    st.metric(

        label="🔥 合計カロリー",

        value=f"{total} kcal"
