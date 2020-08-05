# Backends Available in PHOEBE

## Compute Backends

The following backends are available to run a forward model and are passed as the `kind` argument to [b.add_compute](api/phoebe.frontend.bundle.Bundle.add_compute.md):

* [phoebe](api/phoebe.parameters.compute.phoebe.md)
* [legacy](api/phoebe.parameters.compute.legacy.md)
* [ellc](api/phoebe.parameters.compute.ellc.md)
* [jktebop](api/phoebe.parameters.compute.jktebop.md)

To access this list from PHOEBE, call [phoebe.list_available_computes](api/phoebe.list_available_computes.md).

See the [compute backends comparison table](examples/compute_comparison_table.ipynb) for details on the available support for specific physics and datasets for each of the backend wrappers.

## Solver Backends

Solver backends are split into three categories in PHOEBE: estimators, optimizers, and samplers.

To access the full list of available solvers, you can always call [phoebe.list_available_solvers](api/phoebe.list_available_solvers.md).
These can then be passed as the `kind` argument to [b.add_solver](api/phoebe.frontend.bundle.Bundle.add_solver.md):

### Estimators

* [Tutorial: LC estimators](tutorials/LC_estimators_tutorial.ipynb)
* [Tutorial: RV geometry](tutorials/RV_geometry_tutorial.ipynb)
* [estimator.lc_periodogram](api/phoebe.parameters.solver.estimator.lc_periodogram.md)
* [estimator.rv_periodogram](api/phoebe.parameters.solver.estimator.rv_periodogram.md)
* [estimator.lc_geometry](api/phoebe.parameters.solver.estimator.lc_geometry.md)
* [estimator.rv_geometry](api/phoebe.parameters.solver.estimator.rv_geometry.md)
* [estimator.ebai](api/phoebe.parameters.solver.estimator.ebai.md)

### Optimizers

* [optimizer.cg](api/phoebe.parameters.solver.optimizer.cg.md)
* [optimizer.nelder_mead](api/phoebe.parameters.solver.optimizer.nelder_mead.md)
* [optimizer.powell](api/phoebe.parameters.solver.optimizer.powell.md)

### Samplers

* [sampler.dynesty](api/phoebe.parameters.solver.sampler.dynesty.md)
* [sampler.emcee](api/phoebe.parameters.solver.sampler.emcee.md)
