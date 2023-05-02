import streamlit as st
from streamlit_lottie import st_lottie
import sys
sys.path.append('../')
from src.utils import load_lottieurl

title = "What's next?"
sidebar_name = title

lottie_business_team = load_lottieurl(
        "https://assets4.lottiefiles.com/packages/lf20_ca8zbrdk.json")

def run():
    st_lottie(lottie_business_team, height=250)

    st.title(title)
    st.markdown("---")
    
    col_left, col_right = st.columns([1,8])
    with col_left:
        st.image("assets/technology.png")
    with col_right:
        st.markdown("## Separation of responsibilities")
    st.markdown("""
                    Currently, the model is run by the demo application when the user press predict.
                    While working, this is **:red[not a good practice]** because it requires to **update the
                    demo application** everytime we want to **update the model**.

                    To avoid this, we must create a *separation of responsibilities*: the **demo app**
                    should be where the **user write their data** that are then sent to **another
                    app** (also called API) with sole purpose to **predict the category**
                    and send back the information to the demo app.
                    We would then be free to update each of them separately.

                    This separation could be done either by hosting each app on a different server or by using containers.
                    """)
