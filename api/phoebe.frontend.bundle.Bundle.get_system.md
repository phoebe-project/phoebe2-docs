### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_system

```py

def get_system(self, twig=None, **kwargs)

```



Filter in the 'system' context

:parameter str twig: twig to use for filtering
:parameter **kwargs: any other tags to do the filter
    (except twig or context)

:return: :class:`phoebe.parameters.parameters.Parameter` or
    :class:`phoebe.parameters.parameters.ParameterSet`

