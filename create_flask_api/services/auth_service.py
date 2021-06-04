from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.auth_paths import auth_path
from create_flask_api.assets.questions.auth_questions import auth_questions
from create_flask_api.assets.corrections.auth_fix import auth_fix
from create_flask_api.assets.commands.auth_commands import auth_commands


class AuthService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.project = project
        self.files_to_create_data = auth_path(project)
        
        self.questions = auth_questions
        
        self.files_to_fix_data = auth_fix(project)
        
        self.answers = []
        
        self.commands = []
        
    
    def create_files(self):
        
        if self.answers[0]['Authentication'] == 'JWT-Extended':
            
            self.commands = auth_commands(self.project)

            for file in self.files_to_create_data:
                self.create_templ_file(**file)
                

    def fix_files(self):
        
        if not self.answers[0]['Authentication'] == 'JWT-Extended':

            for file in self.files_to_fix_data:
                self.fix_lines(**file)
