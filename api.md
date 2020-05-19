
# PHOEBE API Documentation

## Package-Level Convenience Functions

### Creating Bundles

* [Bundle](api/phoebe.frontend.bundle.Bundle.__init__.md)
* [default_binary](api/phoebe.frontend.bundle.Bundle.default_binary.md)
* [default_contact_binary](api/phoebe.frontend.bundle.Bundle.default_contact_binary.md)
* [default_star](api/phoebe.frontend.bundle.Bundle.default_star.md)
* [open](api/phoebe.frontend.bundle.Bundle.open.md)
* [from_legacy](api/phoebe.frontend.bundle.Bundle.from_legacy.md)

### Settings

* [logger](api/phoebe.logger.md)
* [mpi_on](api/phoebe.mpi_on.md)
* [mpi_off](api/phoebe.mpi_off.md)
* [interactive_on](api/phoebe.interactive_on.md)
* [interactive_off](api/phoebe.interactive_off.md)
* [interactive_checks_on](api/phoebe.interactive_checks_on.md)
* [interactive_checks_off](api/phoebe.interactive_checks_off.md)
* [interactive_constraints_on](api/phoebe.interactive_constraints_on.md)
* [interactive_constraints_off](api/phoebe.interactive_constraints_off.md)
* [get_download_passband_defaults](api/phoebe.get_download_passband_defaults.md)
* [set_download_passband_defaults](api/phoebe.set_download_passband_defaults.md)
* [reset_settings](api/phoebe.reset_settings.md)

### Atmospheres and Passbands

* [list_passband_directories](api/phoebe.atmospheres.passbands.list_passband_directories.md)
* [list_passbands](api/phoebe.atmospheres.passbands.list_passbands.md)
* [list_installed_passbands](api/phoebe.atmospheres.passbands.list_installed_passbands.md)
* [list_online_passbands](api/phoebe.atmospheres.passbands.list_online_passbands.md)
* [download_passband](api/phoebe.atmospheres.passbands.download_passband.md)
* [install_passband](api/phoebe.atmospheres.passbands.install_passband.md)
* [uninstall_all_passbands](api/phoebe.atmospheres.passbands.uninstall_all_passbands.md)
* [update_passband_available](api/phoebe.atmospheres.passbands.update_passband_available.md)
* [list_all_update_passbands_available](api/phoebe.atmospheres.passbands.list_all_update_passbands_available.md)
* [list_passband_online_history](api/phoebe.atmospheres.passbands.list_passband_online_history.md)
* [update_passband](api/phoebe.atmospheres.passbands.update_passband.md)
* [update_all_passbands](api/phoebe.atmospheres.passbands.update_all_passbands.md)
* [get_passband](api/phoebe.atmospheres.passbands.get_passband.md)


### Available "Kinds"

* [list_available_components](api/phoebe.list_available_components.md)
* [list_available_features](api/phoebe.list_available_features.md)
* [list_available_datasets](api/phoebe.list_available_datasets.md)
* [list_available_figures](api/phoebe.list_available_figures.md)
* [list_available_computes](api/phoebe.list_available_computes.md)
* [list_available_solvers](api/phoebe.list_available_solvers.md)


### Arrays

* [array](api/phoebe.array.md)
* [arange](api/phoebe.arange.md)
* [invspace](api/phoebe.invspace.md)
* [linspace](api/phoebe.linspace.md)
* [logspace](api/phoebe.logspace.md)
* [geomspace](api/phoebe.geomspace.md)

### Distributions

* [gaussian](api/phoebe.gaussian.md)
* [guassian_around](api/phoebe.gaussian_around.md)
* [histogram_from_bins](api/phoebe.histogram_from_bins.md)
* [histogram_from_data](api/phoebe.histogram_from_data.md)
* [mvgaussian](api/phoebe.mvgaussian.md)
* [mvhistogram_from_data](api/phoebe.mvhistogram_from_data.md)
* [uniform](api/phoebe.uniform.md)
* [uniform_around](api/phoebe.uniform_around.md)

## Bundle & ParameterSets

See alphabetical list of [all Bundle methods](api/phoebe.frontend.bundle.Bundle.md) and [all ParameterSet methods](api/phoebe.parameters.ParameterSet.md).

### Saving/Loading

