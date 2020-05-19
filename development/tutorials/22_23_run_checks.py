#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: run_checks
# ============================
# 
# To add increased flexibility for solvers, [b.run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md) has been split into multiple methods:
# 
# * [b.run_checks_system](../api/phoebe.frontend.bundle.Bundle.run_checks_system.md)
# * [b.run_checks_compute](../api/phoebe.frontend.bundle.Bundle.run_checks_compute.md)
# * [b.run_checks_solver](../api/phoebe.frontend.bundle.Bundle.run_checks_solver.md)
# * [b.run_checks_solution](../api/phoebe.frontend.bundle.Bundle.run_checks_solution.md)
# 
# [b.run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md) still exists and calls all the sub-checks, but now [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) will only call and require [b.run_checks_system](../api/phoebe.frontend.bundle.Bundle.run_checks_system.md) and [b.run_checks_compute](../api/phoebe.frontend.bundle.Bundle.run_checks_compute.md) to pass, wherease [run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md) will also require [b.run_checks_solver](../api/phoebe.frontend.bundle.Bundle.run_checks_solver.md) to pass (in addition to [b.run_checks_compute](../api/phoebe.frontend.bundle.Bundle.run_checks_compute.md) at each iteration of the solver)

# In[ ]:




