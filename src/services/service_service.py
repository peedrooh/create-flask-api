from src.project import ProjectSpecs
from .mixins import FeatureMixin
from src.assets.file_paths.service_paths import service_paths

class ServiceService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = service_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
