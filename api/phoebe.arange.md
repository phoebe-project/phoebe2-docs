### [phoebe](phoebe.md).arange (function)


```py

def arange(start, stop, step, unit=None)

```



This is an included dependency from [nparray 1.1.0](https://nparray.readthedocs.io/en/1.1.0/).

===============================================================


This is an nparray wrapper around the numpy function.  The
numpy documentation is included below.  Currently most kwargs
should be accepted with the exception of 'dtype'.  The returned
object should act exactly like the numpy array itself, but with
several extra helpful methods and attributes.  Call help on the
resulting object for more information.

If you have astropy installed, units are supported by passing unit=astropy.unit
to the instantiation functions or by multiplying an array with a unit object.


Arguments
------------
* `start` (int or float): the starting point of the sequence.
* `stop` (int or float): the ending point of the sequence.  The interval
does not include this value, except in some cases where `step` is not an
integer and floating point round-off affects the length of the array.
* `step` (int or float): the stepsize between each item in the sequence.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* [Arange](Arange.md)


===============================================================

** numpy documentation for underlying function: **

arange([start,] stop[, step,], dtype=None)

Return evenly spaced values within a given interval.

Values are generated within the half-open interval ``[start, stop)``
(in other words, the interval including `start` but excluding `stop`).
For integer arguments the function is equivalent to the Python built-in
`range &lt;<a href="http://docs.python.org/lib/built-in-funcs.html&gt;`_">http://docs.python.org/lib/built-in-funcs.html&gt;`_</a> function,
but returns an ndarray rather than a list.

When using a non-integer step, such as 0.1, the results will often not
be consistent.  It is better to use ``linspace`` for these cases.

Parameters
----------
start : number, optional
Start of interval.  The interval includes this value.  The default
start value is 0.
stop : number
End of interval.  The interval does not include this value, except
in some cases where `step` is not an integer and floating point
round-off affects the length of `out`.
step : number, optional
Spacing between values.  For any output `out`, this is the distance
between two adjacent values, ``out[i+1] - out[i]``.  The default
step size is 1.  If `step` is specified as a position argument,
`start` must also be given.
dtype : dtype
The type of the output array.  If `dtype` is not given, infer the data
type from the other input arguments.

Returns
-------
arange : ndarray
Array of evenly spaced values.

For floating point arguments, the length of the result is
``ceil((stop - start)/step)``.  Because of floating point overflow,
this rule may result in the last element of `out` being greater
than `stop`.

See Also
--------
linspace : Evenly spaced numbers with careful handling of endpoints.
ogrid: Arrays of evenly spaced numbers in N-dimensions.
mgrid: Grid-shaped arrays of evenly spaced numbers in N-dimensions.

Examples
--------
&gt;&gt;&gt; np.arange(3)
array([0, 1, 2])
&gt;&gt;&gt; np.arange(3.0)
array([ 0.,  1.,  2.])
&gt;&gt;&gt; np.arange(3,7)
array([3, 4, 5, 6])
&gt;&gt;&gt; np.arange(3,7,2)
array([3, 5])

