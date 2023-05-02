import numpy as np
import streamlit as st
from PIL import Image
import re
import sys
sys.path.append('../')
from src.models import predict_prdtypecode
from src.data.data import CATEGORIES_DIC, DATA_SAMPLE, get_random_product, load_data


def set_example():
    example = next(x for x in DATA_SAMPLE if x[0] ==
                    st.session_state["example"])
    st.session_state["designation"] = example[1]
    st.session_state["description"] = example[2]
    st.session_state["image"] = example[3]

def set_image():
    st.session_state["image"] = st.session_state["image_uploader"]

def set_random_product():
    data = load_data("../data").fillna("")
    prdtypecode = re.findall("[0-9]*", st.session_state["random"])[0]
    designation, description, image = get_random_product(int(prdtypecode), data)
    st.session_state["designation"] = designation
    st.session_state["description"] = description
    st.session_state["image"] = image

title = "Predict your item category"
sidebar_name = title

def run():
    # Set default session_state on the first run
    if "image" not in st.session_state:
        st.session_state["image"] = ""

    st.title(title)
    st.warning("Please note that only French language is supported")
    
    with st.expander(label="Predefined examples"):
        col_predif, col_random = st.columns([1,1])
        with col_predif:
            st.selectbox(label="Example from the list",
                         key="example",
                         options=["", *[i[0] for i in DATA_SAMPLE]],
                         on_change=set_example)

        with col_random:
            st.selectbox(label="Random example from a category",
                         key="random",
                         options=["", *[f"{i} - {CATEGORIES_DIC[i]}" for i in 
                                    list(CATEGORIES_DIC.keys())]],
                         on_change=set_random_product)

    designation = st.text_input(label="Designation", key="designation")
    description = st.text_area(label="Description", key="description")

    col_widget, col_preview = st.columns([5,2])
    with col_widget:
        st.file_uploader(label="Picture", type=["jpg", "jpeg"],
                         on_change=set_image, key="image_uploader")
                                         
    with col_preview:
        if st.session_state["image"] is not "":
            image = Image.open(st.session_state["image"])
            st.image(image)
        else:
            image = np.zeros((254, 254, 3))

    if (st.button(label="Predict", type="primary")):
        # Get the predictions from model
        predictions = predict_prdtypecode(designation, description, np.asarray(image))
        # Get the top best prediction, which in at the first position
        # since the predictions are sorted by probabilities descending
        top_prdtypecode = predictions[0][0][0]
        top_category = CATEGORIES_DIC[top_prdtypecode]
        st.success(f"The product category is {top_prdtypecode} - {top_category}.")
        # Display the top 3 probabilities
        top_3 = [f"{i[0]} - {CATEGORIES_DIC[i[0]]} : {i[1]}%" for i in predictions[0][0:3]]
        text_top_categories = "Bellow are the top 3 probabilities:"
        for category in top_3:
            text_top_categories += f"""  
            - {category}"""
        st.markdown(text_top_categories)
        # Cheap way an extra line down the screen and not have the text too low
        st.write("")
        
