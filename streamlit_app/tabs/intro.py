import streamlit as st
import requests
from streamlit_lottie import st_lottie


sidebar_name = "Introduction"

def load_lottieurl(url):
    """
    Fetch lottie anymation from URL
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_zrqthn6o.json")
lottie_ai = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_rwqo4knz.json")

def run():
    st_lottie(lottie_ai, height=150)   

    st.title("Product Classification for Rakuten")
    st.markdown("---")

    st.subheader("🎯 Objective")
    st.markdown("This project aims to **automatically categorize products** on an e-commerce platform.")

    st.subheader("📄 Context")
    st.markdown("""**E-commerce** is a competitive market with multiple giant contenders: **Rakuten**, Amazon, CDiscount etc.
They have two types of clients: merchants selling their products on the platform and customers buying them.

In order to provide the best user experience, platforms must provide easy to use interfaces and features to make the selling and buying process as easy as possible :
- A **merchant** should be able to submit their product to sell with guided interface to **maximize their chances to sell** them.
- **Customers** looking for product should be able to find the **product** they are **looking for**, but should also be suggested products that **might interest them**.

This can only be done with **:red[good product classification]**. This is why we are going to use **Artificial Intelligence** to help sellers to categorize their products.""")
