class Observer:

    def notify(self, entity, event, *args, **kwargs):
        raise NotImplemented