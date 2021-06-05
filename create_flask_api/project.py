from os.path import join
import os, subprocess
import re


class ProjectSpecs:

    def __init__(self, project_path, args):
        self.project_name = args.project_name
        self.folder_name = re.sub("([\\\/:?<>|]*)$", "", args.project_name)
        self.project_path = join(project_path, self.folder_name)
        self.app_path = join(project_path, self.folder_name, "app")
        self.venv_cmd = 'source' if not subprocess.call(["source"], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT, shell=True) else "."