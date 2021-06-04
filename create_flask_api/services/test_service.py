from os.path import join

from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.test_paths import test_paths
from create_flask_api.assets.questions.test_questions import test_questions
from create_flask_api.assets.commands.test_commands import test_commands


class TestService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        
        self.project = project
        
        self.files_to_create_data = test_paths(project)
        
        self.questions = test_questions
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
        
    
    def create_files(self):

        if self.answers[0]['Test']:
            
            self.commands = test_commands(self.project)
            
            self.start_package(join(self.project.project_path, 'tests'))
            self.start_package(join(self.project.project_path, 'tests', 'user'))
            
            for test_lib in list(self.answers[1].values())[0]:

                for file in self.files_to_create_data[test_lib]:
                    self.create_templ_file(**file)