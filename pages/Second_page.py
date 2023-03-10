import streamlit as st
import requests
import webbrowser


if st.button('Click to run the FIRST MAIN JOB'):
  #requests.post("http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev")
  webbrowser.open_new_tab('http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev')
