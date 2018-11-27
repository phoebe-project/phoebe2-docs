#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: requiv
# ============================

# PHOEBE 2.0.x defined the size of a star by its polar radius, `rpole`. In addition, there was a constraint between `rpole` and the equipotential, `pot`, which could be reversed by the user so that `pot` defines the size. When using different values for `distortion_method` (roche, rotstar, sphere, etc), the polar radius was conserved.
# 
# However, with the introduction of misalignment in PHOEBE 2.1, this way of parameterizing the stars became insufficient.  Starting in PHOEBE 2.1, the sizes of stars are now parametrized by the *equivalent* radius, `requiv`.  When using different values for `distortion_method`, it is the value of `requiv` that is now conserved. Thus, in general, polar radius is no longer conserved.
# 
# For contact binary systems, there is an `requiv` parameter for each star (or each "half" of the contact system), as well as a constrained parameter for the potential (`pot`) and fillout-factor (`fillout_factor`) for the envelope as a whole. As contact binary systems must be aligned, circular and synchronous, and only support `distortion_method='roche'`, this mapping is still possible and provides significant conveniences. By default, the `requiv` of the primary star is adjustable by the user, but the constraints can be reversed so that any *one* of these four parameters can be set, with the rest being constrained.

# In[ ]:




