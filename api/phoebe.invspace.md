### [phoebe](phoebe.md).invspace (function)


```py

def invspace(start, stop, num, endpoint=True, unit=None)

```



This is an included dependency from [nparray 1.1.0](https://nparray.readthedocs.io/en/1.1.0/).

===============================================================


Evenly sampled numbers in inverted space.  This is equivalent to:

```py
1./linspace(1./start, 1./stop, num, endpoint, unit)
```

See also:

* nparray.linspace

Arguments
------------
* `start` (int or float): the starting point of the sequence.
* `stop` (int or float): the ending point of the sequence, unless `endpoint`
is set to False.  In that case, the sequence consists of all but the
last of ``num + 1`` evenly spaced samples, so that `stop` is excluded.
Note that the step size changes when `endpoint` is False.
* `num` (int): number of samples to generate.
* `endpoint` (bool, optional, default=True): If True, `stop` is the last
sample. Otherwise, it is not included.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* Invspace

