from config import set_streamlit_page_config_once

set_streamlit_page_config_once()

import streamlit as st

# --- NAVIGATION MENU ---
st.markdown(
    """
    <style>
    .css-1cpxqw2 {
        width: 100% !important;  /* Adjust the width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)
AMP_Logo = "images/AMP_Logo.png"


st.image(AMP_Logo, width=300)

def main():
    st.title("Home Page")
    st.write("Welcome to the main page! Use the buttons to navigate to other pages.")


    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <style>
            .custom-button {
                display: flex; /* Use flexbox for centering */
                justify-content: center; /* Center text horizontally */
                align-items: center; /* Center text vertically */
                width: 300px; 
                height: 150px; 
                font-size: 25px; 
                font-weight: bold;
                color: white !important; /* Font color */
                background-color: #7AC1E0;
                border: none;
                border-radius: 5px;
                text-align: center;
                cursor: pointer;
                text-decoration: none;
                box-sizing: border-box;
                margin: 10px;
                padding: 0; /* Remove default padding to fit the height */
                white-space: normal; /* Allow text to wrap */
                word-wrap: break-word; /* Ensure long words break to the next line */
            }
            .custom-button:hover {
                background-color: #2fafff;
                color: #ffffff; /* Font color on hover */
            }
            </style>
            <a href="https://bau-app-new-e9uvydrunsxvh8pn5w627h.streamlit.app/Forms" class="custom-button">Go to Forms Page</a>
            <a href="https://bau-app-new-e9uvydrunsxvh8pn5w627h.streamlit.app/Data_Visualization" class="custom-button">Go to Data Visualization Page</a>
            <a href="https://bau-app-new-e9uvydrunsxvh8pn5w627h.streamlit.app/TV_Display" class="custom-button">Go to TV Display Page</a>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <a href="https://bau-app-new-e9uvydrunsxvh8pn5w627h.streamlit.app/Close_Tracker" class="custom-button">Go to Close Tracker Page</a>
            <a href="https://bau-app-new-e9uvydrunsxvh8pn5w627h.streamlit.app//Map_of_States_we_Work_in" class="custom-button">Go to Maps of States Page</a>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()







