import streamlit as st
import git
from git import Repo
import requests
from Components.file_utils import clear_repo_path

st.title('Assignment Checker')

repo_url = st.text_input("Enter GitHub repo URL", 'github.com/ankurdivekar/TinyTools')

if not (repo_url.startswith('https://') or repo_url.startswith('http://')):
    repo_url = f'https://{repo_url}'

response = requests.get(repo_url)
if response.status_code != 200:
    st.write(f'Repo not found! Is the URL correct? ({repo_url})')
else:
    url_split = repo_url.split('/')
    repo_name = url_split[-1]
    user_name = url_split[-2]

    st.write(f'Checking repo {repo_name} for user {user_name}')

    # Set path for local temporary copy of repo
    tmp_repo_path = 'Data/tmp_repo/'

    # Clone repo locally
    clear_repo_path(tmp_repo_path)
    st.write('Cloning repo..')
    Repo.clone_from(repo_url, tmp_repo_path)
    st.write('Repo cloned')
