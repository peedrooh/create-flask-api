import sys, os
from os.path import join


def ma_paths(project):
    return [
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]),'assets', 'templates', 'marshmallow', 'user_serializer'),
            'filename': 'user_serializer.py',
            'output_path': join(project.app_path, 'serializers')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]),'assets', 'templates', 'marshmallow', '__init__'),
            'filename': '__init__.py',
            'output_path': join(project.app_path, 'serializers')
            
        },
        {
            'template_path': join(os.path.abspath(sys.argv[0][:-12]),'assets', 'templates', 'marshmallow', 'config'),
            'filename': 'serializer.py',
            'output_path': join(project.app_path, 'configurations')
            
        },
    ]