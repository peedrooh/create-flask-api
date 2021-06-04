import os
from PyInquirer import prompt

from create_flask_api.styles import custom_style
from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.git_paths import git_paths
from create_flask_api.assets.questions.git_questions import git_questions


class GitService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        
        self.files_to_create_data = git_paths(project)
        
        self.questions = git_questions
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
        
        self.remote_repo = ''
        

    def make_questions(self):

        for question in self.questions:
            
            answer = prompt(question, style=custom_style)
            self.answers.append(answer)
            
            if not answer[question['name']]:
                break
            
        if len(self.answers) > 1:
            
            self.remote_repo = self.answers[1]['Repo']
            
            
    def create_files(self):
        
        if len(self.answers) > 2 and self.answers[2]['Gitignore']:
            
            for file in self.files_to_create_data:
                self.create_templ_file(**file)

            
    def execute_commands(self, project):
        
        if len(self.answers) > 1:
            print('\n\n --*-- Configuring Git --*-- \n\n')
            
            os.system(f'cd  {project.project_name} && git init && git remote add origin {self.remote_repo}')

