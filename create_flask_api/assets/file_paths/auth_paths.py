import sys, os
from os.path import join

def auth_path(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'authentication', 'user_model'),
            'filename': 'user_model.py',
            'output_path': join(project.app_path, 'models')

        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'authentication', 'user_services'),
            'filename': 'user_services.py',
            'output_path': join(project.app_path, 'services')

        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'authentication', 'user_view'),
            'filename': 'user_view.py',
            'output_path': join(project.app_path, 'views')

        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'authentication', 'config'),
            'filename': 'authentication.py',
            'output_path': join(project.app_path, 'configurations')

        },
    ]