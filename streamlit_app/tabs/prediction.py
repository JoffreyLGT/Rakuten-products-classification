import numpy as np
import streamlit as st
from PIL import Image

import sys
sys.path.append('../')

from src.models import predict_prdtypecode

title = "Predict your item category"
sidebar_name = title


def run():
    st.title(title)
    st.warning("Please note that only French language is supported")

    designation = st.text_input(
        "Designation", value="Figurine Skylanders Trap Team Food Fight")
    description = st.text_area(
        "Description", value="Figurine skylanders trap team Food Fight d'élément vie. <br>Elle fonctionne sur le jeu skylanders trap team.")
    uploaded_image = st.file_uploader("Picture", type=["jpg", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image)
    else:
        image = np.zeros((254, 254, 3))

    if (st.button("Predict")):
        prdtypecode = predict_prdtypecode(designation, description, np.asarray(image))
        st.success(f"The product type code is {prdtypecode}")
