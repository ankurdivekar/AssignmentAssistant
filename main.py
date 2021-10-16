from git import Repo
from Components.github_utils import *
from Components.file_utils import *

user_name = "ankurdivekar"
repo_name = "Heimdall"
file_name = "ID_Manager.py"

# Get url for public repo
git_url = get_repo_url(user_name, repo_name)

# Set path for local temporary copy of repo
tmp_repo_path = 'Data/tmp_repo/Level_1'

# Clone repo locally
# Repo.clone_from(git_url, tmp_repo_path)

# Generate some files to test directory stucture
create_test_submission(tmp_repo_path)

# Delete test submission
# clear_repo_path(tmp_repo_path)
