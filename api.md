
# PHOEBE API Documentation

See the full alphabetical lists for the following modules/classes, or keep scrolling for an organized breakdown of the most used functions and methods.

* [phoebe](api/phoebe.md)
* [phoebe.frontend.bundle.Bundle](api/phoebe.frontend.bundle.Bundle.md)
* [phoebe.parameters](api/phoebe.parameters.md)
* [phoebe.parameters.component](api/phoebe.parameters.component.md)
* [phoebe.parameters.compute](api/phoebe.parameters.compute.md)
* [phoebe.parameters.dataset](api/phoebe.parameters.dataset.md)
* [phoebe.parameters.feature](api/phoebe.parameters.feature.md)
* [phoebe.parameters.hierarchy](api/phoebe.parameters.hierarchy.md)
* [phoebe.parameters.ParameterSet](api/phoebe.parameters.ParameterSet.md)
* [phoebe.parameters.Parameter](api/phoebe.parameters.Parameter.md)
* [phoebe.parameters.IntParameter](api/phoebe.parameters.IntParameter.md)
* [phoebe.parameters.BoolParameter](api/phoebe.parameters.BoolParameter.md)
* [phoebe.parameters.StringParameter](api/phoebe.parameters.StringParameter.md)
* [phoebe.parameters.ChoiceParameter](api/phoebe.parameters.ChoiceParameter.md)
* [phoebe.parameters.SelectParameter](api/phoebe.parameters.SelectParameter.md)
* [phoebe.parameters.ConstraintParameter](api/phoebe.parameters.ConstraintParameter.md)
* [phoebe.parameters.HierarchyParameter](api/phoebe.parameters.HierarchyParameter.md)
* [phoebe.parameters.FloatParameter](api/phoebe.parameters.FloatParameter.md)
* [phoebe.parameters.FloatArrayParameter](api/phoebe.parameters.FloatArrayParameter.md)

## Package-Level Convenience Functions

### Creating Bundles

* [Bundle](api/phoebe.frontend.bundle.Bundle.__init__.md)
* [default_binary](api/phoebe.frontend.bundle.Bundle.default_binary.md)
* [default_star](api/phoebe.frontend.bundle.Bundle.default_star.md)
* [open](api/phoebe.parameters.ParameterSet.open.md)
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

* [list_passbands](api/phoebe.list_passbands.md)
* [list_passband_directories](api/phoebe.list_passband_directories.md)
* [list_installed_passbands](api/phoebe.list_installed_passbands.md)
* [list_online_passbands](api/phoebe.list_online_passbands.md)
* [download_passband](api/phoebe.download_passband.md)
* [get_passband](api/phoebe.get_passband.md)
* [install_passband](api/phoebe.install_passband.md)

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
* [save](api/phoebe.frontend.bundle.Bundle.save.md)

Importing/exporting from other codes:

* [from_legacy](api/phoebe.frontend.bundle.Bundle.from_legacy.md)
* [export_legacy](api/phoebe.frontend.bundle.Bundle.export_legacy.md)

### Initializing New Bundles

* [default_binary](api/phoebe.frontend.bundle.Bundle.default_binary.md)
* [default_star](api/phoebe.frontend.bundle.Bundle.default_star.md)
* [open](api/phoebe.frontend.bundle.Bundle.open.md)
* [from_legacy](api/phoebe.frontend.bundle.Bundle.from_legacy.md)

### Filtering

* [filter](api/phoebe.paramters.ParameterSet.filter.md)
* [exclude](api/phoebe.parameters.ParameterSet.exclude.md)
* [get_parameter](api/phoebe.parameters.ParameterSet.get_parameter.md)
* [get_value](api/phoebe.parameters.ParameterSet.get_value.md)
* [set_value](api/phoebe.parameters.ParameterSet.set_value.md)

### Hierarchy

* [set_hierarchy](api/phoebe.frontend.bundle.Bundle.set_hierarchy.md)
* [get_hierarchy](api/phoebe.frontend.bundle.Bundle.get_hierarchy.md)

### Constraints

* [get_constraint](api/phoebe.frontend.bundle.Bundle.get_constraint.md)
* [run_constraint](api/phoebe.frontend.bundle.Bundle.run_constraint.md)
* [flip_constraint](api/phoebe.frontend.bundle.Bundle.flip_constraint.md)

### Components

* [add_component](api/phoebe.frontend.bundle.Bundle.add_component.md)
* [get_component](api/phoebe.frontend.bundle.Bundle.get_component.md)
* [rename_component](api/phoebe.frontend.bundle.Bundle.rename_component.md)
* [add_orbit](api/phoebe.frontend.bundle.Bundle.add_orbit.md)
* [get_orbit](api/phoebe.frontend.bundle.Bundle.get_orbit.md)
* [add_star](api/phoebe.frontend.bundle.Bundle.add_star.md)
* [get_star](api/phoebe.frontend.bundle.Bundle.get_star.md)
* [add_envelope](api/phoebe.frontend.bundle.Bundle.add_envelope.md)
* [get_envelope](api/phoebe.frontend.bundle.Bundle.get_envelope.md)

### Features

* [add_feature](api/phoebe.frontend.bundle.Bundle.add_feature.md)
* [get_feature](api/phoebe.frontend.bundle.Bundle.get_feature.md)
* [rename_feature](api/phoebe.frontend.bundle.Bundle.rename_feature.md)
* [add_spot](api/phoebe.frontend.bundle.Bundle.add_spot.md)
* [get_spot](api/phoebe.frontend.bundle.Bundle.get_spot.md)

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

### Compute

* [add_compute](api/phoebe.frontend.bundle.Bundle.add_compute.md)
* [get_compute](api/phoebe.frontend.bundle.Bundle.get_compute.md)
* [rename_compute](api/phoebe.frontend.bundle.Bundle.rename_compute.md)
* [remove_compute](api/phoebe.frontend.bundle.Bundle.remove_compute.md)
* [run_compute](api/phoebe.frontend.bundle.Bundle.run_compute.md)

### Model

* [get_model](api/phoebe.frontend.bundle.Bundle.get_model.md)
* [rename_model](api/phoebe.frontend.bundle.Bundle.rename_model.md)
* [remove_model](api/phoebe.frontend.bundle.Bundle.remove_model.md)

### Plotting

* [plot](api/phoebe.parameters.ParameterSet.plot.md)
* [show](api/phoebe.parameters.ParameterSet.show.md)
* [savefig](api/phoebe.parameters.ParameterSet.savefig.md)
* [clf](api/phoebe.parameters.ParameterSet.clf.md)
* [gcf](api/phoebe.parameters.ParameterSet.gcf.md)
