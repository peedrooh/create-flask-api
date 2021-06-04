from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.app_paths import app_paths
from create_flask_api.assets.commands.app_commands import app_commands


class AppService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = app_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = app_commands(project)
        