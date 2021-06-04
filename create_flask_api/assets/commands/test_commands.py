def test_commands(project):
    return {
        'commands':[
            f'cd {project.project_name} && source venv/bin/activate && pip install pytest && pip freeze > requirements.txt'
        ],
        'message': '\n\n --*-- Installing Pytest Packages --*-- \n\n' 
    }