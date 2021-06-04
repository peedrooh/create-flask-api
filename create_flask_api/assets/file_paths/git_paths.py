import sys, os
from os.path import join


def git_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'git', 'gitignore'),
            'filename': '.gitignore',
            'output_path': project.project_path
            
        },
    ]