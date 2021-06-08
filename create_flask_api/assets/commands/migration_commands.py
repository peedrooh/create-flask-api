def migration_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && {project.venv_cmd} && pip install flask_migrate && pip freeze > requirements.txt'
        ],
        'message': '' 
    }