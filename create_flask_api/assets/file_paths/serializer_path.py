import sys, os
from os.path import join


def serializer_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'serializer', 'user_serializer'),
            'filename': 'user_serializer.py',
            'output_path': join(project.app_path, 'serializers')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'serializer', '__init__'),
            'filename': '__init__.py',
            'output_path': join(project.app_path, 'serializers')
            
        },
    ]