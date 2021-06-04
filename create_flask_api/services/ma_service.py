from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.ma_paths import ma_paths
from create_flask_api.assets.questions.ma_questions import ma_questions
from create_flask_api.assets.corrections.ma_correction import ma_fix
from create_flask_api.assets.commands.ma_commands import ma_commands


class MaService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.project = project
        
        self.files_to_create_data = ma_paths(project)
        
        self.questions = ma_questions
        
        self.files_to_fix_data = ma_fix(project)
        
        self.answers = []
        
        self.commands = []
        
    
    def create_files(self):
        
        if self.answers[0]['serializer_library']:
            
            self.commands = ma_commands(self.project)
            
            for file in self.files_to_create_data:
                self.create_templ_file(**file)
                

    def fix_files(self):
        
        if not self.answers[0]['serializer_library']:
            
            for file in self.files_to_fix_data:
                self.fix_lines(**file)