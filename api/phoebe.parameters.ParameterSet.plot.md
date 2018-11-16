### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).plot (method)


```py

def plot(self, twig=None, **kwargs)

```



High-level wrapper around matplotlib (by default, but also has some support
for other plotting backends).  This function smartly makes one
or multiple calls to the plotting backend based on the type of data.
Individual lines are each given a label (automatic if not provided).
To see these in a legend simply call `ax.legend([options])`.

```py
ax = ps.plot()
ax.legend()
plt.show()
```

Arguments
-----------
* `*args`: either a twig pointing to a dataset,
    or dictionaries, where each dictionary gets passed back to
    <phoebe.parameters.ParameterSet.plot>
* `time` (float, optional): Current time.  For spectra and meshes, time
    is required to determine at which time to draw.  For other types,
    time will only be used for higlight and uncover (if enabled)
* `backend` (string, optional): Plotting backend to use.  Will default to
    'plotting_backend' from the <phoebe.frontend.bundle.Bundle>
    settings if not provided.
* `highlight` (bool, optional, default=True): whether to highlight the current time
    (defaults to True)
* `highlight_marker` (string, optional, default='o'): if `highlight==True` -
    what marker-type to use for highlighting the current `time`.
* `highlight_ms` (int, optional): if `highlight==True` - what marker-size
    to use for highlighting the current `time`.
* `highlight_color` (string, optional): if `highlight=True` - what marker-color
    to use for highlighting the current `time`.
* `uncover` (bool, optional, default=False): whether to only show data up to the
    current `time`.
* `ax` (matplotlib axes, optional, default=`plt.gca()`): axes to plot on.
* `x` (string, optional): qualifier or twig of the array to plot on the x-axis (will
    default based on the kind if not provided).  Must be a valid
    qualifier with the exception of phase.  To plot phase along the
    x-axis set x to 'phases' or 'phases:[component]'.  This will use
    the ephemeris from <phoebe.frontend.bundle.Bundle.get_ephemeris> if possible.
* `y` (string, optional): qualifier or twig of the array to plot on the y-axis
    (see details for `x` above)
* `z` (string, optional): qualifier or twig of the array to plot on the z-axis if both
    the backend and ax support 3D plotting (see details for `x` above).
* `t0` (string/float, optional): qualifier or float of the t0 that should be used for
    phasing, if applicable.
* `xerrors` (string, optional): qualifier of the array to plot as x-errors (will
    default based on `x` if not provided).
* `yerrors` (string, optional): qualifier of the array to plot as y-errors (will
    default based on `y` if not provided).
* `zerrors` (string, optional): qualifier of the array to plot as z-errors (will
    default based on `z` if not provided)
* `xunit` (unit or valid string, optional): unit to plot the x-array (will
  default based on `x` if not provided)
* `yunit` (unit or valid string, optional): unit to plot the y-array (will
  default based on `y` if not provided)
* `zunit` (unit or valid string, optional): unit to plot the z-array (will
  default based on `z` if not provided)
* `xlabel` (string, optional): label for the x-axis (will default based on `x`
  if not provided, but will not set if ax already has an xlabel).
* `ylabel` (string, optional): label for the x-axis (will default based on `y`
  if not provided, but will not set if ax already has an ylabel).
* `zlabel` (string, optional): label for the x-axis (will default based on `z`
  if not provided, but will not set if ax already has an zlabel).
* `xlim` (tuple, optional):  limits for the x-axis (will default based on data if not provided)
* `ylim` (tuple, optional):  limits for the y-axis (will default based on data if not provided)
* `zlim` (tuple, optional):  limits for the z-axis (will default based on data if not provided)
* `label` (string, optional): label to give to ALL lines in this single plotting call (each
    line with get automatic default labels if not provided)
* `color` (string, optional): matplotlib recognized color string or the qualifier/twig
    of an array to use for color
* `cmap` (string, optional): matplotlib recognized cmap to use if color is
    a qualifier pointing to an array (will be ignored otherwise)
* `facecolor` (string, optional): matplotlib recognized color string or the qualifier/twig
    of an array to use for facecolor (mesh plots only)
* `facecmap` (string, optional): matplotlib recognized cmap to use if facecolor is
    a qualifier pointing to an array (will be ignored otherwise)
* `edgecolor` (string, optional): matplotlib recognized color string or the qualifier/twig
    of an array to use for edgecolor (mesh plots only)
* `edgecap` (string, optional): matplotlib recognized cmap to use if edgecolor is
    a qualifier pointing to an array (will be ignored otherwise)
* `save` (string, optional): filename of the resulting animation.  If provided,
    the animation will be saved automatically.  Either way, the animation
    object is returned (so you can always call `anim.save(fname)`).
* `show` (bool, optional, default=False): whether to automatically show the animation (defaults
    to False).  Either way, the animation object is returned (so you can
    always call `b.show()` or `plt.show()`).
* `**kwargs`:  additional kwargs to filter the ParameterSet OR to pass along
    to the backend plotting call

Returns
----------
* (mpl.axes) the matplotlib axes (or equivalent for other backends)
