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

All keyword arguments also support passing dictionaries.  In this case,
they are applied to any resulting plotting call in which the dictionary
matches (including support for wildcards) to the tags of the respective
ParameterSet.  For example:

```
plot(c={'primary@rv*': 'blue', 'secondary@rv*': 'red'})
```

Note: not all options are listed below.  See the
[autofig](https://autofig.readthedocs.io/en/latest/)
tutorials and documentation for more options which are passed along
via `**kwargs`.

Arguments
----------
* `twig` (string, optional, default=None): twig to use for filtering
    prior to plotting.  See [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* `time` (float, optional): time to use for plotting/animating.  This will
    filter on time for any applicable dataset (i.e. meshes, line profiles),
    will be used for highlighting/uncovering based on the passed value
    to `highlight` and `uncover`.  Use `times` to set the individual
    frames when animating with `animate=True`
* `times` (list/array, optional): times to use for animating.  If
    `animate` is not True, a warning will be raised in the logger.  If
    `animate` is True, and neither `times` nor `time` is passed,
    then the animation will cycle over the tagged times of the model
    datasets (i.e. if mesh or lp datasets exist), or the computed
    times otherwise.
* `t0` (string/float, optional): qualifier/twig or float of the t0 that
    should be used for phasing, if applicable.  If provided as a string,
    `b.get_value(t0)` needs to provide a valid float.  This is used
    if `phase`/`phases` provided instead of `time`/`times` as well as
    if 'phases' is set as any direction (`x`, `y`, `z`, etc).
* `phase` (float, optional): phase to use for plotting/animating.  This
    will convert to `time` using the current ephemeris via
    [phoebe.frontend.bundle.Bundle.to_time](phoebe.frontend.bundle.Bundle.to_time.md) along with the passed value
    of `t0`.  If `time` and `phase` are both provided, an error will be
    raised.  Note: if a dataset uses compute_phases_t0 that differs
    from `t0`, this may result in a different mapping between
    `phase` and `time`.
* `phases` (list/array, optional): phases to use for animating.  This
    will convert to `times` using the current ephemeris via
    [phoebe.frontend.bundle.Bundle.to_time](phoebe.frontend.bundle.Bundle.to_time.md) along with the passed
    value of `t0`.  If `times` and `phases` are both provided, an error
    will be raised.  Note: if a dataset uses compute_phases_t0 that differs
    from `t0`, this may result in a different mapping between
    `phase` and `time`.

* `x` (string/float/array, optional): qualifier/twig of the array to plot on the
    x-axis (will default based on the dataset-kind if not provided).
    With the exception of phase, `b.get_value(x)` needs to provide a
    valid float or array.  To plot phase along the x-axis, pass
    `x='phases'` or `x='phases:[component]'`.  This will use the ephemeris
    from [phoebe.frontend.bundle.Bundle.get_ephemeris](phoebe.frontend.bundle.Bundle.get_ephemeris.md)(component) if
    possible to phase the applicable times array.
* `y` (string/float/array, optional): qualifier/twig of the array to plot on the
    y-axis (will default based on the dataset-kind if not provided).  To
    plot residuals along the y-axis, pass `y='residuals'`.  This will
    call [phoebe.frontend.bundle.Bundle.compute_residuals](phoebe.frontend.bundle.Bundle.compute_residuals.md) for the given
    dataset/model.
* `z` (string/float/array, optional): qualifier/twig of the array to plot on the
    z-axis.  By default, this will just order the points on a 2D plot.
    To plot in 3D, also pass `projection='3d'`.
* `s` (strong/float/array, optional): qualifier/twig of the array to use
    for size.  See the [autofig tutorial on size](https://autofig.readthedocs.io/en/latest/tutorials/size_modes/)
    for more information.
* `c` (string/float/array, optional): qualifier/twig of the array to use
    for color.
* `fc` (string/float/array, optional): qualifier/twig of the array to use
    for facecolor (only applicable for mesh plots).
* `ec` (string/float/array, optional): qualifier/twig of the array to use
    for edgecolor (only applicable for mesh plots).   To disable plotting
    edges, use `ec='none'`.  To plot edges in the same colors as the face,
    use `ec='face'` (not supported if `projection='3d'`).

* `i` (string, optional, default='phases' or 'times'): qualifier/twig to
    use for the independent variable.  In the vast majority of cases,
    using the default is sufficient.  `i` will default to 'times' unless
    'phases' is plotted along `x`, `y`, or `z`.  If 'phases' is plotted,
    then `i` will still default to 'times' if the system is time-dependent,
    according to [phoebe.parameters.HierarchyParameter.is_time_dependent](phoebe.parameters.HierarchyParameter.is_time_dependent.md)
    (note that this is determined based on current values of the relevant
    parameters, not neccessarily those when the model was computed),
    otherwise will default to 'phases'.  If `x` is 'phases' or ('phases:[component]'),
    then setting `i` to phases will sort and connect the points in
    phase-order, whereas if set to `times` they will be sorted and connected
    in time-order, with linebreaks when needed for phase-wrapping.
    See also the [autofig tutorial on a looping independent variable](https://autofig.readthedocs.io/en/latest/gallery/looping_indep/).

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
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.
* `ylim` (tuple/string, optional): limits for the y-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.
* `zlim` (tuple/string, optional): limits for the z-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.
* `slim` (tuple/string, optional): limits for the size-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.
* `clim` (tuple/string, optional): limits for the color-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.
* `fclim` (tuple/string, optional): limits for the facecolor-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.
* `eclim` (tuple/string, optional): limits for the edgecolor-axis (will default on
    data if not provided).  See [autofig tutorial on limits](https://autofig.readthedocs.io/en/latest/tutorials/limits/)
    for more information/choices.

* `fcmap` (string, optional): colormap to use for the facecolor-axis (will default on
    the type of data passed to `fc` if not provided, only applicable for mesh plots).
    See the [matplotlib colormap reference](https://matplotlib.org/3.1.0/gallery/color/colormap_reference.html)
    for a list of options (may vary based on installed version of matplotlib).
* `ecmap` (string, optional): colormap to use for the edgecolor-axis (will default on
    the type of data passed to `ec` if not provided, only applicable for mesh plots).
    See the [matplotlib colormap reference](https://matplotlib.org/3.1.0/gallery/color/colormap_reference.html)
    for a list of options (may vary based on installed version of matplotlib).

* `smode` (string, optional): size mode.  See the [autofig tutorial on sizes](https://autofig.readthedocs.io/en/latest/tutorials/size_modes/)
    for more information.

* `highlight` (bool, optional, default=True): whether to highlight at the
    current time.  Only applicable if `time` or `times` provided.
* `highlight_marker` (string, optional): marker to use for highlighting.
    Only applicable if `highlight=True` and `time` or `times` provided.
* `highlight_color` (string, optional): color to use for highlighting.
    Only applicable if `highlight=True` and `time` or `times` provided.
* `highlight_size` (int, optional): size to use for highlighting.
    Only applicable if `highlight=True` and `time` or `times` provided.

* `uncover` (bool, optional): whether to uncover data based on the current
    time.  Only applicable if `time` or `times` provided.
* `trail` (bool or float, optional): whether trail is enabled.
    If a float, then a value between 0 and 1 indicating the fractional
    length of the trail.  Defaults to 0 for mesh and lineprofiles and False
    otherwise.  Only applicable if `times` or `times` provided.

* `legend` (bool, optional, default=False): whether to draw a legend for
    this axes.
* `legend_kwargs` (dict, optional):  keyword arguments (position,
    formatting, etc) to be passed on to [plt.legend](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html)

* `fig` (matplotlib figure, optional): figure to use for plotting.  If
    not provided, will use `plt.gcf()`.  Ignored unless `save`, `show`,
    or `animate`.

* `save` (string, optional, default=False): filename to save the
    figure (or False to not save).
* `show` (bool, optional, default=False): whether to show the plot
* `animate` (bool, optional, default=False): whether to animate the figure.
* `interval` (int, optional, default=100): time in ms between each
    frame in the animation.  Applicable only if `animate` is True.

* `equal_aspect` (optional): whether to force the aspect ratio of the
    axes to be equal.  If not provided, this will default to True if
    all directions (i.e. `x` and `y` for `projection='2d'` or `x`,
    `y`, and `z` for '3d') are positions and of the same units, or
    False otherwise.
* `pad_aspect` (optional): whether to achieve the equal aspect ratio
    by padding the limits instead of whitespace around the axes.  Only
    applicable if `equal_aspect` is True.  If not provided, this will
    default to True unless `animate` is True, in which case it will
    default to False (as autofig cannot currently handle `pad_aspect`)
    in animations.

* `projection` (string, optional, default='2d'): whether to plot
    on a 2d or 3d axes.  If '3d', the orientation of the axes will
    be provided by `azim` and `elev` (see [autofig tutorial on 3d](https://autofig.readthedocs.io/en/latest/tutorials/3d/))
* `azim` (float or list, optional): azimuth to use when `projection`
    is '3d'.  If `animate` is True, then a tuple or list will allow
    rotating the axes throughout the animation (see [autofig tutorial on 3d](https://autofig.readthedocs.io/en/latest/tutorials/3d/))
* `elev` (float or list, optional): elevation to use when `projection`
    is '3d'.  If `animate` is True, then a tuple or list will allow
    rotating the axes throughout the animation (see [autofig tutorial on 3d](https://autofig.readthedocs.io/en/latest/tutorials/3d/))
* `exclude_back` (bool, optional): whether to exclude plotting the back
    of meshes when in '2d' projections.  Defaults to True if `fc` is
    not 'none' (otherwise defaults to False so that you can "see through"
    the star).

* `draw_sidebars` (bool, optional, default=False): whether to include
    any applicable sidebars (colorbar, sizebar, etc).
* `draw_title` (bool, optional, default=False): whether to draw axes
    titles.
* `subplot_grid` (tuple, optional, default=None): override the subplot
    grid used (see [autofig tutorial on subplots](https://autofig.readthedocs.io/en/latest/tutorials/subplot_positioning/)
    for more details).

* `save_kwargs` (dict, optional): any kwargs necessary to pass on to
    save (only applicable if `animate=True`).  On many systems,
    it may be necessary to pass `save_kwargs={'writer': 'imagemagick'}`.

* `**kwargs`: additional keyword arguments are sent along to [autofig](https://autofig.readthedocs.io/en/latest/).

Returns
--------
* (autofig figure, matplotlib figure)

Raises
------------
* ValueError: if both `time` and `phase` or `times` and `phases` are passed.
* ValueError: if the resulting figure is empty.

