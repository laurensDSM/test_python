import git
import json
import os
import shutil

class Github():
    def __init__(self,repo_url):
        self.repo_url = repo_url
        
    def get_repo(self):
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repo_url, local_directory)
            response = None
            config_file_path = os.path.join(local_directory, "config", "config.txt")
            if os.path.exists(config_file_path):
                with open(config_file_path, "r") as file:
                    response = file.read()
            repo.close()
            shutil.rmtree(local_directory)
            if response:
                return True
            else:
                return False
        except (git.exc.GitCommandError, FileNotFoundError):
            return False
        

    def get_config(self):
        pass
    def log_data():
        pass