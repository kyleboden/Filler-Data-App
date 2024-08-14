from config import set_streamlit_page_config_once
set_streamlit_page_config_once()

import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime, timedelta
import database as db
from config import closers, setters




st.image("images/AMP_Logo.png", width=300)

def filter_data(df, date_column, start_date, end_date):
    # Ensure the date_column is in datetime format
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    df_filtered = df[df[date_column].between(start_date, end_date)]
    df_filtered['Day of Week'] = df_filtered[date_column].dt.day_name()
    return df_filtered

def get_counts_for_days(df):
    counts = {day: 0 for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}
    for day in counts.keys():
        counts[day] = df[df['Day of Week'] == day].shape[0]
    return counts

def create_summary_df(counts_dict, metrics):
    data = {
        'Metric': metrics,
        'Monday': [counts['Monday'] for counts in counts_dict.values()],
        'Tuesday': [counts['Tuesday'] for counts in counts_dict.values()],
        'Wednesday': [counts['Wednesday'] for counts in counts_dict.values()],
        'Thursday': [counts['Thursday'] for counts in counts_dict.values()],
        'Friday': [counts['Friday'] for counts in counts_dict.values()],
        'Total': [sum(counts.values()) for counts in counts_dict.values()]
    }
    return pd.DataFrame(data)

def highlight_row_column(row):
    if row['Name'] == 'Total':
        return ['font-weight: bold' for _ in row]
    else:
        return ['font-weight: bold'] + ['' for _ in row[1:]]

def highlight_cells(val, col_name):
    if col_name in ['Total', 'Metric']:
        return 'background-color: #BDCEE1; font-weight: bold'  # Light blue background for 'Total'
    if col_name in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        return 'background-color: #d9edf7'  # Light yellow for days of the week
    return ''

def create_table(df, highlight_func, width="100%"):
    styled_df = df.style.apply(highlight_func, axis=1).hide(axis='index')
    html = styled_df.to_html()
    return f'<div style="width: {width};">{html}</div>'

# Initialize Google Sheets and load data
sheet = db.sheet
df = pd.DataFrame(sheet.get_all_records())

# Define date ranges
today = datetime.now()
start_of_week = today - timedelta(days=today.weekday())
end_of_week = start_of_week + timedelta(days=4)
start_of_month = today.replace(day=1)
start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)

# Debug: Print DataFrame and column types
print(df.head())
print(df.columns)
print(df.dtypes)

# Filter data
filtered_sets_df = filter_data(df, 'Set Date', start_of_week, end_of_week)
filtered_closes_df = filter_data(df[df['Closer Disposition'] == 'Closed'], 'Close Date', start_of_week, end_of_week)
filtered_appts_df = filter_data(df[df['Close Date'].notna()], 'Close Date', start_of_week, end_of_week)
filtered_dnqs_df = filter_data(df[df['Closer Disposition'] == 'DNQ'], 'Close Date', start_of_week, end_of_week)
filtered_sits_df = filter_data(df[df['Closer Disposition'] != 'No Sit'], 'Close Date', start_of_week, end_of_week)


# Get counts for each type
metrics = ['Sets', 'Appointments', 'Closes', 'DNQs', 'Sits']
counts_dict = {
    'Sets': get_counts_for_days(filtered_sets_df),
    'Appointments': get_counts_for_days(filtered_appts_df),
    'Closes': get_counts_for_days(filtered_closes_df),
    'DNQs': get_counts_for_days(filtered_dnqs_df),
    'Sits': get_counts_for_days(filtered_sits_df)
}

# Create summary DataFrame
summary_df = create_summary_df(counts_dict, metrics)

