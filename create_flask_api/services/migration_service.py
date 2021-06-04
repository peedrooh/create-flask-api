from create_flask_api.project import ProjectSpecs
from .mixins import FeatureMixin
from create_flask_api.assets.file_paths.migration_paths import migration_paths
from create_flask_api.assets.commands.migration_commands import migration_commands


class MigrationService(FeatureMixin):
    
    def __init__(self, project: ProjectSpecs):

        self.files_to_create_data = migration_paths(project)
        
        self.questions = []
        
        self.files_to_fix_data = []
        
        self.answers = []
        
        self.commands = migration_commands(project)
        