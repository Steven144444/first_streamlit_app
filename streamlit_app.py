import streamlit as st
st.title("My Mom's New Healthy Diner")

st.header("Breakfast Favorites")
st.text("Omega 3 & Blueberry Oatmeal")
st.text("Kale, Spinach & Rocket Smoothie")
st.text("Hard Boiled Free-Range Egg")
st.text("Avocado Toast")

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.header("Build Your Own Fruit Smoothie")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

#New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about ?')
st.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# normalization
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output as a table
st.dataframe(fruityvice_normalized)

# don't run anything past here while we troubleshoot
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_fruit = st.text_input('What fruit would you like to eat ?')
st.write('Thanks for adding ', add_my_fruit)

# This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from_streamlit')")
