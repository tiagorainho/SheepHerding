from typing import Callable, Dict, TypeAlias

Service: TypeAlias = Callable
services: Dict[str, Service] = dict()

def registry(name: str, service: Service) -> any:
    if name in services:
        raise Exception("Service already exists")
    
    services[name] = service
    return services[name]

def get_service(name: str) -> any or None:
    if name not in services:
        return None
    
    return services[name]