* [__init__](api/phoebe.frontend.bundle.Bundle.__init__.md)
* [open](api/phoebe.frontend.bundle.Bundle.open.md)
* [save](api/phoebe.parameters.ParameterSet.save.md)

Importing/exporting from other codes:

* [from_legacy](api/phoebe.frontend.bundle.Bundle.from_legacy.md)
* [export_legacy](api/phoebe.frontend.bundle.Bundle.export_legacy.md)

### Initializing New Bundles

* [default_binary](api/phoebe.frontend.bundle.Bundle.default_binary.md)
* [default_contact_binary](api/phoebe.frontend.bundle.Bundle.default_contact_binary.md)
* [default_star](api/phoebe.frontend.bundle.Bundle.default_star.md)
* [open](api/phoebe.frontend.bundle.Bundle.open.md)
* [from_legacy](api/phoebe.frontend.bundle.Bundle.from_legacy.md)

### Filtering & Accessing Parameters

* [filter](api/phoebe.parameters.ParameterSet.filter.md)
* [exclude](api/phoebe.parameters.ParameterSet.exclude.md)
* [get_parameter](api/phoebe.parameters.ParameterSet.get_parameter.md)
* [get_value](api/phoebe.parameters.ParameterSet.get_value.md)
* [set_value](api/phoebe.parameters.ParameterSet.set_value.md)
* [set_value_all](api/phoebe.parameters.ParameterSet.set_value_all.md)
* [get_quantity](api/phoebe.parameters.ParameterSet.get_quantity.md)
* [get_default_unit](api/phoebe.parameters.ParameterSet.get_default_unit.md)
* [set_default_unit](api/phoebe.parameters.ParameterSet.set_default_unit.md)
* [set_default_unit_all](api/phoebe.parameters.ParameterSet.set_default_unit_all.md)
* [export_arrays](api/phoebe.parameters.ParameterSet.export_arrays.md)

### System Checks & References

* [run_checks](api/phoebe.frontend.bundle.Bundle.run_checks.md)
* [run_checks_system](api/phoebe.frontend.bundle.Bundle.run_checks_system.md)
* [run_checks_compute](api/phoebe.frontend.bundle.Bundle.run_checks_compute.md)
* [run_checks_solver](api/phoebe.frontend.bundle.Bundle.run_checks_solver.md)
* [run_checks_solution](api/phoebe.frontend.bundle.Bundle.run_checks_solution.md)
* [run_delayed_constraints](api/phoebe.frontend.bundle.Bundle.run_delayed_constraints.md)
* [run_failed_constraints](api/phoebe.frontend.bundle.Bundle.run_failed_constraints.md)
* [references](api/phoebe.frontend.bundle.Bundle.references.md)

### Hierarchy

* [set_hierarchy](api/phoebe.frontend.bundle.Bundle.set_hierarchy.md)
* [get_hierarchy](api/phoebe.frontend.bundle.Bundle.get_hierarchy.md)

### Constraints

* [add_constraint](api/phoebe.frontend.bundle.Bundle.add_constraint.md)
* [get_constraint](api/phoebe.frontend.bundle.Bundle.get_constraint.md)
* [remove_constraint](api/phoebe.frontend.bundle.Bundle.remove_constraint.md)
* [run_constraint](api/phoebe.frontend.bundle.Bundle.run_constraint.md)
* [run_delayed_constraints](api/phoebe.frontend.bundle.Bundle.run_delayed_constraints.md)
* [run_failed_constraints](api/phoebe.frontend.bundle.Bundle.run_failed_constraints.md)
* [flip_constraint](api/phoebe.frontend.bundle.Bundle.flip_constraint.md)
* [flip_constraints_all](api/phoebe.frontend.bundle.Bundle.flip_constraints_all.md)

Available (optional) constraints ([see all](api/phoebe.parameters.constraint.md)):

* [requivsumfrac](api/phoebe.parameters.constraint.requivsumfrac.md)
* [requivratio](api/phoebe.parameters.constraint.requivratio.md)
* [semidetached](api/phoebe.parameters.constraint.semidetached.md)
* [teffratio](api/phoebe.parameters.constraint.teffratio.md)

### Figures

* [add_figure](api/phoebe.frontend.bundle.Bundle.add_figure.md)
* [get_figure](api/phoebe.frontend.bundle.Bundle.get_figure.md)
* [rename_figure](api/phoebe.frontend.bundle.Bundle.rename_figure.md)
* [remove_figure](api/phoebe.frontend.bundle.Bundle.remove_figure.md)
* [run_figure](api/phoebe.frontend.bundle.Bundle.run_figure.md)

