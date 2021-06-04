import sys, os
from os.path import join


def migration_paths(project):
    return [
            {
                'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'migration', 'config'),
                'filename': 'migration.py',
                'output_path': join(project.app_path, 'configurations')
                
            },
        ]