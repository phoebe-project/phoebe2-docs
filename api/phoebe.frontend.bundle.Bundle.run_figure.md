### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_figure (function)


```py

def run_figure(self, figure=None, **kwargs)

```



Plot a figure for a set of figure options attached to the bundle.

For plotting without the help of figure options, see
[phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md).

In general, `run_figure` is useful for creating simple plots with
consistent defaults for styling across datasets/components/etc,
when plotting from a UI, or when wanting to save plotting options
along with the bundle rather than in a script.  `plot` is more
more flexible, allows for multiple subplots and advanced positioning,
and is less clumsy if plotting from the python frontend.

See also:
* [phoebe.frontend.bundle.Bundle.ui_figures](phoebe.frontend.bundle.Bundle.ui_figures.md)
* [phoebe.frontend.bundle.Bundle.add_figure](phoebe.frontend.bundle.Bundle.add_figure.md)
* [phoebe.frontend.bundle.Bundle.get_figure](phoebe.frontend.bundle.Bundle.get_figure.md)
* [phoebe.frontend.bundle.Bundle.remove_figure](phoebe.frontend.bundle.Bundle.remove_figure.md)
* [phoebe.frontend.bundle.Bundle.rename_figure](phoebe.frontend.bundle.Bundle.rename_figure.md)
* [phoebe.frontend.bundle.Bundle.run_checks_figure](phoebe.frontend.bundle.Bundle.run_checks_figure.md)

Arguments
-----------
* `figure` (string or list, optional): name of the figure(s) options to use.
    If not provided or None, run_figure will run all attached figures
    in subplots, as necessary.
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
* `save` (string, optional, default=False): filename to save the
    figure (or False to not save).
* `show` (bool, optional, default=False): whether to show the plot
* `animate` (bool, optional, default=False): whether to animate the figure.
* `interval` (int, optional, default=100): time in ms between each
    frame in the animation.  Applicable only if `animate` is True.
* `**kwargs`: all additional keyword arguments will be used to override
    parameters in the figure options or passed along to
    [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md).  See the API docs for
    [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md) for an exhaustive list
    of plotting options.  If `figure` is passed as a list (or as None and
    multiple figures exist in the bundle), then kwargs can be passed
    as dictionaries with keys of the individual `figure` labels, which
    will be applied to individual `run_figure` calls when matching.
    For example: `b.run_figure(figure=['lcfig01', 'rvfig01'], axpos={'lcfig01': 121, 'rvfig01', 122}, show=True)`

Returns
-----------
* (autofig figure, matplotlib figure) - the output from the call to
    [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md)


Raises
----------
* ValueError: if `figure` is not provided but is required.

