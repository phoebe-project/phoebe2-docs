#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: distinction between anomalous and sidereal period in apsidal motion cases
# ============================
# 
# In previous releases, the `period` parameter (in orbits) was defined interenally as the anomalistic period.  In order to more cleanly handle [apsidal motion](apsidal_motion.ipynb), the `period` parameter is now defined clearly as the sidereal period with a new `period_anom` parameter (and [constraint](constraints.ipynb)) visible whenever `dperdt != 0.0`.  Note that these two periods are identical in all cases where `dperdt == 0.0`.
# 
# In the case where apsidal motion is present, this distinction affects the default phasing as well as the constraint for Kepler's third law, synchronicity, and [dpdt](dpdt.ipynb).  See the [apsidal motion tutorial](apsidal_motion.ipynb) for full details on the current implementation.
# 
# See also:
# 
# * [apsidal motion (dperdt, period vs period_anom)](apsidal_motion.ipynb)

# In[ ]:




