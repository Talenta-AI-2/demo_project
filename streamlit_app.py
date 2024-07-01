import streamlit as st
from home import main as home
from chatbot import main as chatbot
from stunting_detection import main as stunting_detection
from nutrition_check import main as nutrition_check

def main():
    st.set_page_config(page_title="Nutrimom App", layout="wide")
    
    st.sidebar.title("Navigasi")
    page = st.sidebar.radio("Pilih halaman:", ["home", "stunting detection", "nutrition check","chatbot"])
    
    if page == "home":
        home()
    elif page == "stunting detection":
        stunting_detection()
    elif page == "nutrition check":
        nutrition_check()
    elif page == "chatbot":
        chatbot()

if __name__ == "__main__":
    main()
