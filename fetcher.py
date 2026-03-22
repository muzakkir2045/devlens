import os
from dotenv import load_dotenv
import requests
import base64
from pprint import pprint
load_dotenv()



# def extraction():
    
#     return owner,repo_name


def get_repo_files():
    # url = input("Enter a github repo url : ")
    url = r"https://github.com/muzakkir2045/devlens"
    lst = url.split('/')
    owner = lst[3].strip()
    repo_name = lst[4].strip()

    headers = {
        "Authorization" : f"Bearer {os.getenv("Token")}",
        "Accept": "application/vnd.github+json"
    }
    repo_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/trees/main?recursive=1"
    response = requests.get(repo_url, headers=headers)
    repo_content = response.json()
    # pprint(repo_content)

    CODE_EXTENSIONS = ['.py', '.js', '.ts', '.html', '.css', '.md', '.json', '.yml', '.yaml', '.txt', '.jsx', '.tsx']

    files = [ 
        item['path'] for item in repo_content['tree']
        if item['type'] == 'blob'
        and any(item['path'].endswith(ext) for ext in CODE_EXTENSIONS )
    ]

    content = {}

    for file_path in files:
        content_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}"
        response = requests.get(content_url, headers=headers)
        decoded = base64.b64decode(response.json()['content']).decode('utf-8')
        content[file_path] = decoded
    
    list_content = []

    for k,v in content.items():
        list_content.append({
            'path':k,
            'content':v
    })

    gist = {
        "repo_name" : repo_name,
        "owner": owner,
        "total_files": len(files),
        "files": list_content
    }

    return gist

