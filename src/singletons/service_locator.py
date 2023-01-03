from typing import Callable, Dict, TypeAlias

Service: TypeAlias = Callable
services: Dict[str, Service] = dict()

def registry(service: Service) -> any:
    service_name = service.__class__.__name__
    if service_name in services:
        raise Exception("Service already exists")
    
    services[service_name] = service
    return services[service_name]

def get_service(name: str) -> any or None:
    if name not in services:
        return None
    
    return services[name]