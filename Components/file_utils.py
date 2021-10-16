from pathlib import Path
import shutil


def clear_repo_path(repo_path):
    shutil.rmtree(repo_path)


def create_test_submission(repo_path):

    for week in range(1, 9):
        week_dir = f'{repo_path}/Week_{week:02}'
        Path(week_dir).mkdir(parents=True, exist_ok=True)
        for submission in range(1, 8):
            file_path = f'{week_dir}/Assignment{submission:02}.py'
            with open(file_path, 'w') as fp:
                pass