import streamlit as st
import requests
import subprocess
import shlex

st.title("Test curl command")

matillion = 'curl -X POST -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev'
cmd = '''curl -X POST -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev'''

if st.button('Click to run the FIRST MAIN JOB'):
  x = requests.get('http://51.103.32.188/rest/v1', auth = ('azure-user', 'azure-user'))
  st.text(x)
  
#   subprocess.call([
#     'curl',
#     '-X',
#     'POST',
#     '-u',
#     'azure-user:azure-user',
#     '-k',
#     'http://51.103.32.188/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/1bis-New_data_ingestion/run?environmentName=dev'
#     ])

#   args = shlex.split(cmd)
#   process=subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#   stdout, stderr = process.communicate()

