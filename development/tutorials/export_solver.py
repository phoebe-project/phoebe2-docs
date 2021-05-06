#!/usr/bin/env python
# coding: utf-8

# # Advanced: Exporting Solvers to an External Machine
# 
# Running solvers (especially optimizers and samplers) can be quite expensive and infeasible to run on a desktop or laptop.  However, it is inconvenient to edit the solver options or use interactive sessions on remote machines or High Performance Clusters.
# 
# PHOEBE allows for setting up the options for a solver locally (whether by script, in an interactive python session, in a jupyter notebook session, or in the UI) and then export a standalone script to run in an external thread or machine.
# 
# Automatically submitting and managing jobs on external solvers is supported as of the 2.4 release and will be covered in a [future tutorial on servers](./server.ipynb). Alternatively, you can manually export a script and copy it to any machine to run the computations.
# 
# Once all options are set, simply call [b.save](../api/phoebe.frontend.bundle.Bundle.save.md) to save a copy of the bundle, then [b.export_solver](../api/phoebe.frontend.bundle.Bundle.export_solver.md).  This writes a python script which can be copied to any machine and submitted via a job scheduler, if necessary.  Once complete, call [phoebe.load](../api/phoebe.load.md) to load the saved bundle, followed by [b.import_solution](../api/phoebe.frontend.bundle.Bundle.import_solution.md) on the file created by the script.
# 
# Some solvers (currently [emcee](../api/phoebe.parameters.solver.sampler.emcee.md) and [dynesty](../api/phoebe.parameters.solver.sampler.dynesty.md)) also have a `progress_every_niters` parameter.  If this is non-zero, the resulting output file will be written to disk at the specified number of iterations.  This allows for monitoring the progress of the solver and killing the separate thread/job once sufficiently sampled/converged.  In these cases, it can be convenient to set `niters` to a large number and manually killing the job once the monitored progress achieves a specified criteria.
