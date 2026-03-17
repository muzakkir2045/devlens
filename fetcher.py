import os
from dotenv import load_dotenv
import requests
import base64
from pprint import pprint
load_dotenv()

url = input("Enter a github repo url : ")

def extraction(url):
    lst = url.split('/')
    owner = lst[3].strip()
    repo_name = lst[4].strip()
    return owner,repo_name


def get_repo_files(owner, repo_name):
    headers = {
        "Authorization" : f"Bearer {os.getenv("token")}",
        "Accept": "application/vnd.github+json"
    }
    repo_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/trees/main?recursive=1"
    response = requests.get(repo_url, headers=headers)
    repo_content = response.json()
    # pprint(content)

    files = [ item['path'] for item in repo_content['tree'] if item['type'] == 'blob']
    print(files)

    content = {}

    for file_path in files:
        content_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}"
        response = requests.get(content_url, headers=headers)
        decoded = base64.b64decode(response.json()['content']).decode('utf-8')
        content[file_path] = decoded
    
    print(content)

    
owner, repo_name = extraction(url)

get_repo_files(owner, repo_name)
