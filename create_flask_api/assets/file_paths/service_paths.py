import sys, os
from os.path import join


def service_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'service', 'user_services'),
            'filename': 'user_services.py',
            'output_path': join(project.app_path, 'services')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'service', '__init__'),
            'filename': '__init__.py',
            'output_path': join(project.app_path, 'services')
            
        },
    ]