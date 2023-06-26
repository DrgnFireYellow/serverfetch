import sys
from rich import print
import requests

def help():
    print("[bold]Serverfetch Help[/bold]")
    print("serverfetch \[type] \[category] \[version] \[file]")

def fetch():
    try:
        f = open(sys.argv[4], "wb")
        f.write(requests.get(f"https://serverjars.com/api/fetchJar/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}").content)
        f.close()
    except:
            help()

fetch()