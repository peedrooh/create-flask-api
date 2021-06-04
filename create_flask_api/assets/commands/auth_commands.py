def auth_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && source venv/bin/activate && pip install flask-jwt-extended && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Authentication Packages --*-- \n\n' 
    }