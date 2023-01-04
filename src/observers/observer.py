class Observer:
    """
    Observer to be used in other instances. Methods need to be overridden otherwise it will raise an NotImplementedError
    """

    def notify(self, entity, event, *args, **kwargs):        
        raise NotImplementedError()