#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: Plotting
# ============================

# In PHOEBE 2.1, the plotting logic has been rewritten from scratch within a separate package called [autofig](https://github.com/kecnry/autofig). By doing so, the plotting is now much more flexible and significantly less buggy while also allowing the plotting logic itself to be tested and used outside of PHOEBE.
# 
# Version [1.0 of autofig](https://github.com/kecnry/autofig/tree/1.0.0) is included and built within PHOEBE 2.1 as `phoebe.dependencies.autofig`, regardless of whether you have a standalone autofig installed on your machine.
# 
# When calling [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md), PHOEBE loops through the filtered ParameterSet and makes one or multiple calls to autofig by extracting the necessary arrays and setting reasonable defaults. To see what these calls are, make sure to have the logger set to a level of 'INFO'. [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) then returns the autofig object, as well as the matplotlib figure object (if you set `show=True` or `save=filename`).
# 
# Below we mention the changes to syntax that you need to know if migrating from PHOEBE 2.0 to PHOEBE 2.1.

# ### Linewidth/Markersize
# 
# Autofig attempts to unify calls across matplotlib, including linewidth and markersize. It does so by including the size as an addition dimension `s`. This means that you can pass a value (float) for the size and it will apply to both the linewidth and markersize. If you want separate sizes, you will need to make multiple calls, one with linestyle disabled and the other with marker disabled.
# 
# The benefit of this is that you can also pass an array (or access a PHOEBE array by passing a twig/qualifier) and autofig will map that array and scale the size per-point.
# 
# In PHOEBE 2.0.x: `b.plot(linewidth=4)`
# 
# 
# In PHOEBE 2.1.x: `b.plot(s=4)`, or `b.plot(s='teffs')`.

# ### Facecolor/Edgecolor Options for Meshes
# 
# 
# Similar to size, autofig includes color (for markers and lines), facecolor (for mesh plots only) and edgecolor (for mesh plots only) as additional dimensions.  These are called `c`, `fc`, and `ec`, respectively. This means that you can pass a color (as a string, like 'blue') to any of these arguments, an array (with same length as the underlying data), or a twig/qualifier. The other options for colors (map, lim, unit, label) are all prefixed with this single character (e.g., `fcmap='axmhot'`, `eclabel='temperatures'`).
# 
# PHOEBE 2.1 will attempt to map those onto the autofig names, but it may be less confusing to just stick to the single letter versions. The order of fallback preference for PHOEBE 2.1 is the single character, then the plural version (facecolors), and finally the singular version (facecolor). However, this mapping is NOT done for the extra options (map, lim, etc).
# 

# ### Per-call Styling without Filtering
# 
# If you wanted to manually set your own colors for different datasets, for example, you'd have to filter first and make multiple calls to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) in PHOEBE 2.0.  That will still work in PHOEBE 2.1, but you can now also pass any option as a dictionary, and the values will be applied whenever they match.  For example: `b.plot(..., color={'primary': 'blue', 'secondary': 'red', 'lc01', 'black'})`.
# 
# Note that the previous syntax for passing a bunch of positional arguments, including dictionaries, is now removed.

# ### Better Support for Phase
# 
# In PHOEBE 2.0, if plotting flux vs. phase, for example, the data would be sorted in phase, but if you linestyle be anything other than disabled, the points would be connected in phase-order... which isn't usually what you want.
# 
# In PHOEBE 2.1, with autofig, the points retain there time-order information, are wrapped according to phase, and the line is broken when wrapping in phase (see [this autofig example](http://nbviewer.jupyter.org/github/kecnry/autofig/blob/1.0.0/gallery/looping_indep.ipynb) for a visual explanation).  To disable this behavior, send `linebreak=None` to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md).

# ### Animations
# 
# The `b.animate()` or `PS.animate()` methods have been removed.  Instead, to create an animation, pass `animate=True` (along with `show=True` or `save=filename`) to the [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) call.  In this case, [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) will accept *either* `times` or `time` to be sent as the time for each frame of the animation.
# 
# When animating, [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) will still return the autofig object, but the second returned object will be the matplotlib animation object instead of the figure.

