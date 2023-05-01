from collections import OrderedDict
import streamlit as st
import config
from tabs import intro_tab, categories_tab, dataviz_tab, prediction_tab
import sys
sys.path.append('../')


st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://img.icons8.com/?size=512&id=48282&format=png",
)

with open("style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# TODO: add new and/or renamed tab in this ordered dict by
# passing the name in the sidebar as key and the imported tab
# as value as follow :
TABS = OrderedDict(
    [
        (intro_tab.sidebar_name, intro_tab),
        (categories_tab.sidebar_name, categories_tab),
#        (dataviz_tab.sidebar_name, dataviz_tab),
        (prediction_tab.sidebar_name, prediction_tab),
    ]
)


def run():
    st.sidebar.image(
        "https://dst-studio-template.s3.eu-west-3.amazonaws.com/logo-datascientest.png",
        width=200,
    )
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    tab.run()


if __name__ == "__main__":
    run()
