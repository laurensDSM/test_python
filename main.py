from github import Github

def main():
    github = Github('https://github.com/laurensDSM/python1.git')
    print(github.get_repo())

if __name__ == "__main__":

        main()


