def test_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && {project.venv_cmd} && pip install pytest && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Pytest Packages --*-- \n\n' 
    }