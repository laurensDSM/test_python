import git
import json
import os
import shutil

class Github():
    def __init__(self,repo_url):
        self.repo_url = repo_url

    def check_update(self):
        """Controleer de remote repo op een een config """
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

    
    def get_config(self):
        pass

    def send_logs_to_github(self):

            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repo_url, local_directory)

            logs_directory = os.path.join(local_directory, "logs")
            log_files = os.listdir(logs_directory)

            for file_name in log_files:
                file_path = os.path.join(logs_directory, file_name)
                shutil.copy(file_path, local_directory)

            repo.git.add(all=True)
            repo.index.commit("Add new log entries")
            origin = repo.remote(name="origin")
            origin.push()

            repo.close()
            shutil.rmtree(local_directory)

            return True
            return False