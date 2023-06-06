import os
import datetime
class Test_module():


    def log_text(slef,id):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print(timestamp)
        log_file = f"logs/{id}/log_{timestamp}.txt"
        with open(log_file, "a") as file:
            file.write(f"Hallo ik ben op {timestamp} besmet\n")