# Create and style individual tables
closer_data = {
    'Name': closers + ['Total'],
    'Today\'s Closes': [filtered_closes_df[filtered_closes_df['Closer Name'] == closer].shape[0] for closer in closers] + [filtered_closes_df.shape[0]],
    'Current Week\'s Closes': [filtered_closes_df[filtered_closes_df['Closer Name'] == closer].shape[0] for closer in closers] + [filtered_closes_df.shape[0]],
    'Current Month\'s Closes': [filtered_closes_df[filtered_closes_df['Closer Name'] == closer].shape[0] for closer in closers] + [filtered_closes_df.shape[0]]
}
html_closer = create_table(pd.DataFrame(closer_data), highlight_row_column, width="100%")

setter_close_data = {
    'Name': setters + ['Total'],
    'Today\'s Closes': [filtered_closes_df[filtered_closes_df['Setter Name'] == setter].shape[0] for setter in setters] + [filtered_closes_df.shape[0]],
    'Current Week\'s Closes': [filtered_closes_df[filtered_closes_df['Setter Name'] == setter].shape[0] for setter in setters] + [filtered_closes_df.shape[0]],
    'Current Month\'s Closes': [filtered_closes_df[filtered_closes_df['Setter Name'] == setter].shape[0] for setter in setters] + [filtered_closes_df.shape[0]]
}
html_setter_close = create_table(pd.DataFrame(setter_close_data), highlight_row_column, width="100%")

setter_set_data = {
    'Name': setters + ['Total'],
    'Today\'s Sets': [filtered_sets_df[filtered_sets_df['Setter Name'] == setter].shape[0] for setter in setters] + [filtered_sets_df.shape[0]],
    'Current Week\'s Sets': [filtered_sets_df[filtered_sets_df['Setter Name'] == setter].shape[0] for setter in setters] + [filtered_sets_df.shape[0]],
    'Current Month\'s Sets': [filtered_sets_df[filtered_sets_df['Setter Name'] == setter].shape[0] for setter in setters] + [filtered_sets_df.shape[0]]
}
html_setter_set = create_table(pd.DataFrame(setter_set_data), highlight_row_column, width="100%")

# Style the summary table with color
styled_summary_df = summary_df.style.applymap(lambda v: highlight_cells(v, 'Metric'), subset=['Metric']) \
    .applymap(lambda v: highlight_cells(v, 'Total'), subset=['Total']) \
    .applymap(lambda v: highlight_cells(v, 'Metric'), subset=['Metric']) \
    .applymap(lambda v: highlight_cells(v, 'Monday'), subset=['Monday']) \
    .applymap(lambda v: highlight_cells(v, 'Tuesday'), subset=['Tuesday']) \
    .applymap(lambda v: highlight_cells(v, 'Wednesday'), subset=['Wednesday']) \
    .applymap(lambda v: highlight_cells(v, 'Thursday'), subset=['Thursday']) \
    .applymap(lambda v: highlight_cells(v, 'Friday'), subset=['Friday']) \
    .hide(axis='index')

html_summary = styled_summary_df.to_html()

# Add custom CSS for centering the summary table
center_css = """
<style>
    .center-table {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    .center-table h2 {
        margin-bottom: 20px;  /* Space between title and table */
    }
    .scaled-table {
        width: 60%;
        transform: scale(2);  /* Adjust scaling factor as needed */
        transform-origin: 0 0;
    }
</style>
"""

# Title for the summary table
summary_title = "<h2>Weekly Summary Table</h2>"

# Centered and scaled HTML for the summary table with color
centered_html_summary = f"""
<div class="center-table">
    {summary_title}
    <div class="scaled-table">
        {html_summary}
</div>
"""

# Create three columns for the individual tables at the top
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Closers")
    st.markdown(html_closer, unsafe_allow_html=True)

with col2:
    st.header("Setters Close Table")
    st.markdown(html_setter_close, unsafe_allow_html=True)

with col3:
    st.header("Setters Set Table")
    st.markdown(html_setter_set, unsafe_allow_html=True)

# Add the summary table
st.markdown(center_css, unsafe_allow_html=True)  # Add custom CSS
st.markdown(centered_html_summary, unsafe_allow_html=True)  # Add the centered and scaled summary table