See also the Plotting section below for a non-parameter method access to
the same plotting functionality.

### Components

* [add_component](api/phoebe.frontend.bundle.Bundle.add_component.md)
* [get_component](api/phoebe.frontend.bundle.Bundle.get_component.md)
* [rename_component](api/phoebe.frontend.bundle.Bundle.rename_component.md)
* [remove_component](api/phoebe.frontend.bundle.Bundle.remove_component.md)
* [add_orbit](api/phoebe.frontend.bundle.Bundle.add_orbit.md)
* [get_orbit](api/phoebe.frontend.bundle.Bundle.get_orbit.md)
* [add_star](api/phoebe.frontend.bundle.Bundle.add_star.md)
* [get_star](api/phoebe.frontend.bundle.Bundle.get_star.md)
* [add_envelope](api/phoebe.frontend.bundle.Bundle.add_envelope.md)
* [get_envelope](api/phoebe.frontend.bundle.Bundle.get_envelope.md)

Available components ([see all](api/phoebe.parameters.component.md)):

* [star](api/phoebe.parameters.component.star.md)
* [orbit](api/phoebe.parameters.component.orbit.md)
* [envelope](api/phoebe.parameters.component.envelope.md)

### Features

* [add_feature](api/phoebe.frontend.bundle.Bundle.add_feature.md)
* [get_feature](api/phoebe.frontend.bundle.Bundle.get_feature.md)
* [rename_feature](api/phoebe.frontend.bundle.Bundle.rename_feature.md)
* [remove_feature](api/phoebe.frontend.bundle.Bundle.remove_feature.md)
* [enable_feature](api/phoebe.frontend.bundle.Bundle.enable_feature.md)
* [disable_feature](api/phoebe.frontend.bundle.Bundle.disable_feature.md)
* [add_spot](api/phoebe.frontend.bundle.Bundle.add_spot.md)
* [get_spot](api/phoebe.frontend.bundle.Bundle.get_spot.md)
* [add_gaussian_process](api/phoebe.frontend.bundle.Bundle.add_gaussian_process.md)
* [get_gaussian_process](api/phoebe.frontend.bundle.Bundle.get_gaussian_process.md)

Available features ([see all](api/phoebe.parameters.feature.md)):

* [spot](api/phoebe.parameters.feature.spot.md)
* [gaussian_process](api/phoebe.parameters.feature.gaussian_process.md)

### Datasets

* [add_dataset](api/phoebe.frontend.bundle.Bundle.add_dataset.md)
* [get_dataset](api/phoebe.frontend.bundle.Bundle.get_dataset.md)
* [rename_dataset](api/phoebe.frontend.bundle.Bundle.rename_dataset.md)
* [remove_dataset](api/phoebe.frontend.bundle.Bundle.remove_dataset.md)
* [enable_dataset](api/phoebe.frontend.bundle.Bundle.enable_dataset.md)
* [disable_dataset](api/phoebe.frontend.bundle.Bundle.disable_dataset.md)

Dealing with time/phase:

* [get_ephemeris](api/phoebe.frontend.bundle.Bundle.get_ephemeris.md)
* [to_time](api/phoebe.frontend.bundle.Bundle.to_time.md)
* [to_phase](api/phoebe.frontend.bundle.Bundle.to_phase.md)

Available datasets ([see all](api/phoebe.parameters.dataset.md)):

* [lc](api/phoebe.parameters.dataset.lc.md)
* [rv](api/phoebe.parameters.dataset.rv.md)
* [lp](api/phoebe.parameters.dataset.lp.md)
* [orb](api/phoebe.parameters.dataset.orb.md)
* [mesh](api/phoebe.parameters.dataset.mesh.md)

### Distributions

