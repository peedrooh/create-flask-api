from os.path import join


def heroku_fix(project):
    return [
        {
            'file_path': join(project.project_path, 'config.py'),
            'lines_to_fix': [
                """


# When deploying to Heroku the DATABASE_URL is set to 'postgres://', 
# but since SQLAlquemy version 1.4 the connection uri must start with 'postgresql://'.
# This logic is suppost to fix that.
uri = getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)""",
                    'uri'
            ],
            'fixed_lines': [
                '', 
                'getenv("SQLALCHEMY_DATABASE_URI")'
            ]
        }
    ]