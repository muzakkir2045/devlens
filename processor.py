
import os
from fetcher import get_repo_files
from pprint import pprint

data = get_repo_files()

CODE_EXTENSIONS = ['.py', '.js', '.ts', '.html', '.css', '.md', '.json', '.yml', '.yaml', '.txt', '.jsx', '.tsx']

EXTENSION_MAP = {
    '.py':'Python',
    '.js':'JavaScript',
    '.ts' : 'Typescript',
    '.html' : 'Html',
    '.css' : 'CSS',
    '.jsx' : 'React - JS',
    '.tsx' : 'React - TS'

}
FRAMEWORK_MAP = {
    'requirements.txt': 'Flask/Python project',
    'package.json':     'Node.js project',
    'manage.py':        'Django',
    'pom.xml':          'Java/Maven',
    'Dockerfile':       'Docker',
}

def file_map():
    path_content = {}
    for d in data['files']:
        path_content[d['path']] = d['content']
    return path_content


def detect_languages():
    languages = set()
    for path in file_map().keys():
        ext = os.path.splitext(path)[1]
        if ext in EXTENSION_MAP:
            languages.add(EXTENSION_MAP[ext])
    return languages if languages else None

has_tests = any('test' in path.lower() for path in file_map().keys())

def framework():

    frameworks = []
    for path in file_map().keys():
        fwk = os.path.basename(path)
        if fwk in FRAMEWORK_MAP:
            frameworks.append(FRAMEWORK_MAP[fwk])
    return frameworks if frameworks else None





def entry():
    target_files = {'app.py','main.py','index.js'}
    entry_points = [
        key for key in file_map().keys()
        if os.path.basename(key) in target_files
    ]
    return entry_points if entry_points else None


def config():
    target_files = {'requirements.txt','config.yaml','config.json'}
    config_files = [
        key for key in file_map().keys()
        if os.path.basename(key) in target_files
    ]
    return config_files if config_files else None


def find_readme():
    for path in file_map().keys():
        if path.split('/')[-1] == 'README.md':
            return path
    return None

