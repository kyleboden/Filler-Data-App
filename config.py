import calendar  # Core Python Module
import streamlit as st  # pip install streamlit
import datetime  # Core Python Module
import pytz

page_title = "AMP Smart BAU"
page_icon = ":money_with_wings:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
setters = ['','Hunter Bolen', 'Jake Bolen', 'Danny Timmreck', 'Joshua Killpack', 'Closer Self-Gen']
closers = ['','Kyle Boden', 'Spencer Jackson', 'Michael Oliveira']
states = ['', 'CA', 'CT',  'FL', 'IA', 'IL', 'GA', 'KY', 'MA', 'ME', 'MO', 'NH', 'NJ', 'OH', 'RI', 'TX', 'UT', 'VT']
dispositions = ['', 'Closed', 'No Sit', 'Not Interested', 'Reschedule', 'Pitched, need to Follow Up', 'DNQ', 'We didn\'t call']
system_details = ['', 'System Size in kW', 'Sold PPW', 'Loan Amount']
lenders = ['', 'Enfin', 'Dividend', 'Goodleap', 'Sunlight', 'Mosaic', 'Enium', 'Skylight', 'Palmetto', 'Sunnova', 'Thrive', 'Sungage', 'Cash']
purch_prefs = ['', 'Loan', 'Cash', 'PPA']
set_date = ''
set_time = ''
setter_name = ''
cx_state = ''
cx_name = ''
cx_email = ''
set_comment = ''
close_date = ''
close_time = ''
closer_name = ''
closer_disp = ''
lender = ''
purch_pref = ''
close_comment = ''
syst_size = ''
sold_ppw = ''
loan_amount = ''
#check boxes
lock_close = False
vid_call = False
both_spouses = False
had_UB = False
unpaid_lead = False
on_time = ''
percent_offset = ''

def set_streamlit_page_config_once():
    try:
        st.set_page_config(page_title="Filler Data", page_icon='☼', layout="wide")
        #st.title(page_title + " " + page_icon)
    except st.errors.StreamlitAPIException as e:
        if "can only be called once per app" in e.__str__():
            # ignore this error
            return
        raise e

def get_nearest_15_minute_time():
    timezone = pytz.timezone('America/Denver')  # MDT timezone
    now = datetime.datetime.now(timezone)
    rounded_minute = 15 * round(now.minute / 15)
    if rounded_minute == 60:
        rounded_minute = 0
        now += datetime.timedelta(hours=1)
    return datetime.time(now.hour, rounded_minute)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
#years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
