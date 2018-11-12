### show
```py

def show(self, **kwargs)

```



Show the plot.  This is really just a very generic wrapper based on the
chosen plotting backend.  For matplotlib it is probably just as, if not
even more, convenient to simply import matplotlib yourself and call the
show method.  However, other backends require saving to temporary html
files and opening a webbrowser - so this method provides the ability for
a generic call that should work if you choose to change the plotting backend.

:parameter str backend: which plotting backend to use.  Will default to
        'plotting_backend' from settings in the
        :class:`phoebe.frontend.bundle.Bundle` if not provided.

