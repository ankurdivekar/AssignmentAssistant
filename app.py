import streamlit as st
import git
import requests

st.title('Assignment Checker')

repo_url = st.text_input("Enter GitHub repo URL",)

if not (repo_url.startswith('https://') or repo_url.startswith('http://')):
    repo_url = f'https://{repo_url}'

response = requests.get(repo_url)
if response.status_code == 200:
    st.write('Repo found. Checking now...')
else:
    st.write(f'Repo not found! Is the URL correct? ({repo_url})')