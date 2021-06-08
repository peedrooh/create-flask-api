def auth_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && {project.venv_cmd} && pip install flask-jwt-extended && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Authentication Packages --*-- \n\n' 
    }