from github import Github

github = Github("https://github.com/laurensDSM/python1/blob/master/github.py")
print(github.get_repo())
if __name__ == "__main__":
    pass