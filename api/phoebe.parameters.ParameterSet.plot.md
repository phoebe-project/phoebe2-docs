### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).plot (method)


```py

def plot(self, twig=None, **kwargs)

```



High-level wrapper around matplotlib that uses
[autofig 1.0.0](https://github.com/kecnry/autofig/tree/1.0.0)
under-the-hood for automated figure and animation production.

See also:
* [phoebe.parameters.ParameterSet.show](phoebe.parameters.ParameterSet.show.md)
* [phoebe.parameters.ParameterSet.savefig](phoebe.parameters.ParameterSet.savefig.md)
* [phoebe.parameters.ParameterSet.gcf](phoebe.parameters.ParameterSet.gcf.md)
* [phoebe.parameters.ParameterSet.clf](phoebe.parameters.ParameterSet.clf.md)

Note: not all options are listed below.  See the
[autofig](https://github.com/kecnry/autofig/tree/1.0.0)
tutorials and documentation for more options which are passed along
via `**kwargs`.

Arguments
----------
* `twig` (string, optional, default=None): twig to use for filtering
    prior to plotting.  See [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* `time` (float, optional): time to use for plotting/animating.
* `times` (list/array, optional): times to use for animating (will
    override any value sent to `time`).
* `t0` (string/float, optional): qualifier/twig or float of the t0 that
    should be used for phasing, if applicable.  If provided as a string,
    `b.get_value(t0)` needs to provide a valid float.

* `x` (string/float/array, optional): qualifier/twig of the array to plot on the
    x-axis (will default based on the dataset-kind if not provided).
    With the exception of phase, `b.get_value(x)` needs to provide a
    valid float or array.  To plot phase along the x-axis, pass
    `x='phases'` or `x=phases:[component]`.  This will use the ephemeris
    from &lt;phoebe.frontend.bundle.Bundle.get_ephemeris(component) if
    possible to phase the applicable times array.
* `y` (string/float/array, optional): qualifier/twig of the array to plot on the
    y-axis (will default based on the dataset-kind if not provided).
* `z` (string/float/array, optional): qualifier/twig of the array to plot on the
    z-axis.  By default, this will just order the points on a 2D plot.
    To plot in 3D, also pass `projection='3d'`.
* `s` (strong/float/array, optional): qualifier/twig of the array to use
    for size.  See the [autofig tutorial on size](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/size_modes.ipynb)
    for more information.
* `c` (string/float/array, optional): qualifier/twig of the array to use
    for color.
* `fc` (string/float/array, optional): qualifier/twig of the array to use
    for facecolor (only applicable for mesh plots).
* `ec` (string/float/array, optional): qualifier/twig of the array to use
    for edgecolor (only applicable for mesh plots).

* `xerror` (string/float/array, optional): qualifier/twig of the array to plot as
    x-errors (will default based on `x` if not provided).
* `yerror` (string/float/array, optional): qualifier/twig of the array to plot as
    y-errors (will default based on `y` if not provided).
* `zerror` (string/float/array, optional): qualifier/twig of the array to plot as
    z-errors (will default based on `z` if not provided).

* `xunit` (string/unit, optional): unit to plot on the x-axis (will
    default on `x` if not provided).
* `yunit` (string/unit, optional): unit to plot on the y-axis (will
    default on `y` if not provided).
* `zunit` (string/unit, optional): unit to plot on the z-axis (will
    default on `z` if not provided).
* `cunit` (string/unit, optional): unit to plot on the color-axis (will
    default on `c` if not provided).
* `fcunit` (string/unit, optional): unit to plot on the facecolor-axis (will
    default on `fc` if not provided, only applicable for mesh plots).
* `ecunit` (string/unit, optional): unit to plot on the edgecolor-axis (will
    default on `ec` if not provided, only applicable for mesh plots).

* `xlabel` (string, optional): label for the x-axis (will default on `x`
    if not provided, but will not set if the axes already has an xlabel).
* `ylabel` (string, optional): label for the y-axis (will default on `y`
    if not provided, but will not set if the axes already has an ylabel).
* `zlabel` (string, optional): label for the z-axis (will default on `z`
    if not provided, but will not set if the axes already has an zlabel).
* `slabel` (string, optional): label for the size-axis (will default on `s`
    if not provided, but will not set if the axes already has an slabel).
* `clabel` (string, optional): label for the color-axis (will default on `c`
    if not provided, but will not set if the axes already has an clabel).
* `fclabel` (string, optional): label for the facecolor-axis (will default on `fc`
    if not provided, but will not set if the axes already has an fclabel,
    only applicable for mesh plots).
* `eclabel` (string, optional): label for the edgecolor-axis (will default on `ec`
    if not provided, but will not set if the axes already has an eclabel,
    only applicable for mesh plots).

* `xlim` (tuple/string, optional): limits for the x-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.
* `ylim` (tuple/string, optional): limits for the y-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.
* `zlim` (tuple/string, optional): limits for the z-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.
* `slim` (tuple/string, optional): limits for the size-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.
* `clim` (tuple/string, optional): limits for the color-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.
* `fclim` (tuple/string, optional): limits for the facecolor-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.
* `eclim` (tuple/string, optional): limits for the edgecolor-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/limits.ipynb)
    for more information/choices.

* `smode` (string, optional): size mode.  See the [autofig tutorial on sizes](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/size_modes.ipynb)
    for more information.

* `highlight` (bool, optional, default=True): whether to highlight at the
    current time.  Only applicable if `time` or `times` provided.
* `highlight_marker` (string, optional): marker to use for highlighting.
    Only applicable if `highlight=True` and `time` or `times` provided.
* `highlight_color` (string, optional): color to use for highlighting.
    Only applicable if `highlight=True` and `time` or `times` provided.

* `uncover` (bool, optional): whether to uncover data based on the current
    time.  Only applicable if `time` or `times` provided.

* `legend` (bool, optional, default=False): whether to draw a legend for
    this axes.
* `legend_kwargs` (dict, optional):  keyword arguments (position,
    formatting, etc) to be passed on to [plt.legend](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html)

* `save` (string, optional, default=False): filename to save the
    figure (or False to not save).
* `show` (bool, optional, default=False): whether to show the plot
* `animate` (bool, optional, default=False): whether to animate the figure.
* `draw_sidebars` (bool, optional, default=True): whether to include
    any applicable sidebars (colorbar, sizebar, etc).
* `draw_title` (bool, optional, default=True): whether to draw axes
    titles.
* `subplot_grid` (tuple, optional, default=None): override the subplot
    grid used (see [autofig tutorial on subplots](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/subplot_positioning.ipynb)
    for more details).

* `save_kwargs` (dict, optional): any kwargs necessary to pass on to
    save (only applicable if `animate=True`).

* `**kwargs`: additional keyword arguments are sent along to [autofig](https://github.com/kecnry/autofig/tree/1.0.0).

Returns
--------
* (autofig figure, matplotlib figure)

