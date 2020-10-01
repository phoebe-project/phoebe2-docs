#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: logg constraint units
# ============================
# 
# The [logg constraint](../api/phoebe.parameters.constraint.logg) used to work in SI units, but has now been changed to deal with solar units.  When importing a bundle file from before PHOEBE 2.3, the constraint will be rebuilt.  This change was due to an inconsistency in the way units were translated to SI units within MPI.

# In[ ]:




