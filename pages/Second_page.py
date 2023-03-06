import streamlit as st
import requests


if st.button('Click to run the FIRST MAIN JOB'):
  requests.post("http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev")
