import numpy as np
import streamlit as st
from PIL import Image

import sys
sys.path.append('../')

from src.models import predict_prdtypecode
from src.data.data import CATEGORIES_DIC

title = "Predict your item category"
sidebar_name = title

def run():
    st.title(title)
    st.warning("Please note that only French language is supported")
    designation = st.text_input(label="Designation")
    description = st.text_area(label="Description")
    col_widget, col_preview = st.columns([4,2])

    with col_widget:
        uploaded_image = st.file_uploader(label="Picture", type=["jpg", "jpeg"])

    with col_preview:
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image)
        else:
            image = np.zeros((254, 254, 3))

    if (st.button(label="Predict")):
        prdtypecode = predict_prdtypecode(designation, description, np.asarray(image))
        category = CATEGORIES_DIC[prdtypecode]
        st.success(f"The product category is {prdtypecode} - {category}")

