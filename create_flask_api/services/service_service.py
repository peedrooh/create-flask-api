from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.service_paths import service_paths

class ServiceService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = service_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
