import sys, os
from os.path import join


def test_paths(project):
    return {
        'Pytest': [
            {
                'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'test', 'pytest', 'conftest'),
                'filename': 'conftest.py',
                'output_path': join(project.project_path, 'tests')
            
            },
            {
                'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'test', 'pytest', 'test_routes'),
                'filename': 'test_routes.py',
                'output_path': join(project.project_path, 'tests', 'user')
            },
            {
                'template_path': join(os.path.abspath(sys.argv[0][:-12]), 'assets', 'templates', 'test', 'pytest', 'test_services'),
                'filename': 'test_services.py',
                'output_path': join(project.project_path, 'tests', 'user')
            },
        ],
        'Unit Test': [],
    }