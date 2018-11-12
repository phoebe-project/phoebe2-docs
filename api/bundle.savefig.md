### savefig
```py

def savefig(self, fname, **kwargs)

```



Save the plot.  This is really just a very generic wrapper based on the
chosen plotting backend.  For matplotlib it is probably just as, if not
even more, convenient to simply import matplotlib yourself and call the
savefig method.

:parameter str filename: filename to save to.  Be careful of extensions here...
        matplotlib accepts many different image formats while other
        backends will only export to html.
:parameter str backend: which plotting backend to use.  Will default to
        'plotting_backend' from settings in the
        :class:`phoebe.frontend.bundle.Bundle` if not provided.

