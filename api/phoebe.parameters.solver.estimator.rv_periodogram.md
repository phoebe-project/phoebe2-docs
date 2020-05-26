### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).rv_periodogram (function)


```py

def rv_periodogram(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
radial velocity periodogram period estimator using astropy.  See
https://docs.astropy.org/en/stable/timeseries/lombscargle.html for more details.

NOTE: this requires astropy 3.2+, which in turn requires python 3.  If these
requirements are not met, an error will be raised when attempting to call
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

The input radial velocity datasets (`rv_datasets`) are combined and then
normalized by the absolute maximum value for the primary and secondary star
independently, with the secondary then mirrored.  These combined data are
then sent to the respective periodgram `algorithm` and the resulting period
corresponding to the strongest peak is proposed as an adopted value.  In
addition, the periodgram itself is exposed in the solution and available
for plotting via [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md).

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('estimator.rv_periodogram')
b.run_solver(kind='rv_periodogram')
```

Arguments
----------
* `algorithm` (string, optional, default='bls'): algorithm to use to create
    the periodogram.  ls: LombScargle.
* `rv_datasets` (string or list, optional, default='*'): Radial velocity
    dataset(s) to use to run the periodogram algorithm.
* `component` (string, optional, default=top-level orbit): Component to
    apply the found period.
* `sample_mode` (string, optional, default='auto'): Whether to automatically
    determine sampling periods/frequencies ('auto') or set manually ('manual').
* `sample_periods` (array, optional, default=[]): only applicable if
    `sample_mode` is 'manual'.  Manual period grid for sampling the periodogram.
    Note: if `algorithm` is 'ls', these will be converted to frequencies and
    will be more efficient if sampled evenly in frequency space (consider
    using [phoebe.invspace](phoebe.invspace.md) instead of [phoebe.linspace](phoebe.linspace.md)).
* `samples_per_peak` (int, optional, default=10): only applicable if
    `algorithm` is 'ls' and `sample_mode` is 'auto'.  The approximate number
    of desired samples across the typical peak.  This is passed directly to
    autopower. See
    https://docs.astropy.org/en/stable/api/astropy.timeseries.LombScargle.html#astropy.timeseries.LombScargle.autopower
* `nyquist_factor` (int, optional, default=5): only applicable if
    `algorithm` is 'ls' and `sample_mode` is 'auto'.  The multiple of the
    average nyquist frequency used to choose the maximum frequency.  This is
    passed directly to autopower. See
    https://docs.astropy.org/en/stable/api/astropy.timeseries.LombScargle.html#astropy.timeseries.LombScargle.autopower



Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

