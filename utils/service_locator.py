class ServiceLocator:
    """
    A simple Service Locator utility to manage and provide dependencies.
    """

    _services = {}

    @classmethod
    def register_service(cls, name, service):
        """
        Registers a service with a given name.
        :param name: The name of the service.
        :param service: The service instance or factory.
        """
        cls._services[name] = service

    @classmethod
    def get_service(cls, name):
        """
        Retrieves a registered service by name.
        :param name: The name of the service.
        :return: The service instance.
        :raises KeyError: If the service is not found.
        """
        if name not in cls._services:
            raise KeyError(f"Service '{name}' not found in Service Locator.")
        return cls._services[name]

    @classmethod
    def unregister_service(cls, name):
        """
        Unregisters a service by name.
        :param name: The name of the service.
        """
        if name in cls._services:
            del cls._services[name]

    @classmethod
    def clear_services(cls):
        """
        Clears all registered services.
        """
        cls._services.clear()