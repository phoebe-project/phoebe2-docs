#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: phasing in time-dependent systems
# ============================
# 
# The equations used in [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md) and [b.to_phase](../api/phoebe.frontend.bundle.Bundle.to_phase.md) for cases where `dpdt != 0.0` were incorrect.  These have no been fixed.  In addition, it is now possible to override the `dpdt` used in phasing (including by passing `dpdt=0.0` to ignore `dpdt` entirely) when calling [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md), [b.to_phase](../api/phoebe.frontend.bundle.Bundle.to_phase.md), [b.get_ephemeris](../api/phoebe.frontend.bundle.Bundle.get_ephemeris.md), or when plotting in phase via [b.plot](../api/phoebe.parameters.ParameterSet.plot.md).
# 
# See also:
# 
# * [dpdt](dpdt.ipynb)
# * [mask_phases](mask_phases.ipynb)
# * [compute times & phases](compute_times_phases.ipynb)

# In[ ]:




