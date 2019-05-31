
# PHOEBE API Documentation

See the full alphabetical lists for the following modules/classes, or keep scrolling for an organized breakdown of the most used functions and methods.

* [phoebe](api/phoebe.md)
* [phoebe.frontend.bundle.Bundle](api/phoebe.frontend.bundle.Bundle.md)
* [phoebe.parameters](api/phoebe.parameters.md)
* [phoebe.parameters.component](api/phoebe.parameters.component.md)
* [phoebe.parameters.compute](api/phoebe.parameters.compute.md)
* [phoebe.parameters.constraint](api/phoebe.parameters.constraint.md)
* [phoebe.parameters.dataset](api/phoebe.parameters.dataset.md)
* [phoebe.parameters.feature](api/phoebe.parameters.feature.md)
* [phoebe.parameters.hierarchy](api/phoebe.parameters.hierarchy.md)
* [phoebe.parameters.ParameterSet](api/phoebe.parameters.ParameterSet.md)
* [phoebe.parameters.Parameter](api/phoebe.parameters.Parameter.md)
* [phoebe.parameters.IntParameter](api/phoebe.parameters.IntParameter.md)
* [phoebe.parameters.FloatParameter](api/phoebe.parameters.FloatParameter.md)
* [phoebe.parameters.FloatArrayParameter](api/phoebe.parameters.FloatArrayParameter.md)
* [phoebe.parameters.BoolParameter](api/phoebe.parameters.BoolParameter.md)
* [phoebe.parameters.StringParameter](api/phoebe.parameters.StringParameter.md)
* [phoebe.parameters.ChoiceParameter](api/phoebe.parameters.ChoiceParameter.md)
* [phoebe.parameters.SelectParameter](api/phoebe.parameters.SelectParameter.md)
* [phoebe.parameters.ConstraintParameter](api/phoebe.parameters.ConstraintParameter.md)
* [phoebe.parameters.HierarchyParameter](api/phoebe.parameters.HierarchyParameter.md)
* [phoebe.parameters.JobParameter](api/phoebe.parameters.JobParameter.md)
* [phoebe.atmospheres.passbands](api/phoebe.atmospheres.passbands.md)
* [phoebe.atmospheres.passbands.Passband](api/phoebe.atmospheres.passbands.Passband.md)

## Package-Level Convenience Functions

### Creating Bundles

* [Bundle](api/phoebe.frontend.bundle.Bundle.__init__.md)
* [default_binary](api/phoebe.frontend.bundle.Bundle.default_binary.md)
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
* [reset_settings](api/phoebe.reset_settings.md)

### Atmospheres and Passbands

* [list_passbands](api/phoebe.atmospheres.passbands.list_passbands.md)
* [list_passband_directories](api/phoebe.atmospheres.passbands.list_passband_directories.md)
* [list_installed_passbands](api/phoebe.atmospheres.passbands.list_installed_passbands.md)
* [list_online_passbands](api/phoebe.atmospheres.passbands.list_online_passbands.md)
* [download_passband](api/phoebe.atmospheres.passbands.download_passband.md)
* [install_passband](api/phoebe.atmospheres.passbands.install_passband.md)
* [uninstall_all_passbands](api/phoebe.atmospheres.passbands.uninstall_all_passbands.md)
* [list_all_update_passbands_available](api/phoebe.atmospheres.passbands.list_alll_update_passbands_available.md)
* [update_passband_available](api/phoebe.atmospheres.passbands.update_passband_available.md)
* [update_all_passbands](api/phoebe.atmospheres.passbands.update_all_passbands.md)
* [get_passband](api/phoebe.atmospheres.passbands.get_passband.md)


### Arrays

* [array](api/phoebe.array.md)
* [arange](api/phoebe.arange.md)
* [linspace](api/phoebe.linspace.md)
* [logspace](api/phoebe.logspace.md)
* [geomspace](api/phoebe.geomspace.md)

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
* [default_star](api/phoebe.frontend.bundle.Bundle.default_star.md)
* [open](api/phoebe.frontend.bundle.Bundle.open.md)
* [from_legacy](api/phoebe.frontend.bundle.Bundle.from_legacy.md)

