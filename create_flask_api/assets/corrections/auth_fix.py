from os.path import join


def auth_fix(project):
    return [
        {
            'file_path': join(project.app_path, 'configurations', '__init__.py'),
            'lines_to_fix': [
                """
    authentication.init_app(app)""", 
            ', authentication',
            """from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from datetime import timedelta
"""
            ],
            'fixed_lines': [
                '',
                '', 
                ''
            ]
        },
        {
            'file_path': join(project.app_path, 'services', 'user_services.py'),
            'lines_to_fix': [
                """from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from datetime import timedelta
"""
            ],
            'fixed_lines': [
                ''
            ]
        }
    ]