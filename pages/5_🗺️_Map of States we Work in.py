from config import set_streamlit_page_config_once
set_streamlit_page_config_once()

import pandas as pd
import plotly.express as px
import streamlit as st

st.image("images/AMP_Logo.png", width=300)
st.title("Map of States we Work in")


# Define the data with finance providers
data = {
    'states': ['California', 'Kentucky', 'Ohio', 'Illinois', 'Florida', 'Texas', 'Vermont', 'Maine', 'Massachusetts', 'Connecticut', 'New Hampshire', 'Rhode Island', 'New Jersey', 'Utah', 'Georgia', 'Iowa', 'North Carolina', 'South Carolina', 'West Virginia', 'Virginia', 'Montana', 'Wyoming'],
    'states_code': ['CA', 'KY', 'OH', 'IL', 'FL', 'TX', 'VT', 'ME', 'MA', 'CT', 'NH', 'RI', 'NJ', 'UT', 'GA', 'IA', 'NC', 'SC', 'WV', 'VA', 'MT', 'WY'],
    'Installer': ['ESP', 'Ecovole, Kin', 'Kin', 'Aveyo', 'Kin', 'Kin, Trismart', 'Sunshine', 'Sunshine', 'Sunshine', 'Sunshine', 'Sunshine', 'Sunshine', 'Sunshine', 'Kin', 'Lumina', 'Kin', 'Lumina', 'Lumina', 'Lumina', 'Lumina', 'Lumina', 'Lumina'],
    'We_Work': [2000, 3000, 4000, 5000, 4000, 4000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 4000, 6000, 4000, 6000, 6000, 6000, 6000, 6000, 6000],
}
# finance_providers = {
#     'ESP': 'Enfin<br>Dividend<br>Goodleap<br>Mosaic<br>Thrive PPA',
#     'Ecovole': 'Enfin<br>Dividend<br>Goodleap<br>Mosaic<br>Sunlight<br>Sungage',
#     'Kin Home': 'Enfin<br>Dividend<br>Goodleap<br>Mosaic<br>Sunlight<br>Sungage',
#     'Aveyo': 'Goodleap<br>Sunlight<br>Skeps<br>Sunnova',
#     'Sunshine': 'Enfin<br>Goodleap<br>Sunlight<br>Mosaic<br>Skylight<br>Lightreach<br>Posigen<br>Concert',
#     'Lumina': 'Sunlight<br>Goodleap<br>Sunnova'
# }

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the choropleth map
fig = px.choropleth(df,
                    locations='states_code',
                    locationmode="USA-states",
                    scope="usa",
                    color='We_Work',
                    color_continuous_scale="haline")

fig.update_geos(showcoastlines=False,
                 lakecolor='white',
                 landcolor='white',
                 showland=True,
                 showlakes=True,
                 showsubunits=True,
                 subunitcolor="black",  # Border color for states
                 subunitwidth=.5)      # Border width for states

# Update the layout to make the figure larger
fig.update_layout(
    #autosize=True,
    width=1200,  # Set the width to 1000 pixels
    height=800,  # Set the height to 600 pixels
    margin=dict(l=0, r=0, t=0, b=0)  # Remove margins
)

# Display the map in a Streamlit app with adjusted size
st.plotly_chart(fig, use_container_width=True)
image_path ="images/BAUStateData.png"
st.image(image_path, use_column_width=True)

#
# # Create a table with installers, states, and finance providers
# installers = df['Installer'].unique()
# installers.sort()  # Sort the installers list
#
# # Create a dictionary to hold states for each installer
# installers_dict = {
#     installer: {
#         'states': df[df['Installer'] == installer]['states_code'].tolist(),
#         'finance_providers': finance_providers.get(installer, '')
#     }
#     for installer in installers
# }
#
# # Prepare the Markdown table
# markdown_table = '| Installer | States | Finance Providers |\n'
# markdown_table += '| --- | --- | --- |\n'
# for installer in installers:
#     states_list = '<br>'.join(f'• {state}' for state in installers_dict[installer]['states'])
#     finance_providers = installers_dict[installer]['finance_providers']
#     markdown_table += f'| {installer} | {states_list} | {finance_providers} |\n'
#
# # Display the table in the Streamlit app
# st.markdown(markdown_table, unsafe_allow_html=True)
