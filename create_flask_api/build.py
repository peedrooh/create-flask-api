from .services import services


def build(project):
    service_instances = list()
    
    for Service in services:
        service = Service(project)
        service_instances.append(service)
        
    for service in service_instances:
        service()
        
    for service in service_instances:
        service.execute_commands(project)
        