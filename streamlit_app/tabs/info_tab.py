import streamlit as st
from streamlit_lottie import st_lottie
import sys
import config
sys.path.append('../')
from src.utils import load_lottieurl


sidebar_name = "Information"
lottie_ai = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_rwqo4knz.json")

def run():
    st_lottie(lottie_ai, height=150)   

    st.title("Product Classification for Rakuten")
    st.markdown("---")

    tab_intro, tab_team, tab_thanks = st.tabs(["Introduction", "Team", "Acknowledgements"])

    with tab_intro:
        st.subheader("🎯 Objective")
        st.markdown("This project aims to **automatically categorize products** on an e-commerce platform.")

        st.subheader("📄 Context")
        st.markdown("""**E-commerce** is a competitive market with multiple giant contenders: **Rakuten**, Amazon, CDiscount etc.
    They have two types of clients: merchants selling their products on the platform and customers buying them.

In order to provide the best user experience, platforms must provide easy to use interfaces and features to make the selling and buying process as easy as possible :
    - A **merchant** should be able to submit their product to sell with guided interface to **maximize their chances to sell** them.
    - **Customers** looking for product should be able to find the **product** they are **looking for**, but should also be suggested products that **might interest them**.

This can only be done with **:red[good product classification]**. This is why we are going to use **Artificial Intelligence** to help sellers to categorize their products.""")

    with tab_team:
        st.subheader("Project members")
        member_markdown = ""
        for member in config.TEAM_MEMBERS:
            member_markdown += f"""
                {member.member_section()}
                """
        st.markdown(member_markdown, unsafe_allow_html=True)
        st.subheader("Coordinator")
        st.markdown("- Manu Potrel")

    with tab_thanks:
        st.markdown("""
                    This project was made possible thanks to [Rakuten Institute of Technology](https://rit.rakuten.com) for providing the data used to
                    train our models.

                    We also would like to thanks Manu Potrel, our project coordinator, and [DataScientest.com](https://www.DataScientest.com)
                    for providing us boundaries to make this project a success.
                    """)
        
        col_rakuten, col_ds = st.columns([1,1])
        with col_rakuten:
            st.image("./assets/RIT_logo_big.jpg")
        with col_ds:
            # The 3 lines bellow are to center the logo vertically
            # 02/05/23, still no way to center elements in Streamlit
            st.write("")
            st.write("")
            st.write("")
            st.image("./assets/logo-dscom.png")