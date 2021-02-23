#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: compute_phases_t0 renamed to phases_t0
# ============================
# 
# The parameter which defines the `t0` to use when translating between `compute_times` and `compute_phases` has been renamed in PHOEBE 2.3 from `compute_phases_t0` to `phases_t0` as it is now also used for `mask_phases` and `solver_times`.
# 
# For more details see:
# * [Advanced: Compute Times & Phases](./compute_times_phases.ipynb)
# * [Advanced: Phase Masking](./mask_phases.ipynb)
# * [Advanced: Solver Times](./solver_times.ipynb)
# 
