from typing import Callable, Dict, TypeAlias

Service: TypeAlias = Callable
services: Dict[str, Service] = dict()

def registry(service: Service) -> any:
    """
    Registry a service. The name of the service available on Service.__name__ will be used as a key to then retrieve the desired service instance.
    """
    
    service_name = service.__class__.__name__
    if service_name in services:
        raise Exception(f"Service {service_name} already exists")
    
    services[service_name] = service
    return services[service_name]

def get_service(name: str) -> any or None:
    """
    Retrieve a service based on its name. This can be accessed without any instantiation by Service.__name__.
    """
    
    if name not in services:
        raise Exception(f"Service {name} does not exist")
    
    return services[name]