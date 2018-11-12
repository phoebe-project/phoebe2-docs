### Bundle.compute_pblums

```py

def compute_pblums(self, compute=None, **kwargs)

```



Compute the passband luminosities that will be applied to the system,
following all coupling, etc, as well as all relevant compute options
(ntriangles, distortion_method, etc).  The exposed passband luminosities
(and any coupling) are computed at t0@system.

This method is only for convenience and will be recomputed internally
within run_compute.  Alternatively, you can create a mesh dataset
and request any specific pblum to be exposed (per-time).

:parameter str compute: label of the compute options (note required if
    only one is attached to the bundle)
:parameter component: (optional) label of the component(s) requested
:type component: str or list of strings
:parameter dataset: (optional) label of the dataset(s) requested
:type dataset: str or list of strings
:parameter component: (optional) label of the component(s) requested
:type component: str or list of strings
:return: dictionary with keys &lt;component&gt;@&lt;dataset&gt; and computed pblums
    as values (as quantity objects, default units of W)

