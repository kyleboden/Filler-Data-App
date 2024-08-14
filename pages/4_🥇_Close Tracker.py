from config import set_streamlit_page_config_once
set_streamlit_page_config_once()

import streamlit as st


# Page-specific code
st.image("images/AMP_Logo.png", width=300)
st.title("Close Tracker")
google_sheet_url = "https://docs.google.com/spreadsheets/d/1idziebQqf5CVqqQ64IINvdJXXCZtL5N0Yf_UCAbXEGE/edit?gid=0#gid=0"
st.write("Open the Google Sheet [here](%s)." % google_sheet_url)
