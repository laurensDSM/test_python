from github import Github
import pyuac

def main():
    github = Github()
    print(github.get_repo())

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
        main()


