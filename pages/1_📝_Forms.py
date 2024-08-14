import streamlit as st

from config import set_streamlit_page_config_once
set_streamlit_page_config_once()

from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

#from pages import dataVisualization
import setForm
import closeForm

st.image("images/AMP_Logo.png", width=300)
st.title("Forms Page")

selected = option_menu(
    menu_title=None,
    options=["Setter Form", "Closer Form"],
    icons=["pencil-fill", "bi-brightness-high-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

if selected == "Setter Form":
    setForm.set_form()

if selected == "Closer Form":
    closeForm.close_form()

#if selected == "Data Visualization":
    #dataVisualization.data()
