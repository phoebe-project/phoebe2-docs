### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).show (method)


```py

def show(self, **kwargs)

```



Draw and show the plot.

See also:
* [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md)
* [phoebe.parameters.ParameterSet.savefig](phoebe.parameters.ParameterSet.savefig.md)
* [phoebe.parameters.ParameterSet.gcf](phoebe.parameters.ParameterSet.gcf.md)
* [phoebe.parameters.ParameterSet.clf](phoebe.parameters.ParameterSet.clf.md)

Arguments
----------
* `show` (bool, optional, default=True): whether to show the plot
* `save` (False/string, optional, default=False): filename to save the
    figure (or False to not save).
* `animate` (bool, optional, default=False): whether to animate the figure.
* `fig` (matplotlib figure, optional): figure to use for plotting.  If
    not provided, will use plt.gcf().  Ignored unless `save`, `show`,
    or `animate`.
* `draw_sidebars` (bool, optional, default=True): whether to include
    any applicable sidebars (colorbar, sizebar, etc).
* `draw_title` (bool, optional, default=True): whether to draw axes
    titles.
* `subplot_grid` (tuple, optional, default=None): override the subplot
    grid used (see [autofig tutorial on subplots](https://github.com/kecnry/autofig/blob/1.0.0/tutorials/subplot_positioning.ipynb)
    for more details).
* `time` (float, optional): time to use for plotting/animating.
* `times` (list/array, optional): times to use for animating (will
    override any value sent to `time`).
* `save_kwargs` (dict, optional): any kwargs necessary to pass on to
    save (only applicable if `animate=True`).

Returns
--------
* (autofig figure, matplotlib figure)

