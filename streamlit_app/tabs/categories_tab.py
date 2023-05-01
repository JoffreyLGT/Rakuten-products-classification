import streamlit as st
import pandas as pd
import sys
sys.path.append('../')
from src.data.data import CATEGORIES_DIC


title = "Categories list"
sidebar_name = title


def run():

    st.title(title)
    st.markdown("""
                Bellow is the list of all the **product type codes** the model can identify and a **label** describing their content.
                Please keep in mind the label was **:red[set arbitrarily]** by checking images of the category.
                """)
    categories = pd.DataFrame(
            [(str(i), str(CATEGORIES_DIC[i])) for i in CATEGORIES_DIC.keys()],
            columns=["prdtypecode", "label"])
    categories = categories.set_index("prdtypecode")
    st.dataframe(categories, height=985, width=500)
