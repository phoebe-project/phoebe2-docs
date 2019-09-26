### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).q_for_component (function)


```py

def q_for_component(q, component=1)

```



Flip the mass-ratio `q` if secondary component.

Arguments
-------------
* `q` (float): the mass-ratio of the system/orbit (defined as m2/m1)
* `component` (int, optional, default=1): whether the requested component
    is the primary (1) or secondary (2) component.

Returns
-----------
* (float) `q` if `component` is 1, or `1/q` if component is 2

Raises
-----------
* NotImplementedError: if `component` is neither 1 or 2.

