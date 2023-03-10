import streamlit as st
import requests
import webbrowser
import subprocess

matillion = 'curl -X POST -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev'

if st.button('Click to run the FIRST MAIN JOB'):
  #requests.post("http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev")
  #webbrowser.open_new_tab('http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev')
  subprocess.call([
    'curl',
    '-X',
    'POST',
    '-u',
    azure-user:azure-user,
    '-k',
    'http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev'
    ])
