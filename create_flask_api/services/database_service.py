from os.path import join

from PyInquirer import prompt

from create_flask_api.styles import custom_style
from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.questions.database_questions import db_questions, postgresql_questions, sqlite_questions


class DatabaseService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.project = project
        self.files_to_create_data = []
        
        self.questions = db_questions
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []


    def make_questions(self):

        for question in self.questions:
            
            answer = prompt(question, style=custom_style)
            self.answers.append(answer)
            
        if self.answers[0]['Database'] == 'Postgresql':
            self.answers[1] = {}
            for question in postgresql_questions:
            
                answer = prompt(question, style=custom_style)
                setattr(self.answers[1], **answer)
                # self.answers[1].update(answer)
            
            self.files_to_fix_data = [
                {
                    'file_path': join(self.project.project_path, '.env'),
                    'lines_to_fix': ['SQLALCHEMY_DATABASE_URI='],
                    'fixed_lines': [
                        'SQLALCHEMY_DATABASE_URI=' + 'postgresql://' + self.answers[1]['psql_db'] + ':' + self.answers[1]['psql_user'] + '@localhost:5432/' + self.answers[1]['psql_password']
                    ]
                },
                {
                    'file_path': join(self.project.project_path, '.env.example'),
                    'lines_to_fix': ['SQLALCHEMY_DATABASE_URI='],
                    'fixed_lines': [
                        'SQLALCHEMY_DATABASE_URI=' + 'postgresql://' + self.answers[1]['psql_db'] + ':' + self.answers[1]['psql_user'] + '@localhost:5432/' + self.answers[1]['psql_password']
                    ]
                },
            ]
            
        if self.answers[0]['Database'] == 'SQLite':
            self.answers[1] = {}
            for question in postgresql_questions:
            
                answer = prompt(question, style=custom_style)
                setattr(self.answers[1], **answer)
                # self.answers[1].update(answer)
            
            self.files_to_fix_data = [
                {
                    'file_path': join(self.project.project_path, '.env'),
                    'lines_to_fix': ['SQLALCHEMY_DATABASE_URI='],
                    'fixed_lines': [
                        'SQLALCHEMY_DATABASE_URI=' + 'sqlite:///' + join(self.project.project_path, self.answers[1]['sqlite_db'])
                    ]
                },
                {
                    'file_path': join(self.project.project_path, '.env.example'),
                    'lines_to_fix': ['SQLALCHEMY_DATABASE_URI='],
                    'fixed_lines': [
                        'SQLALCHEMY_DATABASE_URI=' + 'sqlite:///' + join(self.project.project_path, self.answers[1]['sqlite_db'])
                    ]
                },
            ]