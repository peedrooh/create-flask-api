from src.project import ProjectSpecs
from .mixins import FeatureMixin
from src.assets.file_paths.app_paths import app_paths
from src.assets.commands.app_commands import app_commands


class AppService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = app_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = app_commands(project)
        