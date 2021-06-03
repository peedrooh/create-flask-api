def ma_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && source venv/bin/activate && pip install flask-marshmallow marshmallow-sqlalchemy && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Marshmallow Packages --*-- \n\n' 
    }