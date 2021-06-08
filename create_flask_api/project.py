from os.path import join
import os, subprocess
import re


def get_venv_cmd():
    
    if not subprocess.call("(dir 2>&1 *`|echo CMD);&<# rem #>echo($PSVersionTable).PSEdition", stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT, shell=True, executable="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"):
        return '.\\venv\\Scripts\\activate'

    elif not subprocess.call("source", stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT, shell=True):
        return 'source venv/bin/activate'

    else:
        return '. venv/bin/activate'


class ProjectSpecs:

    def __init__(self, project_path, args):
        self.project_name = args.project_name
        self.folder_name = re.sub("([\\\/:?<>|]*)$", "", args.project_name)
        self.project_path = join(project_path, self.folder_name)
        self.app_path = join(project_path, self.folder_name, "app")
        self.venv_cmd = get_venv_cmd()