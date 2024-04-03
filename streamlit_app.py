"""Test for Search Bar und Filter"""


import streamlit as st
import pandas as pd      


#We create a CSV document and give it a DATA URL
DATA_URL = 'Exchange_Partner_list_Test.csv'


#We write functions that Load our data into the web application
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()

#Create the Sidebar filters 
continent_filter = st.sidebar.selectbox('Select Continent', ['All'] + sorted(data['Continent'].unique()))
country_filter = st.sidebar.selectbox('Select Country', ['All'] + sorted(data['Country'].unique()))
academic_level_filter = st.sidebar.selectbox('Select Level for Exchange', ['All', 'Bachelor', 'Master'])
exchange_type_filter = st.sidebar.selectbox('Select Exchange Program', ['All', 'Partner University', 'Free Mover'])


#Create Search bar
search_query = st.text_input('Search for a university')

# Create Function to filter data based on selections
def filter_data(data):
    if continent_filter != 'All':
        data = data[data['Continent'] == continent_filter]
    if country_filter != 'All':
        data = data[data['Country'] == country_filter]
    if academic_level_filter != 'All':
        data = data[data['Level for Exchange'] == academic_level_filter]
    if exchange_type_filter != 'All':
        data = data[data['Exchange Program'] == exchange_type_filter]
    if search_query:
        data = data[data['University Name'].str.contains(search_query, case=False)]
    return data

# Now when you call the filter_data function, pass 'data' as the argument
filtered_data = filter_data(data)


# Display the filtered data
def display_universities(dataframe):
    for index, row in dataframe.iterrows():
        # I only did it now for three things: Name, Country and Continent 
        with st.container():
            st.write(f"### {row['University Name']}")
            st.write(f"Country: {row['Country']}")
            st.write(f"Continent: {row['Continent']}")
            # We add more later

# Call the display function with the filtered data
display_universities(filtered_data)
