from config import set_streamlit_page_config_once
set_streamlit_page_config_once()

import streamlit as st


# Page-specific code
st.image("images/AMP_Logo.png", width=300)
st.title("Close Tracker")
google_sheet_url = "https://docs.google.com/spreadsheets/d/1ofC-iCsJ6p7HBAfgcQ6qzw8eQLaSU5tTa6OzYln7dO0/edit?gid=616940338#gid=616940338"
st.write("Open the Google Sheet [here](%s)." % google_sheet_url)
