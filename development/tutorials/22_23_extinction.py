#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: Extinction
# ============================
# 
# The extinction parameters (`ebv`, `Av`, `Rv`) were originally in the 'dataset' context in the 2.2 release.  These have now been moved to the 'system' context, which means there will only be one set of the parameters per-bundle, making fitting extinction much more practical.  If importing a bundle created in version 2.2, these will be migrated automatically, with a warning raised if different values were found (but ultimately adopting the first set of values found).
# 
# See the [extinction tutorial](./ebv_Av_Rv.ipynb) for more details.

# In[ ]:




