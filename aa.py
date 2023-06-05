import os
import datetime
class Test_module():
    def log_text(text = "Hallo ik ben een test"):
        log_folder = "logs"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = f"{log_folder}/log_{timestamp}.txt"
        
        with open(log_file, "a") as file:
            file.write(f"{text}\n")