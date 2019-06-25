#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: ld_mode & ld_coeffs_source
# ==============================

# PHOEBE 2.2 introduces the capability to interpolate limb-darkening coefficients for a given `ld_func` (i.e. linear, quadratic, etc).  In order to do so, there is now a new parameter called `ld_mode` (for datasets only, bolometric limb-darkening remains unchanged without any interpolation options) which defaults to 'interp'.  This is the same behavior as `ld_func='interp'` in previous version of PHOEBE.  Any code setting `ld_func` to 'interp' should now be changed to set `ld_mode` instead.
# 
# As `ld_mode` is set to 'interp' by default, the `ld_func` parameter is no longer visible.  If setting `ld_func` to something other than 'interp', you must first change the value of `ld_mode` (to either 'manual' which allows setting `ld_coeffs` as in previous releases, or to 'lookup' which is the new behavior introduced in 2.2).
# 
# For a more thorough explanation of the new behavior, see the updated [limb darkening tutorial](limb_darkening.ipynb).
