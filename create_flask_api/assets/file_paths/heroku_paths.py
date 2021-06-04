import sys, os
from os.path import join


def heroku_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'heroku', 'Procfile'),
            'filename': 'Procfile',
            'output_path': project.project_path
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'heroku', 'wsgi'),
            'filename': 'wsgi.py',
            'output_path': project.project_path
            
        },
    ]