from typing import Callable, Dict, TypeAlias

from services.sheep_service import SheepService
from services.dog_service import DogService


Service: TypeAlias = Callable


services: Dict[str, Service] = dict()

def registry(name: str, service: Service) -> any:
    if name in services:
        raise Exception("Service already exists")
    
    services[name] = service()
    return services[name]