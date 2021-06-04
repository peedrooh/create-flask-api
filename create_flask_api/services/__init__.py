from .view_service import ViewService
from .model_service import ModelService
from .app_service import AppService
from .serializer_service import SerializerService
from .service_service import ServiceService
from .ma_service import MaService
from .test_service import TestService
from .git_service import GitService
from .migration_service import MigrationService
from .auth_service import AuthService
from .heroku_service import HerokuService


services = [
    GitService, 
    ViewService, 
    ModelService, 
    AppService, 
    MigrationService, 
    ServiceService, 
    SerializerService, 
    TestService, 
    AuthService,
    MaService, 
    HerokuService,
]