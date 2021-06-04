import sys, os
from os.path import join


def view_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'view', 'user_view'),
            'filename': 'user_view.py',
            'output_path': join(project.app_path, 'views')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'view', '__init__'),
            'filename': '__init__.py',
            'output_path': join(project.app_path, 'views')
            
        },
    ]