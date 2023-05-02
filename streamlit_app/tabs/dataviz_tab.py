import streamlit as st
import pandas as pd
import numpy as np

from src.data import data, analysis


data = data.load_data("../data")

title = "Data exploration and visualization"
sidebar_name = "Data Visualization" 


def run():

    st.title(title)

    st.markdown("""
                ## Description

                All data were provided by the e-commerce giant
                **:red[Rakuten]** to serve as an online challenge called:
                [Rakuten France Multimodal Product Data
                 Classification](https://challengedata.ens.fr/challenges/35).

                The dataset is composed of a train set counting **84916
                labeled observations**
                and a test set counting **13812 observations**.
                Each observation represent a product sold on an e-commerce
                platform.

                We have **two types** of data: text and image.
                """)

    st.markdown("""
                ### Text data

                Bellow is a description of each field of our observations.
                """)
    st.table(pd.DataFrame(analysis.TEXT_DATA_DESCRIPTION[2:],
                          columns=analysis.TEXT_DATA_DESCRIPTION[0]))

