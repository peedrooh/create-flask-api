import os
from os.path import join

from PyInquirer import prompt

from create_flask_api.project import ProjectSpecs
from create_flask_api.styles import custom_style


class FeatureMixin():
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = []
        self.questions = []
        self.files_to_fix_data = []
        self.answers = []
        self.commands = []
        
        
    def __call__(self):
        self.make_questions()
        self.create_files()
        self.fix_files()
    
    
    def create_templ_file(self, template_path, filename, output_path, mode='w'):

        with open(template_path, 'r') as templ:
            
            if not os.path.exists(output_path):
                os.makedirs(output_path)
                
            with open(join(output_path, filename), mode) as file:

                file.writelines(templ)
                
    
    def start_package(self, folder):
        
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        with open(join(folder, '__init__.py'), 'w') as file:
            ...
            
    
    def fix_lines(self, file_path, lines_to_fix, fixed_lines):

        with open(file_path, 'r') as file:
            new_file = file.read()
        
        for old, new in zip(lines_to_fix, fixed_lines):
            new_file = new_file.replace(old, new)

        
        with open(file_path, 'w') as file:
            file.writelines(new_file)

        
    def make_questions(self):

        for question in self.questions:
            answer = prompt(question, style=custom_style)
            self.answers.append(answer)
            if not answer[question['name']]:
                break
            
            
    def create_files(self):
        
        for file in self.files_to_create_data:
            self.create_templ_file(**file)
            
            
    def fix_files(self):

        for file in self.files_to_fix_data:
            self.fix_lines(**file)
            
            
    def execute_commands(self, project):
        
        if len(self.commands):
            
            print(self.commands['message'])
        
            for command in self.commands['commands']:

                os.system(command)