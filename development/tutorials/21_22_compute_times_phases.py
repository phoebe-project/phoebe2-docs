#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: compute_times & compute_phases
# ==============================

# The 2.2 release brings support for defining the times/phases at which a dataset should be computed during [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) *separately* from the times at which the dataset itself is defined.  This is particularly useful for computing residuals between a dataset with a large number of timepoints and a model computed evenly in phase space, for example.
# 
# Besides the introduction of this new ability, the only significant change between 2.1 and 2.2 is that the [mesh dataset](MESH.ipynb) **no longer** has a `times` parameter.  The `times` parameter has been **replaced** by the `compute_times` parameter (as the mesh doesn't have the ability to attach observable data to the dataset).  Passing `times` to [add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md) (for example: `b.add_dataset('mesh', times=[...])`) will raise a warning in the logger and apply that value to the `compute_times` parameter.  However, any scripts that attempts to find the `times` parameter will need to be updated to use the `compute_times` parameter instead.
# 
# For a more thorough explanation of the new behavior, see the new [Compute Times & Phases tutorial](compute_times_phases.ipynb).
