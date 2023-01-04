from typing import Callable, Dict, TypeAlias

class ServiceLocator:
    __instance = None

    Service: TypeAlias = Callable
    services: Dict[str, Service] = dict()

    @staticmethod
    def get_instance():

        if ServiceLocator.__instance == None:
            ServiceLocator()
        return ServiceLocator.__instance
    
    def __init__(self) -> None:
        if ServiceLocator.__instance != None:
            raise Exception(f"{ServiceLocator.__name__} is a singleton!")
        ServiceLocator.__instance = self

    def registry(self, service: Service) -> any:
        """
        Registry a service. The name of the service available on Service.__name__ will be used as a key to then retrieve the desired service instance.
        """
        
        service_name = service.__class__.__name__
        if service_name in self.services:
            raise Exception(f"Service {service_name} already exists")
        
        self.services[service_name] = service
        return self.services[service_name]

    def get_service(self, name: str) -> any or None:
        """
        Retrieve a service based on its name. This can be accessed without any instantiation by Service.__name__.
        """
        
        if name not in self.services:
            raise Exception(f"Service {name} does not exist")
        
        return self.services[name]