import sys, os
from os.path import join


def model_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'model', 'user_model'),
            'filename': 'user_model.py',
            'output_path': join(project.app_path, 'models')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'model', '__init__'),
            'filename': '__init__.py',
            'output_path': join(project.app_path, 'models')
            
        },
    ]