from src.project import ProjectSpecs
from .mixins import FeatureMixin
from src.assets.file_paths.model_paths import model_paths

class ModelService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = model_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
