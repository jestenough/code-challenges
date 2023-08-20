import inspect


class LazyInit(type):
    def __new__(cls, name, bases, attrs):
        if init_method := attrs.get('__init__'):
            init_parameters = inspect.signature(init_method).parameters
            param_names = [name for name, param in init_parameters.items() if name != 'self']

            def lazy_init(self, *args, **kwargs):
                # TODO maybe write for kwargs too (although this is not provided for by the assignment)
                for i, param_name in enumerate(param_names):
                    setattr(self, param_name, args[i])

            attrs['__init__'] = lazy_init

        return super().__new__(cls, name, bases, attrs)
