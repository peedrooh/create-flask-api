from src.project import ProjectSpecs
from .mixins import FeatureMixin
from src.assets.file_paths.serializer_path import serializer_paths


class SerializerService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):
        self.files_to_create_data = serializer_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = []
