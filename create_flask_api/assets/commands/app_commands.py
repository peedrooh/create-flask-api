def app_commands(project): 
    return {
        'commands': [
            f'cd {project.project_name} && python -m venv venv && {project.venv_cmd} venv/bin/activate && pip install flask flask-sqlalchemy psycopg2-binary python-dotenv && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Base Packages --*-- \n\n' 
    }