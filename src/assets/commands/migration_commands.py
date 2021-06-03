def migration_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && source venv/bin/activate && pip install flask_migrate && pip freeze > requirements.txt'
        ],
        'message': '' 
    }