### Filtering

* [filter](api/phoebe.parameters.ParameterSet.filter.md)
* [exclude](api/phoebe.parameters.ParameterSet.exclude.md)
* [get_parameter](api/phoebe.parameters.ParameterSet.get_parameter.md)
* [get_value](api/phoebe.parameters.ParameterSet.get_value.md)
* [set_value](api/phoebe.parameters.ParameterSet.set_value.md)
* [set_value_all](api/phoebe.parameters.ParameterSet.set_value_all.md)
* [get_quantity](api/phoebe.parameters.ParameterSet.get_quantity.md)

### Hierarchy

* [set_hierarchy](api/phoebe.frontend.bundle.Bundle.set_hierarchy.md)
* [get_hierarchy](api/phoebe.frontend.bundle.Bundle.get_hierarchy.md)

### Constraints

* [add_constraint](api/phoebe.frontend.bundle.Bundle.add_constraint.md)
* [get_constraint](api/phoebe.frontend.bundle.Bundle.get_constraint.md)
* [run_constraint](api/phoebe.frontend.bundle.Bundle.run_constraint.md)
* [flip_constraint](api/phoebe.frontend.bundle.Bundle.flip_constraint.md)
* [flip_constraint_all](api/phoebe.frontend.bundle.Bundle.flip_constraint_all.md)

Available (optional) constraints ([see all](api/phoebe.parameters.constraint.md)):

* [semidetached](api/phoebe.parameters.constraint.semidetached.md)
* [logg](api/phoebe.parameters.constraint.logg.md)

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
* [add_spot](api/phoebe.frontend.bundle.Bundle.add_spot.md)
* [get_spot](api/phoebe.frontend.bundle.Bundle.get_spot.md)

Available features ([see all](api/phoebe.parameters.feature.md)):

* [spot](api/phoebe.parameters.feature.spot.md)

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

### Compute

* [add_compute](api/phoebe.frontend.bundle.Bundle.add_compute.md)
* [get_compute](api/phoebe.frontend.bundle.Bundle.get_compute.md)
* [rename_compute](api/phoebe.frontend.bundle.Bundle.rename_compute.md)
* [remove_compute](api/phoebe.frontend.bundle.Bundle.remove_compute.md)
* [run_compute](api/phoebe.frontend.bundle.Bundle.run_compute.md)
* [compute_pblums](api/phoebe.frontend.bundle.Bundle.compute_pblums.md)
* [compute_l3s](api/phoebe.fronted.bundle.Bundle.compute_l3s.md)
* [compute_ld_coeffs](api/phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md)

Available compute backends ([see all](api/phoebe.parameterse.compute.md)):

* [phoebe](api/phoebe.parameters.compute.phoebe.md)
* [legacy](api/phoebe.parameters.compute.legacy.md)

### Model

* [run_compute](api/phoebe.frontend.bundle.Bundle.run_compute.md)
* [get_model](api/phoebe.frontend.bundle.Bundle.get_model.md)
* [rename_model](api/phoebe.frontend.bundle.Bundle.rename_model.md)
* [remove_model](api/phoebe.frontend.bundle.Bundle.remove_model.md)

Methods that act on resulting models:

* [plot](api/phoebe.parameters.ParameterSet.plot.md)
* [compute_residuals](api/phoebe.parameters.ParameterSet.compute_residuals.md)

### Plotting

* [plot](api/phoebe.parameters.ParameterSet.plot.md)
* [show](api/phoebe.parameters.ParameterSet.show.md)
* [savefig](api/phoebe.parameters.ParameterSet.savefig.md)
* [clf](api/phoebe.parameters.ParameterSet.clf.md)
* [gcf](api/phoebe.parameters.ParameterSet.gcf.md)
