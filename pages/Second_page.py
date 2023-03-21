import streamlit as st
import subprocess
import shlex
import pandas as pd
import json
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient



###Azure VM launch###
st.title("Launch the Azure VM 🎸")
if st.button('Click here to launch the VM before querying matillion ⚡'):
      pass



###Curl Command running###
st.title("Test the curl command 🎸")
# command = ['curl', '-X', 'POST', '-u', '[user_name]:[password]', '-k', 'http://[instance_address]/rest/v1/group/name/smensah/project/name/yelp/version/name/default/job/name/test/run?environmentName=dev']

#select your group name
group_list_curl_command = 'curl -X GET -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group'
lauch_group_list_curl_command = subprocess.run(shlex.split(group_list_curl_command), capture_output=True, text=True)
group_list = json.loads(lauch_group_list_curl_command.stdout)
group_selected = st.selectbox('Select your group name :', group_list)
st.write('You selected : ', group_selected,'group')

#select your project name
project_list_curl_command = 'curl -X GET -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/'+group_selected+'/project'
lauch_project_list_curl_command = subprocess.run(shlex.split(project_list_curl_command), capture_output=True, text=True)
project_list = json.loads(lauch_project_list_curl_command.stdout)
project_selected = st.selectbox('Select your project name :', project_list)
st.write('You selected : ', project_selected,'project')

#select your version name
version_list_curl_command = 'curl -X GET -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/'+group_selected+'/project/name/'+project_selected+'/version'
lauch_version_list_curl_command = subprocess.run(shlex.split(version_list_curl_command), capture_output=True, text=True)
version_list = json.loads(lauch_version_list_curl_command.stdout)
version_selected = st.selectbox('Select your version name :', version_list)
st.write('You selected : ', version_selected,'version')

#select your job name
job_list_curl_command = 'curl -X GET -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/'+group_selected+'/project/name/'+project_selected+'/version/name/'+version_selected+'/job'
lauch_job_list_curl_command = subprocess.run(shlex.split(job_list_curl_command), capture_output=True, text=True)
job_list = json.loads(lauch_job_list_curl_command.stdout)
job_selected = st.selectbox('Select your job name :', job_list)
st.write('You selected : ', job_selected,'job')

#select your environment name
environment_list_curl_command = 'curl -X GET -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/'+group_selected+'/project/name/'+project_selected+'/environment'
lauch_environment_list_curl_command = subprocess.run(shlex.split(environment_list_curl_command), capture_output=True, text=True)
environment_list = json.loads(lauch_environment_list_curl_command.stdout)
environment_selected = st.selectbox('Select your environment name :', environment_list)
st.write('You selected : ', environment_selected,'environment')


#Run the matillion job
curl_command = 'curl -X POST -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/'+group_selected+'/project/name/'+project_selected+'/version/name/'+version_selected+'/job/name/'+job_selected+'/run?environmentName='+environment_selected
if st.button('Click here to run the selected job ⚡'):
  result1 = subprocess.run(shlex.split(curl_command), capture_output=True, text=True)
  #Display job details
  st.text(result1.stderr)
  st.dataframe(json.loads(result1.stdout))
  #Fetch the task id
  id = str(json.loads(result1.stdout)["id"])
  st.header('Task Id : '+id)
  #Get deatils of the task
  st.header('Task details')
  get_task_details = 'curl -X GET -u azure-user:azure-user -k http://51.103.32.188/rest/v1/group/name/'+group_selected+'/project/name/yelp/task/id/'+id
  result2 = subprocess.run(shlex.split(get_task_details), capture_output=True, text=True)
  st.dataframe(json.loads(result2.stdout))

  if json.loads(result1.stdout)["success"]==True and json.loads(result2.stdout)["state"]=="SUCCESS":
        st.success('Congratulations ! The curl command works successfully !!!', icon="✅")
        st.balloons()
  else:
      st.error('Sorry. The curl command didnt work successfully !', icon="🚨")
