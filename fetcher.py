
import requests
import base64
from pprint import pprint

url = input("Enter a github repo url : ")

def extraction(url):
    lst = url.split('/')
    owner = lst[3]
    repo_name = lst[4]
    return owner,repo_name

def get_repo_files(owner, repo_name):

    repo_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/trees/main?recursive=1"
    response = requests.get(repo_url)
    content = response.json()
    # pprint(content)

    files = [ item['path'] for item in content['tree'] if item['type'] == 'blob']
    print(files)

    content = {}

    for file_path in files:
        content_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}"
        response = requests.get(content_url)
        decoded = base64.b64decode(response.json()['content']).decode('utf-8')
        content[file_path] = decoded
    
    print(content)

    
owner, repo_name = extraction(url)

get_repo_files(owner, repo_name)