* [add_distribution](api/phoebe.frontend.bundle.Bundle.add_distribution.md)
* [get_distribution](api/phoebe.frontend.bundle.Bundle.get_distribution.md)
* [rename_distribution](api/phoebe.frontend.bundle.Bundle.rename_distribution.md)
* [remove_distribution](api/phoebe.frontend.bundle.Bundle.remove_distribution.md)
* [get_distribution_collection](api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
* [sample_distribution_collection](api/phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
* [plot_distribution_collection](api/phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)

### Compute

* [add_compute](api/phoebe.frontend.bundle.Bundle.add_compute.md)
* [get_compute](api/phoebe.frontend.bundle.Bundle.get_compute.md)
* [rename_compute](api/phoebe.frontend.bundle.Bundle.rename_compute.md)
* [remove_compute](api/phoebe.frontend.bundle.Bundle.remove_compute.md)
* [run_compute](api/phoebe.frontend.bundle.Bundle.run_compute.md)
* [export_compute](api/phoebe.frontend.bundle.Bundle.export_compute.md)
* [compute_pblums](api/phoebe.frontend.bundle.Bundle.compute_pblums.md)
* [compute_l3s](api/phoebe.frontend.bundle.Bundle.compute_l3s.md)
* [compute_ld_coeffs](api/phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md)

Available compute backends ([see all](api/phoebe.parameters.compute.md)):

* [ellc](api/phoebe.parameters.compute.ellc.md)
* [jktebop](api/phoebe.parameters.compute.jktebop)
* [legacy](api/phoebe.parameters.compute.legacy.md)
* [phoebe](api/phoebe.parameters.compute.phoebe.md)

### Model

* [run_compute](api/phoebe.frontend.bundle.Bundle.run_compute.md)
* [attach_job](api/phoebe.frontend.bundle.Bundle.attach_job.md)
* [import_model](api/phoebe.frontend.bundle.Bundle.import_model.md)
* [get_model](api/phoebe.frontend.bundle.Bundle.get_model.md)
* [rename_model](api/phoebe.frontend.bundle.Bundle.rename_model.md)
* [remove_model](api/phoebe.frontend.bundle.Bundle.remove_model.md)

Methods that act on resulting models:

* [plot](api/phoebe.parameters.ParameterSet.plot.md)
* [calculate_residuals](api/phoebe.parameters.ParameterSet.calculate_residuals.md)
* [calculate_chi2](api/phoebe.parameters.ParameterSet.calculate_chi2.md)
* [calculate_lnlikelihood](api/phoebe.parameters.ParameterSet.calculate_lnlikelihood.md)
* [run_figure](api/phoebe.frontend.bundle.Bundle.run_figure.md)


### Solver

* [add_solver](api/phoebe.frontend.bundle.Bundle.add_solver.md)
* [get_solver](api/phoebe.frontend.bundle.Bundle.get_solver.md)
* [rename_solver](api/phoebe.frontend.bundle.Bundle.rename_solver.md)
* [remove_solver](api/phoebe.frontend.bundle.Bundle.remove_solver.md)
* [run_solver](api/phoebe.frontend.bundle.Bundle.run_solver.md)
* [export_solver](api/phoebe.frontend.bundle.Bundle.export_solver.md)

Available solver backends ([see all](api/phoebe.parameters.solver.md)):

* [estimator.lc_periodogram](api/phoebe.parameters.solver.estimator.lc_periodogram.md)
* [estimator.rv_periodogram](api/phoebe.parameters.solver.estimator.rv_periodogram.md)
* [estimator.lc_geometry](api/phoebe.parameters.solver.estimator.lc_geometry.md)
* [estimator.rv_geometry](api/phoebe.parameters.solver.estimator.rv_geometry.md)
* [estimator.ebai](api/phoebe.parameters.solver.estimator.ebai.md)
* [optimizer.cg](api/phoebe.parameters.solver.optimizer.cg.md)
* [optimizer.nelder_mead](api/phoebe.parameters.solver.optimizer.nelder_mead.md)
* [optimizer.powell](api/phoebe.parameters.solver.optimizer.powell.md)
* [sampler.dynesty](api/phoebe.parameters.solver.sampler.dynesty.md)
* [sampler.emcee](api/phoebe.parameters.solver.sampler.emcee.md)

Access to merit-function values:

* [calculate_residuals](api/phoebe.parameters.ParameterSet.calculate_residuals.md)
* [calculate_chi2](api/phoebe.parameters.ParameterSet.calculate_chi2.md)
* [calculate_lnlikelihood](api/phoebe.parameters.ParameterSet.calculate_lnlikelihood.md)
* [calculate_lnp](api/phoebe.frontend.bundle.Bundle.calculate_lnp.md)

### Solution

* [run_solver](api/phoebe.frontend.bundle.Bundle.run_solver.md)
* [attach_job](api/phoebe.frontend.bundle.Bundle.attach_job.md)
* [import_solution](api/phoebe.frontend.bundle.Bundle.import_solution.md)
* [get_solution](api/phoebe.frontend.bundle.Bundle.get_solution.md)
* [adopt_solution](api/phoebe.frontend.bundle.Bundle.adopt_solution.md)
* [rename_solution](api/phoebe.frontend.bundle.Bundle.rename_solution.md)
* [remove_solution](api/phoebe.frontend.bundle.Bundle.remove_solution.md)

### Plotting

* [plot](api/phoebe.parameters.ParameterSet.plot.md)
* [show](api/phoebe.parameters.ParameterSet.show.md)
* [savefig](api/phoebe.parameters.ParameterSet.savefig.md)
* [clf](api/phoebe.parameters.ParameterSet.clf.md)
* [gcf](api/phoebe.parameters.ParameterSet.gcf.md)

See the Figure section above for the ability to define figures via parameters
and rebuild them by calling [run_figure](api/phoebe.frontend.bundle.Bundle.run_figure.md).


## Package Listing

* [phoebe](api/phoebe.md)
* [phoebe.frontend.bundle.Bundle](api/phoebe.frontend.bundle.Bundle.md)
* [phoebe.parameters](api/phoebe.parameters.md)
* [phoebe.parameters.component](api/phoebe.parameters.component.md)
* [phoebe.parameters.compute](api/phoebe.parameters.compute.md)
* [phoebe.parameters.constraint](api/phoebe.parameters.constraint.md)
* [phoebe.parameters.dataset](api/phoebe.parameters.dataset.md)
* [phoebe.parameters.feature](api/phoebe.parameters.feature.md)
* [phoebe.parameters.figure.dataset](api/phoebe.parameters.figure.dataset.md)
* [phoebe.parameters.figure.distribution](api/phoebe.parameters.figure.distribution.md)
* [phoebe.parameters.figure.solution](api/phoebe.parameters.figure.solution.md)
* [phoebe.parameters.hierarchy](api/phoebe.parameters.hierarchy.md)
* [phoebe.parameters.solver.estimator](api/phoebe.parameters.solver.estimator.md)
* [phoebe.parameters.solver.optimizer](api/phoebe.parameters.solver.optimizer.md)
* [phoebe.parameters.solver.sampler](api/phoebe.parameters.solver.sampler.md)
* [phoebe.parameters.ParameterSet](api/phoebe.parameters.ParameterSet.md)
* [phoebe.parameters.Parameter](api/phoebe.parameters.Parameter.md)
* [phoebe.parameters.IntParameter](api/phoebe.parameters.IntParameter.md)
* [phoebe.parameters.FloatParameter](api/phoebe.parameters.FloatParameter.md)
* [phoebe.parameters.FloatArrayParameter](api/phoebe.parameters.FloatArrayParameter.md)
* [phoebe.parameters.BoolParameter](api/phoebe.parameters.BoolParameter.md)
* [phoebe.parameters.StringParameter](api/phoebe.parameters.StringParameter.md)
* [phoebe.parameters.ChoiceParameter](api/phoebe.parameters.ChoiceParameter.md)
* [phoebe.parameters.SelectParameter](api/phoebe.parameters.SelectParameter.md)
* [phoebe.parameters.DictParameter](api/phoebe.parameters.DictParameter.md)
* [phoebe.parameters.ConstraintParameter](api/phoebe.parameters.ConstraintParameter.md)
* [phoebe.parameters.DistributionParameter](api/phoebe.parameters.DistributionParameter.md)
* [phoebe.parameters.HierarchyParameter](api/phoebe.parameters.HierarchyParameter.md)
* [phoebe.parameters.UnitParameter](api/phoebe.parameters.UnitParameter.md)
* [phoebe.parameters.JobParameter](api/phoebe.parameters.JobParameter.md)
* [phoebe.atmospheres.passbands](api/phoebe.atmospheres.passbands.md)
* [phoebe.atmospheres.passbands.Passband](api/phoebe.atmospheres.passbands.Passband.md)
* [phoebe.distortions.roche](api/phoebe.distortions.roche.md)
* [phoebe.distortions.rotstar](api/phoebe.distortions.rotstar.md)
