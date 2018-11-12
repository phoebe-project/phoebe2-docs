### plot
```py

def plot(self, *args, **kwargs)

```



High-level wrapper around matplotlib (by default, but also has some support
for other plotting backends).  This function smartly makes one
or multiple calls to the plotting backend based on the type of data.

Individual lines are each given a label (automatic if not provided).
To see these in a legend simply call ax.legend([options])

>>> ax = ps.plot()
>>> ax.legend()
>>> plt.show()

:parameter *args: either a twig pointing to a dataset,
    or dictionaries, where each dictionary gets passed back to
    :meth:`plot`
:parameter float time: Current time.  For spectra and meshes, time
    is required to determine at which time to draw.  For other types,
    time will only be used for higlight and uncover (if enabled)
:parameter str backend: Plotting backend to use.  Will default to
    'plotting_backend' from the :class:`phoebe.frontend.bundle.Bundle`
    settings if not provided.
:parameter bool highlight: whether to highlight the current time
    (defaults to True)
:parameter str highlight_marker: if highlight==True - what marker-type
    to use for highlighting the current time (defaults to 'o')
:parameter int highlight_ms: if highlight==Ture - what marker-size
    to use for highlighting the current time
:parameter str highlight_color: if highlight==True: what marker-color
    to use for highlighting the current time
:parameter bool uncover: whether to only show data up to the current time
    (defaults to False)
:parameter ax: axes to plot on (defaults to plt.gca())
:type ax: mpl.axes
:parameter str x: qualifier or twig of the array to plot on the x-axis (will
    default based on the kind if not provided).  Must be a valid
    qualifier with the exception of phase.  To plot phase along the
    x-axis set x to 'phases' or 'phases:[component]'.  This will use
    the ephemeris from :meth:`phoebe.frontend.bundle.Bundle.get_ephemeris` if possible.
:parameter str y: qualifier or twig of the array to plot on the y-axis
    (see details for x above)
:parameter str z: qualifier or twig of the array to plot on the z-axis if both
    the backend and ax support 3d plotting (see details for x above)
:parameter t0: qualifier or float of the t0 that should be used for
    phasing, if applicable
:type t0: string or float
:parameter str xerrors: qualifier of the array to plot as x-errors (will
    default based on x if not provided)
:parameter str yerrors: qualifier of the array to plot as y-errors (will
    default based on y if not provided)
:parameter str zerrors: qualifier of the array to plot as z-errors (will
    default based on z if not provided)
:parameter xunit: unit to plot the x-array (will default based on x if not provided)
:type xunit: str or astropy.unit.Unit
:parameter xunit: unit to plot the y-array (will default based on y if not provided)
:type yunit: str or astropy.unit.Unit
:parameter xunit: unit to plot the z-array (will default based on z if not provided)
:type zunit: str or astropy.unit.Unit
:parameter str xlabel: label for the x-axis (will default based on x if not provided, but
    will not set if ax already has an xlabel)
:parameter str ylabel: label for the y-axis (will default based on y if not provided, but
    will not set if ax already has an ylabel)
:parameter str zlabel: label for the z-axis (will default based on z if not provided, but
    will not set if ax already has an zlabel)
:parameter tuple xlim: limits for the x-axis (will default based on data if not provided)
:parameter tuple ylim: limits for the x-axis (will default based on data if not provided)
:parameter tuple zlim: limits for the x-axis (will default based on data if not provided)
:parameter str label: label to give to ALL lines in this single plotting call (each
    line with get automatic default labels if not provided)
:parameter str color: matplotlib recognized color string or the qualifier/twig
    of an array to use for color
:parameter str cmap: matplotlib recognized cmap to use if color is
    a qualifier pointing to an array (will be ignored otherwise)
:parameter str facecolor: matplotlib recognized color string or the qualifier/twig
    of an array to use for facecolor (mesh plots only)
:parameter str facecmap: matplotlib recognized cmap to use if facecolor is
    a qualifier pointing to an array (will be ignored otherwise)
:parameter str edgecolor: matplotlib recognized color string or the qualifier/twig
    of an array to use for edgecolor (mesh plots only)
:parameter str edgecmap: matplotlib recognized cmap to use if edgecolor is
    a qualifier pointing to an array (will be ignored otherwise)


:parameter str save: filename of the resulting animation.  If provided,
    the animation will be saved automatically.  Either way, the animation
    object is returned (so you can always call anim.save(fname)).
:parameter bool show: whether to automatically show the animation (defaults
    to False).  Either way, the animation object is returned (so you can
    always call b.show() or plt.show())
:parameter **kwargs: additional kwargs to filter the ParameterSet OR to pass along
    to the backend plotting call

:returns: the matplotlib axes (or equivalent for other backends)

