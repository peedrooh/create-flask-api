from src.project import ProjectSpecs
from .mixins import FeatureMixin
from src.assets.file_paths.view_paths import view_paths


class ViewService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = view_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
