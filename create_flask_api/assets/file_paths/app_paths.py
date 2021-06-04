import sys, os
from os.path import join


def app_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'create_app'),
            'filename': '__init__.py',
            'output_path': project.app_path
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'config'),
            'filename': 'config.py',
            'output_path': project.project_path
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'env'),
            'filename': '.env',
            'output_path': project.project_path
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'env.example'),
            'filename': '.env.example',
            'output_path': project.project_path
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'configurations'),
            'filename': '__init__.py',
            'output_path': join(project.app_path, 'configurations')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'database'),
            'filename': 'database.py',
            'output_path': join(project.app_path, 'configurations')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'app', 'commands'),
            'filename': 'commands.py',
            'output_path': join(project.app_path, 'configurations')
            
        },
    ]