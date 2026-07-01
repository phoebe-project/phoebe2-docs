### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).blending_factor (function)


```py

def blending_factor(d, func='sigmoid', scale=15, offset=0.5)

```



Computes the amount of blending for coordinate `d`.

This auxiliary function returns a factor between 0 and 1 that is used for
blending a model atmosphere into blackbody atmosphere as the atmosphere
values fall off the grid. By default the function uses a sigmoid to
compute the factor, where a sigmoid is defined as:

f(d) = 1 - (1 + e^{-tau (d-Delta)})^{-1},

where tau is scaling and Delta is offset.

Arguments
---------
* `d` (float or array): distance or distances from the grid
* `func` (string, optional, default='sigmoid'):
    type of blending function; it can be 'linear' or 'sigmoid'
* `scale` (float, optional, default=15):
    if `func`='sigmoid', `scale` is the scaling for the sigmoid
* `offset` (float, optional, default=0.5):
    if `func`='sigmoid', `offset` is the zero-point between 0 and 1.

Returns
-------
* (float) blending factor between 0 and 1

