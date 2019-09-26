### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).pot_for_component (function)


```py

def pot_for_component(pot, q, component=1, reverse=False)

```



Handle converting the potential into the star's frame of reference.

Note: `q` should already be in the frame of the requested star.  If necessary,
pass the output from [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md).

If `component` is 1:
    * `pot` is returned as is

If `component` is 2:
    * if `reverse` is True: `pot/q + 0.5 * (q-1)/q`
    * if `reverse` is False: `q*pot - 0.5 * (q-1)`

Arguments
------------
* `pot` (float): the equipotential of the star as defined as if it were the
    primary component.
* `q` (float): the mass-ratio in the frame of `component`.  If necessary,
    call [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) first.
* `component` (int, optional, default=1): whether the requested component
    is the primary (1) or secondary (2) component.
* `reverse` (bool, optional, default=False): whether to do the reverse operation.
    If True, then `pot` is assumed to be in the reference frame of `component`
    and is returned as if in the reference from of the primary component.

Returns
----------
* (float): the converted equipotential.

Raises
------------
* NotImplementedError: if `component` is neither 1 or 2.)

