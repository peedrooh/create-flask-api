def ma_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && {project.venv_cmd} && pip install flask-marshmallow marshmallow-sqlalchemy && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Marshmallow Packages --*-- \n\n' 
    }