
import os
from fetcher import get_repo_files
from pprint import pprint

data = get_repo_files()

CODE_EXTENSIONS = ['.py', '.js', '.ts', '.html', '.css', '.md', '.json', '.yml', '.yaml', '.txt', '.jsx', '.tsx']

languages = {
    '.py':'Python',
    '.js':'JavaScript',
    '.ts' : 'Typescript',
    '.html' : 'Html',
    '.css' : 'CSS',
    '.jsx' : 'React - JS',
    '.tsx' : 'React - TS'

}


def file_map():
    path_content = {}
    for d in data['files']:
        path_content[d['path']] = d['content']
    
    return path_content

new = file_map()

for path,content in new.items():
    pass

def entry():
    target_files = {'app.py','main.py','index.js'}
    data = file_map()
    entry_points = []
    for key in data.keys():
        file_name = os.path.basename(key)
        if file_name in target_files:
            entry_points.append(key)
    else:
        if entry_points == []:
            return None
    return entry_points


def config():
    target_files = {'requirements.txt','config.yaml','config.json'}
    data = file_map()
    config_files = []
    for key in data.keys():
        file_name = os.path.basename(key)
        if file_name in target_files:
            config_files.append(key)
    else:
        if config_files == []:
            return None
    return config_files

for path in file_map().keys():
    file_name = path.split('/')[-1]

    if file_name == 'README.md':
        readme = path
    else:
        readme = None


# print(f"The entry files are : {entry()}")
# print(f"The config files are : {config()}")
