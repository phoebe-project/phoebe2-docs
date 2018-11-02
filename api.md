# Package phoebe Documentation

Import PHOEBE 2
## Class ArrayParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### append
```py

def append(self, value)

```



        


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class Axes3D
3D axes object.
### \_\_init\_\_
```py

def __init__(self, fig, rect=None, *args, **kwargs)

```



### acorr
```py

def acorr(ax, *args, **kwargs)

```



Plot the autocorrelation of `x`.

Parameters
----------

x : sequence of scalar

hold : boolean, optional, *deprecated*, default: True

detrend : callable, optional, default: `mlab.detrend_none`
    x is detrended by the `detrend` callable. Default is no
    normalization.

normed : boolean, optional, default: True
    if True, input vectors are normalised to unit length.

usevlines : boolean, optional, default: True
    if True, Axes.vlines is used to plot the vertical lines from the
    origin to the acorr. Otherwise, Axes.plot is used.

maxlags : integer, optional, default: 10
    number of lags to show. If None, will return all 2 * len(x) - 1
    lags.

Returns
-------
(lags, c, line, b) : where:

  - `lags` are a length 2`maxlags+1 lag vector.
  - `c` is the 2`maxlags+1 auto correlation vectorI
  - `line` is a `~matplotlib.lines.Line2D` instance returned by
    `plot`.
  - `b` is the x-axis.

Other Parameters
----------------
linestyle : `~matplotlib.lines.Line2D` prop, optional, default: None
    Only used if usevlines is False.

marker : string, optional, default: 'o'

Notes
-----
The cross correlation is performed with :func:`numpy.correlate` with
`mode` = 2.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x'.


### add\_artist
```py

def add_artist(self, a)

```



Add any :class:`~matplotlib.artist.Artist` to the axes.

Use `add_artist` only for artists for which there is no dedicated
"add" method; and if necessary, use a method such as
`update_datalim` or `update_datalim_numerix` to manually update the
dataLim if the artist is to be included in autoscaling.

Returns the artist.


### add\_callback
```py

def add_callback(self, func)

```



Adds a callback function that will be called whenever one of
the :class:`Artist`'s properties changes.

Returns an *id* that is useful for removing the callback with
:meth:`remove_callback` later.


### add\_collection
```py

def add_collection(self, collection, autolim=True)

```



Add a :class:`~matplotlib.collections.Collection` instance
to the axes.

Returns the collection.


### add\_collection3d
```py

def add_collection3d(self, col, zs=0, zdir=u'z')

```



Add a 3D collection object to the plot.

2D collection types are converted to a 3D version by
modifying the object and adding z coordinate information.

Supported are:
    - PolyCollection
    - LineCollection
    - PatchCollection


### add\_container
```py

def add_container(self, container)

```



Add a :class:`~matplotlib.container.Container` instance
to the axes.

Returns the collection.


### add\_contour\_set
```py

def add_contour_set(self, cset, extend3d=False, stride=5, zdir=u'z', offset=None)

```



### add\_contourf\_set
```py

def add_contourf_set(self, cset, zdir=u'z', offset=None)

```



### add\_image
```py

def add_image(self, image)

```



Add a :class:`~matplotlib.image.AxesImage` to the axes.

Returns the image.


### add\_line
```py

def add_line(self, line)

```



Add a :class:`~matplotlib.lines.Line2D` to the list of plot
lines

Returns the line.


### add\_patch
```py

def add_patch(self, p)

```



Add a :class:`~matplotlib.patches.Patch` *p* to the list of
axes patches; the clipbox will be set to the Axes clipping
box.  If the transform is not set, it will be set to
:attr:`transData`.

Returns the patch.


### add\_table
```py

def add_table(self, tab)

```



Add a :class:`~matplotlib.tables.Table` instance to the
list of axes tables

Returns the table.


### angle\_spectrum
```py

def angle_spectrum(ax, *args, **kwargs)

```



Plot the angle spectrum.

Call signature::

  angle_spectrum(x, Fs=2, Fc=0,  window=mlab.window_hanning,
                 pad_to=None, sides='default', **kwargs)

Compute the angle spectrum (wrapped phase spectrum) of *x*.
Data is padded to a length of *pad_to* and the windowing function
*window* is applied to the signal.

Parameters
----------
x : 1-D array or sequence
    Array or sequence containing the data

Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  While not increasing the actual resolution of
    the spectrum (the minimum distance between resolvable peaks),
    this can give more points in the plot, allowing for more
    detail. This corresponds to the *n* parameter in the call to fft().
    The default is None, which sets *pad_to* equal to the length of the
    input signal (i.e. no padding).

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.

Returns
-------
spectrum : 1-D array
    The values for the angle spectrum in radians (real valued)

freqs : 1-D array
    The frequencies corresponding to the elements in *spectrum*

line : a :class:`~matplotlib.lines.Line2D` instance
    The line created by this function

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

See Also
--------
:func:`magnitude_spectrum`
    :func:`angle_spectrum` plots the magnitudes of the corresponding
    frequencies.

:func:`phase_spectrum`
    :func:`phase_spectrum` plots the unwrapped version of this
    function.

:func:`specgram`
    :func:`specgram` can plot the angle spectrum of segments within the
    signal in a colormap.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x'.


### annotate
```py

def annotate(self, *args, **kwargs)

```



Annotate the point ``xy`` with text ``s``.

Additional kwargs are passed to `~matplotlib.text.Text`.

Parameters
----------

s : str
    The text of the annotation

xy : iterable
    Length 2 sequence specifying the *(x,y)* point to annotate

xytext : iterable, optional
    Length 2 sequence specifying the *(x,y)* to place the text
    at.  If None, defaults to ``xy``.

xycoords : str, Artist, Transform, callable or tuple, optional

    The coordinate system that ``xy`` is given in.

    For a `str` the allowed values are:

    =================   ===============================================
    Property            Description
    =================   ===============================================
    'figure points'     points from the lower left of the figure
    'figure pixels'     pixels from the lower left of the figure
    'figure fraction'   fraction of figure from lower left
    'axes points'       points from lower left corner of axes
    'axes pixels'       pixels from lower left corner of axes
    'axes fraction'     fraction of axes from lower left
    'data'              use the coordinate system of the object being
                        annotated (default)
    'polar'             *(theta,r)* if not native 'data' coordinates
    =================   ===============================================

    If a `~matplotlib.artist.Artist` object is passed in the units are
    fraction if it's bounding box.

    If a `~matplotlib.transforms.Transform` object is passed
    in use that to transform ``xy`` to screen coordinates

    If a callable it must take a
    `~matplotlib.backend_bases.RendererBase` object as input
    and return a `~matplotlib.transforms.Transform` or
    `~matplotlib.transforms.Bbox` object

    If a `tuple` must be length 2 tuple of str, `Artist`,
    `Transform` or callable objects.  The first transform is
    used for the *x* coordinate and the second for *y*.

    See :ref:`plotting-guide-annotation` for more details.

    Defaults to ``'data'``

textcoords : str, `Artist`, `Transform`, callable or tuple, optional
    The coordinate system that ``xytext`` is given, which
    may be different than the coordinate system used for
    ``xy``.

    All ``xycoords`` values are valid as well as the following
    strings:

    =================   =========================================
    Property            Description
    =================   =========================================
    'offset points'     offset (in points) from the *xy* value
    'offset pixels'     offset (in pixels) from the *xy* value
    =================   =========================================

    defaults to the input of ``xycoords``

arrowprops : dict, optional
    If not None, properties used to draw a
    `~matplotlib.patches.FancyArrowPatch` arrow between ``xy`` and
    ``xytext``.

    If `arrowprops` does not contain the key ``'arrowstyle'`` the
    allowed keys are:

    ==========   ======================================================
    Key          Description
    ==========   ======================================================
    width        the width of the arrow in points
    headwidth    the width of the base of the arrow head in points
    headlength   the length of the arrow head in points
    shrink       fraction of total length to 'shrink' from both ends
    ?            any key to :class:`matplotlib.patches.FancyArrowPatch`
    ==========   ======================================================

    If the `arrowprops` contains the key ``'arrowstyle'`` the
    above keys are forbidden.  The allowed values of
    ``'arrowstyle'`` are:

    ============   =============================================
    Name           Attrs
    ============   =============================================
    ``'-'``        None
    ``'->'``       head_length=0.4,head_width=0.2
    ``'-['``       widthB=1.0,lengthB=0.2,angleB=None
    ``'|-|'``      widthA=1.0,widthB=1.0
    ``'-|>'``      head_length=0.4,head_width=0.2
    ``'<-'``       head_length=0.4,head_width=0.2
    ``'<->'``      head_length=0.4,head_width=0.2
    ``'<|-'``      head_length=0.4,head_width=0.2
    ``'<|-|>'``    head_length=0.4,head_width=0.2
    ``'fancy'``    head_length=0.4,head_width=0.4,tail_width=0.4
    ``'simple'``   head_length=0.5,head_width=0.5,tail_width=0.2
    ``'wedge'``    tail_width=0.3,shrink_factor=0.5
    ============   =============================================

    Valid keys for `~matplotlib.patches.FancyArrowPatch` are:

    ===============  ==================================================
    Key              Description
    ===============  ==================================================
    arrowstyle       the arrow style
    connectionstyle  the connection style
    relpos           default is (0.5, 0.5)
    patchA           default is bounding box of the text
    patchB           default is None
    shrinkA          default is 2 points
    shrinkB          default is 2 points
    mutation_scale   default is text size (in points)
    mutation_aspect  default is 1.
    ?                any key for :class:`matplotlib.patches.PathPatch`
    ===============  ==================================================

    Defaults to None

annotation_clip : bool, optional
    Controls the visibility of the annotation when it goes
    outside the axes area.

    If `True`, the annotation will only be drawn when the
    ``xy`` is inside the axes. If `False`, the annotation will
    always be drawn regardless of its position.

    The default is `None`, which behave as `True` only if
    *xycoords* is "data".

Returns
-------
Annotation


### apply\_aspect
```py

def apply_aspect(self, position=None)

```



Use :meth:`_aspect` and :meth:`_adjustable` to modify the
axes box or the view limits.


### arrow
```py

def arrow(self, x, y, dx, dy, **kwargs)

```



Add an arrow to the axes.

Draws arrow on specified axis from (`x`, `y`) to (`x` + `dx`,
`y` + `dy`). Uses FancyArrow patch to construct the arrow.

Parameters
----------
x : float
    X-coordinate of the arrow base
y : float
    Y-coordinate of the arrow base
dx : float
    Length of arrow along x-coordinate
dy : float
    Length of arrow along y-coordinate

Returns
-------
a : FancyArrow
    patches.FancyArrow object

Other Parameters
-----------------
Optional kwargs (inherited from FancyArrow patch) control the arrow
construction and properties:

Constructor arguments
  *width*: float (default: 0.001)
    width of full arrow tail

  *length_includes_head*: [True | False] (default: False)
    True if head is to be counted in calculating the length.

  *head_width*: float or None (default: 3*width)
    total width of the full arrow head

  *head_length*: float or None (default: 1.5 * head_width)
    length of arrow head

  *shape*: ['full', 'left', 'right'] (default: 'full')
    draw the left-half, right-half, or full arrow

  *overhang*: float (default: 0)
    fraction that the arrow is swept back (0 overhang means
    triangular shape). Can be negative or greater than one.

  *head_starts_at_zero*: [True | False] (default: False)
    if True, the head starts being drawn at coordinate 0
    instead of ending at coordinate 0.

Other valid kwargs (inherited from :class:`Patch`) are:
  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or aa: [True | False]  or None for default 
  capstyle: ['butt' | 'round' | 'projecting'] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color: matplotlib color spec
  contains: a callable function 
  edgecolor or ec: mpl color spec, None, 'none', or 'auto' 
  facecolor or fc: mpl color spec, or None for default, or 'none' for no color 
  figure: a `~.Figure` instance 
  fill: [True | False] 
  gid: an id string 
  hatch: ['/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*'] 
  joinstyle: ['miter' | 'round' | 'bevel'] 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float or None for default 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  visible: bool 
  zorder: float 

Notes
-----
The resulting arrow is affected by the axes aspect ratio and limits.
This may produce an arrow whose head is not square with its stem. To
create an arrow whose head is square with its stem, use
:meth:`annotate` for example::

    ax.annotate("", xy=(0.5, 0.5), xytext=(0, 0),
        arrowprops=dict(arrowstyle="->"))


### auto\_scale\_xyz
```py

def auto_scale_xyz(self, X, Y, Z=None, had_data=None)

```



### autoscale
```py

def autoscale(self, enable=True, axis=u'both', tight=None)

```



Convenience method for simple axis view autoscaling.
See :meth:`matplotlib.axes.Axes.autoscale` for full explanation.
Note that this function behaves the same, but for all
three axes.  Therfore, 'z' can be passed for *axis*,
and 'both' applies to all three axes.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### autoscale\_view
```py

def autoscale_view(self, tight=None, scalex=True, scaley=True, scalez=True)

```



Autoscale the view limits using the data limits.
See :meth:`matplotlib.axes.Axes.autoscale_view` for documentation.
Note that this function applies to the 3D axes, and as such
adds the *scalez* to the function arguments.

.. versionchanged :: 1.1.0
    Function signature was changed to better match the 2D version.
    *tight* is now explicitly a kwarg and placed first.

.. versionchanged :: 1.2.1
    This is now fully functional.


### axhline
```py

def axhline(self, y=0, xmin=0, xmax=1, **kwargs)

```



Add a horizontal line across the axis.

Parameters
----------
y : scalar, optional, default: 0
    y position in data coordinates of the horizontal line.

xmin : scalar, optional, default: 0
    Should be between 0 and 1, 0 being the far left of the plot, 1 the
    far right of the plot.

xmax : scalar, optional, default: 1
    Should be between 0 and 1, 0 being the far left of the plot, 1 the
    far right of the plot.

Returns
-------
:class:`~matplotlib.lines.Line2D`

Other Parameters
----------------
**kwargs :
    Valid kwargs are :class:`~matplotlib.lines.Line2D` properties,
    with the exception of 'transform':

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

Notes
-----
kwargs are passed to :class:`~matplotlib.lines.Line2D` and can be used
to control the line properties.

Examples
--------

* draw a thick red hline at 'y' = 0 that spans the xrange::

    >>> axhline(linewidth=4, color='r')

* draw a default hline at 'y' = 1 that spans the xrange::

    >>> axhline(y=1)

* draw a default hline at 'y' = .5 that spans the middle half of
  the xrange::

    >>> axhline(y=.5, xmin=0.25, xmax=0.75)

See also
--------
hlines : add horizontal lines in data coordinates
axhspan : add a horizontal span (rectangle) across the axis


### axhspan
```py

def axhspan(self, ymin, ymax, xmin=0, xmax=1, **kwargs)

```



Add a horizontal span (rectangle) across the axis.

Draw a horizontal span (rectangle) from *ymin* to *ymax*.
With the default values of *xmin* = 0 and *xmax* = 1, this
always spans the xrange, regardless of the xlim settings, even
if you change them, e.g., with the :meth:`set_xlim` command.
That is, the horizontal extent is in axes coords: 0=left,
0.5=middle, 1.0=right but the *y* location is in data
coordinates.

Parameters
----------
ymin : float
       Lower limit of the horizontal span in data units.
ymax : float
       Upper limit of the horizontal span in data units.
xmin : float, optional, default: 0
       Lower limit of the vertical span in axes (relative
       0-1) units.
xmax : float, optional, default: 1
       Upper limit of the vertical span in axes (relative
       0-1) units.

Returns
-------
Polygon : `~matplotlib.patches.Polygon`

Other Parameters
----------------
**kwargs : `~matplotlib.patches.Polygon` properties.

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or aa: [True | False]  or None for default 
  capstyle: ['butt' | 'round' | 'projecting'] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color: matplotlib color spec
  contains: a callable function 
  edgecolor or ec: mpl color spec, None, 'none', or 'auto' 
  facecolor or fc: mpl color spec, or None for default, or 'none' for no color 
  figure: a `~.Figure` instance 
  fill: [True | False] 
  gid: an id string 
  hatch: ['/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*'] 
  joinstyle: ['miter' | 'round' | 'bevel'] 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float or None for default 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  visible: bool 
  zorder: float 

See Also
--------
axvspan : add a vertical span across the axes


### axis
```py

def axis(self, *v, **kwargs)

```



Set axis properties.

Valid signatures::

  xmin, xmax, ymin, ymax = axis()
  xmin, xmax, ymin, ymax = axis(list_arg)
  xmin, xmax, ymin, ymax = axis(string_arg)
  xmin, xmax, ymin, ymax = axis(**kwargs)

Parameters
----------
v : list of float or {'on', 'off', 'equal', 'tight', 'scaled',            'normal', 'auto', 'image', 'square'}
    Optional positional argument

    Axis data limits set from a list; or a command relating to axes:

        ========== ================================================
        Value      Description
        ========== ================================================
        'on'       Toggle axis lines and labels on
        'off'      Toggle axis lines and labels off
        'equal'    Equal scaling by changing limits
        'scaled'   Equal scaling by changing box dimensions
        'tight'    Limits set such that all data is shown
        'auto'     Automatic scaling, fill rectangle with data
        'normal'   Same as 'auto'; deprecated
        'image'    'scaled' with axis limits equal to data limits
        'square'   Square plot; similar to 'scaled', but initially                           forcing xmax-xmin = ymax-ymin
        ========== ================================================

emit : bool, optional
    Passed to set_{x,y}lim functions, if observers
    are notified of axis limit change

xmin, ymin, xmax, ymax : float, optional
    The axis limits to be set

Returns
-------
xmin, xmax, ymin, ymax : float
    The axis limits


### axvline
```py

def axvline(self, x=0, ymin=0, ymax=1, **kwargs)

```



Add a vertical line across the axes.

Parameters
----------
x : scalar, optional, default: 0
    x position in data coordinates of the vertical line.

ymin : scalar, optional, default: 0
    Should be between 0 and 1, 0 being the bottom of the plot, 1 the
    top of the plot.

ymax : scalar, optional, default: 1
    Should be between 0 and 1, 0 being the bottom of the plot, 1 the
    top of the plot.

Returns
-------
:class:`~matplotlib.lines.Line2D`

Other Parameters
----------------
**kwargs :
    Valid kwargs are :class:`~matplotlib.lines.Line2D` properties,
    with the exception of 'transform':

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

Examples
--------
* draw a thick red vline at *x* = 0 that spans the yrange::

    >>> axvline(linewidth=4, color='r')

* draw a default vline at *x* = 1 that spans the yrange::

    >>> axvline(x=1)

* draw a default vline at *x* = .5 that spans the middle half of
  the yrange::

    >>> axvline(x=.5, ymin=0.25, ymax=0.75)

See also
--------
vlines : add vertical lines in data coordinates
axvspan : add a vertical span (rectangle) across the axis


### axvspan
```py

def axvspan(self, xmin, xmax, ymin=0, ymax=1, **kwargs)

```



Add a vertical span (rectangle) across the axes.

Draw a vertical span (rectangle) from `xmin` to `xmax`.  With
the default values of `ymin` = 0 and `ymax` = 1. This always
spans the yrange, regardless of the ylim settings, even if you
change them, e.g., with the :meth:`set_ylim` command.  That is,
the vertical extent is in axes coords: 0=bottom, 0.5=middle,
1.0=top but the y location is in data coordinates.

Parameters
----------
xmin : scalar
    Number indicating the first X-axis coordinate of the vertical
    span rectangle in data units.
xmax : scalar
    Number indicating the second X-axis coordinate of the vertical
    span rectangle in data units.
ymin : scalar, optional
    Number indicating the first Y-axis coordinate of the vertical
    span rectangle in relative Y-axis units (0-1). Default to 0.
ymax : scalar, optional
    Number indicating the second Y-axis coordinate of the vertical
    span rectangle in relative Y-axis units (0-1). Default to 1.

Returns
-------
rectangle : matplotlib.patches.Polygon
    Vertical span (rectangle) from (xmin, ymin) to (xmax, ymax).

Other Parameters
----------------
**kwargs
    Optional parameters are properties of the class
    matplotlib.patches.Polygon.

See Also
--------
axhspan : add a horizontal span across the axes

Examples
--------
Draw a vertical, green, translucent rectangle from x = 1.25 to
x = 1.55 that spans the yrange of the axes.

>>> axvspan(1.25, 1.55, facecolor='g', alpha=0.5)


### bar
```py

def bar(self, left, height, zs=0, zdir=u'z', *args, **kwargs)

```



Add 2D bar(s).

==========  ================================================
Argument    Description
==========  ================================================
*left*      The x coordinates of the left sides of the bars.
*height*    The height of the bars.
*zs*        Z coordinate of bars, if one value is specified
            they will all be placed at the same z.
*zdir*      Which direction to use as z ('x', 'y' or 'z')
            when plotting a 2D set.
==========  ================================================

Keyword arguments are passed onto :func:`~matplotlib.axes.Axes.bar`.

Returns a :class:`~mpl_toolkits.mplot3d.art3d.Patch3DCollection`


### bar3d
```py

def bar3d(self, x, y, z, dx, dy, dz, color=None, zsort=u'average', shade=True, *args, **kwargs)

```



Generate a 3D barplot.

This method creates three dimensional barplot where the width,
depth, height, and color of the bars can all be uniquely set.

Parameters
----------
x, y, z : array-like
    The coordinates of the anchor point of the bars.

dx, dy, dz : scalar or array-like
    The width, depth, and height of the bars, respectively.

color : sequence of valid color specifications, optional
    The color of the bars can be specified globally or
    individually. This parameter can be:

      - A single color value, to color all bars the same color.
      - An array of colors of length N bars, to color each bar
        independently.
      - An array of colors of length 6, to color the faces of the
        bars similarly.
      - An array of colors of length 6 * N bars, to color each face
        independently.

    When coloring the faces of the boxes specifically, this is
    the order of the coloring:

      1. -Z (bottom of box)
      2. +Z (top of box)
      3. -Y
      4. +Y
      5. -X
      6. +X

zsort : str, optional
    The z-axis sorting scheme passed onto
    :func:`~mpl_toolkits.mplot3d.art3d.Poly3DCollection`

shade : bool, optional (default = True)
    When true, this shades the dark sides of the bars (relative
    to the plot's source of light).

Any additional keyword arguments are passed onto
:func:`~mpl_toolkits.mplot3d.art3d.Poly3DCollection`

Returns
-------
collection : Poly3DCollection
    A collection of three dimensional polygons representing
    the bars.


### barbs
```py

def barbs(ax, *args, **kwargs)

```



Plot a 2-D field of barbs.

Call signatures::

  barb(U, V, **kw)
  barb(U, V, C, **kw)
  barb(X, Y, U, V, **kw)
  barb(X, Y, U, V, C, **kw)

Arguments:

  *X*, *Y*:
    The x and y coordinates of the barb locations
    (default is head of barb; see *pivot* kwarg)

  *U*, *V*:
    Give the x and y components of the barb shaft

  *C*:
    An optional array used to map colors to the barbs

All arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*
are absent, they will be generated as a uniform grid.  If *U* and *V*
are 2-D arrays but *X* and *Y* are 1-D, and if ``len(X)`` and ``len(Y)``
match the column and row dimensions of *U*, then *X* and *Y* will be
expanded with :func:`numpy.meshgrid`.

*U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not
supported at present.

Keyword arguments:

  *length*:
    Length of the barb in points; the other parts of the barb
    are scaled against this.
    Default is 7.

  *pivot*: [ 'tip' | 'middle' | float ]
    The part of the arrow that is at the grid point; the arrow rotates
    about this point, hence the name *pivot*.  Default is 'tip'. Can
    also be a number, which shifts the start of the barb that many
    points from the origin.

  *barbcolor*: [ color | color sequence ]
    Specifies the color all parts of the barb except any flags.  This
    parameter is analagous to the *edgecolor* parameter for polygons,
    which can be used instead. However this parameter will override
    facecolor.

  *flagcolor*: [ color | color sequence ]
    Specifies the color of any flags on the barb.  This parameter is
    analagous to the *facecolor* parameter for polygons, which can be
    used instead. However this parameter will override facecolor.  If
    this is not set (and *C* has not either) then *flagcolor* will be
    set to match *barbcolor* so that the barb has a uniform color. If
    *C* has been set, *flagcolor* has no effect.

  *sizes*:
    A dictionary of coefficients specifying the ratio of a given
    feature to the length of the barb. Only those values one wishes to
    override need to be included.  These features include:

        - 'spacing' - space between features (flags, full/half barbs)

        - 'height' - height (distance from shaft to top) of a flag or
          full barb

        - 'width' - width of a flag, twice the width of a full barb

        - 'emptybarb' - radius of the circle used for low magnitudes

  *fill_empty*:
    A flag on whether the empty barbs (circles) that are drawn should
    be filled with the flag color.  If they are not filled, they will
    be drawn such that no color is applied to the center.  Default is
    False

  *rounding*:
    A flag to indicate whether the vector magnitude should be rounded
    when allocating barb components.  If True, the magnitude is
    rounded to the nearest multiple of the half-barb increment.  If
    False, the magnitude is simply truncated to the next lowest
    multiple.  Default is True

  *barb_increments*:
    A dictionary of increments specifying values to associate with
    different parts of the barb. Only those values one wishes to
    override need to be included.

        - 'half' - half barbs (Default is 5)

        - 'full' - full barbs (Default is 10)

        - 'flag' - flags (default is 50)

  *flip_barb*:
    Either a single boolean flag or an array of booleans.  Single
    boolean indicates whether the lines and flags should point
    opposite to normal for all barbs.  An array (which should be the
    same size as the other data arrays) indicates whether to flip for
    each individual barb.  Normal behavior is for the barbs and lines
    to point right (comes from wind barbs having these features point
    towards low pressure in the Northern Hemisphere.)  Default is
    False

Barbs are traditionally used in meteorology as a way to plot the speed
and direction of wind observations, but can technically be used to
plot any two dimensional vector quantity.  As opposed to arrows, which
give vector magnitude by the length of the arrow, the barbs give more
quantitative information about the vector magnitude by putting slanted
lines or a triangle for various increments in magnitude, as show
schematically below::

 :     /\    \\
 :    /  \    \\
 :   /    \    \    \\
 :  /      \    \    \\
 : ------------------------------

.. note the double \\ at the end of each line to make the figure
.. render correctly

The largest increment is given by a triangle (or "flag"). After those
come full lines (barbs). The smallest increment is a half line.  There
is only, of course, ever at most 1 half line.  If the magnitude is
small and only needs a single half-line and no full lines or
triangles, the half-line is offset from the end of the barb so that it
can be easily distinguished from barbs with a single full line.  The
magnitude for the barb shown above would nominally be 65, using the
standard increments of 50, 10, and 5.

linewidths and edgecolors can be used to customize the barb.
Additional :class:`~matplotlib.collections.PolyCollection` keyword
arguments:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 


.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### barh
```py

def barh(self, *args, **kwargs)

```



Make a horizontal bar plot.

Call signatures::

   bar(y, width, *, align='center', **kwargs)
   bar(y, width, height, *, align='center', **kwargs)
   bar(y, width, height, left, *, align='center', **kwargs)

Make a horizontal bar plot with rectangles by default bounded by

.. math::

   (left, left + width, y - height/2, y + height/2)

(left, right, bottom and top edges) by default.  *y*, *width*,
*height*, and *left* can be either scalars or sequences.

The *align* keyword-only argument controls if *y* is interpreted
as the center or the bottom edge of the rectangle.


Parameters
----------
y : scalar or array-like
    the y coordinate(s) of the bars

    *align* controls if *y* is the bar center (default)
    or bottom edge.

width : scalar or array-like
    the width(s) of the bars

height : sequence of scalars, optional, default: 0.8
    the heights of the bars

left : sequence of scalars
    the x coordinates of the left sides of the bars

align : {'center', 'edge'}, optional, default: 'center'
    If 'center', interpret the *y* argument as the coordinates
    of the centers of the bars.  If 'edge', aligns bars by
    their bottom edges

    To align the bars on the top edge pass a negative
    *height* and ``align='edge'``

Returns
-------
`matplotlib.patches.Rectangle` instances.

Other Parameters
----------------
color : scalar or array-like, optional
    the colors of the bars

edgecolor : scalar or array-like, optional
    the colors of the bar edges

linewidth : scalar or array-like, optional, default: None
    width of bar edge(s). If None, use default
    linewidth; If 0, don't draw edges.

tick_label : string or array-like, optional, default: None
    the tick labels of the bars

xerr : scalar or array-like, optional, default: None
    if not None, will be used to generate errorbar(s) on the bar chart

yerr : scalar or array-like, optional, default: None
    if not None, will be used to generate errorbar(s) on the bar chart

ecolor : scalar or array-like, optional, default: None
    specifies the color of errorbar(s)

capsize : scalar, optional
   determines the length in points of the error bar caps
   default: None, which will take the value from the
   ``errorbar.capsize`` :data:`rcParam<matplotlib.rcParams>`.

error_kw :
    dictionary of kwargs to be passed to errorbar method. `ecolor` and
    `capsize` may be specified here rather than as independent kwargs.

log : boolean, optional, default: False
    If true, sets the axis to be log scale

See also
--------
bar: Plot a vertical bar plot.

Notes
-----
The optional arguments *color*, *edgecolor*, *linewidth*,
*xerr*, and *yerr* can be either scalars or sequences of
length equal to the number of bars.  This enables you to use
bar as the basis for stacked bar charts, or candlestick plots.
Detail: *xerr* and *yerr* are passed directly to
:meth:`errorbar`, so they can also have shape 2xN for
independent specification of lower and upper errors.

Other optional kwargs:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or aa: [True | False]  or None for default 
  capstyle: ['butt' | 'round' | 'projecting'] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color: matplotlib color spec
  contains: a callable function 
  edgecolor or ec: mpl color spec, None, 'none', or 'auto' 
  facecolor or fc: mpl color spec, or None for default, or 'none' for no color 
  figure: a `~.Figure` instance 
  fill: [True | False] 
  gid: an id string 
  hatch: ['/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*'] 
  joinstyle: ['miter' | 'round' | 'bevel'] 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float or None for default 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  visible: bool 
  zorder: float 


### boxplot
```py

def boxplot(ax, *args, **kwargs)

```



Make a box and whisker plot.

Make a box and whisker plot for each column of ``x`` or each
vector in sequence ``x``.  The box extends from the lower to
upper quartile values of the data, with a line at the median.
The whiskers extend from the box to show the range of the
data.  Flier points are those past the end of the whiskers.

Parameters
----------
x : Array or a sequence of vectors.
    The input data.

notch : bool, optional (False)
    If `True`, will produce a notched box plot. Otherwise, a
    rectangular boxplot is produced. The notches represent the
    confidence interval (CI) around the median. See the entry
    for the ``bootstrap`` parameter for information regarding
    how the locations of the notches are computed.

    .. note::

        In cases where the values of the CI are less than the
        lower quartile or greater than the upper quartile, the
        notches will extend beyond the box, giving it a
        distinctive "flipped" appearance. This is expected
        behavior and consistent with other statistical
        visualization packages.

sym : str, optional
    The default symbol for flier points. Enter an empty string
    ('') if you don't want to show fliers. If `None`, then the
    fliers default to 'b+'  If you want more control use the
    flierprops kwarg.

vert : bool, optional (True)
    If `True` (default), makes the boxes vertical. If `False`,
    everything is drawn horizontally.

whis : float, sequence, or string (default = 1.5)
    As a float, determines the reach of the whiskers to the beyond the
    first and third quartiles. In other words, where IQR is the
    interquartile range (`Q3-Q1`), the upper whisker will extend to
    last datum less than `Q3 + whis*IQR`). Similarly, the lower whisker
    will extend to the first datum greater than `Q1 - whis*IQR`.
    Beyond the whiskers, data
    are considered outliers and are plotted as individual
    points. Set this to an unreasonably high value to force the
    whiskers to show the min and max values. Alternatively, set
    this to an ascending sequence of percentile (e.g., [5, 95])
    to set the whiskers at specific percentiles of the data.
    Finally, ``whis`` can be the string ``'range'`` to force the
    whiskers to the min and max of the data.

bootstrap : int, optional
    Specifies whether to bootstrap the confidence intervals
    around the median for notched boxplots. If ``bootstrap`` is
    None, no bootstrapping is performed, and notches are
    calculated using a Gaussian-based asymptotic approximation
    (see McGill, R., Tukey, J.W., and Larsen, W.A., 1978, and
    Kendall and Stuart, 1967). Otherwise, bootstrap specifies
    the number of times to bootstrap the median to determine its
    95% confidence intervals. Values between 1000 and 10000 are
    recommended.

usermedians : array-like, optional
    An array or sequence whose first dimension (or length) is
    compatible with ``x``. This overrides the medians computed
    by matplotlib for each element of ``usermedians`` that is not
    `None`. When an element of ``usermedians`` is None, the median
    will be computed by matplotlib as normal.

conf_intervals : array-like, optional
    Array or sequence whose first dimension (or length) is
    compatible with ``x`` and whose second dimension is 2. When
    the an element of ``conf_intervals`` is not None, the
    notch locations computed by matplotlib are overridden
    (provided ``notch`` is `True`). When an element of
    ``conf_intervals`` is `None`, the notches are computed by the
    method specified by the other kwargs (e.g., ``bootstrap``).

positions : array-like, optional
    Sets the positions of the boxes. The ticks and limits are
    automatically set to match the positions. Defaults to
    `range(1, N+1)` where N is the number of boxes to be drawn.

widths : scalar or array-like
    Sets the width of each box either with a scalar or a
    sequence. The default is 0.5, or ``0.15*(distance between
    extreme positions)``, if that is smaller.

patch_artist : bool, optional (False)
    If `False` produces boxes with the Line2D artist. Otherwise,
    boxes and drawn with Patch artists.

labels : sequence, optional
    Labels for each dataset. Length must be compatible with
    dimensions  of ``x``.

manage_xticks : bool, optional (True)
    If the function should adjust the xlim and xtick locations.

autorange : bool, optional (False)
    When `True` and the data are distributed such that the  25th and
    75th percentiles are equal, ``whis`` is set to ``'range'`` such
    that the whisker ends are at the minimum and maximum of the
    data.

meanline : bool, optional (False)
    If `True` (and ``showmeans`` is `True`), will try to render
    the mean as a line spanning the full width of the box
    according to ``meanprops`` (see below). Not recommended if
    ``shownotches`` is also True. Otherwise, means will be shown
    as points.

zorder : scalar, optional (None)
    Sets the zorder of the boxplot.

Other Parameters
----------------
showcaps : bool, optional (True)
    Show the caps on the ends of whiskers.
showbox : bool, optional (True)
    Show the central box.
showfliers : bool, optional (True)
    Show the outliers beyond the caps.
showmeans : bool, optional (False)
    Show the arithmetic means.
capprops : dict, optional (None)
    Specifies the style of the caps.
boxprops : dict, optional (None)
    Specifies the style of the box.
whiskerprops : dict, optional (None)
    Specifies the style of the whiskers.
flierprops : dict, optional (None)
    Specifies the style of the fliers.
medianprops : dict, optional (None)
    Specifies the style of the median.
meanprops : dict, optional (None)
    Specifies the style of the mean.

Returns
-------
result : dict
  A dictionary mapping each component of the boxplot to a list
  of the :class:`matplotlib.lines.Line2D` instances
  created. That dictionary has the following keys (assuming
  vertical boxplots):

  - ``boxes``: the main body of the boxplot showing the
    quartiles and the median's confidence intervals if
    enabled.

  - ``medians``: horizontal lines at the median of each box.

  - ``whiskers``: the vertical lines extending to the most
    extreme, non-outlier data points.

  - ``caps``: the horizontal lines at the ends of the
    whiskers.

  - ``fliers``: points representing data that extend beyond
    the whiskers (fliers).

  - ``means``: points or lines representing the means.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### broken\_barh
```py

def broken_barh(ax, *args, **kwargs)

```



Plot horizontal bars.

A collection of horizontal bars spanning *yrange* with a sequence of
*xranges*.

Required arguments:

  =========   ==============================
  Argument    Description
  =========   ==============================
  *xranges*   sequence of (*xmin*, *xwidth*)
  *yrange*    sequence of (*ymin*, *ywidth*)
  =========   ==============================

kwargs are
:class:`matplotlib.collections.BrokenBarHCollection`
properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 

these can either be a single argument, i.e.,::

  facecolors = 'black'

or a sequence of arguments for the various bars, i.e.,::

  facecolors = ('black', 'red', 'green')

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### bxp
```py

def bxp(self, bxpstats, positions=None, widths=None, vert=True, patch_artist=False, shownotches=False, showmeans=False, showcaps=True, showbox=True, showfliers=True, boxprops=None, whiskerprops=None, flierprops=None, medianprops=None, capprops=None, meanprops=None, meanline=False, manage_xticks=True, zorder=None)

```



Drawing function for box and whisker plots.

Make a box and whisker plot for each column of *x* or each
vector in sequence *x*.  The box extends from the lower to
upper quartile values of the data, with a line at the median.
The whiskers extend from the box to show the range of the
data.  Flier points are those past the end of the whiskers.

Parameters
----------

bxpstats : list of dicts
  A list of dictionaries containing stats for each boxplot.
  Required keys are:

  - ``med``: The median (scalar float).

  - ``q1``: The first quartile (25th percentile) (scalar
    float).

  - ``q3``: The third quartile (75th percentile) (scalar
    float).

  - ``whislo``: Lower bound of the lower whisker (scalar
    float).

  - ``whishi``: Upper bound of the upper whisker (scalar
    float).

  Optional keys are:

  - ``mean``: The mean (scalar float). Needed if
    ``showmeans=True``.

  - ``fliers``: Data beyond the whiskers (sequence of floats).
    Needed if ``showfliers=True``.

  - ``cilo`` & ``cihi``: Lower and upper confidence intervals
    about the median. Needed if ``shownotches=True``.

  - ``label``: Name of the dataset (string). If available,
    this will be used a tick label for the boxplot

positions : array-like, default = [1, 2, ..., n]
  Sets the positions of the boxes. The ticks and limits
  are automatically set to match the positions.

widths : array-like, default = None
  Either a scalar or a vector and sets the width of each
  box. The default is ``0.15*(distance between extreme
  positions)``, clipped to no less than 0.15 and no more than
  0.5.

vert : bool, default = False
  If `True` (default), makes the boxes vertical.  If `False`,
  makes horizontal boxes.

patch_artist : bool, default = False
  If `False` produces boxes with the
  `~matplotlib.lines.Line2D` artist.  If `True` produces boxes
  with the `~matplotlib.patches.Patch` artist.

shownotches : bool, default = False
  If `False` (default), produces a rectangular box plot.
  If `True`, will produce a notched box plot

showmeans : bool, default = False
  If `True`, will toggle on the rendering of the means

showcaps  : bool, default = True
  If `True`, will toggle on the rendering of the caps

showbox  : bool, default = True
  If `True`, will toggle on the rendering of the box

showfliers : bool, default = True
  If `True`, will toggle on the rendering of the fliers

boxprops : dict or None (default)
  If provided, will set the plotting style of the boxes

whiskerprops : dict or None (default)
  If provided, will set the plotting style of the whiskers

capprops : dict or None (default)
  If provided, will set the plotting style of the caps

flierprops : dict or None (default)
  If provided will set the plotting style of the fliers

medianprops : dict or None (default)
  If provided, will set the plotting style of the medians

meanprops : dict or None (default)
  If provided, will set the plotting style of the means

meanline : bool, default = False
  If `True` (and *showmeans* is `True`), will try to render the mean
  as a line spanning the full width of the box according to
  *meanprops*. Not recommended if *shownotches* is also True.
  Otherwise, means will be shown as points.

manage_xticks : bool, default = True
  If the function should adjust the xlim and xtick locations.

zorder : scalar,  default = None
  The zorder of the resulting boxplot

Returns
-------
result : dict
  A dictionary mapping each component of the boxplot to a list
  of the :class:`matplotlib.lines.Line2D` instances
  created. That dictionary has the following keys (assuming
  vertical boxplots):

  - ``boxes``: the main body of the boxplot showing the
    quartiles and the median's confidence intervals if
    enabled.

  - ``medians``: horizontal lines at the median of each box.

  - ``whiskers``: the vertical lines extending to the most
    extreme, non-outlier data points.

  - ``caps``: the horizontal lines at the ends of the
    whiskers.

  - ``fliers``: points representing data that extend beyond
    the whiskers (fliers).

  - ``means``: points or lines representing the means.

Examples
--------

.. plot:: gallery/statistics/bxp.py


### can\_pan
```py

def can_pan(self)

```



Return *True* if this axes supports the pan/zoom button functionality.

3D axes objects do not use the pan/zoom button.


### can\_zoom
```py

def can_zoom(self)

```



Return *True* if this axes supports the zoom box button functionality.

3D axes objects do not use the zoom box button.


### cla
```py

def cla(self)

```



Clear axes


### clabel
```py

def clabel(self, *args, **kwargs)

```



This function is currently not implemented for 3D axes.
Returns *None*.


### clear
```py

def clear(self)

```



clear the axes


### cohere
```py

def cohere(ax, *args, **kwargs)

```



Plot the coherence between *x* and *y*.

Plot the coherence between *x* and *y*.  Coherence is the
normalized cross spectral density:

.. math::

  C_{xy} = \frac{|P_{xy}|^2}{P_{xx}P_{yy}}

Parameters
----------
Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  This can be different from *NFFT*, which
    specifies the number of data points used.  While not increasing
    the actual resolution of the spectrum (the minimum distance between
    resolvable peaks), this can give more points in the plot,
    allowing for more detail. This corresponds to the *n* parameter
    in the call to fft(). The default is None, which sets *pad_to*
    equal to *NFFT*

NFFT : integer
    The number of data points used in each block for the FFT.
    A power 2 is most efficient.  The default value is 256.
    This should *NOT* be used to get zero padding, or the scaling of the
    result will be incorrect. Use *pad_to* for this instead.

detrend : {'default', 'constant', 'mean', 'linear', 'none'} or callable
    The function applied to each segment before fft-ing,
    designed to remove the mean or linear trend.  Unlike in
    MATLAB, where the *detrend* parameter is a vector, in
    matplotlib is it a function.  The :mod:`~matplotlib.pylab`
    module defines :func:`~matplotlib.pylab.detrend_none`,
    :func:`~matplotlib.pylab.detrend_mean`, and
    :func:`~matplotlib.pylab.detrend_linear`, but you can use
    a custom function as well.  You can also use a string to choose
    one of the functions.  'default', 'constant', and 'mean' call
    :func:`~matplotlib.pylab.detrend_mean`.  'linear' calls
    :func:`~matplotlib.pylab.detrend_linear`.  'none' calls
    :func:`~matplotlib.pylab.detrend_none`.

scale_by_freq : boolean, optional
    Specifies whether the resulting density values should be scaled
    by the scaling frequency, which gives density in units of Hz^-1.
    This allows for integration over the returned frequency values.
    The default is True for MATLAB compatibility.

noverlap : integer
    The number of points of overlap between blocks.  The
    default value is 0 (no overlap).

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.


Returns
-------
The return value is a tuple (*Cxy*, *f*), where *f* are the
frequencies of the coherence vector.

kwargs are applied to the lines.

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

References
----------
Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
John Wiley & Sons (1986)

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### contains
```py

def contains(self, mouseevent)

```



Test whether the mouse event occurred in the axes.

Returns *True* / *False*, {}


### contains\_point
```py

def contains_point(self, point)

```



Returns *True* if the point (tuple of x,y) is inside the axes
(the area defined by the its patch). A pixel coordinate is
required.


### contour
```py

def contour(self, X, Y, Z, *args, **kwargs)

```



Create a 3D contour plot.

==========  ================================================
Argument    Description
==========  ================================================
*X*, *Y*,   Data values as numpy.arrays
*Z*
*extend3d*  Whether to extend contour in 3D (default: False)
*stride*    Stride (step size) for extending contour
*zdir*      The direction to use: x, y or z (default)
*offset*    If specified plot a projection of the contour
            lines on this position in plane normal to zdir
==========  ================================================

The positional and other keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.contour`

Returns a :class:`~matplotlib.axes.Axes.contour`


### contour3D
```py

def contour3D(self, X, Y, Z, *args, **kwargs)

```



Create a 3D contour plot.

==========  ================================================
Argument    Description
==========  ================================================
*X*, *Y*,   Data values as numpy.arrays
*Z*
*extend3d*  Whether to extend contour in 3D (default: False)
*stride*    Stride (step size) for extending contour
*zdir*      The direction to use: x, y or z (default)
*offset*    If specified plot a projection of the contour
            lines on this position in plane normal to zdir
==========  ================================================

The positional and other keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.contour`

Returns a :class:`~matplotlib.axes.Axes.contour`


### contourf
```py

def contourf(self, X, Y, Z, *args, **kwargs)

```



Create a 3D contourf plot.

==========  ================================================
Argument    Description
==========  ================================================
*X*, *Y*,   Data values as numpy.arrays
*Z*
*zdir*      The direction to use: x, y or z (default)
*offset*    If specified plot a projection of the filled contour
            on this position in plane normal to zdir
==========  ================================================

The positional and keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.contourf`

Returns a :class:`~matplotlib.axes.Axes.contourf`

.. versionchanged :: 1.1.0
    The *zdir* and *offset* kwargs were added.


### contourf3D
```py

def contourf3D(self, X, Y, Z, *args, **kwargs)

```



Create a 3D contourf plot.

==========  ================================================
Argument    Description
==========  ================================================
*X*, *Y*,   Data values as numpy.arrays
*Z*
*zdir*      The direction to use: x, y or z (default)
*offset*    If specified plot a projection of the filled contour
            on this position in plane normal to zdir
==========  ================================================

The positional and keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.contourf`

Returns a :class:`~matplotlib.axes.Axes.contourf`

.. versionchanged :: 1.1.0
    The *zdir* and *offset* kwargs were added.


### convert\_xunits
```py

def convert_xunits(self, x)

```



For artists in an axes, if the xaxis has units support,
convert *x* using xaxis unit type


### convert\_yunits
```py

def convert_yunits(self, y)

```



For artists in an axes, if the yaxis has units support,
convert *y* using yaxis unit type


### convert\_zunits
```py

def convert_zunits(self, z)

```



For artists in an axes, if the zaxis has units support,
convert *z* using zaxis unit type

.. versionadded :: 1.2.1


### csd
```py

def csd(ax, *args, **kwargs)

```



Plot the cross-spectral density.

Call signature::

  csd(x, y, NFFT=256, Fs=2, Fc=0, detrend=mlab.detrend_none,
      window=mlab.window_hanning, noverlap=0, pad_to=None,
      sides='default', scale_by_freq=None, return_line=None, **kwargs)

The cross spectral density :math:`P_{xy}` by Welch's average
periodogram method.  The vectors *x* and *y* are divided into
*NFFT* length segments.  Each segment is detrended by function
*detrend* and windowed by function *window*.  *noverlap* gives
the length of the overlap between segments.  The product of
the direct FFTs of *x* and *y* are averaged over each segment
to compute :math:`P_{xy}`, with a scaling to correct for power
loss due to windowing.

If len(*x*) < *NFFT* or len(*y*) < *NFFT*, they will be zero
padded to *NFFT*.

Parameters
----------
x, y : 1-D arrays or sequences
    Arrays or sequences containing the data

Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  This can be different from *NFFT*, which
    specifies the number of data points used.  While not increasing
    the actual resolution of the spectrum (the minimum distance between
    resolvable peaks), this can give more points in the plot,
    allowing for more detail. This corresponds to the *n* parameter
    in the call to fft(). The default is None, which sets *pad_to*
    equal to *NFFT*

NFFT : integer
    The number of data points used in each block for the FFT.
    A power 2 is most efficient.  The default value is 256.
    This should *NOT* be used to get zero padding, or the scaling of the
    result will be incorrect. Use *pad_to* for this instead.

detrend : {'default', 'constant', 'mean', 'linear', 'none'} or callable
    The function applied to each segment before fft-ing,
    designed to remove the mean or linear trend.  Unlike in
    MATLAB, where the *detrend* parameter is a vector, in
    matplotlib is it a function.  The :mod:`~matplotlib.pylab`
    module defines :func:`~matplotlib.pylab.detrend_none`,
    :func:`~matplotlib.pylab.detrend_mean`, and
    :func:`~matplotlib.pylab.detrend_linear`, but you can use
    a custom function as well.  You can also use a string to choose
    one of the functions.  'default', 'constant', and 'mean' call
    :func:`~matplotlib.pylab.detrend_mean`.  'linear' calls
    :func:`~matplotlib.pylab.detrend_linear`.  'none' calls
    :func:`~matplotlib.pylab.detrend_none`.

scale_by_freq : boolean, optional
    Specifies whether the resulting density values should be scaled
    by the scaling frequency, which gives density in units of Hz^-1.
    This allows for integration over the returned frequency values.
    The default is True for MATLAB compatibility.

noverlap : integer
    The number of points of overlap between segments.
    The default value is 0 (no overlap).

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.

return_line : bool
    Whether to include the line object plotted in the returned values.
    Default is False.

Returns
-------
Pxy : 1-D array
    The values for the cross spectrum `P_{xy}` before scaling
    (complex valued)

freqs : 1-D array
    The frequencies corresponding to the elements in *Pxy*

line : a :class:`~matplotlib.lines.Line2D` instance
    The line created by this function.
    Only returned if *return_line* is True.

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

Notes
-----
For plotting, the power is plotted as
:math:`10\log_{10}(P_{xy})` for decibels, though `P_{xy}` itself
is returned.

References
----------
Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
John Wiley & Sons (1986)

See Also
--------
:func:`psd`
    :func:`psd` is the equivalent to setting y=x.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### disable\_mouse\_rotation
```py

def disable_mouse_rotation(self)

```



Disable mouse button callbacks.
        


### drag\_pan
```py

def drag_pan(self, button, key, x, y)

```



Called when the mouse moves during a pan operation.

*button* is the mouse button number:

* 1: LEFT
* 2: MIDDLE
* 3: RIGHT

*key* is a "shift" key

*x*, *y* are the mouse coordinates in display coords.

.. note::

    Intended to be overridden by new projection types.


### draw
```py

def draw(self, renderer)

```



### draw\_artist
```py

def draw_artist(self, a)

```



This method can only be used after an initial draw which
caches the renderer.  It is used to efficiently update Axes
data (axis ticks, labels, etc are not updated)


### end\_pan
```py

def end_pan(self)

```



Called when a pan operation completes (when the mouse button
is up.)

.. note::

    Intended to be overridden by new projection types.


### errorbar
```py

def errorbar(ax, *args, **kwargs)

```



Plot an errorbar graph.

Plot x versus y with error deltas in yerr and xerr.
Vertical errorbars are plotted if yerr is not None.
Horizontal errorbars are plotted if xerr is not None.

x, y, xerr, and yerr can all be scalars, which plots a
single error bar at x, y.

Parameters
----------
x : scalar or array-like
y : scalar or array-like

xerr/yerr : scalar or array-like, shape(N,) or shape(2,N), optional
    If a scalar number, len(N) array-like object, or a N-element
    array-like object, errorbars are drawn at +/-value relative
    to the data. Default is None.

    If a sequence of shape 2xN, errorbars are drawn at -row1
    and +row2 relative to the data.

fmt : plot format string, optional, default: None
    The plot format symbol. If fmt is 'none' (case-insensitive),
    only the errorbars are plotted.  This is used for adding
    errorbars to a bar plot, for example.  Default is '',
    an empty plot format string; properties are
    then identical to the defaults for :meth:`plot`.

ecolor : mpl color, optional, default: None
    A matplotlib color arg which gives the color the errorbar lines;
    if None, use the color of the line connecting the markers.

elinewidth : scalar, optional, default: None
    The linewidth of the errorbar lines. If None, use the linewidth.

capsize : scalar, optional, default: None
    The length of the error bar caps in points; if None, it will
    take the value from ``errorbar.capsize``
    :data:`rcParam<matplotlib.rcParams>`.

capthick : scalar, optional, default: None
    An alias kwarg to markeredgewidth (a.k.a. - mew). This
    setting is a more sensible name for the property that
    controls the thickness of the error bar cap in points. For
    backwards compatibility, if mew or markeredgewidth are given,
    then they will over-ride capthick. This may change in future
    releases.

barsabove : bool, optional, default: False
    if True , will plot the errorbars above the plot
    symbols. Default is below.

lolims / uplims / xlolims / xuplims : bool, optional, default:None
    These arguments can be used to indicate that a value gives
    only upper/lower limits. In that case a caret symbol is
    used to indicate this. lims-arguments may be of the same
    type as *xerr* and *yerr*.  To use limits with inverted
    axes, :meth:`set_xlim` or :meth:`set_ylim` must be called
    before :meth:`errorbar`.

errorevery : positive integer, optional, default:1
    subsamples the errorbars. e.g., if errorevery=5, errorbars for
    every 5-th datapoint will be plotted. The data plot itself still
    shows all data points.

Returns
-------
plotline : :class:`~matplotlib.lines.Line2D` instance
    x, y plot markers and/or line
caplines : list of :class:`~matplotlib.lines.Line2D` instances
    error bar cap
barlinecols : list of :class:`~matplotlib.collections.LineCollection`
    horizontal and vertical error ranges.

Other Parameters
----------------
**kwargs :
    All other keyword arguments are passed on to the plot
    command for the markers. For example, this code makes big red
    squares with thick green edges::

        x,y,yerr = rand(3,10)
        errorbar(x, y, yerr, marker='s', mfc='red',
                 mec='green', ms=20, mew=4)

    where mfc, mec, ms and mew are aliases for the longer
    property names, markerfacecolor, markeredgecolor, markersize
    and markeredgewidth.

    Valid kwargs for the marker properties are

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'xerr', 'y', 'yerr'.


### eventplot
```py

def eventplot(ax, *args, **kwargs)

```



Plot identical parallel lines at the given positions.

*positions* should be a 1D or 2D array-like object, with each row
corresponding to a row or column of lines.

This type of plot is commonly used in neuroscience for representing
neural events, where it is usually called a spike raster, dot raster,
or raster plot.

However, it is useful in any situation where you wish to show the
timing or position of multiple sets of discrete events, such as the
arrival times of people to a business on each day of the month or the
date of hurricanes each year of the last century.

Parameters
----------
positions : 1D or 2D array-like object
    Each value is an event. If *positions* is a 2D array-like, each
    row corresponds to a row or a column of lines (depending on the
    *orientation* parameter).

orientation : {'horizontal', 'vertical'}, optional
    Controls the direction of the event collections:

        - 'horizontal' : the lines are arranged horizontally in rows,
          and are vertical.
        - 'vertical' : the lines are arranged vertically in columns,
          and are horizontal.

lineoffsets : scalar or sequence of scalars, optional, default: 1
    The offset of the center of the lines from the origin, in the
    direction orthogonal to *orientation*.

linelengths : scalar or sequence of scalars, optional, default: 1
    The total height of the lines (i.e. the lines stretches from
    ``lineoffset - linelength/2`` to ``lineoffset + linelength/2``).

linewidths : scalar, scalar sequence or None, optional, default: None
    The line width(s) of the event lines, in points. If it is None,
    defaults to its rcParams setting.

colors : color, sequence of colors or None, optional, default: None
    The color(s) of the event lines. If it is None, defaults to its
    rcParams setting.

linestyles : str or tuple or a sequence of such values, optional
    Default is 'solid'. Valid strings are ['solid', 'dashed',
    'dashdot', 'dotted', '-', '--', '-.', ':']. Dash tuples
    should be of the form::

        (offset, onoffseq),

    where *onoffseq* is an even length tuple of on and off ink
    in points.

**kwargs : optional
    Other keyword arguments are line collection properties.  See
    :class:`~matplotlib.collections.LineCollection` for a list of
    the valid properties.

Returns
-------

A list of :class:`matplotlib.collections.EventCollection` objects that
were added.

Notes
-----

For *linelengths*, *linewidths*, *colors*, and *linestyles*, if only
a single value is given, that value is applied to all lines.  If an
array-like is given, it must have the same length as *positions*, and
each value will be applied to the corresponding row of the array.

Examples
--------

.. plot:: mpl_examples/lines_bars_and_markers/eventplot_demo.py

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'colors', 'linelengths', 'lineoffsets', 'linestyles', 'linewidths', 'positions'.


### fill
```py

def fill(ax, *args, **kwargs)

```



Plot filled polygons.

Parameters
----------
args : a variable length argument
    It allowing for multiple
    *x*, *y* pairs with an optional color format string; see
    :func:`~matplotlib.pyplot.plot` for details on the argument
    parsing.  For example, each of the following is legal::

        ax.fill(x, y)
        ax.fill(x, y, "b")
        ax.fill(x, y, "b", x, y, "r")

    An arbitrary number of *x*, *y*, *color* groups can be specified::
    ax.fill(x1, y1, 'g', x2, y2, 'r')

Returns
-------
a list of :class:`~matplotlib.patches.Patch`

Other Parameters
----------------
**kwargs : :class:`~matplotlib.patches.Polygon` properties

Notes
-----
The same color strings that :func:`~matplotlib.pyplot.plot`
supports are supported by the fill format string.

If you would like to fill below a curve, e.g., shade a region
between 0 and *y* along *x*, use :meth:`fill_between`

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### fill\_between
```py

def fill_between(ax, *args, **kwargs)

```



Make filled polygons between two curves.


Create a :class:`~matplotlib.collections.PolyCollection`
filling the regions between *y1* and *y2* where
``where==True``

Parameters
----------
x : array
    An N-length array of the x data

y1 : array
    An N-length array (or scalar) of the y data

y2 : array
    An N-length array (or scalar) of the y data

where : array, optional
    If `None`, default to fill between everywhere.  If not `None`,
    it is an N-length numpy boolean array and the fill will
    only happen over the regions where ``where==True``.

interpolate : bool, optional
    If `True`, interpolate between the two lines to find the
    precise point of intersection.  Otherwise, the start and
    end points of the filled region will only occur on explicit
    values in the *x* array.

step : {'pre', 'post', 'mid'}, optional
    If not None, fill with step logic.


Notes
-----

Additional Keyword args passed on to the
:class:`~matplotlib.collections.PolyCollection`.

kwargs control the :class:`~matplotlib.patches.Polygon` properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 

See Also
--------

    :meth:`fill_betweenx`
        for filling between two sets of x-values

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'where', 'x', 'y1', 'y2'.


### fill\_betweenx
```py

def fill_betweenx(ax, *args, **kwargs)

```



Make filled polygons between two horizontal curves.


Create a :class:`~matplotlib.collections.PolyCollection`
filling the regions between *x1* and *x2* where
``where==True``

Parameters
----------
y : array
    An N-length array of the y data

x1 : array
    An N-length array (or scalar) of the x data

x2 : array, optional
    An N-length array (or scalar) of the x data

where : array, optional
    If *None*, default to fill between everywhere.  If not *None*,
    it is a N length numpy boolean array and the fill will
    only happen over the regions where ``where==True``

step : {'pre', 'post', 'mid'}, optional
    If not None, fill with step logic.

interpolate : bool, optional
    If `True`, interpolate between the two lines to find the
    precise point of intersection.  Otherwise, the start and
    end points of the filled region will only occur on explicit
    values in the *x* array.

Notes
-----

keyword args passed on to the
    :class:`~matplotlib.collections.PolyCollection`

kwargs control the :class:`~matplotlib.patches.Polygon` properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 

See Also
--------

    :meth:`fill_between`
        for filling between two sets of y-values

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'where', 'x1', 'x2', 'y'.


### findobj
```py

def findobj(self, match=None, include_self=True)

```



Find artist objects.

Recursively find all :class:`~matplotlib.artist.Artist` instances
contained in self.

*match* can be

  - None: return all objects contained in artist.

  - function with signature ``boolean = match(artist)``
    used to filter matches

  - class instance: e.g., Line2D.  Only return artists of class type.

If *include_self* is True (default), include self in the list to be
checked for a match.


### format\_coord
```py

def format_coord(self, xd, yd)

```



Given the 2D view coordinates attempt to guess a 3D coordinate.
Looks for the nearest edge to the point and then assumes that
the point is at the same z location as the nearest point on the edge.


### format\_cursor\_data
```py

def format_cursor_data(self, data)

```



Return *cursor data* string formatted.


### format\_xdata
```py

def format_xdata(self, x)

```



Return *x* string formatted.  This function will use the attribute
self.fmt_xdata if it is callable, else will fall back on the xaxis
major formatter


### format\_ydata
```py

def format_ydata(self, y)

```



Return y string formatted.  This function will use the
:attr:`fmt_ydata` attribute if it is callable, else will fall
back on the yaxis major formatter


### format\_zdata
```py

def format_zdata(self, z)

```



Return *z* string formatted.  This function will use the
:attr:`fmt_zdata` attribute if it is callable, else will fall
back on the zaxis major formatter


### get\_adjustable
```py

def get_adjustable(self)

```



### get\_agg\_filter
```py

def get_agg_filter(self)

```



Return filter function to be used for agg filter.


### get\_alpha
```py

def get_alpha(self)

```



Return the alpha value used for blending - not supported on all
backends


### get\_anchor
```py

def get_anchor(self)

```



### get\_animated
```py

def get_animated(self)

```



Return the artist's animated state


### get\_aspect
```py

def get_aspect(self)

```



### get\_autoscale\_on
```py

def get_autoscale_on(self)

```



Get whether autoscaling is applied for all axes on plot commands

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### get\_autoscalex\_on
```py

def get_autoscalex_on(self)

```



Get whether autoscaling for the x-axis is applied on plot commands


### get\_autoscaley\_on
```py

def get_autoscaley_on(self)

```



Get whether autoscaling for the y-axis is applied on plot commands


### get\_autoscalez\_on
```py

def get_autoscalez_on(self)

```



Get whether autoscaling for the z-axis is applied on plot commands

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### get\_axes\_locator
```py

def get_axes_locator(self)

```



return axes_locator


### get\_axis\_bgcolor
```py

def get_axis_bgcolor(*args, **kwargs)

```



.. deprecated:: 2.0
    The get_axis_bgcolor function was deprecated in version 2.0. Use get_facecolor instead.

Return the axis background color


### get\_axis\_position
```py

def get_axis_position(self)

```



### get\_axisbelow
```py

def get_axisbelow(self)

```



Get whether axis below is true or not.

For axes3d objects, this will always be *True*

.. versionadded :: 1.1.0
    This function was added for completeness.


### get\_children
```py

def get_children(self)

```



### get\_clip\_box
```py

def get_clip_box(self)

```



Return artist clipbox


### get\_clip\_on
```py

def get_clip_on(self)

```



Return whether artist uses clipping


### get\_clip\_path
```py

def get_clip_path(self)

```



Return artist clip path


### get\_contains
```py

def get_contains(self)

```



Return the _contains test used by the artist, or *None* for default.


### get\_cursor\_data
```py

def get_cursor_data(self, event)

```



Get the cursor data for a given event.


### get\_cursor\_props
```py

def get_cursor_props(*args, **kwargs)

```



.. deprecated:: 2.1
    The get_cursor_props function was deprecated in version 2.1.

Return the cursor propertiess as a (*linewidth*, *color*)
tuple, where *linewidth* is a float and *color* is an RGBA
tuple


### get\_data\_ratio
```py

def get_data_ratio(self)

```



Returns the aspect ratio of the raw data.

This method is intended to be overridden by new projection
types.


### get\_data\_ratio\_log
```py

def get_data_ratio_log(self)

```



Returns the aspect ratio of the raw data in log scale.
Will be used when both axis scales are in log.


### get\_default\_bbox\_extra\_artists
```py

def get_default_bbox_extra_artists(self)

```



### get\_facecolor
```py

def get_facecolor(self)

```



### get\_fc
```py

def get_fc(self)

```



### get\_figure
```py

def get_figure(self)

```



Return the `~.Figure` instance the artist belongs to.


### get\_frame\_on
```py

def get_frame_on(self)

```



Get whether the 3D axes panels are drawn

.. versionadded :: 1.1.0


### get\_gid
```py

def get_gid(self)

```



Returns the group id.


### get\_images
```py

def get_images(self)

```



return a list of Axes images contained by the Axes


### get\_label
```py

def get_label(self)

```



Get the label used for this artist in the legend.


### get\_legend
```py

def get_legend(self)

```



Return the `Legend` instance, or None if no legend is defined.


### get\_legend\_handles\_labels
```py

def get_legend_handles_labels(self, legend_handler_map=None)

```



Return handles and labels for legend

``ax.legend()`` is equivalent to ::

  h, l = ax.get_legend_handles_labels()
  ax.legend(h, l)


### get\_lines
```py

def get_lines(self)

```



Return a list of lines contained by the Axes


### get\_navigate
```py

def get_navigate(self)

```



Get whether the axes responds to navigation commands


### get\_navigate\_mode
```py

def get_navigate_mode(self)

```



Get the navigation toolbar button status: 'PAN', 'ZOOM', or None


### get\_path\_effects
```py

def get_path_effects(self)

```



### get\_picker
```py

def get_picker(self)

```



Return the picker object used by this artist.


### get\_position
```py

def get_position(self, original=False)

```



Return the a copy of the axes rectangle as a Bbox


### get\_proj
```py

def get_proj(self)

```



Create the projection matrix from the current viewing position.

elev stores the elevation angle in the z plane
azim stores the azimuth angle in the x,y plane

dist is the distance of the eye viewing point from the object
point.


### get\_rasterization\_zorder
```py

def get_rasterization_zorder(self)

```



Return the zorder value below which artists will be rasterized.


### get\_rasterized
```py

def get_rasterized(self)

```



Return whether the artist is to be rasterized.


### get\_renderer\_cache
```py

def get_renderer_cache(self)

```



### get\_shared\_x\_axes
```py

def get_shared_x_axes(self)

```



Return a copy of the shared axes Grouper object for x axes


### get\_shared\_y\_axes
```py

def get_shared_y_axes(self)

```



Return a copy of the shared axes Grouper object for y axes


### get\_sketch\_params
```py

def get_sketch_params(self)

```



Returns the sketch parameters for the artist.

Returns
-------
sketch_params : tuple or `None`

A 3-tuple with the following elements:

  * `scale`: The amplitude of the wiggle perpendicular to the
    source line.

  * `length`: The length of the wiggle along the line.

  * `randomness`: The scale factor by which the length is
    shrunken or expanded.

May return `None` if no sketch parameters were set.


### get\_snap
```py

def get_snap(self)

```



Returns the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.


### get\_tightbbox
```py

def get_tightbbox(self, renderer, call_axes_locator=True)

```



Return the tight bounding box of the axes.
The dimension of the Bbox in canvas coordinate.

If *call_axes_locator* is *False*, it does not call the
_axes_locator attribute, which is necessary to get the correct
bounding box. ``call_axes_locator==False`` can be used if the
caller is only intereted in the relative size of the tightbbox
compared to the axes bbox.


### get\_title
```py

def get_title(self, loc=u'center')

```



Get an axes title.

Get one of the three available axes titles. The available titles
are positioned above the axes in the center, flush with the left
edge, and flush with the right edge.

Parameters
----------
loc : {'center', 'left', 'right'}, str, optional
    Which title to get, defaults to 'center'

Returns
-------
title: str
    The title text string.


### get\_transform
```py

def get_transform(self)

```



Return the :class:`~matplotlib.transforms.Transform`
instance used by this artist.


### get\_transformed\_clip\_path\_and\_affine
```py

def get_transformed_clip_path_and_affine(self)

```



Return the clip path with the non-affine part of its
transformation applied, and the remaining affine part of its
transformation.


### get\_url
```py

def get_url(self)

```



Returns the url.


### get\_visible
```py

def get_visible(self)

```



Return the artist's visiblity


### get\_w\_lims
```py

def get_w_lims(self)

```



Get 3D world limits.


### get\_window\_extent
```py

def get_window_extent(self, *args, **kwargs)

```



get the axes bounding box in display space; *args* and
*kwargs* are empty


### get\_xaxis
```py

def get_xaxis(self)

```



Return the XAxis instance.


### get\_xaxis\_text1\_transform
```py

def get_xaxis_text1_transform(self, pad_points)

```



Get the transformation used for drawing x-axis labels, which
will add the given amount of padding (in points) between the
axes and the label.  The x-direction is in data coordinates
and the y-direction is in axis coordinates.  Returns a
3-tuple of the form::

  (transform, valign, halign)

where *valign* and *halign* are requested alignments for the
text.

.. note::

    This transformation is primarily used by the
    :class:`~matplotlib.axis.Axis` class, and is meant to be
    overridden by new kinds of projections that may need to
    place axis elements in different locations.


### get\_xaxis\_text2\_transform
```py

def get_xaxis_text2_transform(self, pad_points)

```



Get the transformation used for drawing the secondary x-axis
labels, which will add the given amount of padding (in points)
between the axes and the label.  The x-direction is in data
coordinates and the y-direction is in axis coordinates.
Returns a 3-tuple of the form::

  (transform, valign, halign)

where *valign* and *halign* are requested alignments for the
text.

.. note::

    This transformation is primarily used by the
    :class:`~matplotlib.axis.Axis` class, and is meant to be
    overridden by new kinds of projections that may need to
    place axis elements in different locations.


### get\_xaxis\_transform
```py

def get_xaxis_transform(self, which=u'grid')

```



Get the transformation used for drawing x-axis labels, ticks
and gridlines.  The x-direction is in data coordinates and the
y-direction is in axis coordinates.

.. note::

    This transformation is primarily used by the
    :class:`~matplotlib.axis.Axis` class, and is meant to be
    overridden by new kinds of projections that may need to
    place axis elements in different locations.


### get\_xbound
```py

def get_xbound(self)

```



Return the lower and upper x-axis bounds, in increasing order.


### get\_xgridlines
```py

def get_xgridlines(self)

```



Get the x grid lines as a list of `Line2D` instances.


### get\_xlabel
```py

def get_xlabel(self)

```



Get the xlabel text string.


### get\_xlim
```py

def get_xlim(self)

```



Get the x-axis range

Returns
-------
xlimits : tuple
    Returns the current x-axis limits as the tuple
    (`left`, `right`).

Notes
-----
The x-axis may be inverted, in which case the `left` value will
be greater than the `right` value.


    .. versionchanged :: 1.1.0
        This function now correctly refers to the 3D x-limits
    


### get\_xlim3d
```py

def get_xlim3d(self)

```



Get the x-axis range

Returns
-------
xlimits : tuple
    Returns the current x-axis limits as the tuple
    (`left`, `right`).

Notes
-----
The x-axis may be inverted, in which case the `left` value will
be greater than the `right` value.


    .. versionchanged :: 1.1.0
        This function now correctly refers to the 3D x-limits
    


### get\_xmajorticklabels
```py

def get_xmajorticklabels(self)

```



Get the major x tick labels.

Returns
-------
labels : list
    List of :class:`~matplotlib.text.Text` instances


### get\_xminorticklabels
```py

def get_xminorticklabels(self)

```



Get the minor x tick labels.

Returns
-------
labels : list
    List of :class:`~matplotlib.text.Text` instances


### get\_xscale
```py

def get_xscale(self)

```



Return the xaxis scale string: linear, log, logit, symlog


### get\_xticklabels
```py

def get_xticklabels(self, minor=False, which=None)

```



Get the x tick labels as a list of :class:`~matplotlib.text.Text`
instances.

Parameters
----------
minor : bool, optional
   If True return the minor ticklabels,
   else return the major ticklabels.

which : None, ('minor', 'major', 'both')
   Overrides `minor`.

   Selects which ticklabels to return

Returns
-------
ret : list
   List of :class:`~matplotlib.text.Text` instances.


### get\_xticklines
```py

def get_xticklines(self)

```



Get the x tick lines as a list of `Line2D` instances.


### get\_xticks
```py

def get_xticks(self, minor=False)

```



Return the x ticks as a list of locations


### get\_yaxis
```py

def get_yaxis(self)

```



Return the YAxis instance.


### get\_yaxis\_text1\_transform
```py

def get_yaxis_text1_transform(self, pad_points)

```



Get the transformation used for drawing y-axis labels, which
will add the given amount of padding (in points) between the
axes and the label.  The x-direction is in axis coordinates
and the y-direction is in data coordinates.  Returns a 3-tuple
of the form::

  (transform, valign, halign)

where *valign* and *halign* are requested alignments for the
text.

.. note::

    This transformation is primarily used by the
    :class:`~matplotlib.axis.Axis` class, and is meant to be
    overridden by new kinds of projections that may need to
    place axis elements in different locations.


### get\_yaxis\_text2\_transform
```py

def get_yaxis_text2_transform(self, pad_points)

```



Get the transformation used for drawing the secondary y-axis
labels, which will add the given amount of padding (in points)
between the axes and the label.  The x-direction is in axis
coordinates and the y-direction is in data coordinates.
Returns a 3-tuple of the form::

  (transform, valign, halign)

where *valign* and *halign* are requested alignments for the
text.

.. note::

    This transformation is primarily used by the
    :class:`~matplotlib.axis.Axis` class, and is meant to be
    overridden by new kinds of projections that may need to
    place axis elements in different locations.


### get\_yaxis\_transform
```py

def get_yaxis_transform(self, which=u'grid')

```



Get the transformation used for drawing y-axis labels, ticks
and gridlines.  The x-direction is in axis coordinates and the
y-direction is in data coordinates.

.. note::

    This transformation is primarily used by the
    :class:`~matplotlib.axis.Axis` class, and is meant to be
    overridden by new kinds of projections that may need to
    place axis elements in different locations.


### get\_ybound
```py

def get_ybound(self)

```



Return the lower and upper y-axis bounds, in increasing order.


### get\_ygridlines
```py

def get_ygridlines(self)

```



Get the y grid lines as a list of `Line2D` instances.


### get\_ylabel
```py

def get_ylabel(self)

```



Get the ylabel text string.


### get\_ylim
```py

def get_ylim(self)

```



Get the y-axis range

Returns
-------
ylimits : tuple
    Returns the current y-axis limits as the tuple
    (`bottom`, `top`).

Notes
-----
The y-axis may be inverted, in which case the `bottom` value
will be greater than the `top` value.


    .. versionchanged :: 1.1.0
        This function now correctly refers to the 3D y-limits.
    


### get\_ylim3d
```py

def get_ylim3d(self)

```



Get the y-axis range

Returns
-------
ylimits : tuple
    Returns the current y-axis limits as the tuple
    (`bottom`, `top`).

Notes
-----
The y-axis may be inverted, in which case the `bottom` value
will be greater than the `top` value.


    .. versionchanged :: 1.1.0
        This function now correctly refers to the 3D y-limits.
    


### get\_ymajorticklabels
```py

def get_ymajorticklabels(self)

```



Get the major y tick labels.

Returns
-------
labels : list
    List of :class:`~matplotlib.text.Text` instances


### get\_yminorticklabels
```py

def get_yminorticklabels(self)

```



Get the minor y tick labels.

Returns
-------
labels : list
    List of :class:`~matplotlib.text.Text` instances


### get\_yscale
```py

def get_yscale(self)

```



Return the yaxis scale string: linear, log, logit, symlog


### get\_yticklabels
```py

def get_yticklabels(self, minor=False, which=None)

```



Get the x tick labels as a list of :class:`~matplotlib.text.Text`
instances.

Parameters
----------
minor : bool
   If True return the minor ticklabels,
   else return the major ticklabels

which : None, ('minor', 'major', 'both')
   Overrides `minor`.

   Selects which ticklabels to return

Returns
-------
ret : list
   List of :class:`~matplotlib.text.Text` instances.


### get\_yticklines
```py

def get_yticklines(self)

```



Get the y tick lines as a list of `Line2D` instances.


### get\_yticks
```py

def get_yticks(self, minor=False)

```



Return the y ticks as a list of locations


### get\_zbound
```py

def get_zbound(self)

```



Returns the z-axis numerical bounds where::

  lowerBound < upperBound

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### get\_zlabel
```py

def get_zlabel(self)

```



Get the z-label text string.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### get\_zlim
```py

def get_zlim(self)

```



Get 3D z limits.


### get\_zlim3d
```py

def get_zlim3d(self)

```



Get 3D z limits.


### get\_zmajorticklabels
```py

def get_zmajorticklabels(self)

```



Get the ztick labels as a list of Text instances

.. versionadded :: 1.1.0


### get\_zminorticklabels
```py

def get_zminorticklabels(self)

```



Get the ztick labels as a list of Text instances

.. note::
    Minor ticks are not supported. This function was added
    only for completeness.

.. versionadded :: 1.1.0


### get\_zorder
```py

def get_zorder(self)

```



Return the artist's zorder.


### get\_zscale
```py

def get_zscale(self)

```



### get\_zticklabels
```py

def get_zticklabels(self, minor=False)

```



Get ztick labels as a list of Text instances.
See :meth:`matplotlib.axes.Axes.get_yticklabels` for more details.

.. note::
    Minor ticks are not supported.

.. versionadded:: 1.1.0


### get\_zticklines
```py

def get_zticklines(self)

```



Get ztick lines as a list of Line2D instances.
Note that this function is provided merely for completeness.
These lines are re-calculated as the display changes.

.. versionadded:: 1.1.0


### get\_zticks
```py

def get_zticks(self, minor=False)

```



Return the z ticks as a list of locations
See :meth:`matplotlib.axes.Axes.get_yticks` for more details.

.. note::
    Minor ticks are not supported.

.. versionadded:: 1.1.0


### grid
```py

def grid(self, b=True, **kwargs)

```



Set / unset 3D grid.

.. note::

    Currently, this function does not behave the same as
    :meth:`matplotlib.axes.Axes.grid`, but it is intended to
    eventually support that behavior.

.. versionchanged :: 1.1.0
    This function was changed, but not tested. Please report any bugs.


### has\_data
```py

def has_data(self)

```



Return *True* if any artists have been added to axes.

This should not be used to determine whether the *dataLim*
need to be updated, and may not actually be useful for
anything.


### have\_units
```py

def have_units(self)

```



Return *True* if units are set on the *x*, *y*, or *z* axes


### hexbin
```py

def hexbin(ax, *args, **kwargs)

```



Make a hexagonal binning plot.

Make a hexagonal binning plot of *x* versus *y*, where *x*,
*y* are 1-D sequences of the same length, *N*. If *C* is *None*
(the default), this is a histogram of the number of occurrences
of the observations at (x[i],y[i]).

If *C* is specified, it specifies values at the coordinate
(x[i],y[i]). These values are accumulated for each hexagonal
bin and then reduced according to *reduce_C_function*, which
defaults to numpy's mean function (np.mean). (If *C* is
specified, it must also be a 1-D sequence of the same length
as *x* and *y*.)

Parameters
----------
x, y : array or masked array

C : array or masked array, optional, default is *None*

gridsize : int or (int, int), optional, default is 100
    The number of hexagons in the *x*-direction, default is
    100. The corresponding number of hexagons in the
    *y*-direction is chosen such that the hexagons are
    approximately regular. Alternatively, gridsize can be a
    tuple with two elements specifying the number of hexagons
    in the *x*-direction and the *y*-direction.

bins : {'log'} or int or sequence, optional, default is *None*
    If *None*, no binning is applied; the color of each hexagon
    directly corresponds to its count value.

    If 'log', use a logarithmic scale for the color
    map. Internally, :math:`log_{10}(i+1)` is used to
    determine the hexagon color.

    If an integer, divide the counts in the specified number
    of bins, and color the hexagons accordingly.

    If a sequence of values, the values of the lower bound of
    the bins to be used.

xscale : {'linear', 'log'}, optional, default is 'linear'
    Use a linear or log10 scale on the horizontal axis.

yscale : {'linear', 'log'}, optional, default is 'linear'
    Use a linear or log10 scale on the vertical axis.

mincnt : int > 0, optional, default is *None*
    If not *None*, only display cells with more than *mincnt*
    number of points in the cell

marginals : bool, optional, default is *False*
    if marginals is *True*, plot the marginal density as
    colormapped rectagles along the bottom of the x-axis and
    left of the y-axis

extent : scalar, optional, default is *None*
    The limits of the bins. The default assigns the limits
    based on *gridsize*, *x*, *y*, *xscale* and *yscale*.

    If *xscale* or *yscale* is set to 'log', the limits are
    expected to be the exponent for a power of 10. E.g. for
    x-limits of 1 and 50 in 'linear' scale and y-limits
    of 10 and 1000 in 'log' scale, enter (1, 50, 1, 3).

    Order of scalars is (left, right, bottom, top).

Other Parameters
----------------
cmap : object, optional, default is *None*
    a :class:`matplotlib.colors.Colormap` instance. If *None*,
    defaults to rc ``image.cmap``.

norm : object, optional, default is *None*
    :class:`matplotlib.colors.Normalize` instance is used to
    scale luminance data to 0,1.

vmin, vmax : scalar, optional, default is *None*
    *vmin* and *vmax* are used in conjunction with *norm* to
    normalize luminance data. If *None*, the min and max of the
    color array *C* are used.  Note if you pass a norm instance
    your settings for *vmin* and *vmax* will be ignored.

alpha : scalar between 0 and 1, optional, default is *None*
    the alpha value for the patches

linewidths : scalar, optional, default is *None*
    If *None*, defaults to 1.0.

edgecolors : {'face', 'none', *None*} or mpl color, optional, default            is 'face'

    If 'face', draws the edges in the same color as the fill color.

    If 'none', no edge is drawn; this can sometimes lead to unsightly
    unpainted pixels between the hexagons.

    If *None*, draws outlines in the default color.

    If a matplotlib color arg, draws outlines in the specified color.

Returns
-------
object
    a :class:`~matplotlib.collections.PolyCollection` instance; use
    :meth:`~matplotlib.collections.PolyCollection.get_array` on
    this :class:`~matplotlib.collections.PolyCollection` to get
    the counts in each hexagon.

    If *marginals* is *True*, horizontal
    bar and vertical bar (both PolyCollections) will be attached
    to the return collection as attributes *hbar* and *vbar*.

Notes
--------
The standard descriptions of all the
:class:`~matplotlib.collections.Collection` parameters:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### hist
```py

def hist(ax, *args, **kwargs)

```



Plot a histogram.

Compute and draw the histogram of *x*. The return value is a
tuple (*n*, *bins*, *patches*) or ([*n0*, *n1*, ...], *bins*,
[*patches0*, *patches1*,...]) if the input contains multiple
data.

Multiple data can be provided via *x* as a list of datasets
of potentially different length ([*x0*, *x1*, ...]), or as
a 2-D ndarray in which each column is a dataset.  Note that
the ndarray form is transposed relative to the list form.

Masked arrays are not supported at present.

Parameters
----------
x : (n,) array or sequence of (n,) arrays
    Input values, this takes either a single array or a sequency of
    arrays which are not required to be of the same length

bins : integer or sequence or 'auto', optional
    If an integer is given, ``bins + 1`` bin edges are calculated and
    returned, consistent with :func:`numpy.histogram`.

    If `bins` is a sequence, gives bin edges, including left edge of
    first bin and right edge of last bin.  In this case, `bins` is
    returned unmodified.

    All but the last (righthand-most) bin is half-open.  In other
    words, if `bins` is::

        [1, 2, 3, 4]

    then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
    the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
    *includes* 4.

    Unequally spaced bins are supported if *bins* is a sequence.

    If Numpy 1.11 is installed, may also be ``'auto'``.

    Default is taken from the rcParam ``hist.bins``.

range : tuple or None, optional
    The lower and upper range of the bins. Lower and upper outliers
    are ignored. If not provided, *range* is ``(x.min(), x.max())``.
    Range has no effect if *bins* is a sequence.

    If *bins* is a sequence or *range* is specified, autoscaling
    is based on the specified bin range instead of the
    range of x.

    Default is ``None``

density : boolean, optional
    If ``True``, the first element of the return tuple will
    be the counts normalized to form a probability density, i.e.,
    the area (or integral) under the histogram will sum to 1.
    This is achieved by dividing the count by the number of
    observations times the bin width and not dividing by the total
    number of observations. If *stacked* is also ``True``, the sum of
    the histograms is normalized to 1.

    Default is ``None`` for both *normed* and *density*. If either is
    set, then that value will be used. If neither are set, then the
    args will be treated as ``False``.

    If both *density* and *normed* are set an error is raised.

weights : (n, ) array_like or None, optional
    An array of weights, of the same shape as *x*.  Each value in *x*
    only contributes its associated weight towards the bin count
    (instead of 1).  If *normed* or *density* is ``True``,
    the weights are normalized, so that the integral of the density
    over the range remains 1.

    Default is ``None``

cumulative : boolean, optional
    If ``True``, then a histogram is computed where each bin gives the
    counts in that bin plus all bins for smaller values. The last bin
    gives the total number of datapoints. If *normed* or *density*
    is also ``True`` then the histogram is normalized such that the
    last bin equals 1. If *cumulative* evaluates to less than 0
    (e.g., -1), the direction of accumulation is reversed.
    In this case, if *normed* and/or *density* is also ``True``, then
    the histogram is normalized such that the first bin equals 1.

    Default is ``False``

bottom : array_like, scalar, or None
    Location of the bottom baseline of each bin.  If a scalar,
    the base line for each bin is shifted by the same amount.
    If an array, each bin is shifted independently and the length
    of bottom must match the number of bins.  If None, defaults to 0.

    Default is ``None``

histtype : {'bar', 'barstacked', 'step',  'stepfilled'}, optional
    The type of histogram to draw.

    - 'bar' is a traditional bar-type histogram.  If multiple data
      are given the bars are aranged side by side.

    - 'barstacked' is a bar-type histogram where multiple
      data are stacked on top of each other.

    - 'step' generates a lineplot that is by default
      unfilled.

    - 'stepfilled' generates a lineplot that is by default
      filled.

    Default is 'bar'

align : {'left', 'mid', 'right'}, optional
    Controls how the histogram is plotted.

        - 'left': bars are centered on the left bin edges.

        - 'mid': bars are centered between the bin edges.

        - 'right': bars are centered on the right bin edges.

    Default is 'mid'

orientation : {'horizontal', 'vertical'}, optional
    If 'horizontal', `~matplotlib.pyplot.barh` will be used for
    bar-type histograms and the *bottom* kwarg will be the left edges.

rwidth : scalar or None, optional
    The relative width of the bars as a fraction of the bin width.  If
    ``None``, automatically compute the width.

    Ignored if *histtype* is 'step' or 'stepfilled'.

    Default is ``None``

log : boolean, optional
    If ``True``, the histogram axis will be set to a log scale. If
    *log* is ``True`` and *x* is a 1D array, empty bins will be
    filtered out and only the non-empty ``(n, bins, patches)``
    will be returned.

    Default is ``False``

color : color or array_like of colors or None, optional
    Color spec or sequence of color specs, one per dataset.  Default
    (``None``) uses the standard line color sequence.

    Default is ``None``

label : string or None, optional
    String, or sequence of strings to match multiple datasets.  Bar
    charts yield multiple patches per dataset, but only the first gets
    the label, so that the legend command will work as expected.

    default is ``None``

stacked : boolean, optional
    If ``True``, multiple data are stacked on top of each other If
    ``False`` multiple data are aranged side by side if histtype is
    'bar' or on top of each other if histtype is 'step'

    Default is ``False``

Returns
-------
n : array or list of arrays
    The values of the histogram bins. See *normed* or *density*
    and *weights* for a description of the possible semantics.
    If input *x* is an array, then this is an array of length
    *nbins*. If input is a sequence arrays
    ``[data1, data2,..]``, then this is a list of arrays with
    the values of the histograms for each of the arrays in the
    same order.

bins : array
    The edges of the bins. Length nbins + 1 (nbins left edges and right
    edge of last bin).  Always a single array even when multiple data
    sets are passed in.

patches : list or list of lists
    Silent list of individual patches used to create the histogram
    or list of such list if multiple input datasets.

Other Parameters
----------------
**kwargs : `~matplotlib.patches.Patch` properties

See also
--------
hist2d : 2D histograms

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'weights', 'x'.


### hist2d
```py

def hist2d(ax, *args, **kwargs)

```



Make a 2D histogram plot.

Parameters
----------
x, y: array_like, shape (n, )
    Input values

bins: [None | int | [int, int] | array_like | [array, array]]

    The bin specification:

        - If int, the number of bins for the two dimensions
          (nx=ny=bins).

        - If [int, int], the number of bins in each dimension
          (nx, ny = bins).

        - If array_like, the bin edges for the two dimensions
          (x_edges=y_edges=bins).

        - If [array, array], the bin edges in each dimension
          (x_edges, y_edges = bins).

    The default value is 10.

range : array_like shape(2, 2), optional, default: None
     The leftmost and rightmost edges of the bins along each dimension
     (if not specified explicitly in the bins parameters): [[xmin,
     xmax], [ymin, ymax]]. All values outside of this range will be
     considered outliers and not tallied in the histogram.

normed : boolean, optional, default: False
     Normalize histogram.

weights : array_like, shape (n, ), optional, default: None
    An array of values w_i weighing each sample (x_i, y_i).

cmin : scalar, optional, default: None
     All bins that has count less than cmin will not be displayed and
     these count values in the return value count histogram will also
     be set to nan upon return

cmax : scalar, optional, default: None
     All bins that has count more than cmax will not be displayed (set
     to none before passing to imshow) and these count values in the
     return value count histogram will also be set to nan upon return

Returns
-------
The return value is ``(counts, xedges, yedges, Image)``.

Other Parameters
----------------
cmap : {Colormap, string}, optional
    A :class:`matplotlib.colors.Colormap` instance.  If not set, use rc
    settings.

norm : Normalize, optional
    A :class:`matplotlib.colors.Normalize` instance is used to
    scale luminance data to ``[0, 1]``. If not set, defaults to
    ``Normalize()``.

vmin/vmax : {None, scalar}, optional
    Arguments passed to the `Normalize` instance.

alpha : ``0 <= scalar <= 1`` or ``None``, optional
    The alpha blending value.

See also
--------
hist : 1D histogram

Notes
-----
Rendering the histogram with a logarithmic color scale is
accomplished by passing a :class:`colors.LogNorm` instance to
the *norm* keyword argument. Likewise, power-law normalization
(similar in effect to gamma correction) can be accomplished with
:class:`colors.PowerNorm`.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'weights', 'x', 'y'.


### hitlist
```py

def hitlist(self, event)

```



List the children of the artist which contain the mouse event *event*.


### hlines
```py

def hlines(ax, *args, **kwargs)

```



Plot horizontal lines at each `y` from `xmin` to `xmax`.

Parameters
----------
y : scalar or sequence of scalar
    y-indexes where to plot the lines.

xmin, xmax : scalar or 1D array_like
    Respective beginning and end of each line. If scalars are
    provided, all lines will have same length.

colors : array_like of colors, optional, default: 'k'

linestyles : ['solid' | 'dashed' | 'dashdot' | 'dotted'], optional

label : string, optional, default: ''

Returns
-------
lines : `~matplotlib.collections.LineCollection`

Other Parameters
----------------
**kwargs :  `~matplotlib.collections.LineCollection` properties.

See also
--------
vlines : vertical lines
axhline: horizontal line across the axes

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'colors', 'xmax', 'xmin', 'y'.


### hold
```py

def hold(*args, **kwargs)

```



.. deprecated:: 2.0
    axes.hold is deprecated.
    See the API Changes document (http://matplotlib.org/api/api_changes.html)
    for more details.

Set the hold state

The ``hold`` mechanism is deprecated and will be removed in
v3.0.  The behavior will remain consistent with the
long-time default value of True.

If *hold* is *None* (default), toggle the *hold* state.  Else
set the *hold* state to boolean value *b*.

Examples::

  # toggle hold
  hold()

  # turn hold on
  hold(True)

  # turn hold off
  hold(False)

When hold is *True*, subsequent plot commands will be added to
the current axes.  When hold is *False*, the current axes and
figure will be cleared on the next plot command


### imshow
```py

def imshow(ax, *args, **kwargs)

```



Display an image on the axes.

Parameters
----------
X : array_like, shape (n, m) or (n, m, 3) or (n, m, 4)
    Display the image in `X` to current axes.  `X` may be an
    array or a PIL image. If `X` is an array, it
    can have the following shapes and types:

    - MxN -- values to be mapped (float or int)
    - MxNx3 -- RGB (float or uint8)
    - MxNx4 -- RGBA (float or uint8)

    The value for each component of MxNx3 and MxNx4 float arrays
    should be in the range 0.0 to 1.0. MxN arrays are mapped
    to colors based on the `norm` (mapping scalar to scalar)
    and the `cmap` (mapping the normed scalar to a color).

cmap : `~matplotlib.colors.Colormap`, optional, default: None
    If None, default to rc `image.cmap` value. `cmap` is ignored
    if `X` is 3-D, directly specifying RGB(A) values.

aspect : ['auto' | 'equal' | scalar], optional, default: None
    If 'auto', changes the image aspect ratio to match that of the
    axes.

    If 'equal', and `extent` is None, changes the axes aspect ratio to
    match that of the image. If `extent` is not `None`, the axes
    aspect ratio is changed to match that of the extent.

    If None, default to rc ``image.aspect`` value.

interpolation : string, optional, default: None
    Acceptable values are 'none', 'nearest', 'bilinear', 'bicubic',
    'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser',
    'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc',
    'lanczos'

    If `interpolation` is None, default to rc `image.interpolation`.
    See also the `filternorm` and `filterrad` parameters.
    If `interpolation` is 'none', then no interpolation is performed
    on the Agg, ps and pdf backends. Other backends will fall back to
    'nearest'.

norm : `~matplotlib.colors.Normalize`, optional, default: None
    A `~matplotlib.colors.Normalize` instance is used to scale
    a 2-D float `X` input to the (0, 1) range for input to the
    `cmap`. If `norm` is None, use the default func:`normalize`.
    If `norm` is an instance of `~matplotlib.colors.NoNorm`,
    `X` must be an array of integers that index directly into
    the lookup table of the `cmap`.

vmin, vmax : scalar, optional, default: None
    `vmin` and `vmax` are used in conjunction with norm to normalize
    luminance data.  Note if you pass a `norm` instance, your
    settings for `vmin` and `vmax` will be ignored.

alpha : scalar, optional, default: None
    The alpha blending value, between 0 (transparent) and 1 (opaque)

origin : ['upper' | 'lower'], optional, default: None
    Place the [0,0] index of the array in the upper left or lower left
    corner of the axes. If None, default to rc `image.origin`.

extent : scalars (left, right, bottom, top), optional, default: None
    The location, in data-coordinates, of the lower-left and
    upper-right corners. If `None`, the image is positioned such that
    the pixel centers fall on zero-based (row, column) indices.

shape : scalars (columns, rows), optional, default: None
    For raw buffer images

filternorm : scalar, optional, default: 1
    A parameter for the antigrain image resize filter.  From the
    antigrain documentation, if `filternorm` = 1, the filter
    normalizes integer values and corrects the rounding errors. It
    doesn't do anything with the source floating point values, it
    corrects only integers according to the rule of 1.0 which means
    that any sum of pixel weights must be equal to 1.0.  So, the
    filter function must produce a graph of the proper shape.

filterrad : scalar, optional, default: 4.0
    The filter radius for filters that have a radius parameter, i.e.
    when interpolation is one of: 'sinc', 'lanczos' or 'blackman'

Returns
-------
image : `~matplotlib.image.AxesImage`

Other Parameters
----------------
**kwargs : `~matplotlib.artist.Artist` properties.

See also
--------
matshow : Plot a matrix or an array as an image.

Notes
-----
Unless *extent* is used, pixel centers will be located at integer
coordinates. In other words: the origin will coincide with the center
of pixel (0, 0).

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### in\_axes
```py

def in_axes(self, mouseevent)

```



Return *True* if the given *mouseevent* (in display coords)
is in the Axes


### invert\_xaxis
```py

def invert_xaxis(self)

```



Invert the x-axis.


### invert\_yaxis
```py

def invert_yaxis(self)

```



Invert the y-axis.


### invert\_zaxis
```py

def invert_zaxis(self)

```



Invert the z-axis.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### is\_figure\_set
```py

def is_figure_set(self)

```



Returns whether the artist is assigned to a `~.Figure`.


### is\_transform\_set
```py

def is_transform_set(self)

```



Returns *True* if :class:`Artist` has a transform explicitly
set.


### ishold
```py

def ishold(*args, **kwargs)

```



.. deprecated:: 2.0
    The ishold function was deprecated in version 2.0.

return the HOLD status of the axes

        The `hold` mechanism is deprecated and will be removed in
        v3.0.


### legend
```py

def legend(self, *args, **kwargs)

```



Places a legend on the axes.

To make a legend for lines which already exist on the axes
(via plot for instance), simply call this function with an iterable
of strings, one for each legend item. For example::

    ax.plot([1, 2, 3])
    ax.legend(['A simple line'])

However, in order to keep the "label" and the legend element
instance together, it is preferable to specify the label either at
artist creation, or by calling the
:meth:`~matplotlib.artist.Artist.set_label` method on the artist::

    line, = ax.plot([1, 2, 3], label='Inline label')
    # Overwrite the label by calling the method.
    line.set_label('Label via method')
    ax.legend()

Specific lines can be excluded from the automatic legend element
selection by defining a label starting with an underscore.
This is default for all artists, so calling :meth:`legend` without
any arguments and without setting the labels manually will result in
no legend being drawn.

For full control of which artists have a legend entry, it is possible
to pass an iterable of legend artists followed by an iterable of
legend labels respectively::

   legend((line1, line2, line3), ('label1', 'label2', 'label3'))

Parameters
----------

loc : int or string or pair of floats, default: 'upper right'
    The location of the legend. Possible codes are:

        ===============   =============
        Location String   Location Code
        ===============   =============
        'best'            0
        'upper right'     1
        'upper left'      2
        'lower left'      3
        'lower right'     4
        'right'           5
        'center left'     6
        'center right'    7
        'lower center'    8
        'upper center'    9
        'center'          10
        ===============   =============


    Alternatively can be a 2-tuple giving ``x, y`` of the lower-left
    corner of the legend in axes coordinates (in which case
    ``bbox_to_anchor`` will be ignored).

bbox_to_anchor : `~.BboxBase` or pair of floats
    Specify any arbitrary location for the legend in `bbox_transform`
    coordinates (default Axes coordinates).

    For example, to put the legend's upper right hand corner in the
    center of the axes the following keywords can be used::

       loc='upper right', bbox_to_anchor=(0.5, 0.5)

ncol : integer
    The number of columns that the legend has. Default is 1.

prop : None or :class:`matplotlib.font_manager.FontProperties` or dict
    The font properties of the legend. If None (default), the current
    :data:`matplotlib.rcParams` will be used.

fontsize : int or float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
    Controls the font size of the legend. If the value is numeric the
    size will be the absolute font size in points. String values are
    relative to the current default font size. This argument is only
    used if `prop` is not specified.

numpoints : None or int
    The number of marker points in the legend when creating a legend
    entry for a line/:class:`matplotlib.lines.Line2D`.
    Default is ``None`` which will take the value from the
    ``legend.numpoints`` :data:`rcParam<matplotlib.rcParams>`.

scatterpoints : None or int
    The number of marker points in the legend when creating a legend
    entry for a scatter plot/
    :class:`matplotlib.collections.PathCollection`.
    Default is ``None`` which will take the value from the
    ``legend.scatterpoints`` :data:`rcParam<matplotlib.rcParams>`.

scatteryoffsets : iterable of floats
    The vertical offset (relative to the font size) for the markers
    created for a scatter plot legend entry. 0.0 is at the base the
    legend text, and 1.0 is at the top. To draw all markers at the
    same height, set to ``[0.5]``. Default ``[0.375, 0.5, 0.3125]``.

markerscale : None or int or float
    The relative size of legend markers compared with the originally
    drawn ones. Default is ``None`` which will take the value from
    the ``legend.markerscale`` :data:`rcParam <matplotlib.rcParams>`.

markerfirst : bool
    If *True*, legend marker is placed to the left of the legend label.
    If *False*, legend marker is placed to the right of the legend
    label.
    Default is *True*.

frameon : None or bool
    Control whether the legend should be drawn on a patch (frame).
    Default is ``None`` which will take the value from the
    ``legend.frameon`` :data:`rcParam<matplotlib.rcParams>`.

fancybox : None or bool
    Control whether round edges should be enabled around
    the :class:`~matplotlib.patches.FancyBboxPatch` which
    makes up the legend's background.
    Default is ``None`` which will take the value from the
    ``legend.fancybox`` :data:`rcParam<matplotlib.rcParams>`.

shadow : None or bool
    Control whether to draw a shadow behind the legend.
    Default is ``None`` which will take the value from the
    ``legend.shadow`` :data:`rcParam<matplotlib.rcParams>`.

framealpha : None or float
    Control the alpha transparency of the legend's background.
    Default is ``None`` which will take the value from the
    ``legend.framealpha`` :data:`rcParam<matplotlib.rcParams>`.
    If shadow is activated and framealpha is ``None`` the
    default value is being ignored.

facecolor : None or "inherit" or a color spec
    Control the legend's background color.
    Default is ``None`` which will take the value from the
    ``legend.facecolor`` :data:`rcParam<matplotlib.rcParams>`.
    If ``"inherit"``, it will take the ``axes.facecolor``
    :data:`rcParam<matplotlib.rcParams>`.

edgecolor : None or "inherit" or a color spec
    Control the legend's background patch edge color.
    Default is ``None`` which will take the value from the
    ``legend.edgecolor`` :data:`rcParam<matplotlib.rcParams>`.
    If ``"inherit"``, it will take the ``axes.edgecolor``
    :data:`rcParam<matplotlib.rcParams>`.

mode : {"expand", None}
    If `mode` is set to ``"expand"`` the legend will be horizontally
    expanded to fill the axes area (or `bbox_to_anchor` if defines
    the legend's size).

bbox_transform : None or :class:`matplotlib.transforms.Transform`
    The transform for the bounding box (`bbox_to_anchor`). For a value
    of ``None`` (default) the Axes'
    :data:`~matplotlib.axes.Axes.transAxes` transform will be used.

title : str or None
    The legend's title. Default is no title (``None``).

borderpad : float or None
    The fractional whitespace inside the legend border.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.borderpad`` :data:`rcParam<matplotlib.rcParams>`.

labelspacing : float or None
    The vertical space between the legend entries.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.labelspacing`` :data:`rcParam<matplotlib.rcParams>`.

handlelength : float or None
    The length of the legend handles.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.handlelength`` :data:`rcParam<matplotlib.rcParams>`.

handletextpad : float or None
    The pad between the legend handle and text.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.handletextpad`` :data:`rcParam<matplotlib.rcParams>`.

borderaxespad : float or None
    The pad between the axes and legend border.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.borderaxespad`` :data:`rcParam<matplotlib.rcParams>`.

columnspacing : float or None
    The spacing between columns.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.columnspacing`` :data:`rcParam<matplotlib.rcParams>`.

handler_map : dict or None
    The custom dictionary mapping instances or types to a legend
    handler. This `handler_map` updates the default handler map
    found at :func:`matplotlib.legend.Legend.get_legend_handler_map`.

Returns
-------

:class:`matplotlib.legend.Legend` instance

Notes
-----

Not all kinds of artist are supported by the legend command. See
:ref:`sphx_glr_tutorials_intermediate_legend_guide.py` for details.

Examples
--------

.. plot:: gallery/api/legend.py


### locator\_params
```py

def locator_params(self, axis=u'both', tight=None, **kwargs)

```



Convenience method for controlling tick locators.

See :meth:`matplotlib.axes.Axes.locator_params` for full
documentation  Note that this is for Axes3D objects,
therefore, setting *axis* to 'both' will result in the
parameters being set for all three axes.  Also, *axis*
can also take a value of 'z' to apply parameters to the
z axis.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### loglog
```py

def loglog(self, *args, **kwargs)

```



Make a plot with log scaling on both the *x* and *y* axis.

:func:`~matplotlib.pyplot.loglog` supports all the keyword
arguments of :func:`~matplotlib.pyplot.plot` and
:meth:`matplotlib.axes.Axes.set_xscale` /
:meth:`matplotlib.axes.Axes.set_yscale`.

Notable keyword arguments:

  *basex*/*basey*: scalar > 1
    Base of the *x*/*y* logarithm

  *subsx*/*subsy*: [ *None* | sequence ]
    The location of the minor *x*/*y* ticks; *None* defaults
    to autosubs, which depend on the number of decades in the
    plot; see :meth:`matplotlib.axes.Axes.set_xscale` /
    :meth:`matplotlib.axes.Axes.set_yscale` for details

  *nonposx*/*nonposy*: ['mask' | 'clip' ]
    Non-positive values in *x* or *y* can be masked as
    invalid, or clipped to a very small positive number

The remaining valid kwargs are
:class:`~matplotlib.lines.Line2D` properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 


### magnitude\_spectrum
```py

def magnitude_spectrum(ax, *args, **kwargs)

```



Plot the magnitude spectrum.

Call signature::

  magnitude_spectrum(x, Fs=2, Fc=0,  window=mlab.window_hanning,
                     pad_to=None, sides='default', **kwargs)

Compute the magnitude spectrum of *x*.  Data is padded to a
length of *pad_to* and the windowing function *window* is applied to
the signal.

Parameters
----------
x : 1-D array or sequence
    Array or sequence containing the data

Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  While not increasing the actual resolution of
    the spectrum (the minimum distance between resolvable peaks),
    this can give more points in the plot, allowing for more
    detail. This corresponds to the *n* parameter in the call to fft().
    The default is None, which sets *pad_to* equal to the length of the
    input signal (i.e. no padding).

scale : [ 'default' | 'linear' | 'dB' ]
    The scaling of the values in the *spec*.  'linear' is no scaling.
    'dB' returns the values in dB scale, i.e., the dB amplitude
    (20 * log10). 'default' is 'linear'.

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.

Returns
-------
spectrum : 1-D array
    The values for the magnitude spectrum before scaling (real valued)

freqs : 1-D array
    The frequencies corresponding to the elements in *spectrum*

line : a :class:`~matplotlib.lines.Line2D` instance
    The line created by this function

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

See Also
--------
:func:`psd`
    :func:`psd` plots the power spectral density.`.

:func:`angle_spectrum`
    :func:`angle_spectrum` plots the angles of the corresponding
    frequencies.

:func:`phase_spectrum`
    :func:`phase_spectrum` plots the phase (unwrapped angle) of the
    corresponding frequencies.

:func:`specgram`
    :func:`specgram` can plot the magnitude spectrum of segments within
    the signal in a colormap.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x'.


### margins
```py

def margins(self, *args, **kw)

```



Convenience method to set or retrieve autoscaling margins.

signatures::
    margins()

returns xmargin, ymargin, zmargin

::

    margins(margin)

    margins(xmargin, ymargin, zmargin)

    margins(x=xmargin, y=ymargin, z=zmargin)

    margins(..., tight=False)

All forms above set the xmargin, ymargin and zmargin
parameters. All keyword parameters are optional.  A single argument
specifies xmargin, ymargin and zmargin.  The *tight* parameter
is passed to :meth:`autoscale_view`, which is executed after
a margin is changed; the default here is *True*, on the
assumption that when margins are specified, no additional
padding to match tick marks is usually desired.  Setting
*tight* to *None* will preserve the previous setting.

Specifying any margin changes only the autoscaling; for example,
if *xmargin* is not None, then *xmargin* times the X data
interval will be added to each end of that interval before
it is used in autoscaling.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### matshow
```py

def matshow(self, Z, **kwargs)

```



Plot a matrix or array as an image.

The matrix will be shown the way it would be printed, with the first
row at the top.  Row and column numbering is zero-based.

Parameters
----------
Z : array_like shape (n, m)
    The matrix to be displayed.

Returns
-------
image : `~matplotlib.image.AxesImage`

Other Parameters
----------------
**kwargs : `~matplotlib.axes.Axes.imshow` arguments
    Sets `origin` to 'upper', 'interpolation' to 'nearest' and
    'aspect' to equal.

See also
--------
imshow : plot an image


### minorticks\_off
```py

def minorticks_off(self)

```



Remove minor ticks from the axes.


### minorticks\_on
```py

def minorticks_on(self)

```



Add autoscaling minor ticks to the axes.


### mouse\_init
```py

def mouse_init(self, rotate_btn=1, zoom_btn=3)

```



Initializes mouse button callbacks to enable 3D rotation of
the axes.  Also optionally sets the mouse buttons for 3D rotation
and zooming.

============  =======================================================
Argument      Description
============  =======================================================
*rotate_btn*  The integer or list of integers specifying which mouse
              button or buttons to use for 3D rotation of the axes.
              Default = 1.

*zoom_btn*    The integer or list of integers specifying which mouse
              button or buttons to use to zoom the 3D axes.
              Default = 3.
============  =======================================================


### pchanged
```py

def pchanged(self)

```



Fire an event when property changed, calling all of the
registered callbacks.


### pcolor
```py

def pcolor(ax, *args, **kwargs)

```



Create a pseudocolor plot of a 2-D array.

Call signatures::

    pcolor(C, **kwargs)
    pcolor(X, Y, C, **kwargs)

pcolor can be very slow for large arrays; consider
using the similar but much faster
:func:`~matplotlib.pyplot.pcolormesh` instead.

Parameters
----------
C : array_like
    An array of color values.

X, Y : array_like, optional
    If given, specify the (x, y) coordinates of the colored
    quadrilaterals; the quadrilateral for ``C[i,j]`` has corners at::

        (X[i,   j],   Y[i,   j]),
        (X[i,   j+1], Y[i,   j+1]),
        (X[i+1, j],   Y[i+1, j]),
        (X[i+1, j+1], Y[i+1, j+1])

    Ideally the dimensions of ``X`` and ``Y`` should be one greater
    than those of ``C``; if the dimensions are the same, then the last
    row and column of ``C`` will be ignored.

    Note that the column index corresponds to the
    x-coordinate, and the row index corresponds to y; for
    details, see the :ref:`Grid Orientation
    <axes-pcolor-grid-orientation>` section below.

    If either or both of ``X`` and ``Y`` are 1-D arrays or column
    vectors, they will be expanded as needed into the appropriate 2-D
    arrays, making a rectangular grid.

cmap : `~matplotlib.colors.Colormap`, optional, default: None
    If `None`, default to rc settings.

norm : `matplotlib.colors.Normalize`, optional, default: None
    An instance is used to scale luminance data to (0, 1).
    If `None`, defaults to :func:`normalize`.

vmin, vmax : scalar, optional, default: None
    ``vmin`` and ``vmax`` are used in conjunction with ``norm`` to
    normalize luminance data.  If either is `None`, it is autoscaled to
    the respective min or max of the color array ``C``.  If not `None`,
    ``vmin`` or ``vmax`` passed in here override any pre-existing
    values supplied in the ``norm`` instance.

edgecolors : {None, 'none', color, color sequence}
    If None, the rc setting is used by default.
    If 'none', edges will not be visible.
    An mpl color or sequence of colors will set the edge color.

alpha : scalar, optional, default: None
    The alpha blending value, between 0 (transparent) and 1 (opaque).

snap : bool, optional, default: False
    Whether to snap the mesh to pixel boundaries.

Returns
-------
collection : `matplotlib.collections.Collection`

Other Parameters
----------------
antialiaseds : bool, optional, default: False
    The default ``antialiaseds`` is False if the default
    ``edgecolors="none"`` is used.  This eliminates artificial lines
    at patch boundaries, and works regardless of the value of alpha.
    If ``edgecolors`` is not "none", then the default ``antialiaseds``
    is taken from ``rcParams['patch.antialiased']``, which defaults to
    True. Stroking the edges may be preferred if ``alpha`` is 1, but
    will cause artifacts otherwise.

**kwargs :

    Any unused keyword arguments are passed along to the
    `~matplotlib.collections.PolyCollection` constructor:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 

See Also
--------
pcolormesh : for an explanation of the differences between
    pcolor and pcolormesh.

Notes
-----
.. _axes-pcolor-grid-orientation:

``X``, ``Y`` and ``C`` may be masked arrays. If either C[i, j], or one
of the vertices surrounding C[i,j] (``X`` or ``Y`` at [i, j], [i+1, j],
[i, j+1], [i+1, j+1]) is masked, nothing is plotted.

The grid orientation follows the MATLAB convention: an array ``C`` with
shape (nrows, ncolumns) is plotted with the column number as ``X`` and
the row number as ``Y``, increasing up; hence it is plotted the way the
array would be printed, except that the ``Y`` axis is reversed. That
is, ``C`` is taken as ``C`` (y, x).

Similarly for :func:`meshgrid`::

    x = np.arange(5)
    y = np.arange(3)
    X, Y = np.meshgrid(x, y)

is equivalent to::

    X = array([[0, 1, 2, 3, 4],
               [0, 1, 2, 3, 4],
               [0, 1, 2, 3, 4]])

    Y = array([[0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1],
               [2, 2, 2, 2, 2]])

so if you have::

    C = rand(len(x), len(y))

then you need to transpose C::

    pcolor(X, Y, C.T)

or::

    pcolor(C.T)

MATLAB :func:`pcolor` always discards the last row and column of ``C``,
but Matplotlib displays the last row and column if ``X`` and ``Y`` are
not specified, or if ``X`` and ``Y`` have one more row and column than
``C``.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### pcolorfast
```py

def pcolorfast(ax, *args, **kwargs)

```



pseudocolor plot of a 2-D array

Experimental; this is a pcolor-type method that
provides the fastest possible rendering with the Agg
backend, and that can handle any quadrilateral grid.
It supports only flat shading (no outlines), it lacks
support for log scaling of the axes, and it does not
have a pyplot wrapper.

Call signatures::

  ax.pcolorfast(C, **kwargs)
  ax.pcolorfast(xr, yr, C, **kwargs)
  ax.pcolorfast(x, y, C, **kwargs)
  ax.pcolorfast(X, Y, C, **kwargs)

C is the 2D array of color values corresponding to quadrilateral
cells. Let (nr, nc) be its shape.  C may be a masked array.

``ax.pcolorfast(C, **kwargs)`` is equivalent to
``ax.pcolorfast([0,nc], [0,nr], C, **kwargs)``

*xr*, *yr* specify the ranges of *x* and *y* corresponding to the
rectangular region bounding *C*.  If::

    xr = [x0, x1]

and::

    yr = [y0,y1]

then *x* goes from *x0* to *x1* as the second index of *C* goes
from 0 to *nc*, etc.  (*x0*, *y0*) is the outermost corner of
cell (0,0), and (*x1*, *y1*) is the outermost corner of cell
(*nr*-1, *nc*-1).  All cells are rectangles of the same size.
This is the fastest version.

*x*, *y* are monotonic 1D arrays of length *nc* +1 and *nr* +1,
respectively, giving the x and y boundaries of the cells.  Hence
the cells are rectangular but the grid may be nonuniform.  The
speed is intermediate.  (The grid is checked, and if found to be
uniform the fast version is used.)

*X* and *Y* are 2D arrays with shape (*nr* +1, *nc* +1) that specify
the (x,y) coordinates of the corners of the colored
quadrilaterals; the quadrilateral for C[i,j] has corners at
(X[i,j],Y[i,j]), (X[i,j+1],Y[i,j+1]), (X[i+1,j],Y[i+1,j]),
(X[i+1,j+1],Y[i+1,j+1]).  The cells need not be rectangular.
This is the most general, but the slowest to render.  It may
produce faster and more compact output using ps, pdf, and
svg backends, however.

Note that the column index corresponds to the x-coordinate,
and the row index corresponds to y; for details, see
:ref:`Grid Orientation <axes-pcolor-grid-orientation>`.

Optional keyword arguments:

  *cmap*: [ *None* | Colormap ]
    A :class:`matplotlib.colors.Colormap` instance from cm. If *None*,
    use rc settings.

  *norm*: [ *None* | Normalize ]
    A :class:`matplotlib.colors.Normalize` instance is used to scale
    luminance data to 0,1. If *None*, defaults to normalize()

  *vmin*/*vmax*: [ *None* | scalar ]
    *vmin* and *vmax* are used in conjunction with norm to normalize
    luminance data.  If either are *None*, the min and max
    of the color array *C* is used.  If you pass a norm instance,
    *vmin* and *vmax* will be *None*.

  *alpha*: ``0 <= scalar <= 1``  or *None*
    the alpha blending value

Return value is an image if a regular or rectangular grid
is specified, and a :class:`~matplotlib.collections.QuadMesh`
collection in the general quadrilateral case.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### pcolormesh
```py

def pcolormesh(ax, *args, **kwargs)

```



Plot a quadrilateral mesh.

Call signatures::

  pcolormesh(C)
  pcolormesh(X, Y, C)
  pcolormesh(C, **kwargs)

Create a pseudocolor plot of a 2-D array.

pcolormesh is similar to :func:`~matplotlib.pyplot.pcolor`,
but uses a different mechanism and returns a different
object; pcolor returns a
:class:`~matplotlib.collections.PolyCollection` but pcolormesh
returns a
:class:`~matplotlib.collections.QuadMesh`.  It is much faster,
so it is almost always preferred for large arrays.

*C* may be a masked array, but *X* and *Y* may not.  Masked
array support is implemented via *cmap* and *norm*; in
contrast, :func:`~matplotlib.pyplot.pcolor` simply does not
draw quadrilaterals with masked colors or vertices.

Keyword arguments:

  *cmap*: [ *None* | Colormap ]
    A :class:`matplotlib.colors.Colormap` instance. If *None*, use
    rc settings.

  *norm*: [ *None* | Normalize ]
    A :class:`matplotlib.colors.Normalize` instance is used to
    scale luminance data to 0,1. If *None*, defaults to
    :func:`normalize`.

  *vmin*/*vmax*: [ *None* | scalar ]
    *vmin* and *vmax* are used in conjunction with *norm* to
    normalize luminance data.  If either is *None*, it
    is autoscaled to the respective min or max
    of the color array *C*.  If not *None*, *vmin* or
    *vmax* passed in here override any pre-existing values
    supplied in the *norm* instance.

  *shading*: [ 'flat' | 'gouraud' ]
    'flat' indicates a solid color for each quad.  When
    'gouraud', each quad will be Gouraud shaded.  When gouraud
    shading, edgecolors is ignored.

  *edgecolors*: [*None* | ``'None'`` | ``'face'`` | color |
                 color sequence]

    If *None*, the rc setting is used by default.

    If ``'None'``, edges will not be visible.

    If ``'face'``, edges will have the same color as the faces.

    An mpl color or sequence of colors will set the edge color

  *alpha*: ``0 <= scalar <= 1``  or *None*
    the alpha blending value

Return value is a :class:`matplotlib.collections.QuadMesh`
object.

kwargs can be used to control the
:class:`matplotlib.collections.QuadMesh` properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float or None 
  animated: bool 
  antialiased or antialiaseds: Boolean or sequence of booleans 
  array: ndarray
  clim: a length 2 sequence of floats 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  cmap: a colormap or registered colormap name 
  color: matplotlib color arg or sequence of rgba tuples
  contains: a callable function 
  edgecolor or edgecolors: matplotlib color spec or sequence of specs 
  facecolor or facecolors: matplotlib color spec or sequence of specs 
  figure: a `~.Figure` instance 
  gid: an id string 
  hatch: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ] 
  label: object 
  linestyle or dashes or linestyles: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or linewidths or lw: float or sequence of floats 
  norm: `~.Normalize`
  offset_position: [ 'screen' | 'data' ] 
  offsets: float or sequence of floats 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  urls: List[str] or None 
  visible: bool 
  zorder: float 

.. seealso::

    :func:`~matplotlib.pyplot.pcolor`
        For an explanation of the grid orientation
        (:ref:`Grid Orientation <axes-pcolor-grid-orientation>`)
        and the expansion of 1-D *X* and/or *Y* to 2-D arrays.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### phase\_spectrum
```py

def phase_spectrum(ax, *args, **kwargs)

```



Plot the phase spectrum.

Call signature::

  phase_spectrum(x, Fs=2, Fc=0,  window=mlab.window_hanning,
                 pad_to=None, sides='default', **kwargs)

Compute the phase spectrum (unwrapped angle spectrum) of *x*.
Data is padded to a length of *pad_to* and the windowing function
*window* is applied to the signal.

Parameters
----------
x : 1-D array or sequence
    Array or sequence containing the data

Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  While not increasing the actual resolution of
    the spectrum (the minimum distance between resolvable peaks),
    this can give more points in the plot, allowing for more
    detail. This corresponds to the *n* parameter in the call to fft().
    The default is None, which sets *pad_to* equal to the length of the
    input signal (i.e. no padding).

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.

Returns
-------
spectrum : 1-D array
    The values for the phase spectrum in radians (real valued)

freqs : 1-D array
    The frequencies corresponding to the elements in *spectrum*

line : a :class:`~matplotlib.lines.Line2D` instance
    The line created by this function

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

See Also
--------
:func:`magnitude_spectrum`
    :func:`magnitude_spectrum` plots the magnitudes of the
    corresponding frequencies.

:func:`angle_spectrum`
    :func:`angle_spectrum` plots the wrapped version of this function.

:func:`specgram`
    :func:`specgram` can plot the phase spectrum of segments within the
    signal in a colormap.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x'.


### pick
```py

def pick(self, *args)

```



Trigger pick event

Call signature::

    pick(mouseevent)

each child artist will fire a pick event if mouseevent is over
the artist and the artist has picker set


### pickable
```py

def pickable(self)

```



Return *True* if :class:`Artist` is pickable.


### pie
```py

def pie(ax, *args, **kwargs)

```



Plot a pie chart.

Make a pie chart of array *x*.  The fractional area of each
wedge is given by ``x/sum(x)``.  If ``sum(x) <= 1``, then the
values of x give the fractional area directly and the array
will not be normalized.  The wedges are plotted
counterclockwise, by default starting from the x-axis.

Parameters
----------
x : array-like
    The input array used to make the pie chart.

explode : array-like, optional, default: None
    If not *None*, is a ``len(x)`` array which specifies the
    fraction of the radius with which to offset each wedge.

labels : list, optional, default: None
    A sequence of strings providing the labels for each wedge

colors : array-like, optional, default: None
    A sequence of matplotlib color args through which the pie chart
    will cycle.  If `None`, will use the colors in the currently
    active cycle.

autopct : None (default), string, or function, optional
    If not *None*, is a string or function used to label the wedges
    with their numeric value.  The label will be placed inside the
    wedge.  If it is a format string, the label will be ``fmt%pct``.
    If it is a function, it will be called.

pctdistance : float, optional, default: 0.6
    The ratio between the center of each pie slice and the
    start of the text generated by *autopct*.  Ignored if
    *autopct* is *None*.

shadow : bool, optional, default: False
    Draw a shadow beneath the pie.

labeldistance : float, optional, default: 1.1
    The radial distance at which the pie labels are drawn

startangle : float, optional, default: None
    If not *None*, rotates the start of the pie chart by *angle*
    degrees counterclockwise from the x-axis.

radius : float, optional, default: None
    The radius of the pie, if *radius* is *None* it will be set to 1.

counterclock : bool, optional, default: True
    Specify fractions direction, clockwise or counterclockwise.

wedgeprops : dict, optional, default: None
    Dict of arguments passed to the wedge objects making the pie.
    For example, you can pass in``wedgeprops = {'linewidth': 3}``
    to set the width of the wedge border lines equal to 3.
    For more details, look at the doc/arguments of the wedge object.
    By default ``clip_on=False``.

textprops : dict, optional, default: None
    Dict of arguments to pass to the text objects.

center :  list of float, optional, default: (0, 0)
    Center position of the chart. Takes value (0, 0) or is a
    sequence of 2 scalars.

frame : bool, optional, default: False
    Plot axes frame with the chart if true.

rotatelabels : bool, optional, default: False
    Rotate each label to the angle of the corresponding slice if true.

Returns
-------
patches : list
    A sequence of :class:`matplotlib.patches.Wedge` instances

texts : list
    A is a list of the label :class:`matplotlib.text.Text` instances.

autotexts : list
    A is a list of :class:`~matplotlib.text.Text` instances for the
    numeric labels. Is returned only if parameter *autopct* is
    not *None*.

Notes
-----
The pie chart will probably look best if the figure and axes are
square, or the Axes aspect is equal.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'colors', 'explode', 'labels', 'x'.


### plot
```py

def plot(self, xs, ys, *args, **kwargs)

```



Plot 2D or 3D data.

==========  ================================================
Argument    Description
==========  ================================================
*xs*, *ys*  x, y coordinates of vertices

*zs*        z value(s), either one for all points or one for
            each point.
*zdir*      Which direction to use as z ('x', 'y' or 'z')
            when plotting a 2D set.
==========  ================================================

Other arguments are passed on to
:func:`~matplotlib.axes.Axes.plot`


### plot3D
```py

def plot3D(self, xs, ys, *args, **kwargs)

```



Plot 2D or 3D data.

==========  ================================================
Argument    Description
==========  ================================================
*xs*, *ys*  x, y coordinates of vertices

*zs*        z value(s), either one for all points or one for
            each point.
*zdir*      Which direction to use as z ('x', 'y' or 'z')
            when plotting a 2D set.
==========  ================================================

Other arguments are passed on to
:func:`~matplotlib.axes.Axes.plot`


### plot\_date
```py

def plot_date(ax, *args, **kwargs)

```



A plot with data that contains dates.

Similar to the :func:`~matplotlib.pyplot.plot` command, except
the *x* or *y* (or both) data is considered to be dates, and the
axis is labeled accordingly.

*x* and/or *y* can be a sequence of dates represented as float
days since 0001-01-01 UTC.

Note if you are using custom date tickers and formatters, it
may be necessary to set the formatters/locators after the call
to :meth:`plot_date` since :meth:`plot_date` will set the
default tick locator to
:class:`matplotlib.dates.AutoDateLocator` (if the tick
locator is not already set to a
:class:`matplotlib.dates.DateLocator` instance) and the
default tick formatter to
:class:`matplotlib.dates.AutoDateFormatter` (if the tick
formatter is not already set to a
:class:`matplotlib.dates.DateFormatter` instance).


Parameters
----------
fmt : string
    The plot format string.

tz : [ *None* | timezone string | :class:`tzinfo` instance]
    The time zone to use in labeling dates. If *None*, defaults to rc
    value.

xdate : boolean
    If *True*, the *x*-axis will be labeled with dates.

ydate : boolean
    If *True*, the *y*-axis will be labeled with dates.


Returns
-------
lines


See Also
--------
matplotlib.dates : helper functions on dates
matplotlib.dates.date2num : how to convert dates to num
matplotlib.dates.num2date : how to convert num to dates
matplotlib.dates.drange : how floating point dates

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### plot\_surface
```py

def plot_surface(self, X, Y, Z, *args, **kwargs)

```



Create a surface plot.

By default it will be colored in shades of a solid color, but it also
supports color mapping by supplying the *cmap* argument.

.. note::

   The *rcount* and *ccount* kwargs, which both default to 50,
   determine the maximum number of samples used in each direction.  If
   the input data is larger, it will be downsampled (by slicing) to
   these numbers of points.

Parameters
----------
X, Y, Z : 2d arrays
    Data values.

rcount, ccount : int
    Maximum number of samples used in each direction.  If the input
    data is larger, it will be downsampled (by slicing) to these
    numbers of points.  Defaults to 50.

    .. versionadded:: 2.0

rstride, cstride : int
    Downsampling stride in each direction.  These arguments are
    mutually exclusive with *rcount* and *ccount*.  If only one of
    *rstride* or *cstride* is set, the other defaults to 10.

    'classic' mode uses a default of ``rstride = cstride = 10`` instead
    of the new default of ``rcount = ccount = 50``.

color : color-like
    Color of the surface patches.

cmap : Colormap
    Colormap of the surface patches.

facecolors : array-like of colors.
    Colors of each individual patch.

norm : Normalize
    Normalization for the colormap.

vmin, vmax : float
    Bounds for the normalization.

shade : bool
    Whether to shade the face colors.

**kwargs :
    Other arguments are forwarded to `~.Poly3DCollection`.


### plot\_trisurf
```py

def plot_trisurf(self, *args, **kwargs)

```



============= ================================================
Argument      Description
============= ================================================
*X*, *Y*, *Z* Data values as 1D arrays
*color*       Color of the surface patches
*cmap*        A colormap for the surface patches.
*norm*        An instance of Normalize to map values to colors
*vmin*        Minimum value to map
*vmax*        Maximum value to map
*shade*       Whether to shade the facecolors
============= ================================================

The (optional) triangulation can be specified in one of two ways;
either::

  plot_trisurf(triangulation, ...)

where triangulation is a :class:`~matplotlib.tri.Triangulation`
object, or::

  plot_trisurf(X, Y, ...)
  plot_trisurf(X, Y, triangles, ...)
  plot_trisurf(X, Y, triangles=triangles, ...)

in which case a Triangulation object will be created.  See
:class:`~matplotlib.tri.Triangulation` for a explanation of
these possibilities.

The remaining arguments are::

  plot_trisurf(..., Z)

where *Z* is the array of values to contour, one per point
in the triangulation.

Other arguments are passed on to
:class:`~mpl_toolkits.mplot3d.art3d.Poly3DCollection`

**Examples:**

.. plot:: gallery/mplot3d/trisurf3d.py
.. plot:: gallery/mplot3d/trisurf3d_2.py

.. versionadded:: 1.2.0
    This plotting function was added for the v1.2.0 release.


### plot\_wireframe
```py

def plot_wireframe(self, X, Y, Z, *args, **kwargs)

```



Plot a 3D wireframe.

.. note::

   The *rcount* and *ccount* kwargs, which both default to 50,
   determine the maximum number of samples used in each direction.  If
   the input data is larger, it will be downsampled (by slicing) to
   these numbers of points.

Parameters
----------
X, Y, Z : 2d arrays
    Data values.

rcount, ccount : int
    Maximum number of samples used in each direction.  If the input
    data is larger, it will be downsampled (by slicing) to these
    numbers of points.  Setting a count to zero causes the data to be
    not sampled in the corresponding direction, producing a 3D line
    plot rather than a wireframe plot.  Defaults to 50.

    .. versionadded:: 2.0

rstride, cstride : int
    Downsampling stride in each direction.  These arguments are
    mutually exclusive with *rcount* and *ccount*.  If only one of
    *rstride* or *cstride* is set, the other defaults to 1.  Setting a
    stride to zero causes the data to be not sampled in the
    corresponding direction, producing a 3D line plot rather than a
    wireframe plot.

    'classic' mode uses a default of ``rstride = cstride = 1`` instead
    of the new default of ``rcount = ccount = 50``.

**kwargs :
    Other arguments are forwarded to `~.Line3DCollection`.


### properties
```py

def properties(self)

```



return a dictionary mapping property name -> value for all Artist props


### psd
```py

def psd(ax, *args, **kwargs)

```



Plot the power spectral density.

Call signature::

  psd(x, NFFT=256, Fs=2, Fc=0, detrend=mlab.detrend_none,
      window=mlab.window_hanning, noverlap=0, pad_to=None,
      sides='default', scale_by_freq=None, return_line=None, **kwargs)

The power spectral density :math:`P_{xx}` by Welch's average
periodogram method.  The vector *x* is divided into *NFFT* length
segments.  Each segment is detrended by function *detrend* and
windowed by function *window*.  *noverlap* gives the length of
the overlap between segments.  The :math:`|\mathrm{fft}(i)|^2`
of each segment :math:`i` are averaged to compute :math:`P_{xx}`,
with a scaling to correct for power loss due to windowing.

If len(*x*) < *NFFT*, it will be zero padded to *NFFT*.

Parameters
----------
x : 1-D array or sequence
    Array or sequence containing the data

Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  This can be different from *NFFT*, which
    specifies the number of data points used.  While not increasing
    the actual resolution of the spectrum (the minimum distance between
    resolvable peaks), this can give more points in the plot,
    allowing for more detail. This corresponds to the *n* parameter
    in the call to fft(). The default is None, which sets *pad_to*
    equal to *NFFT*

NFFT : integer
    The number of data points used in each block for the FFT.
    A power 2 is most efficient.  The default value is 256.
    This should *NOT* be used to get zero padding, or the scaling of the
    result will be incorrect. Use *pad_to* for this instead.

detrend : {'default', 'constant', 'mean', 'linear', 'none'} or callable
    The function applied to each segment before fft-ing,
    designed to remove the mean or linear trend.  Unlike in
    MATLAB, where the *detrend* parameter is a vector, in
    matplotlib is it a function.  The :mod:`~matplotlib.pylab`
    module defines :func:`~matplotlib.pylab.detrend_none`,
    :func:`~matplotlib.pylab.detrend_mean`, and
    :func:`~matplotlib.pylab.detrend_linear`, but you can use
    a custom function as well.  You can also use a string to choose
    one of the functions.  'default', 'constant', and 'mean' call
    :func:`~matplotlib.pylab.detrend_mean`.  'linear' calls
    :func:`~matplotlib.pylab.detrend_linear`.  'none' calls
    :func:`~matplotlib.pylab.detrend_none`.

scale_by_freq : boolean, optional
    Specifies whether the resulting density values should be scaled
    by the scaling frequency, which gives density in units of Hz^-1.
    This allows for integration over the returned frequency values.
    The default is True for MATLAB compatibility.

noverlap : integer
    The number of points of overlap between segments.
    The default value is 0 (no overlap).

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.

return_line : bool
    Whether to include the line object plotted in the returned values.
    Default is False.

Returns
-------
Pxx : 1-D array
    The values for the power spectrum `P_{xx}` before scaling
    (real valued)

freqs : 1-D array
    The frequencies corresponding to the elements in *Pxx*

line : a :class:`~matplotlib.lines.Line2D` instance
    The line created by this function.
    Only returned if *return_line* is True.

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

Notes
-----
For plotting, the power is plotted as
:math:`10\log_{10}(P_{xx})` for decibels, though *Pxx* itself
is returned.

References
----------
Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
John Wiley & Sons (1986)

See Also
--------
:func:`specgram`
    :func:`specgram` differs in the default overlap; in not returning
    the mean of the segment periodograms; in returning the times of the
    segments; and in plotting a colormap instead of a line.

:func:`magnitude_spectrum`
    :func:`magnitude_spectrum` plots the magnitude spectrum.

:func:`csd`
    :func:`csd` plots the spectral density between two signals.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x'.


### quiver
```py

def quiver(self, *args, **kwargs)

```



Plot a 3D field of arrows.

call signatures::

    quiver(X, Y, Z, U, V, W, **kwargs)

Arguments:

    *X*, *Y*, *Z*:
        The x, y and z coordinates of the arrow locations (default is
        tail of arrow; see *pivot* kwarg)

    *U*, *V*, *W*:
        The x, y and z components of the arrow vectors

The arguments could be array-like or scalars, so long as they
they can be broadcast together. The arguments can also be
masked arrays. If an element in any of argument is masked, then
that corresponding quiver element will not be plotted.

Keyword arguments:

    *length*: [1.0 | float]
        The length of each quiver, default to 1.0, the unit is
        the same with the axes

    *arrow_length_ratio*: [0.3 | float]
        The ratio of the arrow head with respect to the quiver,
        default to 0.3

    *pivot*: [ 'tail' | 'middle' | 'tip' ]
        The part of the arrow that is at the grid point; the arrow
        rotates about this point, hence the name *pivot*.
        Default is 'tail'

    *normalize*: [False | True]
        When True, all of the arrows will be the same length. This
        defaults to False, where the arrows will be different lengths
        depending on the values of u,v,w.

Any additional keyword arguments are delegated to
:class:`~matplotlib.collections.LineCollection`


### quiver3D
```py

def quiver3D(self, *args, **kwargs)

```



Plot a 3D field of arrows.

call signatures::

    quiver(X, Y, Z, U, V, W, **kwargs)

Arguments:

    *X*, *Y*, *Z*:
        The x, y and z coordinates of the arrow locations (default is
        tail of arrow; see *pivot* kwarg)

    *U*, *V*, *W*:
        The x, y and z components of the arrow vectors

The arguments could be array-like or scalars, so long as they
they can be broadcast together. The arguments can also be
masked arrays. If an element in any of argument is masked, then
that corresponding quiver element will not be plotted.

Keyword arguments:

    *length*: [1.0 | float]
        The length of each quiver, default to 1.0, the unit is
        the same with the axes

    *arrow_length_ratio*: [0.3 | float]
        The ratio of the arrow head with respect to the quiver,
        default to 0.3

    *pivot*: [ 'tail' | 'middle' | 'tip' ]
        The part of the arrow that is at the grid point; the arrow
        rotates about this point, hence the name *pivot*.
        Default is 'tail'

    *normalize*: [False | True]
        When True, all of the arrows will be the same length. This
        defaults to False, where the arrows will be different lengths
        depending on the values of u,v,w.

Any additional keyword arguments are delegated to
:class:`~matplotlib.collections.LineCollection`


### quiverkey
```py

def quiverkey(self, *args, **kw)

```



Add a key to a quiver plot.

Call signature::

  quiverkey(Q, X, Y, U, label, **kw)

Arguments:

  *Q*:
    The Quiver instance returned by a call to quiver.

  *X*, *Y*:
    The location of the key; additional explanation follows.

  *U*:
    The length of the key

  *label*:
    A string with the length and units of the key

Keyword arguments:

  *angle* = 0
    The angle of the key arrow. Measured in degrees anti-clockwise from the
    x-axis.

  *coordinates* = [ 'axes' | 'figure' | 'data' | 'inches' ]
    Coordinate system and units for *X*, *Y*: 'axes' and 'figure' are
    normalized coordinate systems with 0,0 in the lower left and 1,1
    in the upper right; 'data' are the axes data coordinates (used for
    the locations of the vectors in the quiver plot itself); 'inches'
    is position in the figure in inches, with 0,0 at the lower left
    corner.

  *color*:
    overrides face and edge colors from *Q*.

  *labelpos* = [ 'N' | 'S' | 'E' | 'W' ]
    Position the label above, below, to the right, to the left of the
    arrow, respectively.

  *labelsep*:
    Distance in inches between the arrow and the label.  Default is
    0.1

  *labelcolor*:
    defaults to default :class:`~matplotlib.text.Text` color.

  *fontproperties*:
    A dictionary with keyword arguments accepted by the
    :class:`~matplotlib.font_manager.FontProperties` initializer:
    *family*, *style*, *variant*, *size*, *weight*

Any additional keyword arguments are used to override vector
properties taken from *Q*.

The positioning of the key depends on *X*, *Y*, *coordinates*, and
*labelpos*.  If *labelpos* is 'N' or 'S', *X*, *Y* give the position
of the middle of the key arrow.  If *labelpos* is 'E', *X*, *Y*
positions the head, and if *labelpos* is 'W', *X*, *Y* positions the
tail; in either of these two cases, *X*, *Y* is somewhere in the
middle of the arrow+label key object.


### redraw\_in\_frame
```py

def redraw_in_frame(self)

```



This method can only be used after an initial draw which
caches the renderer.  It is used to efficiently update Axes
data (axis ticks, labels, etc are not updated)


### relim
```py

def relim(self, visible_only=False)

```



Recompute the data limits based on current artists. If you want to
exclude invisible artists from the calculation, set
``visible_only=True``

At present, :class:`~matplotlib.collections.Collection`
instances are not supported.


### remove
```py

def remove(self)

```



Remove the artist from the figure if possible.  The effect
will not be visible until the figure is redrawn, e.g., with
:meth:`matplotlib.axes.Axes.draw_idle`.  Call
:meth:`matplotlib.axes.Axes.relim` to update the axes limits
if desired.

Note: :meth:`~matplotlib.axes.Axes.relim` will not see
collections even if the collection was added to axes with
*autolim* = True.

Note: there is no support for removing the artist's legend entry.


### remove\_callback
```py

def remove_callback(self, oid)

```



Remove a callback based on its *id*.

.. seealso::

    :meth:`add_callback`
       For adding callbacks


### reset\_position
```py

def reset_position(self)

```



Make the original position the active position


### scatter
```py

def scatter(self, xs, ys, zs=0, zdir=u'z', s=20, c=None, depthshade=True, *args, **kwargs)

```



Create a scatter plot.

============  ========================================================
Argument      Description
============  ========================================================
*xs*, *ys*    Positions of data points.
*zs*          Either an array of the same length as *xs* and
              *ys* or a single value to place all points in
              the same plane. Default is 0.
*zdir*        Which direction to use as z ('x', 'y' or 'z')
              when plotting a 2D set.
*s*           Size in points^2.  It is a scalar or an array of the
              same length as *x* and *y*.

*c*           A color. *c* can be a single color format string, or a
              sequence of color specifications of length *N*, or a
              sequence of *N* numbers to be mapped to colors using the
              *cmap* and *norm* specified via kwargs (see below). Note
              that *c* should not be a single numeric RGB or RGBA
              sequence because that is indistinguishable from an array
              of values to be colormapped.  *c* can be a 2-D array in
              which the rows are RGB or RGBA, however, including the
              case of a single row to specify the same color for
              all points.

*depthshade*
              Whether or not to shade the scatter markers to give
              the appearance of depth. Default is *True*.
============  ========================================================

Keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.scatter`.

Returns a :class:`~mpl_toolkits.mplot3d.art3d.Patch3DCollection`


### scatter3D
```py

def scatter3D(self, xs, ys, zs=0, zdir=u'z', s=20, c=None, depthshade=True, *args, **kwargs)

```



Create a scatter plot.

============  ========================================================
Argument      Description
============  ========================================================
*xs*, *ys*    Positions of data points.
*zs*          Either an array of the same length as *xs* and
              *ys* or a single value to place all points in
              the same plane. Default is 0.
*zdir*        Which direction to use as z ('x', 'y' or 'z')
              when plotting a 2D set.
*s*           Size in points^2.  It is a scalar or an array of the
              same length as *x* and *y*.

*c*           A color. *c* can be a single color format string, or a
              sequence of color specifications of length *N*, or a
              sequence of *N* numbers to be mapped to colors using the
              *cmap* and *norm* specified via kwargs (see below). Note
              that *c* should not be a single numeric RGB or RGBA
              sequence because that is indistinguishable from an array
              of values to be colormapped.  *c* can be a 2-D array in
              which the rows are RGB or RGBA, however, including the
              case of a single row to specify the same color for
              all points.

*depthshade*
              Whether or not to shade the scatter markers to give
              the appearance of depth. Default is *True*.
============  ========================================================

Keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.scatter`.

Returns a :class:`~mpl_toolkits.mplot3d.art3d.Patch3DCollection`


### semilogx
```py

def semilogx(self, *args, **kwargs)

```



Make a plot with log scaling on the *x* axis.

Parameters
----------
basex : float, optional
    Base of the *x* logarithm. The scalar should be larger
    than 1.

subsx : array_like, optional
    The location of the minor xticks; *None* defaults to
    autosubs, which depend on the number of decades in the
    plot; see :meth:`~matplotlib.axes.Axes.set_xscale` for
    details.

nonposx : string, optional, {'mask', 'clip'}
    Non-positive values in *x* can be masked as
    invalid, or clipped to a very small positive number.

Returns
-------
`~matplotlib.pyplot.plot`
    Log-scaled plot on the *x* axis.

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

Notes
-----
This function supports all the keyword arguments of
:func:`~matplotlib.pyplot.plot` and
:meth:`matplotlib.axes.Axes.set_xscale`.


### semilogy
```py

def semilogy(self, *args, **kwargs)

```



Make a plot with log scaling on the *y* axis.

Parameters
----------
basey : float, optional
    Base of the *y* logarithm. The scalar should be larger
    than 1.

subsy : array_like, optional
    The location of the minor yticks; *None* defaults to
    autosubs, which depend on the number of decades in the
    plot; see :meth:`~matplotlib.axes.Axes.set_yscale` for
    details.

nonposy : string, optional, {'mask', 'clip'}
    Non-positive values in *y* can be masked as
    invalid, or clipped to a very small positive number.

Returns
-------
`~matplotlib.pyplot.plot`
    Log-scaled plot on the *y* axis.

Other Parameters
----------------
**kwargs :
    Keyword arguments control the :class:`~matplotlib.lines.Line2D`
    properties:

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

Notes
-----
This function supports all the keyword arguments of
:func:`~matplotlib.pyplot.plot` and
:meth:`matplotlib.axes.Axes.set_yscale`.


### set
```py

def set(self, **kwargs)

```



A property batch setter. Pass *kwargs* to set properties.
        


### set\_adjustable
```py

def set_adjustable(self, adjustable)

```



ACCEPTS: [ 'box' | 'datalim' | 'box-forced']


### set\_agg\_filter
```py

def set_agg_filter(self, filter_func)

```



Set the agg filter.

Parameters
----------
filter_func : callable
    A filter function, which takes a (m, n, 3) float array and a dpi
    value, and returns a (m, n, 3) array.

    ..
        ACCEPTS: a filter function, which takes a (m, n, 3) float array
        and a dpi value, and returns a (m, n, 3) array


### set\_alpha
```py

def set_alpha(self, alpha)

```



Set the alpha value used for blending - not supported on
all backends.

Parameters
----------
alpha : float
    ..
        ACCEPTS: float (0.0 transparent through 1.0 opaque)


### set\_anchor
```py

def set_anchor(self, anchor)

```



*anchor*

  =====  ============
  value  description
  =====  ============
  'C'    center
  'SW'   bottom left
  'S'    bottom
  'SE'   bottom right
  'E'    right
  'NE'   top right
  'N'    top
  'NW'   top left
  'W'    left
  =====  ============

..
    ACCEPTS:
    [ 'C' | 'SW' | 'S' | 'SE' | 'E' | 'NE' | 'N' | 'NW' | 'W' ]


### set\_animated
```py

def set_animated(self, b)

```



Set the artist's animation state.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_aspect
```py

def set_aspect(self, aspect, adjustable=None, anchor=None)

```



*aspect*

  ========   ================================================
  value      description
  ========   ================================================
  'auto'     automatic; fill position rectangle with data
  'equal'    same scaling from data to plot units for x and y
   num       a circle will be stretched such that the height
             is num times the width. aspect=1 is the same as
             aspect='equal'.
  ========   ================================================

*adjustable*

  ============   =====================================
  value          description
  ============   =====================================
  'box'          change physical size of axes
  'datalim'      change xlim or ylim
  'box-forced'   same as 'box', but axes can be shared
  ============   =====================================

'box' does not allow axes sharing, as this can cause
unintended side effect. For cases when sharing axes is
fine, use 'box-forced'.

*anchor*

  =====   =====================
  value   description
  =====   =====================
  'C'     centered
  'SW'    lower left corner
  'S'     middle of bottom edge
  'SE'    lower right corner
  etc.
  =====   =====================


### set\_autoscale\_on
```py

def set_autoscale_on(self, b)

```



Set whether autoscaling is applied on plot commands

accepts: [ *True* | *False* ]

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### set\_autoscalex\_on
```py

def set_autoscalex_on(self, b)

```



Set whether autoscaling for the x-axis is applied on plot commands

..
    ACCEPTS: bool

Parameters
----------
b : bool


### set\_autoscaley\_on
```py

def set_autoscaley_on(self, b)

```



Set whether autoscaling for the y-axis is applied on plot commands

..
    ACCEPTS: bool

Parameters
----------
b : bool


### set\_autoscalez\_on
```py

def set_autoscalez_on(self, b)

```



Set whether autoscaling for the z-axis is applied on plot commands

accepts: [ *True* | *False* ]

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### set\_axes\_locator
```py

def set_axes_locator(self, locator)

```



Set the axes locator.

..
    ACCEPTS: a callable object which takes an axes instance and
    renderer and returns a bbox.

Parameters
----------
locator : callable
    A locator function, which takes an axes and a renderer and returns
    a bbox.


### set\_axis\_bgcolor
```py

def set_axis_bgcolor(*args, **kwargs)

```



.. deprecated:: 2.0
    The set_axis_bgcolor function was deprecated in version 2.0. Use set_facecolor instead.

set the axes background color

ACCEPTS: any matplotlib color - see
:func:`~matplotlib.pyplot.colors`


### set\_axis\_off
```py

def set_axis_off(self)

```



### set\_axis\_on
```py

def set_axis_on(self)

```



### set\_axisbelow
```py

def set_axisbelow(self, b)

```



Set whether the axis ticks and gridlines are above or below
most artists

For axes3d objects, this will ignore any settings and just use *True*

ACCEPTS: [ *True* | *False* ]

.. versionadded :: 1.1.0
    This function was added for completeness.


### set\_clip\_box
```py

def set_clip_box(self, clipbox)

```



Set the artist's clip `~.Bbox`.

Parameters
----------
clipbox : `~.Bbox`
    ..
        ACCEPTS: a `~.Bbox` instance


### set\_clip\_on
```py

def set_clip_on(self, b)

```



Set whether artist uses clipping.

When False artists will be visible out side of the axes which
can lead to unexpected results.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_clip\_path
```py

def set_clip_path(self, path, transform=None)

```



Set the artist's clip path, which may be:

- a :class:`~matplotlib.patches.Patch` (or subclass) instance; or
- a :class:`~matplotlib.path.Path` instance, in which case a
  :class:`~matplotlib.transforms.Transform` instance, which will be
  applied to the path before using it for clipping, must be provided;
  or
- ``None``, to remove a previously set clipping path.

For efficiency, if the path happens to be an axis-aligned rectangle,
this method will set the clipping box to the corresponding rectangle
and set the clipping path to ``None``.

ACCEPTS: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None]


### set\_color\_cycle
```py

def set_color_cycle(self, clist)

```



Set the color cycle for any future plot commands on this Axes.

*clist* is a list of mpl color specifiers.

.. deprecated:: 1.5


### set\_contains
```py

def set_contains(self, picker)

```



Replace the contains test used by this artist. The new picker
should be a callable function which determines whether the
artist is hit by the mouse event::

    hit, props = picker(artist, mouseevent)

If the mouse event is over the artist, return *hit* = *True*
and *props* is a dictionary of properties you want returned
with the contains test.

Parameters
----------
picker : callable
    ..
        ACCEPTS: a callable function


### set\_cursor\_props
```py

def set_cursor_props(*args, **kwargs)

```



.. deprecated:: 2.1
    The set_cursor_props function was deprecated in version 2.1.

Set the cursor property as

        Call signature ::

          ax.set_cursor_props(linewidth, color)

        or::

          ax.set_cursor_props((linewidth, color))

        ACCEPTS: a (*float*, *color*) tuple


### set\_facecolor
```py

def set_facecolor(self, color)

```



Set the Axes facecolor.

..
    ACCEPTS: color

Parameters
----------
color : color


### set\_fc
```py

def set_fc(self, color)

```



Set the Axes facecolor.

..
    ACCEPTS: color

Parameters
----------
color : color


### set\_figure
```py

def set_figure(self, fig)

```



Set the `~.Figure` for this `~.Axes`.

..
    ACCEPTS: `~.Figure`

Parameters
----------
fig : `~.Figure`


### set\_frame\_on
```py

def set_frame_on(self, b)

```



Set whether the 3D axes panels are drawn

ACCEPTS: [ *True* | *False* ]

.. versionadded :: 1.1.0


### set\_gid
```py

def set_gid(self, gid)

```



Sets the (group) id for the artist.

Parameters
----------
gid : str
    ..
        ACCEPTS: an id string


### set\_label
```py

def set_label(self, s)

```



Set the label to *s* for auto legend.

Parameters
----------
s : object
    *s* will be converted to a string by calling `str` (`unicode` on
    Py2).

    ..
        ACCEPTS: object


### set\_navigate
```py

def set_navigate(self, b)

```



Set whether the axes responds to navigation toolbar commands

..
    ACCEPTS: bool

Parameters
----------
b : bool


### set\_navigate\_mode
```py

def set_navigate_mode(self, b)

```



Set the navigation toolbar button status;

.. warning::
    this is not a user-API function.


### set\_path\_effects
```py

def set_path_effects(self, path_effects)

```



Set the path effects.

Parameters
----------
path_effects : `~.AbstractPathEffect`
    ..
        ACCEPTS: `~.AbstractPathEffect`


### set\_picker
```py

def set_picker(self, picker)

```



Set the epsilon for picking used by this artist

*picker* can be one of the following:

  * *None*: picking is disabled for this artist (default)

  * A boolean: if *True* then picking will be enabled and the
    artist will fire a pick event if the mouse event is over
    the artist

  * A float: if picker is a number it is interpreted as an
    epsilon tolerance in points and the artist will fire
    off an event if it's data is within epsilon of the mouse
    event.  For some artists like lines and patch collections,
    the artist may provide additional data to the pick event
    that is generated, e.g., the indices of the data within
    epsilon of the pick event

  * A function: if picker is callable, it is a user supplied
    function which determines whether the artist is hit by the
    mouse event::

      hit, props = picker(artist, mouseevent)

    to determine the hit test.  if the mouse event is over the
    artist, return *hit=True* and props is a dictionary of
    properties you want added to the PickEvent attributes.

Parameters
----------
picker : None or bool or float or callable
    ..
        ACCEPTS: [None | bool | float | callable]


### set\_position
```py

def set_position(self, pos, which=u'both')

```



Set the axes position

The expected shape of ``pos`` is::

  pos = [left, bottom, width, height]

in relative 0,1 coords, or *pos* can be a
:class:`~matplotlib.transforms.Bbox`

There are two position variables: one which is ultimately
used, but which may be modified by :meth:`apply_aspect`, and a
second which is the starting point for :meth:`apply_aspect`.

Optional keyword arguments:
  *which*

    ==========   ====================
    value        description
    ==========   ====================
    'active'     to change the first
    'original'   to change the second
    'both'       to change both
    ==========   ====================


### set\_proj\_type
```py

def set_proj_type(self, proj_type)

```



Set the projection type.

Parameters
----------
proj_type : str
    Type of projection, accepts 'persp' and 'ortho'.


### set\_prop\_cycle
```py

def set_prop_cycle(self, *args, **kwargs)

```



Set the property cycle for any future plot commands on this Axes.

set_prop_cycle(arg)
set_prop_cycle(label, itr)
set_prop_cycle(label1=itr1[, label2=itr2[, ...]])

Form 1 simply sets given `Cycler` object.

Form 2 creates and sets  a `Cycler` from a label and an iterable.

Form 3 composes and sets  a `Cycler` as an inner product of the
pairs of keyword arguments. In other words, all of the
iterables are cycled simultaneously, as if through zip().

Parameters
----------
arg : Cycler
    Set the given Cycler.
    Can also be `None` to reset to the cycle defined by the
    current style.

label : str
    The property key. Must be a valid `Artist` property.
    For example, 'color' or 'linestyle'. Aliases are allowed,
    such as 'c' for 'color' and 'lw' for 'linewidth'.

itr : iterable
    Finite-length iterable of the property values. These values
    are validated and will raise a ValueError if invalid.

See Also
--------
    :func:`cycler`      Convenience function for creating your
                        own cyclers.


### set\_rasterization\_zorder
```py

def set_rasterization_zorder(self, z)

```



Parameters
----------
z : float or None
    zorder below which artists are rasterized.  ``None`` means that
    artists do not get rasterized based on zorder.

    ..
        ACCEPTS: float or None


### set\_rasterized
```py

def set_rasterized(self, rasterized)

```



Force rasterized (bitmap) drawing in vector backend output.

Defaults to None, which implies the backend's default behavior.

Parameters
----------
rasterized : bool or None
    ..
        ACCEPTS: bool or None


### set\_sketch\_params
```py

def set_sketch_params(self, scale=None, length=None, randomness=None)

```



Sets the sketch parameters.

Parameters
----------

scale : float, optional
    The amplitude of the wiggle perpendicular to the source
    line, in pixels.  If scale is `None`, or not provided, no
    sketch filter will be provided.

length : float, optional
     The length of the wiggle along the line, in pixels
     (default 128.0)

randomness : float, optional
    The scale factor by which the length is shrunken or
    expanded (default 16.0)

    ..
        ACCEPTS: (scale: float, length: float, randomness: float)


### set\_snap
```py

def set_snap(self, snap)

```



Sets the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

Parameters
----------
snap : bool or None
    ..
        ACCEPTS: bool or None


### set\_title
```py

def set_title(self, label, fontdict=None, loc=u'center', **kwargs)

```



Set a title for the axes.

Set one of the three available axes titles. The available titles
are positioned above the axes in the center, flush with the left
edge, and flush with the right edge.

Parameters
----------
label : str
    Text to use for the title

fontdict : dict
    A dictionary controlling the appearance of the title text,
    the default `fontdict` is::

       {'fontsize': rcParams['axes.titlesize'],
        'fontweight' : rcParams['axes.titleweight'],
        'verticalalignment': 'baseline',
        'horizontalalignment': loc}

loc : {'center', 'left', 'right'}, str, optional
    Which title to set, defaults to 'center'

Returns
-------
text : :class:`~matplotlib.text.Text`
    The matplotlib text instance representing the title

Other Parameters
----------------
**kwargs : `~matplotlib.text.Text` properties
    Other keyword arguments are text properties, see
    :class:`~matplotlib.text.Text` for a list of valid text
    properties.


### set\_top\_view
```py

def set_top_view(self)

```



### set\_transform
```py

def set_transform(self, t)

```



Set the artist transform.

Parameters
----------
t : `~.Transform`
    ..
        ACCEPTS: `~.Transform`


### set\_url
```py

def set_url(self, url)

```



Sets the url for the artist.

Parameters
----------
url : str
    ..
        ACCEPTS: a url string


### set\_visible
```py

def set_visible(self, b)

```



Set the artist's visibility.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_xbound
```py

def set_xbound(self, lower=None, upper=None)

```



Set the lower and upper numerical bounds of the x-axis.

This method will honor axes inversion regardless of parameter order.
It will not change the _autoscaleXon attribute.

..
    ACCEPTS: (lower: float, upper: float)


### set\_xlabel
```py

def set_xlabel(self, xlabel, fontdict=None, labelpad=None, **kwargs)

```



Set the label for the xaxis.

Parameters
----------
xlabel : string
    x label

labelpad : scalar, optional, default: None
    spacing in points between the label and the x-axis

Other Parameters
----------------
**kwargs : `~matplotlib.text.Text` properties

See also
--------
text : for information on how override and the optional args work


### set\_xlim
```py

def set_xlim(self, left=None, right=None, emit=True, auto=False, **kw)

```



Set 3D x limits.

See :meth:`matplotlib.axes.Axes.set_xlim` for full documentation.


### set\_xlim3d
```py

def set_xlim3d(self, left=None, right=None, emit=True, auto=False, **kw)

```



Set 3D x limits.

See :meth:`matplotlib.axes.Axes.set_xlim` for full documentation.


### set\_xmargin
```py

def set_xmargin(self, m)

```



Set padding of X data limits prior to autoscaling.

*m* times the data interval will be added to each
end of that interval before it is used in autoscaling.

accepts: float in range 0 to 1


### set\_xscale
```py

def set_xscale(self, value, **kwargs)

```



Set the x-axis scale.

..
    ACCEPTS: [ 'linear' | 'log' | 'symlog' | 'logit' | ... ]

Parameters
----------
value : {"linear", "log", "symlog", "logit"}
    scaling strategy to apply

Notes
-----
Different kwargs are accepted, depending on the scale. See
the `~matplotlib.scale` module for more information.

See also
--------
matplotlib.scale.LinearScale : linear transfrom

matplotlib.scale.LogTransform : log transform

matplotlib.scale.SymmetricalLogTransform : symlog transform

matplotlib.scale.LogisticTransform : logit transform


    .. versionadded :: 1.1.0
        This function was added, but not tested. Please report any bugs.
    


### set\_xticklabels
```py

def set_xticklabels(self, labels, fontdict=None, minor=False, **kwargs)

```



Set the x-tick labels with list of string labels.

..
    ACCEPTS: list of string labels

Parameters
----------
labels : list of str
    List of string labels.

fontdict : dict, optional
    A dictionary controlling the appearance of the ticklabels.
    The default `fontdict` is::

       {'fontsize': rcParams['axes.titlesize'],
        'fontweight': rcParams['axes.titleweight'],
        'verticalalignment': 'baseline',
        'horizontalalignment': loc}

minor : bool, optional
    Whether to set the minor ticklabels rather than the major ones.

Returns
-------
A list of `~.text.Text` instances.

Other Parameters
-----------------
**kwargs : `~.text.Text` properties.


### set\_xticks
```py

def set_xticks(self, ticks, minor=False)

```



Set the x ticks with list of *ticks*

..
    ACCEPTS: list of tick locations.

Parameters
----------
ticks : list
    List of x-axis tick locations.

minor : bool, optional
    If ``False`` sets major ticks, if ``True`` sets minor ticks.
    Default is ``False``.


### set\_ybound
```py

def set_ybound(self, lower=None, upper=None)

```



Set the lower and upper numerical bounds of the y-axis.
This method will honor axes inversion regardless of parameter order.
It will not change the _autoscaleYon attribute.

..
    ACCEPTS: (lower: float, upper: float)


### set\_ylabel
```py

def set_ylabel(self, ylabel, fontdict=None, labelpad=None, **kwargs)

```



Set the label for the yaxis

Parameters
----------
ylabel : string
    y label

labelpad : scalar, optional, default: None
    spacing in points between the label and the x-axis

Other Parameters
----------------
**kwargs : `~matplotlib.text.Text` properties

See also
--------
text : for information on how override and the optional args work


### set\_ylim
```py

def set_ylim(self, bottom=None, top=None, emit=True, auto=False, **kw)

```



Set 3D y limits.

See :meth:`matplotlib.axes.Axes.set_ylim` for full documentation.


### set\_ylim3d
```py

def set_ylim3d(self, bottom=None, top=None, emit=True, auto=False, **kw)

```



Set 3D y limits.

See :meth:`matplotlib.axes.Axes.set_ylim` for full documentation.


### set\_ymargin
```py

def set_ymargin(self, m)

```



Set padding of Y data limits prior to autoscaling.

*m* times the data interval will be added to each
end of that interval before it is used in autoscaling.

accepts: float in range 0 to 1


### set\_yscale
```py

def set_yscale(self, value, **kwargs)

```



Set the y-axis scale.

..
    ACCEPTS: [ 'linear' | 'log' | 'symlog' | 'logit' | ... ]

Parameters
----------
value : {"linear", "log", "symlog", "logit"}
    scaling strategy to apply

Notes
-----
Different kwargs are accepted, depending on the scale. See
the `~matplotlib.scale` module for more information.

See also
--------
matplotlib.scale.LinearScale : linear transfrom

matplotlib.scale.LogTransform : log transform

matplotlib.scale.SymmetricalLogTransform : symlog transform

matplotlib.scale.LogisticTransform : logit transform


    .. versionadded :: 1.1.0
        This function was added, but not tested. Please report any bugs.
    


### set\_yticklabels
```py

def set_yticklabels(self, labels, fontdict=None, minor=False, **kwargs)

```



Set the y-tick labels with list of strings labels.

..
    ACCEPTS: list of string labels

Parameters
----------
labels : list of str
    list of string labels

fontdict : dict, optional
    A dictionary controlling the appearance of the ticklabels.
    The default `fontdict` is::

       {'fontsize': rcParams['axes.titlesize'],
        'fontweight': rcParams['axes.titleweight'],
        'verticalalignment': 'baseline',
        'horizontalalignment': loc}

minor : bool, optional
    Whether to set the minor ticklabels rather than the major ones.

Returns
-------
A list of `~.text.Text` instances.

Other Parameters
----------------
**kwargs : `~.text.Text` properties.


### set\_yticks
```py

def set_yticks(self, ticks, minor=False)

```



Set the y ticks with list of *ticks*

..
    ACCEPTS: list of tick locations.

Parameters
----------
ticks : sequence
    List of y-axis tick locations

minor : bool, optional
    If ``False`` sets major ticks, if ``True`` sets minor ticks.
    Default is ``False``.


### set\_zbound
```py

def set_zbound(self, lower=None, upper=None)

```



Set the lower and upper numerical bounds of the z-axis.
This method will honor axes inversion regardless of parameter order.
It will not change the :attr:`_autoscaleZon` attribute.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### set\_zlabel
```py

def set_zlabel(self, zlabel, fontdict=None, labelpad=None, **kwargs)

```



Set zlabel.  See doc for :meth:`set_ylabel` for description.


### set\_zlim
```py

def set_zlim(self, bottom=None, top=None, emit=True, auto=False, **kw)

```



Set 3D z limits.

See :meth:`matplotlib.axes.Axes.set_ylim` for full documentation


### set\_zlim3d
```py

def set_zlim3d(self, bottom=None, top=None, emit=True, auto=False, **kw)

```



Set 3D z limits.

See :meth:`matplotlib.axes.Axes.set_ylim` for full documentation


### set\_zmargin
```py

def set_zmargin(self, m)

```



Set padding of Z data limits prior to autoscaling.

*m* times the data interval will be added to each
end of that interval before it is used in autoscaling.

accepts: float in range 0 to 1

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### set\_zorder
```py

def set_zorder(self, level)

```



Set the zorder for the artist.  Artists with lower zorder
values are drawn first.

Parameters
----------
level : float
    ..
        ACCEPTS: float


### set\_zscale
```py

def set_zscale(self, value, **kwargs)

```



Set the scaling of the z-axis: u'linear' | u'log' | u'logit' | u'symlog'

ACCEPTS: [u'linear' | u'log' | u'logit' | u'symlog']

Different kwargs are accepted, depending on the scale:
    'linear'

        


    'log'

        *basex*/*basey*:
           The base of the logarithm
        
        *nonposx*/*nonposy*: ['mask' | 'clip' ]
          non-positive values in *x* or *y* can be masked as
          invalid, or clipped to a very small positive number
        
        *subsx*/*subsy*:
           Where to place the subticks between each major tick.
           Should be a sequence of integers.  For example, in a log10
           scale: ``[2, 3, 4, 5, 6, 7, 8, 9]``
        
           will place 8 logarithmically spaced minor ticks between
           each major tick.


    'logit'

        *nonpos*: ['mask' | 'clip' ]
          values beyond ]0, 1[ can be masked as invalid, or clipped to a number
          very close to 0 or 1


    'symlog'

        *basex*/*basey*:
           The base of the logarithm
        
        *linthreshx*/*linthreshy*:
          A single float which defines the range (-*x*, *x*), within
          which the plot is linear. This avoids having the plot go to
          infinity around zero.
        
        *subsx*/*subsy*:
           Where to place the subticks between each major tick.
           Should be a sequence of integers.  For example, in a log10
           scale: ``[2, 3, 4, 5, 6, 7, 8, 9]``
        
           will place 8 logarithmically spaced minor ticks between
           each major tick.
        
        *linscalex*/*linscaley*:
           This allows the linear range (-*linthresh* to *linthresh*)
           to be stretched relative to the logarithmic range.  Its
           value is the number of decades to use for each half of the
           linear range.  For example, when *linscale* == 1.0 (the
           default), the space used for the positive and negative
           halves of the linear range will be equal to one decade in
           the logarithmic range.

.. note ::
    Currently, Axes3D objects only supports linear scales.
    Other scales may or may not work, and support for these
    is improving with each release.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### set\_zticklabels
```py

def set_zticklabels(self, *args, **kwargs)

```



Set z-axis tick labels.
See :meth:`matplotlib.axes.Axes.set_yticklabels` for more details.

.. note::
    Minor ticks are not supported by Axes3D objects.

.. versionadded:: 1.1.0


### set\_zticks
```py

def set_zticks(self, *args, **kwargs)

```



Set z-axis tick locations.
See :meth:`matplotlib.axes.Axes.set_yticks` for more details.

.. note::
    Minor ticks are not supported.

.. versionadded:: 1.1.0


### specgram
```py

def specgram(ax, *args, **kwargs)

```



Plot a spectrogram.

Call signature::

  specgram(x, NFFT=256, Fs=2, Fc=0, detrend=mlab.detrend_none,
           window=mlab.window_hanning, noverlap=128,
           cmap=None, xextent=None, pad_to=None, sides='default',
           scale_by_freq=None, mode='default', scale='default',
           **kwargs)

Compute and plot a spectrogram of data in *x*.  Data are split into
*NFFT* length segments and the spectrum of each section is
computed.  The windowing function *window* is applied to each
segment, and the amount of overlap of each segment is
specified with *noverlap*. The spectrogram is plotted as a colormap
(using imshow).

Parameters
----------
x : 1-D array or sequence
    Array or sequence containing the data.

Fs : scalar
    The sampling frequency (samples per time unit).  It is used
    to calculate the Fourier frequencies, freqs, in cycles per time
    unit. The default value is 2.

window : callable or ndarray
    A function or a vector of length *NFFT*. To create window
    vectors see :func:`window_hanning`, :func:`window_none`,
    :func:`numpy.blackman`, :func:`numpy.hamming`,
    :func:`numpy.bartlett`, :func:`scipy.signal`,
    :func:`scipy.signal.get_window`, etc. The default is
    :func:`window_hanning`.  If a function is passed as the
    argument, it must take a data segment as an argument and
    return the windowed version of the segment.

sides : [ 'default' | 'onesided' | 'twosided' ]
    Specifies which sides of the spectrum to return.  Default gives the
    default behavior, which returns one-sided for real data and both
    for complex data.  'onesided' forces the return of a one-sided
    spectrum, while 'twosided' forces two-sided.

pad_to : integer
    The number of points to which the data segment is padded when
    performing the FFT.  This can be different from *NFFT*, which
    specifies the number of data points used.  While not increasing
    the actual resolution of the spectrum (the minimum distance between
    resolvable peaks), this can give more points in the plot,
    allowing for more detail. This corresponds to the *n* parameter
    in the call to fft(). The default is None, which sets *pad_to*
    equal to *NFFT*

NFFT : integer
    The number of data points used in each block for the FFT.
    A power 2 is most efficient.  The default value is 256.
    This should *NOT* be used to get zero padding, or the scaling of the
    result will be incorrect. Use *pad_to* for this instead.

detrend : {'default', 'constant', 'mean', 'linear', 'none'} or callable
    The function applied to each segment before fft-ing,
    designed to remove the mean or linear trend.  Unlike in
    MATLAB, where the *detrend* parameter is a vector, in
    matplotlib is it a function.  The :mod:`~matplotlib.pylab`
    module defines :func:`~matplotlib.pylab.detrend_none`,
    :func:`~matplotlib.pylab.detrend_mean`, and
    :func:`~matplotlib.pylab.detrend_linear`, but you can use
    a custom function as well.  You can also use a string to choose
    one of the functions.  'default', 'constant', and 'mean' call
    :func:`~matplotlib.pylab.detrend_mean`.  'linear' calls
    :func:`~matplotlib.pylab.detrend_linear`.  'none' calls
    :func:`~matplotlib.pylab.detrend_none`.

scale_by_freq : boolean, optional
    Specifies whether the resulting density values should be scaled
    by the scaling frequency, which gives density in units of Hz^-1.
    This allows for integration over the returned frequency values.
    The default is True for MATLAB compatibility.

mode : [ 'default' | 'psd' | 'magnitude' | 'angle' | 'phase' ]
    What sort of spectrum to use.  Default is 'psd', which takes
    the power spectral density.  'complex' returns the complex-valued
    frequency spectrum.  'magnitude' returns the magnitude spectrum.
    'angle' returns the phase spectrum without unwrapping.  'phase'
    returns the phase spectrum with unwrapping.

noverlap : integer
    The number of points of overlap between blocks.  The
    default value is 128.

scale : [ 'default' | 'linear' | 'dB' ]
    The scaling of the values in the *spec*.  'linear' is no scaling.
    'dB' returns the values in dB scale.  When *mode* is 'psd',
    this is dB power (10 * log10).  Otherwise this is dB amplitude
    (20 * log10). 'default' is 'dB' if *mode* is 'psd' or
    'magnitude' and 'linear' otherwise.  This must be 'linear'
    if *mode* is 'angle' or 'phase'.

Fc : integer
    The center frequency of *x* (defaults to 0), which offsets
    the x extents of the plot to reflect the frequency range used
    when a signal is acquired and then filtered and downsampled to
    baseband.

cmap :
    A :class:`matplotlib.colors.Colormap` instance; if *None*, use
    default determined by rc

xextent : [None | (xmin, xmax)]
    The image extent along the x-axis. The default sets *xmin* to the
    left border of the first bin (*spectrum* column) and *xmax* to the
    right border of the last bin. Note that for *noverlap>0* the width
    of the bins is smaller than those of the segments.

**kwargs :
    Additional kwargs are passed on to imshow which makes the
    specgram image

Notes
-----
    *detrend* and *scale_by_freq* only apply when *mode* is set to
    'psd'

Returns
-------
spectrum : 2-D array
    Columns are the periodograms of successive segments.

freqs : 1-D array
    The frequencies corresponding to the rows in *spectrum*.

t : 1-D array
    The times corresponding to midpoints of segments (i.e., the columns
    in *spectrum*).

im : instance of class :class:`~matplotlib.image.AxesImage`
    The image created by imshow containing the spectrogram

See Also
--------
:func:`psd`
    :func:`psd` differs in the default overlap; in returning the mean
    of the segment periodograms; in not returning times; and in
    generating a line plot instead of colormap.

:func:`magnitude_spectrum`
    A single spectrum, similar to having a single segment when *mode*
    is 'magnitude'. Plots a line instead of a colormap.

:func:`angle_spectrum`
    A single spectrum, similar to having a single segment when *mode*
    is 'angle'. Plots a line instead of a colormap.

:func:`phase_spectrum`
    A single spectrum, similar to having a single segment when *mode*
    is 'phase'. Plots a line instead of a colormap.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x'.


### spy
```py

def spy(self, Z, precision=0, marker=None, markersize=None, aspect=u'equal', origin=u'upper', **kwargs)

```



Plot the sparsity pattern on a 2-D array.

``spy(Z)`` plots the sparsity pattern of the 2-D array *Z*.

Parameters
----------

Z : sparse array (n, m)
    The array to be plotted.

precision : float, optional, default: 0
    If *precision* is 0, any non-zero value will be plotted; else,
    values of :math:`|Z| > precision` will be plotted.

    For :class:`scipy.sparse.spmatrix` instances, there is a special
    case: if *precision* is 'present', any value present in the array
    will be plotted, even if it is identically zero.

origin : ["upper", "lower"], optional, default: "upper"
    Place the [0,0] index of the array in the upper left or lower left
    corner of the axes.

aspect : ['auto' | 'equal' | scalar], optional, default: "equal"

    If 'equal', and `extent` is None, changes the axes aspect ratio to
    match that of the image. If `extent` is not `None`, the axes
    aspect ratio is changed to match that of the extent.


    If 'auto', changes the image aspect ratio to match that of the
    axes.

    If None, default to rc ``image.aspect`` value.

Two plotting styles are available: image or marker. Both
are available for full arrays, but only the marker style
works for :class:`scipy.sparse.spmatrix` instances.

If *marker* and *markersize* are *None*, an image will be
returned and any remaining kwargs are passed to
:func:`~matplotlib.pyplot.imshow`; else, a
:class:`~matplotlib.lines.Line2D` object will be returned with
the value of marker determining the marker type, and any
remaining kwargs passed to the
:meth:`~matplotlib.axes.Axes.plot` method.

If *marker* and *markersize* are *None*, useful kwargs include:

* *cmap*
* *alpha*

See also
--------
imshow : for image options.
plot : for plotting options


### stackplot
```py

def stackplot(ax, *args, **kwargs)

```



Draws a stacked area plot.

*x* : 1d array of dimension N

*y* : 2d array of dimension MxN, OR any number 1d arrays each of dimension
      1xN. The data is assumed to be unstacked. Each of the following
      calls is legal::

        stackplot(x, y)               # where y is MxN
        stackplot(x, y1, y2, y3, y4)  # where y1, y2, y3, y4, are all 1xNm

Keyword arguments:

*baseline* : ['zero', 'sym', 'wiggle', 'weighted_wiggle']
            Method used to calculate the baseline. 'zero' is just a
            simple stacked plot. 'sym' is symmetric around zero and
            is sometimes called `ThemeRiver`.  'wiggle' minimizes the
            sum of the squared slopes. 'weighted_wiggle' does the
            same but weights to account for size of each layer.
            It is also called `Streamgraph`-layout. More details
            can be found at http://leebyron.com/streamgraph/.


*labels* : A list or tuple of labels to assign to each data series.


*colors* : A list or tuple of colors. These will be cycled through and
           used to colour the stacked areas.
           All other keyword arguments are passed to
           :func:`~matplotlib.Axes.fill_between`

Returns *r* : A list of
:class:`~matplotlib.collections.PolyCollection`, one for each
element in the stacked area plot.


### start\_pan
```py

def start_pan(self, x, y, button)

```



Called when a pan operation has started.

*x*, *y* are the mouse coordinates in display coords.
button is the mouse button number:

* 1: LEFT
* 2: MIDDLE
* 3: RIGHT

.. note::

    Intended to be overridden by new projection types.


### stem
```py

def stem(ax, *args, **kwargs)

```



Create a stem plot.

Call signatures::

  stem(y, linefmt='b-', markerfmt='bo', basefmt='r-')
  stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')

A stem plot plots vertical lines (using *linefmt*) at each *x*
location from the baseline to *y*, and places a marker there
using *markerfmt*.  A horizontal line at 0 is plotted using
*basefmt*.

If no *x* values are provided, the default is (0, 1, ..., len(y) - 1)

Return value is a tuple (*markerline*, *stemlines*,
*baseline*). See :class:`~matplotlib.container.StemContainer`

.. seealso::
    This
    `document <http://www.mathworks.com/help/techdoc/ref/stem.html>`_
    for details.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All positional and all keyword arguments.


### step
```py

def step(ax, *args, **kwargs)

```



Make a step plot.

Parameters
----------
x : array_like
    1-D sequence, and it is assumed, but not checked,
    that it is uniformly increasing.

y : array_like
    1-D sequence

Returns
-------
list
    List of lines that were added.

Other Parameters
----------------
where : [ 'pre' | 'post' | 'mid'  ]
    If 'pre' (the default), the interval from
    ``x[i]`` to ``x[i+1]`` has level ``y[i+1]``.

    If 'post', that interval has level ``y[i]``.

    If 'mid', the jumps in *y* occur half-way between the
    *x*-values.

Notes
-----
Additional parameters are the same as those for
:func:`~matplotlib.pyplot.plot`.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### streamplot
```py

def streamplot(ax, *args, **kwargs)

```



Draws streamlines of a vector flow.

*x*, *y* : 1d arrays
    an *evenly spaced* grid.
*u*, *v* : 2d arrays
    x and y-velocities. Number of rows should match length of y, and
    the number of columns should match x.
*density* : float or 2-tuple
    Controls the closeness of streamlines. When `density = 1`, the domain
    is divided into a 30x30 grid---*density* linearly scales this grid.
    Each cell in the grid can have, at most, one traversing streamline.
    For different densities in each direction, use [density_x, density_y].
*linewidth* : numeric or 2d array
    vary linewidth when given a 2d array with the same shape as velocities.
*color* : matplotlib color code, or 2d array
    Streamline color. When given an array with the same shape as
    velocities, *color* values are converted to colors using *cmap*.
*cmap* : :class:`~matplotlib.colors.Colormap`
    Colormap used to plot streamlines and arrows. Only necessary when using
    an array input for *color*.
*norm* : :class:`~matplotlib.colors.Normalize`
    Normalize object used to scale luminance data to 0, 1. If None, stretch
    (min, max) to (0, 1). Only necessary when *color* is an array.
*arrowsize* : float
    Factor scale arrow size.
*arrowstyle* : str
    Arrow style specification.
    See :class:`~matplotlib.patches.FancyArrowPatch`.
*minlength* : float
    Minimum length of streamline in axes coordinates.
*start_points*: Nx2 array
    Coordinates of starting points for the streamlines.
    In data coordinates, the same as the ``x`` and ``y`` arrays.
*zorder* : int
    any number
*maxlength* : float
    Maximum length of streamline in axes coordinates.
*integration_direction* : ['forward', 'backward', 'both']
    Integrate the streamline in forward, backward or both directions.

Returns:

    *stream_container* : StreamplotSet
        Container object with attributes

            - lines: `matplotlib.collections.LineCollection` of streamlines

            - arrows: collection of `matplotlib.patches.FancyArrowPatch`
              objects representing arrows half-way along stream
              lines.

        This container will probably change in the future to allow changes
        to the colormap, alpha, etc. for both lines and arrows, but these
        changes should be backward compatible.


### table
```py

def table(self, **kwargs)

```



Add a table to the current axes.

Call signature::

  table(cellText=None, cellColours=None,
        cellLoc='right', colWidths=None,
        rowLabels=None, rowColours=None, rowLoc='left',
        colLabels=None, colColours=None, colLoc='center',
        loc='bottom', bbox=None):

Returns a :class:`matplotlib.table.Table` instance. Either `cellText`
or `cellColours` must be provided. For finer grained control over
tables, use the :class:`~matplotlib.table.Table` class and add it to
the axes with :meth:`~matplotlib.axes.Axes.add_table`.

Thanks to John Gill for providing the class and table.

kwargs control the :class:`~matplotlib.table.Table`
properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  contains: a callable function 
  figure: a `~.Figure` instance 
  fontsize: a float in points 
  gid: an id string 
  label: object 
  path_effects: `~.AbstractPathEffect` 
  picker: [None | bool | float | callable] 
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  transform: `~.Transform` 
  url: a url string 
  visible: bool 
  zorder: float 


### text
```py

def text(self, x, y, z, s, zdir=None, **kwargs)

```



Add text to the plot. kwargs will be passed on to Axes.text,
except for the `zdir` keyword, which sets the direction to be
used as the z direction.


### text2D
```py

def text2D(self, x, y, s, fontdict=None, withdash=False, **kwargs)

```



Add text to the axes.

Add text in string `s` to axis at location `x`, `y`, data
coordinates.

Parameters
----------
x, y : scalars
    data coordinates

s : string
    text

fontdict : dictionary, optional, default: None
    A dictionary to override the default text properties. If fontdict
    is None, the defaults are determined by your rc parameters.

withdash : boolean, optional, default: False
    Creates a `~matplotlib.text.TextWithDash` instance instead of a
    `~matplotlib.text.Text` instance.

Other Parameters
----------------
**kwargs : `~matplotlib.text.Text` properties.
    Other miscellaneous text parameters.

Examples
--------
Individual keyword arguments can be used to override any given
parameter::

    >>> text(x, y, s, fontsize=12)

The default transform specifies that text is in data coords,
alternatively, you can specify text in axis coords (0,0 is
lower-left and 1,1 is upper-right).  The example below places
text in the center of the axes::

    >>> text(0.5, 0.5,'matplotlib', horizontalalignment='center',
    ...      verticalalignment='center',
    ...      transform=ax.transAxes)

You can put a rectangular box around the text instance (e.g., to
set a background color) by using the keyword `bbox`.  `bbox` is
a dictionary of `~matplotlib.patches.Rectangle`
properties.  For example::

    >>> text(x, y, s, bbox=dict(facecolor='red', alpha=0.5))


### text3D
```py

def text3D(self, x, y, z, s, zdir=None, **kwargs)

```



Add text to the plot. kwargs will be passed on to Axes.text,
except for the `zdir` keyword, which sets the direction to be
used as the z direction.


### tick\_params
```py

def tick_params(self, axis=u'both', **kwargs)

```



Convenience method for changing the appearance of ticks and
tick labels.

See :meth:`matplotlib.axes.Axes.tick_params` for more complete
documentation.

The only difference is that setting *axis* to 'both' will
mean that the settings are applied to all three axes. Also,
the *axis* parameter also accepts a value of 'z', which
would mean to apply to only the z-axis.

Also, because of how Axes3D objects are drawn very differently
from regular 2D axes, some of these settings may have
ambiguous meaning.  For simplicity, the 'z' axis will
accept settings as if it was like the 'y' axis.

.. note::
    While this function is currently implemented, the core part
    of the Axes3D object may ignore some of these settings.
    Future releases will fix this. Priority will be given to
    those who file bugs.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### ticklabel\_format
```py

def ticklabel_format(self, **kwargs)

```



Convenience method for manipulating the ScalarFormatter
used by default for linear axes in Axed3D objects.

See :meth:`matplotlib.axes.Axes.ticklabel_format` for full
documentation.  Note that this version applies to all three
axes of the Axes3D object.  Therefore, the *axis* argument
will also accept a value of 'z' and the value of 'both' will
apply to all three axes.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### tricontour
```py

def tricontour(self, *args, **kwargs)

```



Create a 3D contour plot.

==========  ================================================
Argument    Description
==========  ================================================
*X*, *Y*,   Data values as numpy.arrays
*Z*
*extend3d*  Whether to extend contour in 3D (default: False)
*stride*    Stride (step size) for extending contour
*zdir*      The direction to use: x, y or z (default)
*offset*    If specified plot a projection of the contour
            lines on this position in plane normal to zdir
==========  ================================================

Other keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.tricontour`

Returns a :class:`~matplotlib.axes.Axes.contour`

.. versionchanged:: 1.3.0
    Added support for custom triangulations

EXPERIMENTAL:  This method currently produces incorrect output due to a
longstanding bug in 3D PolyCollection rendering.


### tricontourf
```py

def tricontourf(self, *args, **kwargs)

```



Create a 3D contourf plot.

==========  ================================================
Argument    Description
==========  ================================================
*X*, *Y*,   Data values as numpy.arrays
*Z*
*zdir*      The direction to use: x, y or z (default)
*offset*    If specified plot a projection of the contour
            lines on this position in plane normal to zdir
==========  ================================================

Other keyword arguments are passed on to
:func:`~matplotlib.axes.Axes.tricontour`

Returns a :class:`~matplotlib.axes.Axes.contour`

.. versionchanged :: 1.3.0
    Added support for custom triangulations

EXPERIMENTAL:  This method currently produces incorrect output due to a
longstanding bug in 3D PolyCollection rendering.


### tripcolor
```py

def tripcolor(self, *args, **kwargs)

```



Create a pseudocolor plot of an unstructured triangular grid.

The triangulation can be specified in one of two ways; either::

  tripcolor(triangulation, ...)

where triangulation is a :class:`matplotlib.tri.Triangulation`
object, or

::

  tripcolor(x, y, ...)
  tripcolor(x, y, triangles, ...)
  tripcolor(x, y, triangles=triangles, ...)
  tripcolor(x, y, mask=mask, ...)
  tripcolor(x, y, triangles, mask=mask, ...)

in which case a Triangulation object will be created.  See
:class:`~matplotlib.tri.Triangulation` for a explanation of these
possibilities.

The next argument must be *C*, the array of color values, either
one per point in the triangulation if color values are defined at
points, or one per triangle in the triangulation if color values
are defined at triangles. If there are the same number of points
and triangles in the triangulation it is assumed that color
values are defined at points; to force the use of color values at
triangles use the kwarg ``facecolors=C`` instead of just ``C``.

*shading* may be 'flat' (the default) or 'gouraud'. If *shading*
is 'flat' and C values are defined at points, the color values
used for each triangle are from the mean C of the triangle's
three points. If *shading* is 'gouraud' then color values must be
defined at points.

The remaining kwargs are the same as for
:meth:`~matplotlib.axes.Axes.pcolor`.


### triplot
```py

def triplot(self, *args, **kwargs)

```



Draw a unstructured triangular grid as lines and/or markers.

The triangulation to plot can be specified in one of two ways;
either::

  triplot(triangulation, ...)

where triangulation is a :class:`matplotlib.tri.Triangulation`
object, or

::

  triplot(x, y, ...)
  triplot(x, y, triangles, ...)
  triplot(x, y, triangles=triangles, ...)
  triplot(x, y, mask=mask, ...)
  triplot(x, y, triangles, mask=mask, ...)

in which case a Triangulation object will be created.  See
:class:`~matplotlib.tri.Triangulation` for a explanation of these
possibilities.

The remaining args and kwargs are the same as for
:meth:`~matplotlib.axes.Axes.plot`.

Return a list of 2 :class:`~matplotlib.lines.Line2D` containing
respectively:

    - the lines plotted for triangles edges
    - the markers plotted for triangles nodes


### tunit\_cube
```py

def tunit_cube(self, vals=None, M=None)

```



### tunit\_edges
```py

def tunit_edges(self, vals=None, M=None)

```



### twinx
```py

def twinx(self)

```



Create a twin Axes sharing the xaxis

Create a new Axes instance with an invisible x-axis and an independent
y-axis positioned opposite to the original one (i.e. at right). The
x-axis autoscale setting will be inherited from the original Axes.
To ensure that the tick marks of both y-axes align, see
`~matplotlib.ticker.LinearLocator`

Returns
-------
ax_twin : Axes
    The newly created Axes instance

Notes
-----
For those who are 'picking' artists while using twinx, pick
events are only called for the artists in the top-most axes.


### twiny
```py

def twiny(self)

```



Create a twin Axes sharing the yaxis

Create a new Axes instance with an invisible y-axis and an independent
x-axis positioned opposite to the original one (i.e. at top). The
y-axis autoscale setting will be inherited from the original Axes.
To ensure that the tick marks of both x-axes align, see
`~matplotlib.ticker.LinearLocator`

Returns
-------
ax_twin : Axes
    The newly created Axes instance

Notes
-----
For those who are 'picking' artists while using twiny, pick
events are only called for the artists in the top-most axes.


### unit\_cube
```py

def unit_cube(self, vals=None)

```



### update
```py

def update(self, props)

```



Update this artist's properties from the dictionary *prop*.


### update\_datalim
```py

def update_datalim(self, xys, **kwargs)

```



### update\_datalim\_bounds
```py

def update_datalim_bounds(self, bounds)

```



Update the datalim to include the given
:class:`~matplotlib.transforms.Bbox` *bounds*


### update\_datalim\_numerix
```py

def update_datalim_numerix(*args, **kwargs)

```



.. deprecated:: 2.0
    The update_datalim_numerix function was deprecated in version 2.0. Use update_datalim instead.

Update the data lim bbox with seq of xy tups


### update\_from
```py

def update_from(self, other)

```



Copy properties from *other* to *self*.


### view\_init
```py

def view_init(self, elev=None, azim=None)

```



Set the elevation and azimuth of the axes.

This can be used to rotate the axes programatically.

'elev' stores the elevation angle in the z plane.
'azim' stores the azimuth angle in the x,y plane.

if elev or azim are None (default), then the initial value
is used which was specified in the :class:`Axes3D` constructor.


### violin
```py

def violin(self, vpstats, positions=None, vert=True, widths=0.5, showmeans=False, showextrema=True, showmedians=False)

```



Drawing function for violin plots.

Draw a violin plot for each column of `vpstats`. Each filled area
extends to represent the entire data range, with optional lines at the
mean, the median, the minimum, and the maximum.

Parameters
----------

vpstats : list of dicts
  A list of dictionaries containing stats for each violin plot.
  Required keys are:

  - ``coords``: A list of scalars containing the coordinates that
    the violin's kernel density estimate were evaluated at.

  - ``vals``: A list of scalars containing the values of the
    kernel density estimate at each of the coordinates given
    in *coords*.

  - ``mean``: The mean value for this violin's dataset.

  - ``median``: The median value for this violin's dataset.

  - ``min``: The minimum value for this violin's dataset.

  - ``max``: The maximum value for this violin's dataset.

positions : array-like, default = [1, 2, ..., n]
  Sets the positions of the violins. The ticks and limits are
  automatically set to match the positions.

vert : bool, default = True.
  If true, plots the violins veritcally.
  Otherwise, plots the violins horizontally.

widths : array-like, default = 0.5
  Either a scalar or a vector that sets the maximal width of
  each violin. The default is 0.5, which uses about half of the
  available horizontal space.

showmeans : bool, default = False
  If true, will toggle rendering of the means.

showextrema : bool, default = True
  If true, will toggle rendering of the extrema.

showmedians : bool, default = False
  If true, will toggle rendering of the medians.

Returns
-------
result : dict
  A dictionary mapping each component of the violinplot to a
  list of the corresponding collection instances created. The
  dictionary has the following keys:

    - ``bodies``: A list of the
      :class:`matplotlib.collections.PolyCollection` instances
      containing the filled area of each violin.

    - ``cmeans``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the mean values of each of the
      violin's distribution.

    - ``cmins``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the bottom of each violin's
      distribution.

    - ``cmaxes``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the top of each violin's
      distribution.

    - ``cbars``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the centers of each violin's
      distribution.

    - ``cmedians``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the median values of each of the
      violin's distribution.


### violinplot
```py

def violinplot(ax, *args, **kwargs)

```



Make a violin plot.

Make a violin plot for each column of *dataset* or each vector in
sequence *dataset*.  Each filled area extends to represent the
entire data range, with optional lines at the mean, the median,
the minimum, and the maximum.

Parameters
----------
dataset : Array or a sequence of vectors.
  The input data.

positions : array-like, default = [1, 2, ..., n]
  Sets the positions of the violins. The ticks and limits are
  automatically set to match the positions.

vert : bool, default = True.
  If true, creates a vertical violin plot.
  Otherwise, creates a horizontal violin plot.

widths : array-like, default = 0.5
  Either a scalar or a vector that sets the maximal width of
  each violin. The default is 0.5, which uses about half of the
  available horizontal space.

showmeans : bool, default = False
  If `True`, will toggle rendering of the means.

showextrema : bool, default = True
  If `True`, will toggle rendering of the extrema.

showmedians : bool, default = False
  If `True`, will toggle rendering of the medians.

points : scalar, default = 100
  Defines the number of points to evaluate each of the
  gaussian kernel density estimations at.

bw_method : str, scalar or callable, optional
  The method used to calculate the estimator bandwidth.  This can be
  'scott', 'silverman', a scalar constant or a callable.  If a
  scalar, this will be used directly as `kde.factor`.  If a
  callable, it should take a `GaussianKDE` instance as its only
  parameter and return a scalar. If None (default), 'scott' is used.

Returns
-------

result : dict
  A dictionary mapping each component of the violinplot to a
  list of the corresponding collection instances created. The
  dictionary has the following keys:

    - ``bodies``: A list of the
      :class:`matplotlib.collections.PolyCollection` instances
      containing the filled area of each violin.

    - ``cmeans``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the mean values of each of the
      violin's distribution.

    - ``cmins``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the bottom of each violin's
      distribution.

    - ``cmaxes``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the top of each violin's
      distribution.

    - ``cbars``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the centers of each violin's
      distribution.

    - ``cmedians``: A
      :class:`matplotlib.collections.LineCollection` instance
      created to identify the median values of each of the
      violin's distribution.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'dataset'.


### vlines
```py

def vlines(ax, *args, **kwargs)

```



Plot vertical lines.

Plot vertical lines at each `x` from `ymin` to `ymax`.

Parameters
----------
x : scalar or 1D array_like
    x-indexes where to plot the lines.

ymin, ymax : scalar or 1D array_like
    Respective beginning and end of each line. If scalars are
    provided, all lines will have same length.

colors : array_like of colors, optional, default: 'k'

linestyles : ['solid' | 'dashed' | 'dashdot' | 'dotted'], optional

label : string, optional, default: ''

Returns
-------
lines : `~matplotlib.collections.LineCollection`

Other Parameters
----------------
**kwargs : `~matplotlib.collections.LineCollection` properties.

See also
--------
hlines : horizontal lines
axvline: vertical line across the axes

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'colors', 'x', 'ymax', 'ymin'.


### voxels
```py

def voxels(self, *args, **kwargs)

```



ax.voxels([x, y, z,] /, filled, **kwargs)

Plot a set of filled voxels

All voxels are plotted as 1x1x1 cubes on the axis, with filled[0,0,0]
placed with its lower corner at the origin. Occluded faces are not
plotted.

Call signatures::

    voxels(filled, facecolors=fc, edgecolors=ec, **kwargs)
    voxels(x, y, z, filled, facecolors=fc, edgecolors=ec, **kwargs)

.. versionadded:: 2.1

Parameters
----------
filled : 3D np.array of bool
    A 3d array of values, with truthy values indicating which voxels
    to fill

x, y, z : 3D np.array, optional
    The coordinates of the corners of the voxels. This should broadcast
    to a shape one larger in every dimension than the shape of `filled`.
    These can be used to plot non-cubic voxels.

    If not specified, defaults to increasing integers along each axis,
    like those returned by :func:`~numpy.indices`.
    As indicated by the ``/`` in the function signature, these arguments
    can only be passed positionally.

facecolors, edgecolors : array_like, optional
    The color to draw the faces and edges of the voxels. Can only be
    passed as keyword arguments.
    This parameter can be:

      - A single color value, to color all voxels the same color. This
        can be either a string, or a 1D rgb/rgba array
      - ``None``, the default, to use a single color for the faces, and
        the style default for the edges.
      - A 3D ndarray of color names, with each item the color for the
        corresponding voxel. The size must match the voxels.
      - A 4D ndarray of rgb/rgba data, with the components along the
        last axis.

**kwargs
    Additional keyword arguments to pass onto
    :func:`~mpl_toolkits.mplot3d.art3d.Poly3DCollection`

Returns
-------
faces : dict
    A dictionary indexed by coordinate, where ``faces[i,j,k]`` is a
    `Poly3DCollection` of the faces drawn for the voxel
    ``filled[i,j,k]``. If no faces were drawn for a given voxel, either
    because it was not asked to be drawn, or it is fully occluded, then
    ``(i,j,k) not in faces``.

Examples
--------
.. plot:: gallery/mplot3d/voxels.py
.. plot:: gallery/mplot3d/voxels_rgb.py
.. plot:: gallery/mplot3d/voxels_torus.py
.. plot:: gallery/mplot3d/voxels_numpy_logo.py


### xaxis\_date
```py

def xaxis_date(self, tz=None)

```



Sets up x-axis ticks and labels that treat the x data as dates.

Parameters
----------
tz : string or :class:`tzinfo` instance, optional
    Timezone string or timezone. Defaults to rc value.


### xaxis\_inverted
```py

def xaxis_inverted(self)

```



Return whether the x-axis is inverted.


### xcorr
```py

def xcorr(ax, *args, **kwargs)

```



Plot the cross correlation between *x* and *y*.

The correlation with lag k is defined as sum_n x[n+k] * conj(y[n]).

Parameters
----------

x : sequence of scalars of length n

y : sequence of scalars of length n

hold : boolean, optional, *deprecated*, default: True

detrend : callable, optional, default: `mlab.detrend_none`
    x is detrended by the `detrend` callable. Default is no
    normalization.

normed : boolean, optional, default: True
    if True, input vectors are normalised to unit length.

usevlines : boolean, optional, default: True
    if True, Axes.vlines is used to plot the vertical lines from the
    origin to the acorr. Otherwise, Axes.plot is used.

maxlags : integer, optional, default: 10
    number of lags to show. If None, will return all 2 * len(x) - 1
    lags.

Returns
-------
(lags, c, line, b) : where:

  - `lags` are a length 2`maxlags+1 lag vector.
  - `c` is the 2`maxlags+1 auto correlation vectorI
  - `line` is a `~matplotlib.lines.Line2D` instance returned by
    `plot`.
  - `b` is the x-axis (none, if plot is used).

Other Parameters
----------------
linestyle : `~matplotlib.lines.Line2D` prop, optional, default: None
    Only used if usevlines is False.

marker : string, optional, default: 'o'

Notes
-----
The cross correlation is performed with :func:`numpy.correlate` with
`mode` = 2.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.


### yaxis\_date
```py

def yaxis_date(self, tz=None)

```



Sets up y-axis ticks and labels that treat the y data as dates.

Parameters
----------
tz : string or :class:`tzinfo` instance, optional
    Timezone string or timezone. Defaults to rc value.


### yaxis\_inverted
```py

def yaxis_inverted(self)

```



Return whether the y-axis is inverted.


### zaxis\_date
```py

def zaxis_date(self, tz=None)

```



Sets up z-axis ticks and labels that treat the z data as dates.

*tz* is a timezone string or :class:`tzinfo` instance.
Defaults to rc value.

.. note::
    This function is merely provided for completeness.
    Axes3D objects do not officially support dates for ticks,
    and so this may or may not work as expected.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.


### zaxis\_inverted
```py

def zaxis_inverted(self)

```



Returns True if the z-axis is inverted.

.. versionadded :: 1.1.0
    This function was added, but not tested. Please report any bugs.




## Class BoolParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class Bundle
Main container class for PHOEBE 2.

The :class:`Bundle` is the main object in PHOEBE 2 which is used to store
and filter all available system parameters as well as handling attaching
datasets, running models, and accessing synthetic data.

The Bundle is simply a glorified
:class:`phoebe.parameters.parameters.ParameterSet`. In fact, filtering on
a Bundle gives you a ParameterSet (and filtering on a ParameterSet gives
you another ParameterSet).  The only difference is that most "actions" are
only available at the Bundle level (as they need to access /all/
parameters).

Make sure to also see the documentation and methods for  *
:class:`phoebe.parameters.parameters.ParameterSet` *
:class:`phoebe.parameters.parameters.Parameter` *
:class:`phoebe.parameters.parameters.FloatParameter` *
:class:`phoebe.parameters.parameters.ArrayParameter`

To initialize a new bundle, see:
    * :meth:`open`
    * :meth:`from_legacy`
    * :meth:`default_binary`

To filter parameters and set values, see:
    * :meth:`phoebe.parameters.parameters.ParameterSet.filter`
    * :meth:`phoebe.parameters.parameters.ParameterSet.get_value`
    * :meth:`phoebe.parameters.parameters.ParameterSet.set_value`

To deal with datasets, see:
    * :meth:`add_dataset`
    * :meth:`get_dataset`
    * :meth:`remove_dataset`
    * :meth:`enable_dataset`
    * :meth:`disable_dataset`

To compute forward models, see:
    * :meth:`add_compute`
    * :meth:`get_compute`
    * :meth:`run_compute`
    * :meth:`get_model`

To plot observations or synthetic datasets, see:
    * :meth:`phoebe.parameters.parameters.ParameterSet.plot`
### \_\_init\_\_
```py

def __init__(self, params=None)

```



Initialize a new Bundle.

Initializing a new bundle without a constructor is possible, but not
advised.  It is suggested that you use one of the constructors below.

Available constructors:
    * :meth:`open`
    * :meth:`from_legacy`
    * :meth:`default_binary`

:param list parameters: list of
    :class:`phoebe.parameters.parameters.Parameter` to create the
    Bundle (optional)
:return: instantiated :class:`Bundle` object


### add\_component
```py

def add_component(self, kind, **kwargs)

```



Add a new component (star or orbit) to the system.  If not provided,
'component' (the name of the new star or orbit) will be created for
you and can be accessed by the 'component' attribute of the returned
ParameterSet.

>>> b.add_component(component.star)

or

>>> b.add_component('orbit', period=2.5)

Available kinds include:
    * :func:`phoebe.parameters.component.star`
    * :func:`phoebe.parameters.component.orbit`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default
    values, or the name of a function (as a string) that can
    be found in the :mod:`phoebe.parameters.component` module
    (ie. 'star', 'orbit')
:type kind: str or callable
:parameter str component: (optional) name of the newly-created
    component
:parameter **kwargs: default values for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented


### add\_compute
```py

def add_compute(self, kind=<function phoebe at 0x7fa1035596e0>, **kwargs)

```



Add a set of computeoptions for a given backend to the bundle.
The label ('compute') can then be sent to :meth:`run_compute`.

If not provided, 'compute' will be created for you and can be
accessed by the 'compute' attribute of the returned
ParameterSet.

Available kinds include:
    * :func:`phoebe.parameters.compute.phoebe`
    * :func:`phoebe.parameters.compute.legacy`
    * :func:`phoebe.parameters.compute.photodynam`
    * :func:`phoebe.parameters.compute.jktebop`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default
    values, or the name of a function (as a string) that can
    be found in the :mod:`phoebe.parameters.compute` module
:type kind: str or callable
:parameter str compute: (optional) name of the newly-created
    compute optins
:parameter **kwargs: default values for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented


### add\_constraint
```py

def add_constraint(self, *args, **kwargs)

```



TODO: add documentation

args can be string representation (length 1)
func and strings to pass to function


### add\_dataset
```py

def add_dataset(self, kind, component=None, **kwargs)

```



Add a new dataset to the bundle.  If not provided,
'dataset' (the name of the new dataset) will be created for
you and can be accessed by the 'dataset' attribute of the returned
ParameterSet.

For light curves, if you do not provide a value for 'component',
the light curve will be generated for the entire system.

For radial velocities, you need to provide a list of components
for which values should be computed.

Available kinds include:
    * :func:`phoebe.parameters.dataset.lc`
    * :func:`phoebe.parameters.dataset.rv`
    * :func:`phoebe.parameters.dataset.etv`
    * :func:`phoebe.parameters.dataset.orb`
    * :func:`phoebe.parameters.dataset.mesh`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default
    values, or the name of a function (as a string) that can
    be found in the :mod:`phoebe.parameters.dataset` module
:type kind: str or callable
:parameter component: a list of
    components for which to compute the observables.  For
    light curves this should be left at None to always compute
    the light curve for the entire system.  For most other
    types, you need to provide at least one component.
:type component: str or list of strings or None
:parameter str dataset: (optional) name of the newly-created dataset
:parameter **kwargs: default values for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented


### add\_envelope
```py

def add_envelope(self, component=None, **kwargs)

```



[NOT SUPPORTED]

Shortcut to :meth:`add_component` but with kind='envelope'


### add\_feature
```py

def add_feature(self, kind, component, **kwargs)

```



Add a new feature (spot, etc) to a component in the system.  If not
provided, 'feature' (the name of the new feature) will be created
for you and can be accessed by the 'feature' attribute of the returned
ParameterSet

>>> b.add_feature(feature.spot, component='mystar')

or

>>> b.add_feature('spot', 'mystar', colat=90)

Available kinds include:
    * :func:`phoebe.parameters.feature.spot`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default values,
    or the name of a function (as a string) that can be found in the
    :mod:`phoebe.parameters.feature` module (ie. 'spot')
:type kind: str or callable
:parameter str component: name of the component to attach the feature
:parameter str feature: (optional) name of the newly-created feature
:parameter **kwargs: default value for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented


### add\_feedback
```py

def add_feedback(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### add\_fitting
```py

def add_fitting(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### add\_orbit
```py

def add_orbit(self, component=None, **kwargs)

```



Shortcut to :meth:`add_component` but with kind='orbit'


### add\_parameter
```py

def add_parameter(self)

```



[NOT IMPLEMENTED]

Add a new parameter to the bundle

:raises NotImplementedError: because it isn't


### add\_plugin
```py

def add_plugin(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### add\_prior
```py

def add_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### add\_spot
```py

def add_spot(self, component=None, feature=None, **kwargs)

```



Shortcut to :meth:`add_feature` but with kind='spot'


### add\_star
```py

def add_star(self, component=None, **kwargs)

```



Shortcut to :meth:`add_component` but with kind='star'


### animate
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


### as\_client
```py

def as_client(self, as_client=True, server='http://localhost:5555', bundleid=None)

```



[NOT IMPLEMENTED]


### change\_component
```py

def change_component(self, old_component, new_component)

```



Change the label of a component attached to the Bundle

:parameter str old_component: the current name of the component
    (must exist)
:parameter str new_component: the desired new name of the component
    (must not exist)
:return: None
:raises ValueError: if the new_component is forbidden


### client\_update
```py

def client_update(self)

```



[NOT IMPLEMENTED]


### compute\_critical\_pots
```py

def compute_critical_pots(self, component, L1=True, L2=True, L3=True)

```



### compute\_critical\_rpoles
```py

def compute_critical_rpoles(self, component, L1=True, L2=True, L3=True)

```



returns in solRad


### default\_binary
```py

def default_binary(cls, starA='primary', starB='secondary', orbit='binary', contact_binary=False)

```



Load a bundle with a default binary as the system.

primary - secondary

This is a constructor, so should be called as:

>>> b = Bundle.default_binary()

:return: instantiated :class:`Bundle` object


### default\_star
```py

def default_star(cls, starA='starA')

```



Load a bundle with a default single star as the system.

sun

This is a constructor, so should be called as:

>>> b = Bundle.default_binary()

:return: instatiated :class`Bundle` object


### default\_triple
```py

def default_triple(cls, inner_as_primary=True, inner_as_overcontact=False, starA='starA', starB='starB', starC='starC', inner='inner', outer='outer', contact_envelope='contact_envelope')

```



Load a bundle with a default triple system.

Set inner_as_primary based on what hierarchical configuration you want.

inner_as_primary = True:

starA - starB -- starC

inner_as_primary = False:

starC -- starA - starB

This is a constructor, so should be called as:

>>> b = Bundle.default_triple_primary()

:parameter bool inner_as_primary: whether the inner-binary should be
    the primary component of the outer-orbit
:return: instantiated :class:`Bundle` object


### disable\_dataset
```py

def disable_dataset(self, dataset=None, **kwargs)

```



Disable a 'dataset'.  Datasets that are enabled will be computed
during :meth:`run_compute` and included in the cost function
during :meth:`run_fitting`.

:parameter str dataset: name of the dataset
:parameter **kwargs: any other tags to do the filter
    (except dataset or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`
    of the disabled dataset


### disable\_history
```py

def disable_history(self)

```



Disable logging history items (undo/redo)

You can check wither history is enabled using :meth:`history_enabled`.

Shortcut to b.get_setting('log_history').set_value(False)


### disable\_prior
```py

def disable_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### draw\_from\_posterior
```py

def draw_from_posterior(self, twig=None, feedback=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### draw\_from\_prior
```py

def draw_from_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### enable\_dataset
```py

def enable_dataset(self, dataset=None, **kwargs)

```



Enable a 'dataset'.  Datasets that are enabled will be computed
during :meth:`run_compute` and included in the cost function
during :meth:`run_fitting`.

:parameter str dataset: name of the dataset
:parameter **kwargs: any other tags to do the filter
    (except dataset or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`
    of the enabled dataset


### enable\_history
```py

def enable_history(self)

```



Enable logging history items (undo/redo).

You can check wither history is enabled using :meth:`history_enabled`.

Shortcut to b.get_setting('log_history').set_value(True)


### enable\_prior
```py

def enable_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### exclude
```py

def exclude(self, twig=None, check_visible=True, **kwargs)

```



Exclude the results from this filter from the current ParameterSet.

See :meth:`filter` for options.


### export\_legacy
```py

def export_legacy(self, filename)

```



TODO: add docs


### filter
```py

def filter(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Filter the ParameterSet based on the meta-tags of the Parameters
and return another ParameterSet.

Because another ParameterSet is returned, these filter calls are
chainable.

>>> b.filter(context='component').filter(component='starA')

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`ParameterSet`


### filter\_or\_get
```py

def filter_or_get(self, twig=None, autocomplete=False, force_ps=False, check_visible=True, check_default=True, **kwargs)

```



Filter the :class:`ParameterSet` based on the meta-tags of its
Parameters and return another :class:`ParameterSet` unless there is
exactly 1 result, in which case the :class:`Parameter` itself is
returned (set force_ps=True to avoid this from happening or call filter
instead).

In the case when another :class:`ParameterSet` is returned, these
filter calls are chainable.

>>> b.filter_or_get(context='component').filter_or_get(component='starA')

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool force_ps: whether to force a ParameterSet
        to be returned even if only a single result is found.
        This is helpful if you want to write generic code
        that chains filter calls (since Parameter does not have
        a filter method).
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: :class:`Parameter` if length of results is exactly 1 and
    force_ps==False. Otherwise another :class:`ParameterSet` will be
    returned.


### flip\_constraint
```py

def flip_constraint(self, twig=None, solve_for=None, **kwargs)

```



Flip an existing constraint to solve for a different parameter

:parameter str twig: twig to filter the constraint
:parameter solve_for: twig or actual parameter object of the new
    parameter which this constraint should constraint (solve for).
:type solve_for: str or :class:`phoebe.parameters.parameters.Parameter
:parameter **kwargs: any other tags to do the filter
    (except twig or context)


### from\_catalog
```py

def from_catalog(cls, identifier)

```



Load a new bundle from the phoebe catalog.

[NOTIMPLEMENTED]

Load a bundle from the online catalog.  This is a constructor
so should be called as:

>>> b = Bundle.from_catalog(identifier)

:parameter str identifier: identifier of the object in the catalog
:return: instantiated :class:`Bundle` object
:raises NotImplementedError: because this isn't implemented yet


### from\_legacy
```py

def from_legacy(cls, filename, add_compute_legacy=False, add_compute_phoebe=True)

```



Load a bundle from a PHOEBE 1.0 Legacy file.

This is a constructor so should be called as:

>>> b = Bundle.from_legacy('myfile.phoebe')

:parameter str filename: relative or full path to the file
:return: instantiated :class:`Bundle` object


### from\_server
```py

def from_server(cls, bundleid, server='http://localhost:5555', as_client=True)

```



Load a new bundle from a server.

[NOT IMPLEMENTED]

Load a bundle from a phoebe server.  This is a constructor so should be
called as:

>>> b = Bundle.from_server('asdf', as_client=False)

:parameter str bundleid: the identifier given to the bundle by the
    server
:parameter str server: the host (and port) of the server
:parameter bool as_client: whether to attach in client mode
    (default: True)


### get
```py

def get(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Get a single parameter from this ParameterSet.  This works exactly the
same as filter except there must be only a single result, and the Parameter
itself is returned instead of a ParameterSet.

Also see :meth:`get_parameter` (which is simply an alias of this method)

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`Parameter`
:raises ValueError: if either 0 or more than 1 results are found
        matching the search.


### get\_adjust
```py

def get_adjust(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### get\_component
```py

def get_component(self, component=None, **kwargs)

```



Filter in the 'component' context

:parameter str component: name of the component (optional)
:parameter **kwargs: any other tags to do the filter
    (except component or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_compute
```py

def get_compute(self, compute=None, **kwargs)

```



Filter in the 'compute' context

:parameter str compute: name of the compute options (optional)
:parameter **kwargs: any other tags to do the filter
    (except compute or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_constraint
```py

def get_constraint(self, twig=None, **kwargs)

```



Filter in the 'constraint' context

:parameter str constraint: name of the constraint (optional)
:parameter **kwargs: any other tags to do the filter
    (except constraint or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_dataset
```py

def get_dataset(self, dataset=None, **kwargs)

```



Filter in the 'dataset' context

:parameter str dataset: name of the dataset (optional)
:parameter **kwargs: any other tags to do the filter
    (except dataset or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_default\_unit
```py

def get_default_unit(self, twig=None, **kwargs)

```



TODO: add documentation


### get\_description
```py

def get_description(self, twig=None, **kwargs)

```



TODO: add documentation


### get\_enabled
```py

def get_enabled(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### get\_envelope
```py

def get_envelope(self, component=None, **kwargs)

```



[NOT SUPPORTED]

Shortcut to :meth:`get_component` but with kind='envelope'


### get\_ephemeris
```py

def get_ephemeris(self, component=None, t0='t0_supconj', shift=True, **kwargs)

```



Get the ephemeris of a component (star or orbit)

:parameter str component: name of the component.  If not given,
    component will default to the top-most level of the current
    hierarchy
:parameter t0: qualifier of the parameter to be used for t0
:type t0: str
:parameter shift: if true, phase shift is applied (which should be
    done to models); if false, it is not applied (which is suitable
    for data).
:type shift: boolean
:parameter **kwargs: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, phshift, dpdt).
    Note: be careful about units - input values will not be converted.
:return: dictionary containing period, t0 (t0_supconj if orbit),
    phshift, dpdt (as applicable)
:rtype: dict


### get\_feature
```py

def get_feature(self, feature=None, **kwargs)

```



Filter in the 'proerty' context

:parameter str feature: name of the feature (optional)
:parameter **kwargs: any other tags to do the filter
    (except component or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_feedback
```py

def get_feedback(self, feedback=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### get\_fitting
```py

def get_fitting(self, fitting=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### get\_hierarchy
```py

def get_hierarchy(self)

```



Get the hierarchy parameter

:return: the hierarcy :class:`phoebe.parameters.parameters.Parameter`
    or None (if no hierarchy exists)


### get\_history
```py

def get_history(self, i=None)

```



Get a history item by index.

You can toggle whether history is recorded using
    * :meth:`enable_history`
    * :meth:`disable_history`

:parameter int i: integer for indexing (can be positive or
    negative).  If i is None or not provided, the entire list
    of history items will be returned
:return: :class:`phoebe.parameters.parameters.Parameter` if i is
    an int, or :class:`phoebe.parameters.parameters.ParameterSet` if i
    is not provided
:raises ValueError: if no history items have been recorded.


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



Dictionary of all meta-tags, with option to ignore certain tags.

See all the meta-tag properties that are shared by ALL Parameters.
If a given value is 'None', that means that it is not shared
among ALL Parameters.  To see the different values among the
Parameters, you can access that attribute.

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_model
```py

def get_model(self, model=None, **kwargs)

```



Filter in the 'model' context

:parameter str model: name of the model (optional)
:parameter **kwargs: any other tags to do the filter
    (except model or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_or\_create
```py

def get_or_create(self, qualifier, new_parameter, **kwargs)

```



Get a :class:`Parameter` from the ParameterSet, if it does not exist,
create and attach it.

Note: running this on a ParameterSet that is NOT a
:class:`phoebe.frontend.bundle.Bundle`,
will NOT add the Parameter to the bundle, but only the temporary
ParameterSet

:parameter str qualifier: the qualifier of the :class:`Parameter`
    (note, not the twig)
:parameter new_parameter: the parameter to attach if no
        result is found
:type new_parameter: :class:`Parameter`
:parameter **kwargs: meta-tags to search - will also be applied to
        new_parameter if it is attached.
:return: Parameter, created
:rtype: :class:`Parameter`, bool
:raises ValueError: if more than 1 result was found using the search
        criteria.


### get\_orbit
```py

def get_orbit(self, component=None, **kwargs)

```



Shortcut to :meth:`get_component` but with kind='star'


### get\_parameter
```py

def get_parameter(self, twig=None, **kwargs)

```



Get a :class:`Parameter` from this ParameterSet.  This simply calls get

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`Parameter`
:raises ValueError: if either 0 or more than 1 results are found
        matching the search.


### get\_plotting\_info
```py

def get_plotting_info(self, twig=None, **kwargs)

```



[ADD DOCUMENTATION]


### get\_plugin
```py

def get_plugin(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### get\_posterior
```py

def get_posterior(self, twig=None, feedback=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### get\_prior
```py

def get_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### get\_quantity
```py

def get_quantity(self, twig=None, unit=None, default=None, t=None, **kwargs)

```



TODO: add documentation


### get\_setting
```py

def get_setting(self, twig=None, **kwargs)

```



Filter in the 'setting' context

:parameter str twig: the twig used for filtering
:parameter **kwargs: any other tags to do the filter (except tag or
    context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`


### get\_spot
```py

def get_spot(self, feature=None, **kwargs)

```



Shortcut to :meth:`get_feature` but with kind='spot'


### get\_star
```py

def get_star(self, component=None, **kwargs)

```



Shortcut to :meth:`get_component` but with kind='star'


### get\_system
```py

def get_system(self, twig=None, **kwargs)

```



Filter in the 'system' context

:parameter str twig: twig to use for filtering
:parameter **kwargs: any other tags to do the filter
    (except twig or context)

:return: :class:`phoebe.parameters.parameters.Parameter` or
    :class:`phoebe.parameters.parameters.ParameterSet`


### get\_value
```py

def get_value(self, twig=None, unit=None, default=None, t=None, **kwargs)

```



Get the value of a :class:`Parameter` in this ParameterSet

:parameter str twig: the twig to search for the parameter
:parameter unit: units for the returned result (if
    applicable).  If None or not provided, the value will
    be returned in that Parameter's default_unit (if
    applicable)
:type unit: str or astropy.units.Unit
:parameter default: what to return if the parameter cannot be found.
    If this is None (default) then an error will be raised instead.
    Note that the units of default will not be converted.
:parameter time: time at which to compute the
    value (will only affect time-dependent parameters).  If provided
    as a float it is assumed that the units are the same as t0.
    NOTE: this is not fully supported yet, use with caution.
:parameter **kwargs: meta-tags to search
:return: value (type depeding on the type of the :class:`Parameter`)


### items
```py

def items(self)

```



Returns the items (key, value pairs) from :func:`to_dict`

:return: string, :class:`Parameter` or :class:`ParameterSet` pairs


### keys
```py

def keys(self)

```



Return the keys from :func:`to_dict`

:return: list of strings


### open
```py

def open(cls, filename)

```



Open a new bundle.

Open a bundle from a JSON-formatted PHOEBE 2.0 (beta) file.
This is a constructor so should be called as:


>>> b = Bundle.open('test.phoebe')


:parameter str filename: relative or full path to the file
:return: instantiated :class:`Bundle` object


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


### redo
```py

def redo(self, i=-1)

```



Redo an item in the history logs

:parameter int i: integer for indexing (can be positive or
    negative).  Defaults to -1 if not provided (the latest
    recorded history item)
:raises ValueError: if no history items have been recorded


### remove\_component
```py

def remove_component(self, component=None, **kwargs)

```



[NOT IMPLEMENTED]

Remove a 'component' from the bundle

:raises NotImplementedError: because this isn't implemented yet


### remove\_compute
```py

def remove_compute(self, compute, **kwargs)

```



[NOT IMPLEMENTED]
Remove a 'constraint' from the bundle

:parameter str twig: twig to filter for the compute options
:parameter **kwargs: any other tags to do the filter
    (except twig or context)
:raise NotImplementedError: because it isn't


### remove\_constraint
```py

def remove_constraint(self, twig=None, **kwargs)

```



Remove a 'constraint' from the bundle

:parameter str twig: twig to filter for the constraint
:parameter **kwargs: any other tags to do the filter
    (except twig or context)


### remove\_dataset
```py

def remove_dataset(self, dataset=None, **kwargs)

```



Remove a dataset from the Bundle.

This removes all matching Parameters from the dataset, model, and
constraint contexts (by default if the context tag is not provided).

You must provide some sort of filter or this will raise an Error (so
that all Parameters are not accidentally removed).

:parameter str dataset: name of the dataset
:parameter **kwargs: any other tags to do the filter (except qualifier
    and dataset)
:raises ValueError: if no filter is provided


### remove\_envelope
```py

def remove_envelope(self, component=None, **kwargs)

```



[NOT SUPPORTED]
[NOT IMPLEMENTED]

Shortcut to :meth:`remove_component` but with kind='envelope'


### remove\_feature
```py

def remove_feature(self, feature=None, **kwargs)

```



[NOT IMPLEMENTED]

Remove a 'feature' from the bundle

:raises NotImplementedError: because this isn't implemented yet


### remove\_feedback
```py

def remove_feedback(self, feedback=None)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### remove\_fitting
```py

def remove_fitting(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### remove\_history
```py

def remove_history(self, i=None)

```



Remove a history item from the bundle by index.

You can toggle whether history is recorded using
    * :meth:`enable_history`
    * :meth:`disable_history`


:parameter int i: integer for indexing (can be positive or
    negative).  If i is None or not provided, the entire list
    of history items will be removed
:raises ValueError: if no history items have been recorded.


### remove\_model
```py

def remove_model(self, model, **kwargs)

```



Remove a 'model' from the bundle

:parameter str twig: twig to filter for the model
:parameter **kwargs: any other tags to do the filter
    (except twig or context)


### remove\_orbit
```py

def remove_orbit(self, component=None, **kwargs)

```



[NOT IMPLEMENTED]

Shortcut to :meth:`remove_component` but with kind='star'


### remove\_parameter
```py

def remove_parameter(self, twig=None, **kwargs)

```



Remove a :class:`Parameter` from the ParameterSet

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter **kwargs: meta-tags to search
:raises ValueError: if 0 or more than 1 results are found using the
        provided search criteria.


### remove\_parameters\_all
```py

def remove_parameters_all(self, twig=None, **kwargs)

```



Remove all :class:`Parameter`s that match the search from the
ParameterSet.

Any Parameter that would be included in the resulting ParameterSet
from a :func:`filter` call with the same arguments will be
removed from this ParameterSet.

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter **kwargs: meta-tags to search


### remove\_plugin
```py

def remove_plugin(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### remove\_posterior
```py

def remove_posterior(self, twig=None, feedback=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### remove\_prior
```py

def remove_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### remove\_spot
```py

def remove_spot(self, feature=None, **kwargs)

```



[NOT IMPLEMENTED]

Shortcut to :meth:`remove_feature` but with kind='spot'


### remove\_star
```py

def remove_star(self, component=None, **kwargs)

```



[NOT IMPLEMENTED]

Shortcut to :meth:`remove_component` but with kind='star'


### run\_checks
```py

def run_checks(self, **kwargs)

```



Check to see whether the system is expected to be computable.

This is called by default for each set_value but will only raise a
logger warning if fails.  This is also called immediately when calling
:meth:`run_compute`.

:return: True if passed, False if failed and a message


### run\_compute
```py

def run_compute(self, *args, **kwargs)

```



Run a forward model of the system on the enabled dataset using
a specified set of compute options.

To attach and set custom values for compute options, including choosing
which backend to use, see:
    * :meth:`add_compute`

To define the dataset types and times at which the model should be
computed see:
    * :meth:`add_dataset`

To disable or enable existing datasets see:
    * :meth:`enable_dataset`
    * :meth:`disable_dataset`

:parameter str compute: (optional) name of the compute options to use.
    If not provided or None, run_compute will use an existing set of
    attached compute options if only 1 exists.  If more than 1 exist,
    then compute becomes a required argument.  If no compute options
    exist, then this will use default options and create and attach
    a new set of compute options with a default label.
:parameter str model: (optional) name of the resulting model.  If not
    provided this will default to 'latest'.  NOTE: existing models
    with the same name will be overwritten - including 'latest'
:parameter bool datach: [EXPERIMENTAL] whether to detach from the computation run,
    or wait for computations to complete.  If detach is True, see
    :meth:`get_model` and :meth:`phoebe.parameters.parameters.JobParameter`
    for details on how to check the job status and retrieve the results.
    Alternatively, you can provide the server location (host and port) as
    a string to detach and the bundle will temporarily enter client mode,
    submit the job to the server, and leave client mode.  The resulting
    :meth:`phoebe.parameters.parameters.JobParameter` will then contain
    the necessary information to pull the results from the server at anytime
    in the future.
:parameter animate: [EXPERIMENTAL] information to send to :meth:`animate`
    while the synthetics are being built.  If not False (in which case
    live animation will not be done), animate should be a dictionary or
    list of dictionaries and a new frame will be displayed and plotted
    as they are computed.  This really only makes sense for backends
    that compute per-time rather than per-dataset.  Note: animation
    may significantly slow down the time of run_compute, especially
    for a large number of time-points or if meshes are being stored/plotted.
    Also note: animate will obviously be ignored if detach=True, this
    isn't magic.  NOTE: fixed_limits are not supported from run_compute,
    axes limits will be updated each frame, but all colorlimits will
    be determined per-frame and will not be constant across the animation.
:parameter list times: [EXPERIMENTAL] override the times at which to compute the model.
    NOTE: this only (temporarily) replaces the time array for datasets
    with times provided (ie empty time arrays are still ignored).  So if
    you attach a rv to a single component, the model will still only
    compute for that single component.  ALSO NOTE: this option is ignored
    if detach=True (at least for now).
:parameter **kwargs: any values in the compute options to temporarily
    override for this single compute run (parameter values will revert
    after run_compute is finished)
:return: :class:`phoebe.parameters.parameters.ParameterSet` of the
    newly-created model containing the synthetic data.


### run\_constraint
```py

def run_constraint(self, twig=None, **kwargs)

```



Run a given 'constraint' now and set the value of the constrained
parameter.  In general, there shouldn't be any need to manually
call this - constraints should automatically be run whenever a
dependent parameter's value is change.

:parameter str twig: twig to filter for the constraint
:parameter **kwargs: any other tags to do the filter
    (except twig or context)
:return: the resulting value of the constraint
:rtype: float or units.Quantity


### run\_delayed\_constraints
```py

def run_delayed_constraints(self)

```



        


### run\_fitting
```py

def run_fitting(self, **kwargs)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### run\_plugin
```py

def run_plugin(self)

```



[NOT IMPLEMENTED]

:raises NotImplementedError: because it isn't


### save
```py

def save(self, filename, clear_history=True, incl_uniqueid=False)

```



Save the bundle to a JSON-formatted ASCII file.

:parameter str filename: relative or full path to the file
:parameter bool clear_history: whether to clear history log
    items before saving (default: True)
:parameter bool incl_uniqueid: whether to including uniqueids in the
    file (only needed if its necessary to maintain the uniqueids when
    reloading)
:return: the filename


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


### set
```py

def set(self, key, value, **kwargs)

```



Set the value of a Parameter in the ParameterSet.

If :func:`get` would retrieve a Parameter, this will set the
value of that parameter.

Or you can provide 'value@...' or 'default_unit@...', etc
to specify what attribute to set.

:parameter str key: the twig (called key here to be analagous
    to a normal dict)
:parameter value: value to set
:parameter **kwargs: other filter parameters (must result in
    returning a single :class:`Parameter`)
:return: the value of the :class:`Parameter` after setting the
    new value (including converting units if applicable)


### set\_adjust
```py

def set_adjust(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_adjust\_all
```py

def set_adjust_all(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_default\_unit
```py

def set_default_unit(self, twig=None, unit=None, **kwargs)

```



TODO: add documentation


### set\_default\_unit\_all
```py

def set_default_unit_all(self, twig=None, unit=None, **kwargs)

```



TODO: add documentation


### set\_enabled
```py

def set_enabled(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_hierarchy
```py

def set_hierarchy(self, *args, **kwargs)

```



Set the hierarchy of the system.

See tutorial on building a system.

TODO: provide documentation
args can be
- string representation (preferably passed through hierarchy already)
- func and strings/PSs/params to pass to function


### set\_meta
```py

def set_meta(self, **kwargs)

```



Set the value of tags for all Parameters in this ParameterSet.


### set\_prior
```py

def set_prior(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_quantity
```py

def set_quantity(self, twig=None, value=None, **kwargs)

```



TODO: add documentation


### set\_value
```py

def set_value(self, twig=None, value=None, **kwargs)

```



Set the value of a :class:`Parameter` in this ParameterSet

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the :class:`phoebe.frontend.bundle.Bundle`)

:parameter set twig: the twig to search for the parameter
:parameter value: the value to set.  Provide units, if necessary, by
    sending a Quantity object (ie 2.4*u.rad)
:parameter **kwargs: meta-tags to search
:raises ValueError:  if 0 or more than 1 results are found matching
    the search criteria.


### set\_value\_all
```py

def set_value_all(self, twig=None, value=None, check_default=False, **kwargs)

```



Set the value of all returned :class:`Parameter`s in this ParameterSet.

Any :class:`Parameter` that would be included in the resulting ParameterSet
from a :func:`filter` call with the same arguments will have
their value set.

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter value: the value to set.  Provide units, if necessary, by
        sending a Quantity object (ie 2.4*u.rad)
:parameter bool check_default: whether to exclude any default values.
        Defaults to False (unlike all filtering).  Note that this
        acts on the current ParameterSet so any filtering done before
        this call will EXCLUDE defaults by default.
:parameter **kwargs: meta-tags to search


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


### to\_dict
```py

def to_dict(self, field=None, **kwargs)

```



Convert the ParameterSet to a structured (nested) dictionary
to allow traversing the structure from the bottom up

:parameter str field: (optional) build the dictionary with keys at
    a given level/field.  Can be any of the keys in
    :func:`meta`.  If None, the keys will be the lowest
    level in which Parameters have different values.
:return: dict of :class:`Parameter`s or :class:`ParameterSet`s


### to\_flat\_dict
```py

def to_flat_dict(self, **kwargs)

```



Convert the :class:`ParameterSet` to a flat dictionary, with keys being
uniquetwigs to access the parameter and values being the :class:`Parameter`
objects themselves.

:return: dict of :class:`Parameter`s


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



Convert the ParameterSet to a json-compatible dictionary

:return: list of dictionaries


### to\_list
```py

def to_list(self, **kwargs)

```



Convert the :class:`ParameterSet` to a list of :class:`Parameter`s

:return: list of class:`Parameter` objects


### to\_list\_of\_dicts
```py

def to_list_of_dicts(self, **kwargs)

```



Convert the :class:`ParameterSet` to a list of the dictionary representation
of each :class:`Parameter`

:return: list of dicts


### to\_phase
```py

def to_phase(self, time, shift=True, component=None, t0='t0_supconj', **kwargs)

```



Get the phase(s) of a time(s) for a given ephemeris

:parameter time: time to convert to phases (should be in same system
    as t0s)
:type time: float, list, or array
:parameter shift: if true, phase shift is applied (which should be
    done to models); if false, it is not applied (which is suitable
    for data).
:type shift: boolean
:parameter t0: qualifier of the parameter to be used for t0
:type t0: str
:parameter str component: component for which to get the ephemeris.
    If not given, component will default to the top-most level of the
    current hierarchy
:parameter **kwargs: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, phshift, dpdt).
    Note: be careful about units - input values will not be converted.
:return: phase (float) or phases (array)


### to\_time
```py

def to_time(self, phase, shift=True, component=None, t0='t0_supconj', **kwargs)

```



    Get the time(s) of a phase(s) for a given ephemeris

    :parameter phase: phase to convert to times (should be in
        same system as t0s)
    :type phase: float, list, or array
    :parameter shift: if true, phase shift is applied (which should be
        done to models); if false, it is not applied (which is suitable
        for data).
    :type shift: boolean
`   :parameter str component: component for which to get the ephemeris.
        If not given, component will default to the top-most level of the
        current hierarchy
    :parameter t0: qualifier of the parameter to be used for t0
    :type t0: str
    :parameter **kwargs: any value passed through kwargs will override the
        ephemeris retrieved by component (ie period, t0, phshift, dpdt).
        Note: be careful about units - input values will not be converted.
    :return: time (float) or times (array)
    


### ui
```py

def ui(self, client='http://localhost:4200', **kwargs)

```



[NOT IMPLEMENTED]

The bundle must be in client mode in order to open the web-interface.
See :meth:`Bundle:as_client` to switch to client mode.

:parameter str client: URL of the running client which must be connected
    to the same server as the bundle
:return: URL of the parameterset of this bundle in the client (will also
    attempt to open webbrowser)
:rtype: str


### undo
```py

def undo(self, i=-1)

```



Undo an item in the history logs

:parameter int i: integer for indexing (can be positive or
    negative).  Defaults to -1 if not provided (the latest
    recorded history item)
:raises ValueError: if no history items have been recorded


### values
```py

def values(self)

```



Return the values from :func:`to_dict`

:return: list of :class:`Parameter`s or :class:`ParameterSet`s




## Class ChoiceParameter
Parameter in which the value has to match one of the pre-defined choices
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_choices
```py

def get_choices(self)

```



### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class ConstraintParameter
One side of a constraint (not an equality)

qualifier: constrained parameter
value: expression
### \_\_init\_\_
```py

def __init__(self, bundle, value, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### flip\_for
```py

def flip_for(self, twig=None, expression=None, **kwargs)

```



flip the constraint to solve for for any of the parameters in the expression

expression (optional if sympy available, required if not)


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_constrained\_parameter
```py

def get_constrained_parameter(self)

```



        


### get\_default\_unit
```py

def get_default_unit(self)

```



### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parameter
```py

def get_parameter(self, twig=None, **kwargs)

```



get a parameter from those that are variables


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_result
```py

def get_result(self, t=None)

```



        


### get\_value
```py

def get_value(self)

```



        


### set\_default\_unit
```py

def set_default_unit(self, unit)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, value, **kwargs)

```



kwargs are passed on to filter


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class ConstraintVar
None
### \_\_init\_\_
```py

def __init__(self, bundle, twig)

```



### get\_parameter
```py

def get_parameter(self)

```



get the parameter object from the system for this var

needs to be backend safe (not passing or storing bundle)


### get\_quantity
```py

def get_quantity(self, units=None, t=None)

```



        


### get\_value
```py

def get_value(self, units=None, t=None)

```



get the value (either of the constant or from the parameter) for this var

needs to be backend safe (not passing or storing bundle)


### update\_user\_label
```py

def update_user_label(self)

```



finds this parameter and gets the least_unique_twig from the bundle




## Class DictParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class FloatArrayParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### append
```py

def append(self, value)

```



        


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_default\_unit
```py

def get_default_unit(self)

```



### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_limits
```py

def get_limits(self)

```



### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_quantity
```py

def get_quantity(self, *args, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type


### get\_timederiv
```py

def get_timederiv(self)

```



        


### get\_value
```py

def get_value(self, unit=None, t=None, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type


### interp\_value
```py

def interp_value(self, **kwargs)

```



Interpolate to find the value in THIS array given a value from
ANOTHER array in the SAME parent :class:`ParameterSet`

This currently only supports simple 1d linear interpolation (via
numpy.interp) and does no checks to make sure you're interpolating
with respect to an independent parameter - so use with caution.

>>> print this_param.get_parent_ps().qualifiers
>>> 'other_qualifier' in this_param.get_parent_ps().qualifiers
True
>>> this_param.interp_value(other_qualifier=5)

where other_qualifier must be in this_param.get_parent_ps().qualifiers
AND must point to another FloatArrayParameter.

Example:

>>> b['flux@lc01@model'].interp_value(time=10.2)

NOTE: Interpolation by phase is not currently supported - but you can use
:meth:`phoebe.frontend.bundle.Bundle.to_time` to convert to a valid
time first (just make sure its in the bounds of the time array).

NOTE: this method does not currently support units.  You must provide
the interpolating value in its default units and are returned the
value in the default units (no support for quantities).

:parameter **kwargs: see examples above, must provide a single
    qualifier-value pair to use for interpolation.  In most cases
    this will probably be time=value or wavelength=value.
:raises KeyError: if more than one qualifier is passed
:raises KeyError: if no qualifier is passed that belongs to the
    parent :class:`ParameterSet`
:raises KeyError: if the qualifier does not point to another
    :class:`FloatArrayParameter`


### set\_default\_unit
```py

def set_default_unit(self, unit)

```



        


### set\_index\_value
```py

def set_index_value(self, index, value, **kwargs)

```



        


### set\_limits
```py

def set_limits(self, limits=(None, None))

```



### set\_quantity
```py

def set_quantity(self, *args, **kwargs)

```



If unit is not provided, will default to self.default_unit.
Units can either be provided by passing a astropy.Quantity (value * astropy.units.Unit)
as value, or by passing the astropy.units.Unit to unit.  If units are provided with both
but do not agree, an error will be raised.

:parameter value: new value
:type value: depends on cast_type
:parameter unit: unit of the provided value (will not change default_unit)
:type unit: astropy.units.Unit
:parameter bool run_checks: whether to see if the new value will be expected
    to cause the system to be non-computable (will not raise an error, but
    will cause a warning in the logger)


### set\_timederiv
```py

def set_timederiv(self, timederiv)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, value, unit=None, force=False, run_checks=None, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter


### within\_limits
```py

def within_limits(self, value)

```



check whether a value falls within the set limits

:parameter value: float or Quantity to test.  If value is a float, it is
    assumed that it has the same units as default_units




## Class FloatParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`

additional options:
default_unit


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_default\_unit
```py

def get_default_unit(self)

```



### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_limits
```py

def get_limits(self)

```



### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_quantity
```py

def get_quantity(self, *args, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type


### get\_timederiv
```py

def get_timederiv(self)

```



        


### get\_value
```py

def get_value(self, unit=None, t=None, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type


### set\_default\_unit
```py

def set_default_unit(self, unit)

```



        


### set\_limits
```py

def set_limits(self, limits=(None, None))

```



### set\_quantity
```py

def set_quantity(self, *args, **kwargs)

```



If unit is not provided, will default to self.default_unit.
Units can either be provided by passing a astropy.Quantity (value * astropy.units.Unit)
as value, or by passing the astropy.units.Unit to unit.  If units are provided with both
but do not agree, an error will be raised.

:parameter value: new value
:type value: depends on cast_type
:parameter unit: unit of the provided value (will not change default_unit)
:type unit: astropy.units.Unit
:parameter bool run_checks: whether to see if the new value will be expected
    to cause the system to be non-computable (will not raise an error, but
    will cause a warning in the logger)


### set\_timederiv
```py

def set_timederiv(self, timederiv)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, value, unit=None, force=False, run_checks=None, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter


### within\_limits
```py

def within_limits(self, value)

```



check whether a value falls within the set limits

:parameter value: float or Quantity to test.  If value is a float, it is
    assumed that it has the same units as default_units




## Class HierarchyParameter
None
### \_\_init\_\_
```py

def __init__(self, value, **kwargs)

```



see :meth:`Parameter.__init__`


### change\_component
```py

def change_component(self, old_component, new_component)

```



        


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_child\_of
```py

def get_child_of(self, component, ind, kind=None)

```



get a child (by index) of a given component


### get\_children\_of
```py

def get_children_of(self, component, kind=None)

```



get to component labels of the children of a given component


### get\_components
```py

def get_components(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_kind\_of
```py

def get_kind_of(self, component)

```



        


### get\_meshables
```py

def get_meshables(self)

```



return a list of components that are meshable (generally stars, but handles
    the envelope for an contact_binary)


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_orbits
```py

def get_orbits(self)

```



get 'component' of all orbits in order primary -> secondary


### get\_parent\_of
```py

def get_parent_of(self, component)

```



        


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_primary\_or\_secondary
```py

def get_primary_or_secondary(self, component, return_ind=False)

```



return whether a given component is the 'primary' or 'secondary'
component in its parent orbit


### get\_sibling\_of
```py

def get_sibling_of(self, component, kind=None)

```



        


### get\_siblings\_of
```py

def get_siblings_of(self, component, kind=None)

```



        


### get\_stars
```py

def get_stars(self)

```



get 'component' of all stars in order primary -> secondary


### get\_stars\_of\_children\_of
```py

def get_stars_of_children_of(self, component)

```



same as get_children_of except if any of the children are orbits, this will recursively
follow the tree to return a list of all children (grandchildren, etc) stars under that orbit


### get\_stars\_of\_sibling\_of
```py

def get_stars_of_sibling_of(self, component)

```



same as get_sibling_of except if the sibling is an orbit, this will recursively
follow the tree to return a list of all stars under that orbit


### get\_top
```py

def get_top(self)

```



        


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### is\_binary
```py

def is_binary(self, component)

```



especially useful for constraints

tells whether any component (star, envelope) is part of a binary
by checking its parent


### is\_contact\_binary
```py

def is_contact_binary(self, component)

```



especially useful for constraints

tells whether any component (star, envelope) is part of a contact_binary
by checking its siblings for an envelope


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class HistoryParameter
None
### \_\_init\_\_
```py

def __init__(self, bundle, redo_func, redo_kwargs, undo_func, undo_kwargs, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_affected\_params
```py

def get_affected_params(self, return_twigs=False)

```



        


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @update_if_client decorator.
Please see the individual classes documentation:

    * :meth:`FloatParameter.get_value`
    * :meth:`ArrayParameter.get_value`
    * :meth:`HierarchyParameter.get_value`
    * :meth:`IntParameter.get_value`
    * :meth:`BoolParameter.get_value`
    * :meth:`ChoiceParameter.get_value`
    * :meth:`ConstraintParameter.get_value`
    * :meth:`HistoryParameter.get_value`

If subclassing, this method needs to:
    * cast to the correct type/units, handling defaults

:raises NotImplementedError: because this must be subclassed


### redo
```py

def redo(self)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @send_if_client decorator
Please see the individual classes for documentation:

    * :meth:`FloatParameter.set_value`
    * :meth:`ArrayParameter.set_value`
    * :meth:`HierarchyParameter.set_value`
    * :meth:`IntParameter.set_value`
    * :meth:`BoolParameter.set_value`
    * :meth:`ChoiceParameter.set_value`
    * :meth:`ConstraintParameter.set_value`
    * :meth:`HistoryParameter.set_value`

If subclassing, this method needs to:
    * check the inputs for the correct format/agreement/cast_type
    * make sure that converting back to default_unit will work (if applicable)
    * make sure that in choices (if a choose)
    * make sure that not out of limits
    * make sure that not out of prior ??

:raises NotImplementedError: because this must be subclassed


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



        


### undo
```py

def undo(self)

```



        




## Class IntArrayParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



### append
```py

def append(self, value)

```



        


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_default\_unit
```py

def get_default_unit(self)

```



### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_limits
```py

def get_limits(self)

```



### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_quantity
```py

def get_quantity(self, *args, **kwargs)

```



IntParameters don't have units, but we may want a Quantity object returned nonetheless


### get\_timederiv
```py

def get_timederiv(self)

```



        


### get\_value
```py

def get_value(self, unit=None, t=None, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type


### interp\_value
```py

def interp_value(self, **kwargs)

```



Interpolate to find the value in THIS array given a value from
ANOTHER array in the SAME parent :class:`ParameterSet`

This currently only supports simple 1d linear interpolation (via
numpy.interp) and does no checks to make sure you're interpolating
with respect to an independent parameter - so use with caution.

>>> print this_param.get_parent_ps().qualifiers
>>> 'other_qualifier' in this_param.get_parent_ps().qualifiers
True
>>> this_param.interp_value(other_qualifier=5)

where other_qualifier must be in this_param.get_parent_ps().qualifiers
AND must point to another FloatArrayParameter.

Example:

>>> b['flux@lc01@model'].interp_value(time=10.2)

NOTE: Interpolation by phase is not currently supported - but you can use
:meth:`phoebe.frontend.bundle.Bundle.to_time` to convert to a valid
time first (just make sure its in the bounds of the time array).

NOTE: this method does not currently support units.  You must provide
the interpolating value in its default units and are returned the
value in the default units (no support for quantities).

:parameter **kwargs: see examples above, must provide a single
    qualifier-value pair to use for interpolation.  In most cases
    this will probably be time=value or wavelength=value.
:raises KeyError: if more than one qualifier is passed
:raises KeyError: if no qualifier is passed that belongs to the
    parent :class:`ParameterSet`
:raises KeyError: if the qualifier does not point to another
    :class:`FloatArrayParameter`


### set\_default\_unit
```py

def set_default_unit(self, unit)

```



        


### set\_index\_value
```py

def set_index_value(self, index, value, **kwargs)

```



        


### set\_limits
```py

def set_limits(self, limits=(None, None))

```



### set\_quantity
```py

def set_quantity(self, *args, **kwargs)

```



If unit is not provided, will default to self.default_unit.
Units can either be provided by passing a astropy.Quantity (value * astropy.units.Unit)
as value, or by passing the astropy.units.Unit to unit.  If units are provided with both
but do not agree, an error will be raised.

:parameter value: new value
:type value: depends on cast_type
:parameter unit: unit of the provided value (will not change default_unit)
:type unit: astropy.units.Unit
:parameter bool run_checks: whether to see if the new value will be expected
    to cause the system to be non-computable (will not raise an error, but
    will cause a warning in the logger)


### set\_timederiv
```py

def set_timederiv(self, timederiv)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter


### within\_limits
```py

def within_limits(self, value)

```



check whether a value falls within the set limits

:parameter value: float or Quantity to test.  If value is a float, it is
    assumed that it has the same units as default_units




## Class IntParameter
None
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_limits
```py

def get_limits(self)

```



### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_limits
```py

def set_limits(self, limits=(None, None))

```



### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter


### within\_limits
```py

def within_limits(self, value)

```



check whether a value falls within the set limits

:parameter value: float or Quantity to test.  If value is a float, it is
    assumed that it has the same units as default_units




## Class JobParameter
Parameter that tracks a submitted job (detached run_compute or run_fitting)
### \_\_init\_\_
```py

def __init__(self, b, location, status_method, retrieve_method, server_status=None, **kwargs)

```



see :meth:`Parameter.__init__`


### attach
```py

def attach(self, sleep=5, cleanup=True)

```



:parameter int sleep: number of seconds to sleep between status checks
:parameter bool cleanup: whether to delete this parameter and any temporary
    files once the results are loaded (default: True)
:raises ValueError: if not attached to a bundle
:raises NotImplementedError: because it isn't


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_status
```py

def get_status(self)

```



[NOT IMPLEMENTED]


### get\_value
```py

def get_value(self)

```



JobParameter doesn't really have a value, but for the sake of Parameter
representations, we'll provide the current status.

Also see:
    * :meth:`location`
    * :meth:`status_method`
    * :meth:`retrieve_method`
    * :meth:`status`
    * :meth:`attach`


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



JobParameter is read-only

:raises NotImplementedError: because this never will be


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class LineCollection
All parameters must be sequences or scalars; if scalars, they will
be converted to sequences.  The property of the ith line
segment is::

   prop[i % len(props)]

i.e., the properties cycle if the ``len`` of props is less than the
number of segments.
### \_\_init\_\_
```py

def __init__(self, segments, linewidths=None, colors=None, antialiaseds=None, linestyles=u'solid', offsets=None, transOffset=None, norm=None, cmap=None, pickradius=5, zorder=2, facecolors=u'none', **kwargs)

```



*segments*
    a sequence of (*line0*, *line1*, *line2*), where::

        linen = (x0, y0), (x1, y1), ... (xm, ym)

    or the equivalent numpy array with two columns. Each line
    can be a different length.

*colors*
    must be a sequence of RGBA tuples (e.g., arbitrary color
    strings, etc, not allowed).

*antialiaseds*
    must be a sequence of ones or zeros

*linestyles* [ 'solid' | 'dashed' | 'dashdot' | 'dotted' ]
    a string or dash tuple. The dash tuple is::

        (offset, onoffseq),

    where *onoffseq* is an even length tuple of on and off ink
    in points.

If *linewidths*, *colors*, or *antialiaseds* is None, they
default to their rcParams setting, in sequence form.

If *offsets* and *transOffset* are not None, then
*offsets* are transformed by *transOffset* and applied after
the segments have been transformed to display coordinates.

If *offsets* is not None but *transOffset* is None, then the
*offsets* are added to the segments before any transformation.
In this case, a single offset can be specified as::

    offsets=(xo,yo)

and this value will be added cumulatively to each successive
segment, so as to produce a set of successively offset curves.

*norm*
    None (optional for :class:`matplotlib.cm.ScalarMappable`)
*cmap*
    None (optional for :class:`matplotlib.cm.ScalarMappable`)

*pickradius* is the tolerance for mouse clicks picking a line.
The default is 5 pt.

*zorder*
   The zorder of the LineCollection.  Default is 2

*facecolors*
   The facecolors of the LineCollection. Default is 'none'
   Setting to a value other than 'none' will lead to a filled
   polygon being drawn between points on each line.

The use of :class:`~matplotlib.cm.ScalarMappable` is optional.
If the :class:`~matplotlib.cm.ScalarMappable` array
:attr:`~matplotlib.cm.ScalarMappable._A` is not None (i.e., a call to
:meth:`~matplotlib.cm.ScalarMappable.set_array` has been made), at
draw time a call to scalar mappable will be made to set the colors.


### add\_callback
```py

def add_callback(self, func)

```



Adds a callback function that will be called whenever one of
the :class:`Artist`'s properties changes.

Returns an *id* that is useful for removing the callback with
:meth:`remove_callback` later.


### add\_checker
```py

def add_checker(self, checker)

```



Add an entry to a dictionary of boolean flags
that are set to True when the mappable is changed.


### autoscale
```py

def autoscale(self)

```



Autoscale the scalar limits on the norm instance using the
current array


### autoscale\_None
```py

def autoscale_None(self)

```



Autoscale the scalar limits on the norm instance using the
current array, changing only limits that are None


### changed
```py

def changed(self)

```



Call this whenever the mappable is changed to notify all the
callbackSM listeners to the 'changed' signal


### check\_update
```py

def check_update(self, checker)

```



If mappable has changed since the last check,
return True; else return False


### contains
```py

def contains(self, mouseevent)

```



Test whether the mouse event occurred in the collection.

Returns True | False, ``dict(ind=itemlist)``, where every
item in itemlist contains the event.


### convert\_xunits
```py

def convert_xunits(self, x)

```



For artists in an axes, if the xaxis has units support,
convert *x* using xaxis unit type


### convert\_yunits
```py

def convert_yunits(self, y)

```



For artists in an axes, if the yaxis has units support,
convert *y* using yaxis unit type


### draw
```py

def draw(artist, renderer, *args, **kwargs)

```



### findobj
```py

def findobj(self, match=None, include_self=True)

```



Find artist objects.

Recursively find all :class:`~matplotlib.artist.Artist` instances
contained in self.

*match* can be

  - None: return all objects contained in artist.

  - function with signature ``boolean = match(artist)``
    used to filter matches

  - class instance: e.g., Line2D.  Only return artists of class type.

If *include_self* is True (default), include self in the list to be
checked for a match.


### format\_cursor\_data
```py

def format_cursor_data(self, data)

```



Return *cursor data* string formatted.


### get\_agg\_filter
```py

def get_agg_filter(self)

```



Return filter function to be used for agg filter.


### get\_alpha
```py

def get_alpha(self)

```



Return the alpha value used for blending - not supported on all
backends


### get\_animated
```py

def get_animated(self)

```



Return the artist's animated state


### get\_array
```py

def get_array(self)

```



Return the array


### get\_children
```py

def get_children(self)

```



Return a list of the child :class:`Artist`s this
:class:`Artist` contains.


### get\_clim
```py

def get_clim(self)

```



return the min, max of the color limits for image scaling


### get\_clip\_box
```py

def get_clip_box(self)

```



Return artist clipbox


### get\_clip\_on
```py

def get_clip_on(self)

```



Return whether artist uses clipping


### get\_clip\_path
```py

def get_clip_path(self)

```



Return artist clip path


### get\_cmap
```py

def get_cmap(self)

```



return the colormap


### get\_color
```py

def get_color(self)

```



### get\_colors
```py

def get_colors(self)

```



### get\_contains
```py

def get_contains(self)

```



Return the _contains test used by the artist, or *None* for default.


### get\_cursor\_data
```py

def get_cursor_data(self, event)

```



Get the cursor data for a given event.


### get\_dashes
```py

def get_dashes(self)

```



### get\_datalim
```py

def get_datalim(self, transData)

```



### get\_edgecolor
```py

def get_edgecolor(self)

```



### get\_edgecolors
```py

def get_edgecolors(self)

```



### get\_facecolor
```py

def get_facecolor(self)

```



### get\_facecolors
```py

def get_facecolors(self)

```



### get\_figure
```py

def get_figure(self)

```



Return the `~.Figure` instance the artist belongs to.


### get\_fill
```py

def get_fill(self)

```



return whether fill is set


### get\_gid
```py

def get_gid(self)

```



Returns the group id.


### get\_hatch
```py

def get_hatch(self)

```



Return the current hatching pattern.


### get\_label
```py

def get_label(self)

```



Get the label used for this artist in the legend.


### get\_linestyle
```py

def get_linestyle(self)

```



### get\_linestyles
```py

def get_linestyles(self)

```



### get\_linewidth
```py

def get_linewidth(self)

```



### get\_linewidths
```py

def get_linewidths(self)

```



### get\_offset\_position
```py

def get_offset_position(self)

```



Returns how offsets are applied for the collection.  If
*offset_position* is 'screen', the offset is applied after the
master transform has been applied, that is, the offsets are in
screen coordinates.  If offset_position is 'data', the offset
is applied before the master transform, i.e., the offsets are
in data coordinates.


### get\_offset\_transform
```py

def get_offset_transform(self)

```



### get\_offsets
```py

def get_offsets(self)

```



Return the offsets for the collection.


### get\_path\_effects
```py

def get_path_effects(self)

```



### get\_paths
```py

def get_paths(self)

```



### get\_picker
```py

def get_picker(self)

```



Return the picker object used by this artist.


### get\_pickradius
```py

def get_pickradius(self)

```



### get\_rasterized
```py

def get_rasterized(self)

```



Return whether the artist is to be rasterized.


### get\_segments
```py

def get_segments(self)

```



### get\_sketch\_params
```py

def get_sketch_params(self)

```



Returns the sketch parameters for the artist.

Returns
-------
sketch_params : tuple or `None`

A 3-tuple with the following elements:

  * `scale`: The amplitude of the wiggle perpendicular to the
    source line.

  * `length`: The length of the wiggle along the line.

  * `randomness`: The scale factor by which the length is
    shrunken or expanded.

May return `None` if no sketch parameters were set.


### get\_snap
```py

def get_snap(self)

```



Returns the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.


### get\_transform
```py

def get_transform(self)

```



Return the :class:`~matplotlib.transforms.Transform`
instance used by this artist.


### get\_transformed\_clip\_path\_and\_affine
```py

def get_transformed_clip_path_and_affine(self)

```



Return the clip path with the non-affine part of its
transformation applied, and the remaining affine part of its
transformation.


### get\_transforms
```py

def get_transforms(self)

```



### get\_url
```py

def get_url(self)

```



Returns the url.


### get\_urls
```py

def get_urls(self)

```



### get\_visible
```py

def get_visible(self)

```



Return the artist's visiblity


### get\_window\_extent
```py

def get_window_extent(self, renderer)

```



### get\_zorder
```py

def get_zorder(self)

```



Return the artist's zorder.


### have\_units
```py

def have_units(self)

```



Return *True* if units are set on the *x* or *y* axes


### hitlist
```py

def hitlist(self, event)

```



List the children of the artist which contain the mouse event *event*.


### is\_figure\_set
```py

def is_figure_set(self)

```



Returns whether the artist is assigned to a `~.Figure`.


### is\_transform\_set
```py

def is_transform_set(self)

```



Returns *True* if :class:`Artist` has a transform explicitly
set.


### pchanged
```py

def pchanged(self)

```



Fire an event when property changed, calling all of the
registered callbacks.


### pick
```py

def pick(self, mouseevent)

```



Process pick event

each child artist will fire a pick event if *mouseevent* is over
the artist and the artist has picker set


### pickable
```py

def pickable(self)

```



Return *True* if :class:`Artist` is pickable.


### properties
```py

def properties(self)

```



return a dictionary mapping property name -> value for all Artist props


### remove
```py

def remove(self)

```



Remove the artist from the figure if possible.  The effect
will not be visible until the figure is redrawn, e.g., with
:meth:`matplotlib.axes.Axes.draw_idle`.  Call
:meth:`matplotlib.axes.Axes.relim` to update the axes limits
if desired.

Note: :meth:`~matplotlib.axes.Axes.relim` will not see
collections even if the collection was added to axes with
*autolim* = True.

Note: there is no support for removing the artist's legend entry.


### remove\_callback
```py

def remove_callback(self, oid)

```



Remove a callback based on its *id*.

.. seealso::

    :meth:`add_callback`
       For adding callbacks


### set
```py

def set(self, **kwargs)

```



A property batch setter. Pass *kwargs* to set properties.
        


### set\_agg\_filter
```py

def set_agg_filter(self, filter_func)

```



Set the agg filter.

Parameters
----------
filter_func : callable
    A filter function, which takes a (m, n, 3) float array and a dpi
    value, and returns a (m, n, 3) array.

    ..
        ACCEPTS: a filter function, which takes a (m, n, 3) float array
        and a dpi value, and returns a (m, n, 3) array


### set\_alpha
```py

def set_alpha(self, alpha)

```



Set the alpha tranparencies of the collection.  *alpha* must be
a float or *None*.

ACCEPTS: float or None


### set\_animated
```py

def set_animated(self, b)

```



Set the artist's animation state.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_antialiased
```py

def set_antialiased(self, aa)

```



Set the antialiasing state for rendering.

ACCEPTS: Boolean or sequence of booleans


### set\_antialiaseds
```py

def set_antialiaseds(self, aa)

```



alias for set_antialiased


### set\_array
```py

def set_array(self, A)

```



Set the image array from numpy array *A*.

..
    ACCEPTS: ndarray

Parameters
----------
A : ndarray


### set\_clim
```py

def set_clim(self, vmin=None, vmax=None)

```



set the norm limits for image scaling; if *vmin* is a length2
sequence, interpret it as ``(vmin, vmax)`` which is used to
support setp

ACCEPTS: a length 2 sequence of floats


### set\_clip\_box
```py

def set_clip_box(self, clipbox)

```



Set the artist's clip `~.Bbox`.

Parameters
----------
clipbox : `~.Bbox`
    ..
        ACCEPTS: a `~.Bbox` instance


### set\_clip\_on
```py

def set_clip_on(self, b)

```



Set whether artist uses clipping.

When False artists will be visible out side of the axes which
can lead to unexpected results.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_clip\_path
```py

def set_clip_path(self, path, transform=None)

```



Set the artist's clip path, which may be:

- a :class:`~matplotlib.patches.Patch` (or subclass) instance; or
- a :class:`~matplotlib.path.Path` instance, in which case a
  :class:`~matplotlib.transforms.Transform` instance, which will be
  applied to the path before using it for clipping, must be provided;
  or
- ``None``, to remove a previously set clipping path.

For efficiency, if the path happens to be an axis-aligned rectangle,
this method will set the clipping box to the corresponding rectangle
and set the clipping path to ``None``.

ACCEPTS: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None]


### set\_cmap
```py

def set_cmap(self, cmap)

```



set the colormap for luminance data

ACCEPTS: a colormap or registered colormap name


### set\_color
```py

def set_color(self, c)

```



Set the color(s) of the line collection.  *c* can be a
matplotlib color arg (all patches have same color), or a
sequence or rgba tuples; if it is a sequence the patches will
cycle through the sequence.

ACCEPTS: matplotlib color arg or sequence of rgba tuples


### set\_contains
```py

def set_contains(self, picker)

```



Replace the contains test used by this artist. The new picker
should be a callable function which determines whether the
artist is hit by the mouse event::

    hit, props = picker(artist, mouseevent)

If the mouse event is over the artist, return *hit* = *True*
and *props* is a dictionary of properties you want returned
with the contains test.

Parameters
----------
picker : callable
    ..
        ACCEPTS: a callable function


### set\_dashes
```py

def set_dashes(self, ls)

```



alias for set_linestyle


### set\_edgecolor
```py

def set_edgecolor(self, c)

```



Set the edgecolor(s) of the collection. *c* can be a
matplotlib color spec (all patches have same color), or a
sequence of specs; if it is a sequence the patches will
cycle through the sequence.

If *c* is 'face', the edge color will always be the same as
the face color.  If it is 'none', the patch boundary will not
be drawn.

ACCEPTS: matplotlib color spec or sequence of specs


### set\_edgecolors
```py

def set_edgecolors(self, c)

```



alias for set_edgecolor


### set\_facecolor
```py

def set_facecolor(self, c)

```



Set the facecolor(s) of the collection.  *c* can be a
matplotlib color spec (all patches have same color), or a
sequence of specs; if it is a sequence the patches will
cycle through the sequence.

If *c* is 'none', the patch will not be filled.

ACCEPTS: matplotlib color spec or sequence of specs


### set\_facecolors
```py

def set_facecolors(self, c)

```



alias for set_facecolor


### set\_figure
```py

def set_figure(self, fig)

```



Set the `~.Figure` instance the artist belongs to.

Parameters
----------
fig : `~.Figure`
    ..
        ACCEPTS: a `~.Figure` instance


### set\_gid
```py

def set_gid(self, gid)

```



Sets the (group) id for the artist.

Parameters
----------
gid : str
    ..
        ACCEPTS: an id string


### set\_hatch
```py

def set_hatch(self, hatch)

```



Set the hatching pattern

*hatch* can be one of::

  /   - diagonal hatching
  \   - back diagonal
  |   - vertical
  -   - horizontal
  +   - crossed
  x   - crossed diagonal
  o   - small circle
  O   - large circle
  .   - dots
  *   - stars

Letters can be combined, in which case all the specified
hatchings are done.  If same letter repeats, it increases the
density of hatching of that pattern.

Hatching is supported in the PostScript, PDF, SVG and Agg
backends only.

Unlike other properties such as linewidth and colors, hatching
can only be specified for the collection as a whole, not separately
for each member.

ACCEPTS: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ]


### set\_label
```py

def set_label(self, s)

```



Set the label to *s* for auto legend.

Parameters
----------
s : object
    *s* will be converted to a string by calling `str` (`unicode` on
    Py2).

    ..
        ACCEPTS: object


### set\_linestyle
```py

def set_linestyle(self, ls)

```



Set the linestyle(s) for the collection.

===========================   =================
linestyle                     description
===========================   =================
``'-'`` or ``'solid'``        solid line
``'--'`` or  ``'dashed'``     dashed line
``'-.'`` or  ``'dashdot'``    dash-dotted line
``':'`` or ``'dotted'``       dotted line
===========================   =================

Alternatively a dash tuple of the following form can be provided::

    (offset, onoffseq),

where ``onoffseq`` is an even length tuple of on and off ink
in points.

ACCEPTS: ['solid' | 'dashed', 'dashdot', 'dotted' |
           (offset, on-off-dash-seq) |
           ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` |
           ``' '`` | ``''``]

Parameters
----------
ls : { '-',  '--', '-.', ':'} and more see description
    The line style.


### set\_linestyles
```py

def set_linestyles(self, ls)

```



alias for set_linestyle


### set\_linewidth
```py

def set_linewidth(self, lw)

```



Set the linewidth(s) for the collection.  *lw* can be a scalar
or a sequence; if it is a sequence the patches will cycle
through the sequence

ACCEPTS: float or sequence of floats


### set\_linewidths
```py

def set_linewidths(self, lw)

```



alias for set_linewidth


### set\_lw
```py

def set_lw(self, lw)

```



alias for set_linewidth


### set\_norm
```py

def set_norm(self, norm)

```



Set the normalization instance.

..
    ACCEPTS: `~.Normalize`

Parameters
----------
norm : `~.Normalize`


### set\_offset\_position
```py

def set_offset_position(self, offset_position)

```



Set how offsets are applied.  If *offset_position* is 'screen'
(default) the offset is applied after the master transform has
been applied, that is, the offsets are in screen coordinates.
If offset_position is 'data', the offset is applied before the
master transform, i.e., the offsets are in data coordinates.

..
    ACCEPTS: [ 'screen' | 'data' ]


### set\_offsets
```py

def set_offsets(self, offsets)

```



Set the offsets for the collection.  *offsets* can be a scalar
or a sequence.

ACCEPTS: float or sequence of floats


### set\_path\_effects
```py

def set_path_effects(self, path_effects)

```



Set the path effects.

Parameters
----------
path_effects : `~.AbstractPathEffect`
    ..
        ACCEPTS: `~.AbstractPathEffect`


### set\_paths
```py

def set_paths(self, segments)

```



### set\_picker
```py

def set_picker(self, picker)

```



Set the epsilon for picking used by this artist

*picker* can be one of the following:

  * *None*: picking is disabled for this artist (default)

  * A boolean: if *True* then picking will be enabled and the
    artist will fire a pick event if the mouse event is over
    the artist

  * A float: if picker is a number it is interpreted as an
    epsilon tolerance in points and the artist will fire
    off an event if it's data is within epsilon of the mouse
    event.  For some artists like lines and patch collections,
    the artist may provide additional data to the pick event
    that is generated, e.g., the indices of the data within
    epsilon of the pick event

  * A function: if picker is callable, it is a user supplied
    function which determines whether the artist is hit by the
    mouse event::

      hit, props = picker(artist, mouseevent)

    to determine the hit test.  if the mouse event is over the
    artist, return *hit=True* and props is a dictionary of
    properties you want added to the PickEvent attributes.

Parameters
----------
picker : None or bool or float or callable
    ..
        ACCEPTS: [None | bool | float | callable]


### set\_pickradius
```py

def set_pickradius(self, pr)

```



Set the pick radius used for containment tests.

..
    ACCEPTS: float distance in points

Parameters
----------
d : float
    Pick radius, in points.


### set\_rasterized
```py

def set_rasterized(self, rasterized)

```



Force rasterized (bitmap) drawing in vector backend output.

Defaults to None, which implies the backend's default behavior.

Parameters
----------
rasterized : bool or None
    ..
        ACCEPTS: bool or None


### set\_segments
```py

def set_segments(self, segments)

```



### set\_sketch\_params
```py

def set_sketch_params(self, scale=None, length=None, randomness=None)

```



Sets the sketch parameters.

Parameters
----------

scale : float, optional
    The amplitude of the wiggle perpendicular to the source
    line, in pixels.  If scale is `None`, or not provided, no
    sketch filter will be provided.

length : float, optional
     The length of the wiggle along the line, in pixels
     (default 128.0)

randomness : float, optional
    The scale factor by which the length is shrunken or
    expanded (default 16.0)

    ..
        ACCEPTS: (scale: float, length: float, randomness: float)


### set\_snap
```py

def set_snap(self, snap)

```



Sets the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

Parameters
----------
snap : bool or None
    ..
        ACCEPTS: bool or None


### set\_transform
```py

def set_transform(self, t)

```



Set the artist transform.

Parameters
----------
t : `~.Transform`
    ..
        ACCEPTS: `~.Transform`


### set\_url
```py

def set_url(self, url)

```



Sets the url for the artist.

Parameters
----------
url : str
    ..
        ACCEPTS: a url string


### set\_urls
```py

def set_urls(self, urls)

```



Parameters
----------
urls : List[str] or None
    ..
        ACCEPTS: List[str] or None


### set\_verts
```py

def set_verts(self, segments)

```



### set\_visible
```py

def set_visible(self, b)

```



Set the artist's visibility.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_zorder
```py

def set_zorder(self, level)

```



Set the zorder for the artist.  Artists with lower zorder
values are drawn first.

Parameters
----------
level : float
    ..
        ACCEPTS: float


### to\_rgba
```py

def to_rgba(self, x, alpha=None, bytes=False, norm=True)

```



Return a normalized rgba array corresponding to *x*.

In the normal case, *x* is a 1-D or 2-D sequence of scalars, and
the corresponding ndarray of rgba values will be returned,
based on the norm and colormap set for this ScalarMappable.

There is one special case, for handling images that are already
rgb or rgba, such as might have been read from an image file.
If *x* is an ndarray with 3 dimensions,
and the last dimension is either 3 or 4, then it will be
treated as an rgb or rgba array, and no mapping will be done.
The array can be uint8, or it can be floating point with
values in the 0-1 range; otherwise a ValueError will be raised.
If it is a masked array, the mask will be ignored.
If the last dimension is 3, the *alpha* kwarg (defaulting to 1)
will be used to fill in the transparency.  If the last dimension
is 4, the *alpha* kwarg is ignored; it does not
replace the pre-existing alpha.  A ValueError will be raised
if the third dimension is other than 3 or 4.

In either case, if *bytes* is *False* (default), the rgba
array will be floats in the 0-1 range; if it is *True*,
the returned rgba array will be uint8 in the 0 to 255 range.

If norm is False, no normalization of the input data is
performed, and it is assumed to be in the range (0-1).


### update
```py

def update(self, props)

```



Update this artist's properties from the dictionary *prop*.


### update\_from
```py

def update_from(self, other)

```



copy properties from other to self


### update\_scalarmappable
```py

def update_scalarmappable(self)

```



If the scalar mappable array is not none, update colors
from scalar data




## Class OrderedDict
Dictionary that remembers insertion order
### \_\_init\_\_
```py

def __init__(*args, **kwds)

```



Initialize an ordered dictionary.  The signature is the same as
regular dictionaries, but keyword arguments are not recommended because
their insertion order is arbitrary.


### clear
```py

def clear(self)

```



od.clear() -> None.  Remove all items from od.


### copy
```py

def copy(self)

```



od.copy() -> a shallow copy of od


### fromkeys
```py

def fromkeys(cls, iterable, value=None)

```



OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
If not specified, the value defaults to None.


### items
```py

def items(self)

```



od.items() -> list of (key, value) pairs in od


### iteritems
```py

def iteritems(self)

```



od.iteritems -> an iterator over the (key, value) pairs in od


### iterkeys
```py

def iterkeys(self)

```



od.iterkeys() -> an iterator over the keys in od


### itervalues
```py

def itervalues(self)

```



od.itervalues -> an iterator over the values in od


### keys
```py

def keys(self)

```



od.keys() -> list of keys in od


### pop
```py

def pop(self, key, default=<object object at 0x7fa130066090>)

```



od.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise KeyError
is raised.


### popitem
```py

def popitem(self, last=True)

```



od.popitem() -> (k, v), return and remove a (key, value) pair.
Pairs are returned in LIFO order if last is true or FIFO order if false.


### setdefault
```py

def setdefault(self, key, default=None)

```



od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od


### update
```py

def update(*args, **kwds)

```



D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


### values
```py

def values(self)

```



od.values() -> list of values in od


### viewitems
```py

def viewitems(self)

```



od.viewitems() -> a set-like object providing a view on od's items


### viewkeys
```py

def viewkeys(self)

```



od.viewkeys() -> a set-like object providing a view on od's keys


### viewvalues
```py

def viewvalues(self)

```



od.viewvalues() -> an object providing a view on od's values




## Class Parameter
None
### \_\_init\_\_
```py

def __init__(self, qualifier, value=None, description='', **kwargs)

```



This is a generic class for a Parameter.  Any Parameter that
will actually be usable will be a subclass of this class.

Parameters are the base of PHOEBE and hold, at the minimum,
the value of the parameter, a description, and meta-tags
which are used to collect and filter a list of Parameters
inside a ParameterSet.

Some subclasses of Parameter can add additional methods
or attributes.  For example :class:`FloatParameter` handles
converting units and storing a default_unit.


Any subclass of Parameter must (at the minimum):
- method for get_value
- method for set_value,
- call to set_value in the overload of __init__
- self._dict_fields_other defined in __init__
- self._dict_fields = _meta_fields_all + self._dict_fields_other in __init__

:parameter value: value to initialize the parameter
:parameter str description: description of the parameter
:parameter bundle: (optional) parent :class:`phoebe.frontend.bundle.Bundle`
:parameter str uniqueid: uniqueid for the parameter (suggested to leave blank
    and a random string will be generated)

:parameter float time: (optional) value for the time tag
:parameter str history: (optional) label for the history tag
:parameter str feature: (optional) label for the feature tag
:parameter str component: (optional) label for the component tag
:parameter str dataset: (optional) label for the dataset tag
:parameter str constraint: (optional) label for the constraint tag
:parameter str compute: (optional) label for the compute tag
:parameter str model: (optional) label for the model tag
:parameter str fitting: (optional) label for the fitting tag
:parameter str feedback: (optional) label for the feedback tag
:parameter str plugin: (optional) label for the plugin tag
:parameter str kind: (optional) label for the kind tag
:parameter str context: (optional) which context this parameter belongs in

:parameter copy_for: (optional) dictionary of filter arguments for which this
    parameter must be copied (use with caution)
:type copy_for: dict or False
:parameter str visible_if: (optional) string to check the value of another
    parameter holding the same meta-tags (except qualifier) to determine
    whether this parameter is visible and therefore shown in filters
    (example: visible_if='otherqualifier:True')


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @update_if_client decorator.
Please see the individual classes documentation:

    * :meth:`FloatParameter.get_value`
    * :meth:`ArrayParameter.get_value`
    * :meth:`HierarchyParameter.get_value`
    * :meth:`IntParameter.get_value`
    * :meth:`BoolParameter.get_value`
    * :meth:`ChoiceParameter.get_value`
    * :meth:`ConstraintParameter.get_value`
    * :meth:`HistoryParameter.get_value`

If subclassing, this method needs to:
    * cast to the correct type/units, handling defaults

:raises NotImplementedError: because this must be subclassed


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @send_if_client decorator
Please see the individual classes for documentation:

    * :meth:`FloatParameter.set_value`
    * :meth:`ArrayParameter.set_value`
    * :meth:`HierarchyParameter.set_value`
    * :meth:`IntParameter.set_value`
    * :meth:`BoolParameter.set_value`
    * :meth:`ChoiceParameter.set_value`
    * :meth:`ConstraintParameter.set_value`
    * :meth:`HistoryParameter.set_value`

If subclassing, this method needs to:
    * check the inputs for the correct format/agreement/cast_type
    * make sure that converting back to default_unit will work (if applicable)
    * make sure that in choices (if a choose)
    * make sure that not out of limits
    * make sure that not out of prior ??

:raises NotImplementedError: because this must be subclassed


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class ParameterSet
ParameterSet.

The ParameterSet is an abstract list of Parameters which can then be
filtered into another ParameterSet or Parameter by filtering on set tags of
the Parameter or on "twig" notation (a single string using '@' symbols to
separate these same tags).
### \_\_init\_\_
```py

def __init__(self, params=[])

```



Initialize a new ParameterSet.

:parameter list params: list of :class:`Parameter` to
    create the ParameterSet (optional)
:return: instantiated :class:`ParameterSet`


### animate
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


### exclude
```py

def exclude(self, twig=None, check_visible=True, **kwargs)

```



Exclude the results from this filter from the current ParameterSet.

See :meth:`filter` for options.


### filter
```py

def filter(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Filter the ParameterSet based on the meta-tags of the Parameters
and return another ParameterSet.

Because another ParameterSet is returned, these filter calls are
chainable.

>>> b.filter(context='component').filter(component='starA')

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`ParameterSet`


### filter\_or\_get
```py

def filter_or_get(self, twig=None, autocomplete=False, force_ps=False, check_visible=True, check_default=True, **kwargs)

```



Filter the :class:`ParameterSet` based on the meta-tags of its
Parameters and return another :class:`ParameterSet` unless there is
exactly 1 result, in which case the :class:`Parameter` itself is
returned (set force_ps=True to avoid this from happening or call filter
instead).

In the case when another :class:`ParameterSet` is returned, these
filter calls are chainable.

>>> b.filter_or_get(context='component').filter_or_get(component='starA')

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool force_ps: whether to force a ParameterSet
        to be returned even if only a single result is found.
        This is helpful if you want to write generic code
        that chains filter calls (since Parameter does not have
        a filter method).
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: :class:`Parameter` if length of results is exactly 1 and
    force_ps==False. Otherwise another :class:`ParameterSet` will be
    returned.


### get
```py

def get(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Get a single parameter from this ParameterSet.  This works exactly the
same as filter except there must be only a single result, and the Parameter
itself is returned instead of a ParameterSet.

Also see :meth:`get_parameter` (which is simply an alias of this method)

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`Parameter`
:raises ValueError: if either 0 or more than 1 results are found
        matching the search.


### get\_adjust
```py

def get_adjust(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### get\_default\_unit
```py

def get_default_unit(self, twig=None, **kwargs)

```



TODO: add documentation


### get\_description
```py

def get_description(self, twig=None, **kwargs)

```



TODO: add documentation


### get\_enabled
```py

def get_enabled(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



Dictionary of all meta-tags, with option to ignore certain tags.

See all the meta-tag properties that are shared by ALL Parameters.
If a given value is 'None', that means that it is not shared
among ALL Parameters.  To see the different values among the
Parameters, you can access that attribute.

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_or\_create
```py

def get_or_create(self, qualifier, new_parameter, **kwargs)

```



Get a :class:`Parameter` from the ParameterSet, if it does not exist,
create and attach it.

Note: running this on a ParameterSet that is NOT a
:class:`phoebe.frontend.bundle.Bundle`,
will NOT add the Parameter to the bundle, but only the temporary
ParameterSet

:parameter str qualifier: the qualifier of the :class:`Parameter`
    (note, not the twig)
:parameter new_parameter: the parameter to attach if no
        result is found
:type new_parameter: :class:`Parameter`
:parameter **kwargs: meta-tags to search - will also be applied to
        new_parameter if it is attached.
:return: Parameter, created
:rtype: :class:`Parameter`, bool
:raises ValueError: if more than 1 result was found using the search
        criteria.


### get\_parameter
```py

def get_parameter(self, twig=None, **kwargs)

```



Get a :class:`Parameter` from this ParameterSet.  This simply calls get

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`Parameter`
:raises ValueError: if either 0 or more than 1 results are found
        matching the search.


### get\_plotting\_info
```py

def get_plotting_info(self, twig=None, **kwargs)

```



[ADD DOCUMENTATION]


### get\_posterior
```py

def get_posterior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### get\_prior
```py

def get_prior(self, twig=None, **kwargs)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### get\_quantity
```py

def get_quantity(self, twig=None, unit=None, default=None, t=None, **kwargs)

```



TODO: add documentation


### get\_value
```py

def get_value(self, twig=None, unit=None, default=None, t=None, **kwargs)

```



Get the value of a :class:`Parameter` in this ParameterSet

:parameter str twig: the twig to search for the parameter
:parameter unit: units for the returned result (if
    applicable).  If None or not provided, the value will
    be returned in that Parameter's default_unit (if
    applicable)
:type unit: str or astropy.units.Unit
:parameter default: what to return if the parameter cannot be found.
    If this is None (default) then an error will be raised instead.
    Note that the units of default will not be converted.
:parameter time: time at which to compute the
    value (will only affect time-dependent parameters).  If provided
    as a float it is assumed that the units are the same as t0.
    NOTE: this is not fully supported yet, use with caution.
:parameter **kwargs: meta-tags to search
:return: value (type depeding on the type of the :class:`Parameter`)


### items
```py

def items(self)

```



Returns the items (key, value pairs) from :func:`to_dict`

:return: string, :class:`Parameter` or :class:`ParameterSet` pairs


### keys
```py

def keys(self)

```



Return the keys from :func:`to_dict`

:return: list of strings


### open
```py

def open(cls, filename)

```



Open a ParameterSet from a JSON-formatted file.
This is a constructor so should be called as:


>>> b = ParameterSet.open('test.json')


:parameter str filename: relative or full path to the file
:return: instantiated :class:`ParameterSet` object


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


### remove\_parameter
```py

def remove_parameter(self, twig=None, **kwargs)

```



Remove a :class:`Parameter` from the ParameterSet

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter **kwargs: meta-tags to search
:raises ValueError: if 0 or more than 1 results are found using the
        provided search criteria.


### remove\_parameters\_all
```py

def remove_parameters_all(self, twig=None, **kwargs)

```



Remove all :class:`Parameter`s that match the search from the
ParameterSet.

Any Parameter that would be included in the resulting ParameterSet
from a :func:`filter` call with the same arguments will be
removed from this ParameterSet.

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter **kwargs: meta-tags to search


### remove\_posterior
```py

def remove_posterior(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### remove\_prior
```py

def remove_prior(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### save
```py

def save(self, filename, incl_uniqueid=False)

```



Save the ParameterSet to a JSON-formatted ASCII file

:parameter str filename: relative or fullpath to the file
:return: filename
:rtype: str


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


### set
```py

def set(self, key, value, **kwargs)

```



Set the value of a Parameter in the ParameterSet.

If :func:`get` would retrieve a Parameter, this will set the
value of that parameter.

Or you can provide 'value@...' or 'default_unit@...', etc
to specify what attribute to set.

:parameter str key: the twig (called key here to be analagous
    to a normal dict)
:parameter value: value to set
:parameter **kwargs: other filter parameters (must result in
    returning a single :class:`Parameter`)
:return: the value of the :class:`Parameter` after setting the
    new value (including converting units if applicable)


### set\_adjust
```py

def set_adjust(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_adjust\_all
```py

def set_adjust_all(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_default\_unit
```py

def set_default_unit(self, twig=None, unit=None, **kwargs)

```



TODO: add documentation


### set\_default\_unit\_all
```py

def set_default_unit_all(self, twig=None, unit=None, **kwargs)

```



TODO: add documentation


### set\_enabled
```py

def set_enabled(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_meta
```py

def set_meta(self, **kwargs)

```



Set the value of tags for all Parameters in this ParameterSet.


### set\_prior
```py

def set_prior(self)

```



[NOT IMPLEMENTED]

raises NotImplementedError: because it isn't


### set\_quantity
```py

def set_quantity(self, twig=None, value=None, **kwargs)

```



TODO: add documentation


### set\_value
```py

def set_value(self, twig=None, value=None, **kwargs)

```



Set the value of a :class:`Parameter` in this ParameterSet

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the :class:`phoebe.frontend.bundle.Bundle`)

:parameter set twig: the twig to search for the parameter
:parameter value: the value to set.  Provide units, if necessary, by
    sending a Quantity object (ie 2.4*u.rad)
:parameter **kwargs: meta-tags to search
:raises ValueError:  if 0 or more than 1 results are found matching
    the search criteria.


### set\_value\_all
```py

def set_value_all(self, twig=None, value=None, check_default=False, **kwargs)

```



Set the value of all returned :class:`Parameter`s in this ParameterSet.

Any :class:`Parameter` that would be included in the resulting ParameterSet
from a :func:`filter` call with the same arguments will have
their value set.

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter value: the value to set.  Provide units, if necessary, by
        sending a Quantity object (ie 2.4*u.rad)
:parameter bool check_default: whether to exclude any default values.
        Defaults to False (unlike all filtering).  Note that this
        acts on the current ParameterSet so any filtering done before
        this call will EXCLUDE defaults by default.
:parameter **kwargs: meta-tags to search


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


### to\_dict
```py

def to_dict(self, field=None, **kwargs)

```



Convert the ParameterSet to a structured (nested) dictionary
to allow traversing the structure from the bottom up

:parameter str field: (optional) build the dictionary with keys at
    a given level/field.  Can be any of the keys in
    :func:`meta`.  If None, the keys will be the lowest
    level in which Parameters have different values.
:return: dict of :class:`Parameter`s or :class:`ParameterSet`s


### to\_flat\_dict
```py

def to_flat_dict(self, **kwargs)

```



Convert the :class:`ParameterSet` to a flat dictionary, with keys being
uniquetwigs to access the parameter and values being the :class:`Parameter`
objects themselves.

:return: dict of :class:`Parameter`s


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



Convert the ParameterSet to a json-compatible dictionary

:return: list of dictionaries


### to\_list
```py

def to_list(self, **kwargs)

```



Convert the :class:`ParameterSet` to a list of :class:`Parameter`s

:return: list of class:`Parameter` objects


### to\_list\_of\_dicts
```py

def to_list_of_dicts(self, **kwargs)

```



Convert the :class:`ParameterSet` to a list of the dictionary representation
of each :class:`Parameter`

:return: list of dicts


### ui
```py

def ui(self, client='http://localhost:4200', **kwargs)

```



[NOT IMPLEMENTED]

The bundle must be in client mode in order to open the web-interface.
See :meth:`Bundle:as_client` to switch to client mode.

:parameter str client: URL of the running client which must be connected
    to the same server as the bundle
:return: URL of the parameterset of this bundle in the client (will also
    attempt to open webbrowser)
:rtype: str


### values
```py

def values(self)

```



Return the values from :func:`to_dict`

:return: list of :class:`Parameter`s or :class:`ParameterSet`s




## Class Poly3DCollection
A collection of 3D polygons.
### \_\_init\_\_
```py

def __init__(self, verts, *args, **kwargs)

```



Create a Poly3DCollection.

*verts* should contain 3D coordinates.

Keyword arguments:
zsort, see set_zsort for options.

Note that this class does a bit of magic with the _facecolors
and _edgecolors properties.


### add\_callback
```py

def add_callback(self, func)

```



Adds a callback function that will be called whenever one of
the :class:`Artist`'s properties changes.

Returns an *id* that is useful for removing the callback with
:meth:`remove_callback` later.


### add\_checker
```py

def add_checker(self, checker)

```



Add an entry to a dictionary of boolean flags
that are set to True when the mappable is changed.


### autoscale
```py

def autoscale(self)

```



Autoscale the scalar limits on the norm instance using the
current array


### autoscale\_None
```py

def autoscale_None(self)

```



Autoscale the scalar limits on the norm instance using the
current array, changing only limits that are None


### changed
```py

def changed(self)

```



Call this whenever the mappable is changed to notify all the
callbackSM listeners to the 'changed' signal


### check\_update
```py

def check_update(self, checker)

```



If mappable has changed since the last check,
return True; else return False


### contains
```py

def contains(self, mouseevent)

```



Test whether the mouse event occurred in the collection.

Returns True | False, ``dict(ind=itemlist)``, where every
item in itemlist contains the event.


### convert\_xunits
```py

def convert_xunits(self, x)

```



For artists in an axes, if the xaxis has units support,
convert *x* using xaxis unit type


### convert\_yunits
```py

def convert_yunits(self, y)

```



For artists in an axes, if the yaxis has units support,
convert *y* using yaxis unit type


### do\_3d\_projection
```py

def do_3d_projection(self, renderer)

```



Perform the 3D projection for this object.


### draw
```py

def draw(self, renderer)

```



### findobj
```py

def findobj(self, match=None, include_self=True)

```



Find artist objects.

Recursively find all :class:`~matplotlib.artist.Artist` instances
contained in self.

*match* can be

  - None: return all objects contained in artist.

  - function with signature ``boolean = match(artist)``
    used to filter matches

  - class instance: e.g., Line2D.  Only return artists of class type.

If *include_self* is True (default), include self in the list to be
checked for a match.


### format\_cursor\_data
```py

def format_cursor_data(self, data)

```



Return *cursor data* string formatted.


### get\_agg\_filter
```py

def get_agg_filter(self)

```



Return filter function to be used for agg filter.


### get\_alpha
```py

def get_alpha(self)

```



Return the alpha value used for blending - not supported on all
backends


### get\_animated
```py

def get_animated(self)

```



Return the artist's animated state


### get\_array
```py

def get_array(self)

```



Return the array


### get\_children
```py

def get_children(self)

```



Return a list of the child :class:`Artist`s this
:class:`Artist` contains.


### get\_clim
```py

def get_clim(self)

```



return the min, max of the color limits for image scaling


### get\_clip\_box
```py

def get_clip_box(self)

```



Return artist clipbox


### get\_clip\_on
```py

def get_clip_on(self)

```



Return whether artist uses clipping


### get\_clip\_path
```py

def get_clip_path(self)

```



Return artist clip path


### get\_cmap
```py

def get_cmap(self)

```



return the colormap


### get\_contains
```py

def get_contains(self)

```



Return the _contains test used by the artist, or *None* for default.


### get\_cursor\_data
```py

def get_cursor_data(self, event)

```



Get the cursor data for a given event.


### get\_dashes
```py

def get_dashes(self)

```



### get\_datalim
```py

def get_datalim(self, transData)

```



### get\_edgecolor
```py

def get_edgecolor(self)

```



### get\_edgecolors
```py

def get_edgecolors(self)

```



### get\_facecolor
```py

def get_facecolor(self)

```



### get\_facecolors
```py

def get_facecolors(self)

```



### get\_figure
```py

def get_figure(self)

```



Return the `~.Figure` instance the artist belongs to.


### get\_fill
```py

def get_fill(self)

```



return whether fill is set


### get\_gid
```py

def get_gid(self)

```



Returns the group id.


### get\_hatch
```py

def get_hatch(self)

```



Return the current hatching pattern.


### get\_label
```py

def get_label(self)

```



Get the label used for this artist in the legend.


### get\_linestyle
```py

def get_linestyle(self)

```



### get\_linestyles
```py

def get_linestyles(self)

```



### get\_linewidth
```py

def get_linewidth(self)

```



### get\_linewidths
```py

def get_linewidths(self)

```



### get\_offset\_position
```py

def get_offset_position(self)

```



Returns how offsets are applied for the collection.  If
*offset_position* is 'screen', the offset is applied after the
master transform has been applied, that is, the offsets are in
screen coordinates.  If offset_position is 'data', the offset
is applied before the master transform, i.e., the offsets are
in data coordinates.


### get\_offset\_transform
```py

def get_offset_transform(self)

```



### get\_offsets
```py

def get_offsets(self)

```



Return the offsets for the collection.


### get\_path\_effects
```py

def get_path_effects(self)

```



### get\_paths
```py

def get_paths(self)

```



### get\_picker
```py

def get_picker(self)

```



Return the picker object used by this artist.


### get\_pickradius
```py

def get_pickradius(self)

```



### get\_rasterized
```py

def get_rasterized(self)

```



Return whether the artist is to be rasterized.


### get\_sizes
```py

def get_sizes(self)

```



Returns the sizes of the elements in the collection.  The
value represents the 'area' of the element.

Returns
-------
sizes : array
    The 'area' of each element.


### get\_sketch\_params
```py

def get_sketch_params(self)

```



Returns the sketch parameters for the artist.

Returns
-------
sketch_params : tuple or `None`

A 3-tuple with the following elements:

  * `scale`: The amplitude of the wiggle perpendicular to the
    source line.

  * `length`: The length of the wiggle along the line.

  * `randomness`: The scale factor by which the length is
    shrunken or expanded.

May return `None` if no sketch parameters were set.


### get\_snap
```py

def get_snap(self)

```



Returns the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.


### get\_transform
```py

def get_transform(self)

```



Return the :class:`~matplotlib.transforms.Transform`
instance used by this artist.


### get\_transformed\_clip\_path\_and\_affine
```py

def get_transformed_clip_path_and_affine(self)

```



Return the clip path with the non-affine part of its
transformation applied, and the remaining affine part of its
transformation.


### get\_transforms
```py

def get_transforms(self)

```



### get\_url
```py

def get_url(self)

```



Returns the url.


### get\_urls
```py

def get_urls(self)

```



### get\_vector
```py

def get_vector(self, segments3d)

```



Optimize points for projection


### get\_visible
```py

def get_visible(self)

```



Return the artist's visiblity


### get\_window\_extent
```py

def get_window_extent(self, renderer)

```



### get\_zorder
```py

def get_zorder(self)

```



Return the artist's zorder.


### have\_units
```py

def have_units(self)

```



Return *True* if units are set on the *x* or *y* axes


### hitlist
```py

def hitlist(self, event)

```



List the children of the artist which contain the mouse event *event*.


### is\_figure\_set
```py

def is_figure_set(self)

```



Returns whether the artist is assigned to a `~.Figure`.


### is\_transform\_set
```py

def is_transform_set(self)

```



Returns *True* if :class:`Artist` has a transform explicitly
set.


### pchanged
```py

def pchanged(self)

```



Fire an event when property changed, calling all of the
registered callbacks.


### pick
```py

def pick(self, mouseevent)

```



Process pick event

each child artist will fire a pick event if *mouseevent* is over
the artist and the artist has picker set


### pickable
```py

def pickable(self)

```



Return *True* if :class:`Artist` is pickable.


### properties
```py

def properties(self)

```



return a dictionary mapping property name -> value for all Artist props


### remove
```py

def remove(self)

```



Remove the artist from the figure if possible.  The effect
will not be visible until the figure is redrawn, e.g., with
:meth:`matplotlib.axes.Axes.draw_idle`.  Call
:meth:`matplotlib.axes.Axes.relim` to update the axes limits
if desired.

Note: :meth:`~matplotlib.axes.Axes.relim` will not see
collections even if the collection was added to axes with
*autolim* = True.

Note: there is no support for removing the artist's legend entry.


### remove\_callback
```py

def remove_callback(self, oid)

```



Remove a callback based on its *id*.

.. seealso::

    :meth:`add_callback`
       For adding callbacks


### set
```py

def set(self, **kwargs)

```



A property batch setter. Pass *kwargs* to set properties.
        


### set\_3d\_properties
```py

def set_3d_properties(self)

```



### set\_agg\_filter
```py

def set_agg_filter(self, filter_func)

```



Set the agg filter.

Parameters
----------
filter_func : callable
    A filter function, which takes a (m, n, 3) float array and a dpi
    value, and returns a (m, n, 3) array.

    ..
        ACCEPTS: a filter function, which takes a (m, n, 3) float array
        and a dpi value, and returns a (m, n, 3) array


### set\_alpha
```py

def set_alpha(self, alpha)

```



Set the alpha tranparencies of the collection.  *alpha* must be
a float or *None*.

ACCEPTS: float or None


### set\_animated
```py

def set_animated(self, b)

```



Set the artist's animation state.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_antialiased
```py

def set_antialiased(self, aa)

```



Set the antialiasing state for rendering.

ACCEPTS: Boolean or sequence of booleans


### set\_antialiaseds
```py

def set_antialiaseds(self, aa)

```



alias for set_antialiased


### set\_array
```py

def set_array(self, A)

```



Set the image array from numpy array *A*.

..
    ACCEPTS: ndarray

Parameters
----------
A : ndarray


### set\_clim
```py

def set_clim(self, vmin=None, vmax=None)

```



set the norm limits for image scaling; if *vmin* is a length2
sequence, interpret it as ``(vmin, vmax)`` which is used to
support setp

ACCEPTS: a length 2 sequence of floats


### set\_clip\_box
```py

def set_clip_box(self, clipbox)

```



Set the artist's clip `~.Bbox`.

Parameters
----------
clipbox : `~.Bbox`
    ..
        ACCEPTS: a `~.Bbox` instance


### set\_clip\_on
```py

def set_clip_on(self, b)

```



Set whether artist uses clipping.

When False artists will be visible out side of the axes which
can lead to unexpected results.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_clip\_path
```py

def set_clip_path(self, path, transform=None)

```



Set the artist's clip path, which may be:

- a :class:`~matplotlib.patches.Patch` (or subclass) instance; or
- a :class:`~matplotlib.path.Path` instance, in which case a
  :class:`~matplotlib.transforms.Transform` instance, which will be
  applied to the path before using it for clipping, must be provided;
  or
- ``None``, to remove a previously set clipping path.

For efficiency, if the path happens to be an axis-aligned rectangle,
this method will set the clipping box to the corresponding rectangle
and set the clipping path to ``None``.

ACCEPTS: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None]


### set\_cmap
```py

def set_cmap(self, cmap)

```



set the colormap for luminance data

ACCEPTS: a colormap or registered colormap name


### set\_color
```py

def set_color(self, c)

```



Set both the edgecolor and the facecolor.

ACCEPTS: matplotlib color arg or sequence of rgba tuples

.. seealso::

    :meth:`set_facecolor`, :meth:`set_edgecolor`
       For setting the edge or face color individually.


### set\_contains
```py

def set_contains(self, picker)

```



Replace the contains test used by this artist. The new picker
should be a callable function which determines whether the
artist is hit by the mouse event::

    hit, props = picker(artist, mouseevent)

If the mouse event is over the artist, return *hit* = *True*
and *props* is a dictionary of properties you want returned
with the contains test.

Parameters
----------
picker : callable
    ..
        ACCEPTS: a callable function


### set\_dashes
```py

def set_dashes(self, ls)

```



alias for set_linestyle


### set\_edgecolor
```py

def set_edgecolor(self, colors)

```



### set\_edgecolors
```py

def set_edgecolors(self, colors)

```



### set\_facecolor
```py

def set_facecolor(self, colors)

```



### set\_facecolors
```py

def set_facecolors(self, colors)

```



### set\_figure
```py

def set_figure(self, fig)

```



Set the `~.Figure` instance the artist belongs to.

Parameters
----------
fig : `~.Figure`
    ..
        ACCEPTS: a `~.Figure` instance


### set\_gid
```py

def set_gid(self, gid)

```



Sets the (group) id for the artist.

Parameters
----------
gid : str
    ..
        ACCEPTS: an id string


### set\_hatch
```py

def set_hatch(self, hatch)

```



Set the hatching pattern

*hatch* can be one of::

  /   - diagonal hatching
  \   - back diagonal
  |   - vertical
  -   - horizontal
  +   - crossed
  x   - crossed diagonal
  o   - small circle
  O   - large circle
  .   - dots
  *   - stars

Letters can be combined, in which case all the specified
hatchings are done.  If same letter repeats, it increases the
density of hatching of that pattern.

Hatching is supported in the PostScript, PDF, SVG and Agg
backends only.

Unlike other properties such as linewidth and colors, hatching
can only be specified for the collection as a whole, not separately
for each member.

ACCEPTS: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ]


### set\_label
```py

def set_label(self, s)

```



Set the label to *s* for auto legend.

Parameters
----------
s : object
    *s* will be converted to a string by calling `str` (`unicode` on
    Py2).

    ..
        ACCEPTS: object


### set\_linestyle
```py

def set_linestyle(self, ls)

```



Set the linestyle(s) for the collection.

===========================   =================
linestyle                     description
===========================   =================
``'-'`` or ``'solid'``        solid line
``'--'`` or  ``'dashed'``     dashed line
``'-.'`` or  ``'dashdot'``    dash-dotted line
``':'`` or ``'dotted'``       dotted line
===========================   =================

Alternatively a dash tuple of the following form can be provided::

    (offset, onoffseq),

where ``onoffseq`` is an even length tuple of on and off ink
in points.

ACCEPTS: ['solid' | 'dashed', 'dashdot', 'dotted' |
           (offset, on-off-dash-seq) |
           ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` |
           ``' '`` | ``''``]

Parameters
----------
ls : { '-',  '--', '-.', ':'} and more see description
    The line style.


### set\_linestyles
```py

def set_linestyles(self, ls)

```



alias for set_linestyle


### set\_linewidth
```py

def set_linewidth(self, lw)

```



Set the linewidth(s) for the collection.  *lw* can be a scalar
or a sequence; if it is a sequence the patches will cycle
through the sequence

ACCEPTS: float or sequence of floats


### set\_linewidths
```py

def set_linewidths(self, lw)

```



alias for set_linewidth


### set\_lw
```py

def set_lw(self, lw)

```



alias for set_linewidth


### set\_norm
```py

def set_norm(self, norm)

```



Set the normalization instance.

..
    ACCEPTS: `~.Normalize`

Parameters
----------
norm : `~.Normalize`


### set\_offset\_position
```py

def set_offset_position(self, offset_position)

```



Set how offsets are applied.  If *offset_position* is 'screen'
(default) the offset is applied after the master transform has
been applied, that is, the offsets are in screen coordinates.
If offset_position is 'data', the offset is applied before the
master transform, i.e., the offsets are in data coordinates.

..
    ACCEPTS: [ 'screen' | 'data' ]


### set\_offsets
```py

def set_offsets(self, offsets)

```



Set the offsets for the collection.  *offsets* can be a scalar
or a sequence.

ACCEPTS: float or sequence of floats


### set\_path\_effects
```py

def set_path_effects(self, path_effects)

```



Set the path effects.

Parameters
----------
path_effects : `~.AbstractPathEffect`
    ..
        ACCEPTS: `~.AbstractPathEffect`


### set\_paths
```py

def set_paths(self, verts, closed=True)

```



This allows one to delay initialization of the vertices.


### set\_picker
```py

def set_picker(self, picker)

```



Set the epsilon for picking used by this artist

*picker* can be one of the following:

  * *None*: picking is disabled for this artist (default)

  * A boolean: if *True* then picking will be enabled and the
    artist will fire a pick event if the mouse event is over
    the artist

  * A float: if picker is a number it is interpreted as an
    epsilon tolerance in points and the artist will fire
    off an event if it's data is within epsilon of the mouse
    event.  For some artists like lines and patch collections,
    the artist may provide additional data to the pick event
    that is generated, e.g., the indices of the data within
    epsilon of the pick event

  * A function: if picker is callable, it is a user supplied
    function which determines whether the artist is hit by the
    mouse event::

      hit, props = picker(artist, mouseevent)

    to determine the hit test.  if the mouse event is over the
    artist, return *hit=True* and props is a dictionary of
    properties you want added to the PickEvent attributes.

Parameters
----------
picker : None or bool or float or callable
    ..
        ACCEPTS: [None | bool | float | callable]


### set\_pickradius
```py

def set_pickradius(self, pr)

```



Set the pick radius used for containment tests.

..
    ACCEPTS: float distance in points

Parameters
----------
d : float
    Pick radius, in points.


### set\_rasterized
```py

def set_rasterized(self, rasterized)

```



Force rasterized (bitmap) drawing in vector backend output.

Defaults to None, which implies the backend's default behavior.

Parameters
----------
rasterized : bool or None
    ..
        ACCEPTS: bool or None


### set\_sizes
```py

def set_sizes(self, sizes, dpi=72.0)

```



Set the sizes of each member of the collection.

Parameters
----------
sizes : ndarray or None
    The size to set for each element of the collection.  The
    value is the 'area' of the element.

dpi : float
    The dpi of the canvas. Defaults to 72.0.


### set\_sketch\_params
```py

def set_sketch_params(self, scale=None, length=None, randomness=None)

```



Sets the sketch parameters.

Parameters
----------

scale : float, optional
    The amplitude of the wiggle perpendicular to the source
    line, in pixels.  If scale is `None`, or not provided, no
    sketch filter will be provided.

length : float, optional
     The length of the wiggle along the line, in pixels
     (default 128.0)

randomness : float, optional
    The scale factor by which the length is shrunken or
    expanded (default 16.0)

    ..
        ACCEPTS: (scale: float, length: float, randomness: float)


### set\_snap
```py

def set_snap(self, snap)

```



Sets the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

Parameters
----------
snap : bool or None
    ..
        ACCEPTS: bool or None


### set\_sort\_zpos
```py

def set_sort_zpos(self, val)

```



Set the position to use for z-sorting.


### set\_transform
```py

def set_transform(self, t)

```



Set the artist transform.

Parameters
----------
t : `~.Transform`
    ..
        ACCEPTS: `~.Transform`


### set\_url
```py

def set_url(self, url)

```



Sets the url for the artist.

Parameters
----------
url : str
    ..
        ACCEPTS: a url string


### set\_urls
```py

def set_urls(self, urls)

```



Parameters
----------
urls : List[str] or None
    ..
        ACCEPTS: List[str] or None


### set\_verts
```py

def set_verts(self, verts, closed=True)

```



Set 3D vertices.


### set\_verts\_and\_codes
```py

def set_verts_and_codes(self, verts, codes)

```



Sets 3D vertices with path codes


### set\_visible
```py

def set_visible(self, b)

```



Set the artist's visibility.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_zorder
```py

def set_zorder(self, level)

```



Set the zorder for the artist.  Artists with lower zorder
values are drawn first.

Parameters
----------
level : float
    ..
        ACCEPTS: float


### set\_zsort
```py

def set_zsort(self, zsort)

```



Set z-sorting behaviour:
    boolean: if True use default 'average'
    string: 'average', 'min' or 'max'


### to\_rgba
```py

def to_rgba(self, x, alpha=None, bytes=False, norm=True)

```



Return a normalized rgba array corresponding to *x*.

In the normal case, *x* is a 1-D or 2-D sequence of scalars, and
the corresponding ndarray of rgba values will be returned,
based on the norm and colormap set for this ScalarMappable.

There is one special case, for handling images that are already
rgb or rgba, such as might have been read from an image file.
If *x* is an ndarray with 3 dimensions,
and the last dimension is either 3 or 4, then it will be
treated as an rgb or rgba array, and no mapping will be done.
The array can be uint8, or it can be floating point with
values in the 0-1 range; otherwise a ValueError will be raised.
If it is a masked array, the mask will be ignored.
If the last dimension is 3, the *alpha* kwarg (defaulting to 1)
will be used to fill in the transparency.  If the last dimension
is 4, the *alpha* kwarg is ignored; it does not
replace the pre-existing alpha.  A ValueError will be raised
if the third dimension is other than 3 or 4.

In either case, if *bytes* is *False* (default), the rgba
array will be floats in the 0-1 range; if it is *True*,
the returned rgba array will be uint8 in the 0 to 255 range.

If norm is False, no normalization of the input data is
performed, and it is assumed to be in the range (0-1).


### update
```py

def update(self, props)

```



Update this artist's properties from the dictionary *prop*.


### update\_from
```py

def update_from(self, other)

```



copy properties from other to self


### update\_scalarmappable
```py

def update_scalarmappable(self)

```



If the scalar mappable array is not none, update colors
from scalar data




## Class PolyCollection
None
### \_\_init\_\_
```py

def __init__(self, verts, sizes=None, closed=True, **kwargs)

```



*verts* is a sequence of ( *verts0*, *verts1*, ...) where
*verts_i* is a sequence of *xy* tuples of vertices, or an
equivalent :mod:`numpy` array of shape (*nv*, 2).

*sizes* is *None* (default) or a sequence of floats that
scale the corresponding *verts_i*.  The scaling is applied
before the Artist master transform; if the latter is an identity
transform, then the overall scaling is such that if
*verts_i* specify a unit square, then *sizes_i* is the area
of that square in points^2.
If len(*sizes*) < *nv*, the additional values will be
taken cyclically from the array.

*closed*, when *True*, will explicitly close the polygon.

    Valid Collection keyword arguments:

        * *edgecolors*: None
        * *facecolors*: None
        * *linewidths*: None
        * *antialiaseds*: None
        * *offsets*: None
        * *transOffset*: transforms.IdentityTransform()
        * *norm*: None (optional for
          :class:`matplotlib.cm.ScalarMappable`)
        * *cmap*: None (optional for
          :class:`matplotlib.cm.ScalarMappable`)

    *offsets* and *transOffset* are used to translate the patch after
    rendering (default no offsets)

    If any of *edgecolors*, *facecolors*, *linewidths*, *antialiaseds*
    are None, they default to their :data:`matplotlib.rcParams` patch
    setting, in sequence form.


### add\_callback
```py

def add_callback(self, func)

```



Adds a callback function that will be called whenever one of
the :class:`Artist`'s properties changes.

Returns an *id* that is useful for removing the callback with
:meth:`remove_callback` later.


### add\_checker
```py

def add_checker(self, checker)

```



Add an entry to a dictionary of boolean flags
that are set to True when the mappable is changed.


### autoscale
```py

def autoscale(self)

```



Autoscale the scalar limits on the norm instance using the
current array


### autoscale\_None
```py

def autoscale_None(self)

```



Autoscale the scalar limits on the norm instance using the
current array, changing only limits that are None


### changed
```py

def changed(self)

```



Call this whenever the mappable is changed to notify all the
callbackSM listeners to the 'changed' signal


### check\_update
```py

def check_update(self, checker)

```



If mappable has changed since the last check,
return True; else return False


### contains
```py

def contains(self, mouseevent)

```



Test whether the mouse event occurred in the collection.

Returns True | False, ``dict(ind=itemlist)``, where every
item in itemlist contains the event.


### convert\_xunits
```py

def convert_xunits(self, x)

```



For artists in an axes, if the xaxis has units support,
convert *x* using xaxis unit type


### convert\_yunits
```py

def convert_yunits(self, y)

```



For artists in an axes, if the yaxis has units support,
convert *y* using yaxis unit type


### draw
```py

def draw(artist, renderer, *args, **kwargs)

```



### findobj
```py

def findobj(self, match=None, include_self=True)

```



Find artist objects.

Recursively find all :class:`~matplotlib.artist.Artist` instances
contained in self.

*match* can be

  - None: return all objects contained in artist.

  - function with signature ``boolean = match(artist)``
    used to filter matches

  - class instance: e.g., Line2D.  Only return artists of class type.

If *include_self* is True (default), include self in the list to be
checked for a match.


### format\_cursor\_data
```py

def format_cursor_data(self, data)

```



Return *cursor data* string formatted.


### get\_agg\_filter
```py

def get_agg_filter(self)

```



Return filter function to be used for agg filter.


### get\_alpha
```py

def get_alpha(self)

```



Return the alpha value used for blending - not supported on all
backends


### get\_animated
```py

def get_animated(self)

```



Return the artist's animated state


### get\_array
```py

def get_array(self)

```



Return the array


### get\_children
```py

def get_children(self)

```



Return a list of the child :class:`Artist`s this
:class:`Artist` contains.


### get\_clim
```py

def get_clim(self)

```



return the min, max of the color limits for image scaling


### get\_clip\_box
```py

def get_clip_box(self)

```



Return artist clipbox


### get\_clip\_on
```py

def get_clip_on(self)

```



Return whether artist uses clipping


### get\_clip\_path
```py

def get_clip_path(self)

```



Return artist clip path


### get\_cmap
```py

def get_cmap(self)

```



return the colormap


### get\_contains
```py

def get_contains(self)

```



Return the _contains test used by the artist, or *None* for default.


### get\_cursor\_data
```py

def get_cursor_data(self, event)

```



Get the cursor data for a given event.


### get\_dashes
```py

def get_dashes(self)

```



### get\_datalim
```py

def get_datalim(self, transData)

```



### get\_edgecolor
```py

def get_edgecolor(self)

```



### get\_edgecolors
```py

def get_edgecolors(self)

```



### get\_facecolor
```py

def get_facecolor(self)

```



### get\_facecolors
```py

def get_facecolors(self)

```



### get\_figure
```py

def get_figure(self)

```



Return the `~.Figure` instance the artist belongs to.


### get\_fill
```py

def get_fill(self)

```



return whether fill is set


### get\_gid
```py

def get_gid(self)

```



Returns the group id.


### get\_hatch
```py

def get_hatch(self)

```



Return the current hatching pattern.


### get\_label
```py

def get_label(self)

```



Get the label used for this artist in the legend.


### get\_linestyle
```py

def get_linestyle(self)

```



### get\_linestyles
```py

def get_linestyles(self)

```



### get\_linewidth
```py

def get_linewidth(self)

```



### get\_linewidths
```py

def get_linewidths(self)

```



### get\_offset\_position
```py

def get_offset_position(self)

```



Returns how offsets are applied for the collection.  If
*offset_position* is 'screen', the offset is applied after the
master transform has been applied, that is, the offsets are in
screen coordinates.  If offset_position is 'data', the offset
is applied before the master transform, i.e., the offsets are
in data coordinates.


### get\_offset\_transform
```py

def get_offset_transform(self)

```



### get\_offsets
```py

def get_offsets(self)

```



Return the offsets for the collection.


### get\_path\_effects
```py

def get_path_effects(self)

```



### get\_paths
```py

def get_paths(self)

```



### get\_picker
```py

def get_picker(self)

```



Return the picker object used by this artist.


### get\_pickradius
```py

def get_pickradius(self)

```



### get\_rasterized
```py

def get_rasterized(self)

```



Return whether the artist is to be rasterized.


### get\_sizes
```py

def get_sizes(self)

```



Returns the sizes of the elements in the collection.  The
value represents the 'area' of the element.

Returns
-------
sizes : array
    The 'area' of each element.


### get\_sketch\_params
```py

def get_sketch_params(self)

```



Returns the sketch parameters for the artist.

Returns
-------
sketch_params : tuple or `None`

A 3-tuple with the following elements:

  * `scale`: The amplitude of the wiggle perpendicular to the
    source line.

  * `length`: The length of the wiggle along the line.

  * `randomness`: The scale factor by which the length is
    shrunken or expanded.

May return `None` if no sketch parameters were set.


### get\_snap
```py

def get_snap(self)

```



Returns the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.


### get\_transform
```py

def get_transform(self)

```



Return the :class:`~matplotlib.transforms.Transform`
instance used by this artist.


### get\_transformed\_clip\_path\_and\_affine
```py

def get_transformed_clip_path_and_affine(self)

```



Return the clip path with the non-affine part of its
transformation applied, and the remaining affine part of its
transformation.


### get\_transforms
```py

def get_transforms(self)

```



### get\_url
```py

def get_url(self)

```



Returns the url.


### get\_urls
```py

def get_urls(self)

```



### get\_visible
```py

def get_visible(self)

```



Return the artist's visiblity


### get\_window\_extent
```py

def get_window_extent(self, renderer)

```



### get\_zorder
```py

def get_zorder(self)

```



Return the artist's zorder.


### have\_units
```py

def have_units(self)

```



Return *True* if units are set on the *x* or *y* axes


### hitlist
```py

def hitlist(self, event)

```



List the children of the artist which contain the mouse event *event*.


### is\_figure\_set
```py

def is_figure_set(self)

```



Returns whether the artist is assigned to a `~.Figure`.


### is\_transform\_set
```py

def is_transform_set(self)

```



Returns *True* if :class:`Artist` has a transform explicitly
set.


### pchanged
```py

def pchanged(self)

```



Fire an event when property changed, calling all of the
registered callbacks.


### pick
```py

def pick(self, mouseevent)

```



Process pick event

each child artist will fire a pick event if *mouseevent* is over
the artist and the artist has picker set


### pickable
```py

def pickable(self)

```



Return *True* if :class:`Artist` is pickable.


### properties
```py

def properties(self)

```



return a dictionary mapping property name -> value for all Artist props


### remove
```py

def remove(self)

```



Remove the artist from the figure if possible.  The effect
will not be visible until the figure is redrawn, e.g., with
:meth:`matplotlib.axes.Axes.draw_idle`.  Call
:meth:`matplotlib.axes.Axes.relim` to update the axes limits
if desired.

Note: :meth:`~matplotlib.axes.Axes.relim` will not see
collections even if the collection was added to axes with
*autolim* = True.

Note: there is no support for removing the artist's legend entry.


### remove\_callback
```py

def remove_callback(self, oid)

```



Remove a callback based on its *id*.

.. seealso::

    :meth:`add_callback`
       For adding callbacks


### set
```py

def set(self, **kwargs)

```



A property batch setter. Pass *kwargs* to set properties.
        


### set\_agg\_filter
```py

def set_agg_filter(self, filter_func)

```



Set the agg filter.

Parameters
----------
filter_func : callable
    A filter function, which takes a (m, n, 3) float array and a dpi
    value, and returns a (m, n, 3) array.

    ..
        ACCEPTS: a filter function, which takes a (m, n, 3) float array
        and a dpi value, and returns a (m, n, 3) array


### set\_alpha
```py

def set_alpha(self, alpha)

```



Set the alpha tranparencies of the collection.  *alpha* must be
a float or *None*.

ACCEPTS: float or None


### set\_animated
```py

def set_animated(self, b)

```



Set the artist's animation state.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_antialiased
```py

def set_antialiased(self, aa)

```



Set the antialiasing state for rendering.

ACCEPTS: Boolean or sequence of booleans


### set\_antialiaseds
```py

def set_antialiaseds(self, aa)

```



alias for set_antialiased


### set\_array
```py

def set_array(self, A)

```



Set the image array from numpy array *A*.

..
    ACCEPTS: ndarray

Parameters
----------
A : ndarray


### set\_clim
```py

def set_clim(self, vmin=None, vmax=None)

```



set the norm limits for image scaling; if *vmin* is a length2
sequence, interpret it as ``(vmin, vmax)`` which is used to
support setp

ACCEPTS: a length 2 sequence of floats


### set\_clip\_box
```py

def set_clip_box(self, clipbox)

```



Set the artist's clip `~.Bbox`.

Parameters
----------
clipbox : `~.Bbox`
    ..
        ACCEPTS: a `~.Bbox` instance


### set\_clip\_on
```py

def set_clip_on(self, b)

```



Set whether artist uses clipping.

When False artists will be visible out side of the axes which
can lead to unexpected results.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_clip\_path
```py

def set_clip_path(self, path, transform=None)

```



Set the artist's clip path, which may be:

- a :class:`~matplotlib.patches.Patch` (or subclass) instance; or
- a :class:`~matplotlib.path.Path` instance, in which case a
  :class:`~matplotlib.transforms.Transform` instance, which will be
  applied to the path before using it for clipping, must be provided;
  or
- ``None``, to remove a previously set clipping path.

For efficiency, if the path happens to be an axis-aligned rectangle,
this method will set the clipping box to the corresponding rectangle
and set the clipping path to ``None``.

ACCEPTS: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None]


### set\_cmap
```py

def set_cmap(self, cmap)

```



set the colormap for luminance data

ACCEPTS: a colormap or registered colormap name


### set\_color
```py

def set_color(self, c)

```



Set both the edgecolor and the facecolor.

ACCEPTS: matplotlib color arg or sequence of rgba tuples

.. seealso::

    :meth:`set_facecolor`, :meth:`set_edgecolor`
       For setting the edge or face color individually.


### set\_contains
```py

def set_contains(self, picker)

```



Replace the contains test used by this artist. The new picker
should be a callable function which determines whether the
artist is hit by the mouse event::

    hit, props = picker(artist, mouseevent)

If the mouse event is over the artist, return *hit* = *True*
and *props* is a dictionary of properties you want returned
with the contains test.

Parameters
----------
picker : callable
    ..
        ACCEPTS: a callable function


### set\_dashes
```py

def set_dashes(self, ls)

```



alias for set_linestyle


### set\_edgecolor
```py

def set_edgecolor(self, c)

```



Set the edgecolor(s) of the collection. *c* can be a
matplotlib color spec (all patches have same color), or a
sequence of specs; if it is a sequence the patches will
cycle through the sequence.

If *c* is 'face', the edge color will always be the same as
the face color.  If it is 'none', the patch boundary will not
be drawn.

ACCEPTS: matplotlib color spec or sequence of specs


### set\_edgecolors
```py

def set_edgecolors(self, c)

```



alias for set_edgecolor


### set\_facecolor
```py

def set_facecolor(self, c)

```



Set the facecolor(s) of the collection.  *c* can be a
matplotlib color spec (all patches have same color), or a
sequence of specs; if it is a sequence the patches will
cycle through the sequence.

If *c* is 'none', the patch will not be filled.

ACCEPTS: matplotlib color spec or sequence of specs


### set\_facecolors
```py

def set_facecolors(self, c)

```



alias for set_facecolor


### set\_figure
```py

def set_figure(self, fig)

```



Set the `~.Figure` instance the artist belongs to.

Parameters
----------
fig : `~.Figure`
    ..
        ACCEPTS: a `~.Figure` instance


### set\_gid
```py

def set_gid(self, gid)

```



Sets the (group) id for the artist.

Parameters
----------
gid : str
    ..
        ACCEPTS: an id string


### set\_hatch
```py

def set_hatch(self, hatch)

```



Set the hatching pattern

*hatch* can be one of::

  /   - diagonal hatching
  \   - back diagonal
  |   - vertical
  -   - horizontal
  +   - crossed
  x   - crossed diagonal
  o   - small circle
  O   - large circle
  .   - dots
  *   - stars

Letters can be combined, in which case all the specified
hatchings are done.  If same letter repeats, it increases the
density of hatching of that pattern.

Hatching is supported in the PostScript, PDF, SVG and Agg
backends only.

Unlike other properties such as linewidth and colors, hatching
can only be specified for the collection as a whole, not separately
for each member.

ACCEPTS: [ '/' | '\\' | '|' | '-' | '+' | 'x' | 'o' | 'O' | '.' | '*' ]


### set\_label
```py

def set_label(self, s)

```



Set the label to *s* for auto legend.

Parameters
----------
s : object
    *s* will be converted to a string by calling `str` (`unicode` on
    Py2).

    ..
        ACCEPTS: object


### set\_linestyle
```py

def set_linestyle(self, ls)

```



Set the linestyle(s) for the collection.

===========================   =================
linestyle                     description
===========================   =================
``'-'`` or ``'solid'``        solid line
``'--'`` or  ``'dashed'``     dashed line
``'-.'`` or  ``'dashdot'``    dash-dotted line
``':'`` or ``'dotted'``       dotted line
===========================   =================

Alternatively a dash tuple of the following form can be provided::

    (offset, onoffseq),

where ``onoffseq`` is an even length tuple of on and off ink
in points.

ACCEPTS: ['solid' | 'dashed', 'dashdot', 'dotted' |
           (offset, on-off-dash-seq) |
           ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` |
           ``' '`` | ``''``]

Parameters
----------
ls : { '-',  '--', '-.', ':'} and more see description
    The line style.


### set\_linestyles
```py

def set_linestyles(self, ls)

```



alias for set_linestyle


### set\_linewidth
```py

def set_linewidth(self, lw)

```



Set the linewidth(s) for the collection.  *lw* can be a scalar
or a sequence; if it is a sequence the patches will cycle
through the sequence

ACCEPTS: float or sequence of floats


### set\_linewidths
```py

def set_linewidths(self, lw)

```



alias for set_linewidth


### set\_lw
```py

def set_lw(self, lw)

```



alias for set_linewidth


### set\_norm
```py

def set_norm(self, norm)

```



Set the normalization instance.

..
    ACCEPTS: `~.Normalize`

Parameters
----------
norm : `~.Normalize`


### set\_offset\_position
```py

def set_offset_position(self, offset_position)

```



Set how offsets are applied.  If *offset_position* is 'screen'
(default) the offset is applied after the master transform has
been applied, that is, the offsets are in screen coordinates.
If offset_position is 'data', the offset is applied before the
master transform, i.e., the offsets are in data coordinates.

..
    ACCEPTS: [ 'screen' | 'data' ]


### set\_offsets
```py

def set_offsets(self, offsets)

```



Set the offsets for the collection.  *offsets* can be a scalar
or a sequence.

ACCEPTS: float or sequence of floats


### set\_path\_effects
```py

def set_path_effects(self, path_effects)

```



Set the path effects.

Parameters
----------
path_effects : `~.AbstractPathEffect`
    ..
        ACCEPTS: `~.AbstractPathEffect`


### set\_paths
```py

def set_paths(self, verts, closed=True)

```



This allows one to delay initialization of the vertices.


### set\_picker
```py

def set_picker(self, picker)

```



Set the epsilon for picking used by this artist

*picker* can be one of the following:

  * *None*: picking is disabled for this artist (default)

  * A boolean: if *True* then picking will be enabled and the
    artist will fire a pick event if the mouse event is over
    the artist

  * A float: if picker is a number it is interpreted as an
    epsilon tolerance in points and the artist will fire
    off an event if it's data is within epsilon of the mouse
    event.  For some artists like lines and patch collections,
    the artist may provide additional data to the pick event
    that is generated, e.g., the indices of the data within
    epsilon of the pick event

  * A function: if picker is callable, it is a user supplied
    function which determines whether the artist is hit by the
    mouse event::

      hit, props = picker(artist, mouseevent)

    to determine the hit test.  if the mouse event is over the
    artist, return *hit=True* and props is a dictionary of
    properties you want added to the PickEvent attributes.

Parameters
----------
picker : None or bool or float or callable
    ..
        ACCEPTS: [None | bool | float | callable]


### set\_pickradius
```py

def set_pickradius(self, pr)

```



Set the pick radius used for containment tests.

..
    ACCEPTS: float distance in points

Parameters
----------
d : float
    Pick radius, in points.


### set\_rasterized
```py

def set_rasterized(self, rasterized)

```



Force rasterized (bitmap) drawing in vector backend output.

Defaults to None, which implies the backend's default behavior.

Parameters
----------
rasterized : bool or None
    ..
        ACCEPTS: bool or None


### set\_sizes
```py

def set_sizes(self, sizes, dpi=72.0)

```



Set the sizes of each member of the collection.

Parameters
----------
sizes : ndarray or None
    The size to set for each element of the collection.  The
    value is the 'area' of the element.

dpi : float
    The dpi of the canvas. Defaults to 72.0.


### set\_sketch\_params
```py

def set_sketch_params(self, scale=None, length=None, randomness=None)

```



Sets the sketch parameters.

Parameters
----------

scale : float, optional
    The amplitude of the wiggle perpendicular to the source
    line, in pixels.  If scale is `None`, or not provided, no
    sketch filter will be provided.

length : float, optional
     The length of the wiggle along the line, in pixels
     (default 128.0)

randomness : float, optional
    The scale factor by which the length is shrunken or
    expanded (default 16.0)

    ..
        ACCEPTS: (scale: float, length: float, randomness: float)


### set\_snap
```py

def set_snap(self, snap)

```



Sets the snap setting which may be:

  * True: snap vertices to the nearest pixel center

  * False: leave vertices as-is

  * None: (auto) If the path contains only rectilinear line
    segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

Parameters
----------
snap : bool or None
    ..
        ACCEPTS: bool or None


### set\_transform
```py

def set_transform(self, t)

```



Set the artist transform.

Parameters
----------
t : `~.Transform`
    ..
        ACCEPTS: `~.Transform`


### set\_url
```py

def set_url(self, url)

```



Sets the url for the artist.

Parameters
----------
url : str
    ..
        ACCEPTS: a url string


### set\_urls
```py

def set_urls(self, urls)

```



Parameters
----------
urls : List[str] or None
    ..
        ACCEPTS: List[str] or None


### set\_verts
```py

def set_verts(self, verts, closed=True)

```



This allows one to delay initialization of the vertices.


### set\_verts\_and\_codes
```py

def set_verts_and_codes(self, verts, codes)

```



This allows one to initialize vertices with path codes.


### set\_visible
```py

def set_visible(self, b)

```



Set the artist's visibility.

Parameters
----------
b : bool
    ..
        ACCEPTS: bool


### set\_zorder
```py

def set_zorder(self, level)

```



Set the zorder for the artist.  Artists with lower zorder
values are drawn first.

Parameters
----------
level : float
    ..
        ACCEPTS: float


### to\_rgba
```py

def to_rgba(self, x, alpha=None, bytes=False, norm=True)

```



Return a normalized rgba array corresponding to *x*.

In the normal case, *x* is a 1-D or 2-D sequence of scalars, and
the corresponding ndarray of rgba values will be returned,
based on the norm and colormap set for this ScalarMappable.

There is one special case, for handling images that are already
rgb or rgba, such as might have been read from an image file.
If *x* is an ndarray with 3 dimensions,
and the last dimension is either 3 or 4, then it will be
treated as an rgb or rgba array, and no mapping will be done.
The array can be uint8, or it can be floating point with
values in the 0-1 range; otherwise a ValueError will be raised.
If it is a masked array, the mask will be ignored.
If the last dimension is 3, the *alpha* kwarg (defaulting to 1)
will be used to fill in the transparency.  If the last dimension
is 4, the *alpha* kwarg is ignored; it does not
replace the pre-existing alpha.  A ValueError will be raised
if the third dimension is other than 3 or 4.

In either case, if *bytes* is *False* (default), the rgba
array will be floats in the 0-1 range; if it is *True*,
the returned rgba array will be uint8 in the 0 to 255 range.

If norm is False, no normalization of the input data is
performed, and it is assumed to be in the range (0-1).


### update
```py

def update(self, props)

```



Update this artist's properties from the dictionary *prop*.


### update\_from
```py

def update_from(self, other)

```



copy properties from other to self


### update\_scalarmappable
```py

def update_scalarmappable(self)

```



If the scalar mappable array is not none, update colors
from scalar data




## Class Settings
None
### \_\_init\_\_
```py

def __init__(self)

```



### devel\_off
```py

def devel_off(self)

```



### devel\_on
```py

def devel_on(self)

```



### interactive\_off
```py

def interactive_off(self)

```



### interactive\_on
```py

def interactive_on(self)

```





## Class StringParameter
Parameter that accepts any string for the value
### \_\_init\_\_
```py

def __init__(self, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



        


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class TwigParameter
Parameter that handles referencing any other *parameter* by twig (must exist)
This stores the uniqueid but will display as the current uniquetwig for that item
### \_\_init\_\_
```py

def __init__(self, bundle, *args, **kwargs)

```



see :meth:`Parameter.__init__`


### copy
```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object


### get\_attributes
```py

def get_attributes(self)

```



        


### get\_description
```py

def get_description(self)

```



:return: the description of this parameter


### get\_meta
```py

def get_meta(self, ignore=['uniqueid'])

```



See all the meta-tag properties for this Parameter

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties


### get\_parameter
```py

def get_parameter(self)

```



return the parameter that this points to


### get\_parent\_ps
```py

def get_parent_ps(self)

```



Return a :class:`ParameterSet` of all Parameters in the same
:class:`phoebe.frontend.bundle.Bundle` which share the same
meta-tags (except qualifier, twig, uniquetwig)

:return: the parent :class:`ParameterSet`


### get\_value
```py

def get_value(self, *args, **kwargs)

```



        


### set\_uniqueid
```py

def set_uniqueid(self, uniqueid)

```



Set the uniqueid of this Parameter.  There is no real need
for a user to call this unless there is some conflict or they
manually want to set the uniqueids.

NOTE: this does not check for conflicts, and having two parameters
without the same uniqueid (not really unique anymore is it) will
surely cause unexpected results.  Use with caution.

:parameter str uniqueid: the new uniqueid


### set\_value
```py

def set_value(self, *args, **kwargs)

```



kwargs are passed on to filter


### to\_constraint
```py

def to_constraint(self)

```



Convert this Parameter to a :class:`ConstraintParameter`.  Use
with caution.

:return: the :class:`ConstraintParameter`


### to\_dict
```py

def to_dict(self)

```



:return: the dictionary representation of the parameter


### to\_json
```py

def to_json(self, incl_uniqueid=False)

```



:return: a JSON-ready dictionary holding all information for this
    parameter


### to\_string
```py

def to_string(self)

```



see also :meth:`to_string_short`

:return: the string representation of the parameter


### to\_string\_short
```py

def to_string_short(self)

```



see also :meth:`to_string`

:return: a shorter abreviated string reprentation of the parameter




## Class datetime
datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints or longs.

