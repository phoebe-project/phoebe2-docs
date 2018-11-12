### ParameterSet.animate

```py

def animate(self, *args, **kwargs)

```



NOTE: any drawing done to the figure (or its children axes) before calling
animate will remain on every frame and will not update.

NOTE: if show and save provided, the live plot will be shown first,
as soon as the plot is closed the animation will be re-compiled and saved to
disk, and then the anim object will be returned.

NOTE: during 'show' the plotting speed may be slower than the provided
interval - especially if plotting meshes.

:parameter *args: either a twig pointing to a dataset,
    or dictionaries, where each dictionary gets passed to
    :meth:`plot` for each frame (see example scripts for more details).
:parameter times: list of times - each time will create a single
    frame in the animation
:parameter bool fixed_limits: whether all the axes should have the
    same limits for each frame (if True), or resizing limits based
    on the contents of that individual frame (if False).  Note: if False,
    limits will be automatically set at each frame - meaning manually zooming
    in the matplotlib will revert at the next drawn frame.
:parameter int interval: time interval in ms between each frame (default: 100)
:parameter str save: filename of the resulting animation.  If provided,
    the animation will be saved automatically.  Either way, the animation
    object is returned (so you can always call anim.save(fname)).
:parameter list save_args: any additional arguments that need to be sent
    to the anim.save call (as extra_args)
:parameter bool show: whether to automatically show the animation (defaults
    to False).  Either way, the animation object is returned (so you can
    always call b.show() or plt.show())
:parameter kwargs: any additional arguments will be passed along to each
    call of :meth:`plot`, unless they are already specified (ie. twig_or_list_of_kwargs
    has priority of kwargs)
:return fname: returns the created filename

