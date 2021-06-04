from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.heroku_paths import heroku_paths
from create_flask_api.assets.questions.heroku_questions import heroku_questions
from create_flask_api.assets.corrections.heroku_fix import heroku_fix


class HerokuService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = heroku_paths(project)
        
        self.questions = heroku_questions
        
        self.files_to_fix_data = heroku_fix(project)
        
        self.answers = []
        
        self.commands = []


    def create_files(self):
        
        if self.answers[0]['Heroku']:
            
            for file in self.files_to_create_data:
                self.create_templ_file(**file)
                
    
    def fix_files(self):
        
        if not self.answers[0]['Heroku']:

            for file in self.files_to_fix_data:
                self.fix_lines(**file)