# ### Returned Autofig Object
# 
# Calling [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) now returns the autofig object (as well as the matplotlib figure if showing or saving a figure, otherwise the second returned item will be `None`).
# 
# In PHOEBE 2.0.x: `axs, artists = b.plot(..., show=True)`
# 
# In PHOEBE 2.1.x: `afig, mplfig = b.plot(..., show=True)` or `afig, mplanim = b.plot(..., animate=True, show=True)`.
# 
# With the returned autofig object, you can do anything in the autofig docs, including adding your own external data, re-drawing at different times, re-animating, changing options, etc.  With the returned matplotlib object, you can do anything that you normally could to the matplotlib figure.
# 
# But be careful: successive calls to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) will keep appending to the same autofig figure **until** you call [show()](../api/phoebe.parameters.ParameterSet.show.md) and/or [savefig()](../api/phoebe.parameters.ParameterSet.savefig.md). At that point, the next call to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) will start over on a blank figure.  So, if you want to make any changes, you'll either need to rerun the same lines of code, or keep track of the autofig object itself and make changes there.

# ### Legends
# 
# In PHOEBE 2.0, labels were automatically assigned to draw matplotlib objects, but you were responsible for drawing the legend yourself.  Now in PHOEBE 2.1, simply pass `legend=True` when calling [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md).  Note that if you're building a figure with multiple subplots, this must be done an a per-axes basis and must be sent when calling [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) not [b.show()](../api/phoebe.parameters.ParameterSet.show.md), [b.savefig()](../api/phoebe.parameters.ParameterSet.savefig.md), etc.
# 
# If you'd like to customize any options (location, styling, etc), pass those to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) as `legend_kwargs`.  For example: `b.plot(..., legend=True, legend_kwargs={'loc': 3})`.  See the [matplotlib legend documention](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html) for a list of available options.
# 
# To override the default labels added to the legend, pass a value for `label` to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md).  Note that this label will be applied to all subcalls.  So if you're making one call to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) for multiple datasets, either filter first or you can pass label as a dictionary (see above for more details).

# ### Custom Subplots
# 
# In PHOEBE 2.0 you could pass matplotlib axes instances to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md).  With autofig, you can now pass `axorder`, `axpos`, and/or `subplot_grid` when calling [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md).  See the [autofig tutorial on axes positioning](http://nbviewer.jupyter.org/github/kecnry/autofig/blob/1.0.0/tutorials/subplot_positioning.ipynb) for more details.
# 
# You're of course also always welcome to plot your own arrays using matplotlib or manipulate the returned autofig or matplotlib figure objects.

# ### 3D Axes
# 
# In PHOEBE 2.0, the only way to plot in 3D was by passing a 3d matplotlib axes instance to the plot call.  Now, simply pass `projection='3d'` to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md).  Note that if you're building a figure with multiple subplots, this must be done on a per-axes basis and must be sent when calling [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) not [b.show()](../api/phoebe.parameters.ParameterSet.show.md), [b.savefig()](../api/phoebe.parameters.ParameterSet.savefig.md), etc.

# ### 3D Perspective
# 
# Want to have your 3D axes rotate during your animation?  Why not!  Just pass `azim` and/or `elev` to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) and they'll be passed along to autofig (as long as you also have `projection='3d'`).  See this [autofig animation](http://nbviewer.jupyter.org/github/kecnry/autofig/blob/1.0.0/gallery/3d_animation.ipynb) for more details.

# ### Numerous Bugfixes
# 
# Plotting in PHOEBE 2.0 suffered from a number of minor bugs, especially when making multiple calls to [b.plot()](../api/phoebe.parameters.ParameterSet.plot.md) (with meshes overlapping), or trying to plot meshes with facecolor from a dataset and PHOEBE complaining about finding multiple matches, or colorbars not remaining fixed between components or frames of an animation.  Autofig now handles all of this logic and should fix the vast majority of these annoying bugs.

# In[ ]:




