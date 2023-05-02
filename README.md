# Product Classification for Rakuten

## 🎯 Objective

This project aims to **automatically categorize products** on an e-commerce platform.

## 📄 Context

**E-commerce** is a competitive market with multiple giant contenders: **Rakuten**, Amazon, CDiscount etc.
They have two types of clients: merchants selling their products on the platform and customers buying them.

In order to provide the best user experience, platforms must provide easy to use interfaces and features to make the selling and buying process as easy as possible :
- A **merchant** should be able to submit their product to sell with guided interface to **maximize their chances to sell** them.
- **Customers** looking for product should be able to find the **product** they are **looking for**, but should also be suggested products that **might interest them**.

This can only be done with **good product classification**. This is why we are going to use **Artificial Intelligence** to help sellers to categorize their products.

## 💻 Project's team

This project was developed by the following team :

- Joffrey Lagut ([GitHub](https://github.com/JoffreyLGT) / [LinkedIn](https://www.linkedin.com/in/joffrey-lagut-9b3b1076/))
- Heiko Agnoli ([GitHub](https://github.com/ha2sunny) / [LinkedIn](https://www.linkedin.com/in/heikoagnoli/))
- Thi Bich Ngan Le ([GitHub](https://github.com/lethibichngan) / [LinkedIn](https://www.linkedin.com/in/thi-bich-ngan-le-287b38127/))


## 🚀 Setup

### Environment

To setup your Python environment and install all the packages, execute the commands bellow:
8
```shell
conda create --name rakuten python=3.9
conda activate rakuten
pip install -r requirements.txt
```

### Demo app

*Be sure to have setup the environment prior to running the streamlit app.*

This project contains a demo app using [Streamlit](https://streamlit.io/).  
Use the commands bellow to start it.

```shell
conda activate rakuten
cd streamlit_app
streamlit run app.py
```

