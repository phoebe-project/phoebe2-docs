### [phoebe](phoebe.md).[frontend](frontend.md).[Bundle](Bundle.md).get_system

```py

def get_system(self, twig=None, **kwargs)

```



Filter in the 'system' context

:parameter str twig: twig to use for filtering
:parameter **kwargs: any other tags to do the filter
    (except twig or context)

:return: :class:`phoebe.parameters.parameters.Parameter` or
    :class:`phoebe.parameters.parameters.ParameterSet`

