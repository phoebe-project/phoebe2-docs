
# PHOEBE API Documentation

See the full alphabetical lists for the following modules/classes, or see below for a list of the most used functions and methods.

* [Bundle](api/Bundle.md)
* [ParameterSet](api/ParameterSet.md)
* [Parameter](api/Parameter.md)
* [IntParameter](api/IntParameter.md)
* [BoolParameter](api/BoolParameter.md)
* [StringParameter](api/StringParameter.md)
* [ChoiceParameter](api/ChoiceParameter.md)
* [SelectParameter](api/SelectParameter.md)
* [FloatParameter](api/FloatParameter.md)
* [FloatArrayParameter](api/FloatArrayParameter.md)

## Package-Level Convenience Functions

### Creating Bundles

* [Bundle](api/Bundle.__init__.md)
* [default_binary](api/Bundle.default_binary.md)
* [default_star](api/Bundle.default_star.md)
* [open](api/ParameterSet.open.md)
* [from_legacy](api/Bundle.from_legacy.md)

### Settings

* logger
* mpi_on
* mpi_off
* interactive_on
* interactive_off
* interactive_checks_on
* interactive_checks_off
* interactive_constraints_on
* interactive_constraints_off
* reset_settings

### Units and Constants

* u (units)
* c (constants)

### Atmospheres and Passbands

* list_passbands
* list_passband_directories
* list_installed_passbands
* list_online_passbands
* download_passband
* get_passband
* install_passband

### Arrays

* array
* arange
* linspace
* logspace
* geomspace


## Bundle & ParameterSets

See alphabetical list of [all Bundle methods](api/Bundle.md) and [all ParameterSet methods](api/ParameterSet.md).

### Saving/Loading

* [__init__](api/Bundle.__init__.md)
* [open](api/ParameterSet.open.md)
* [save](api/ParameterSet.save.md)

Importing/exporting from other codes:

* [from_legacy](api/Bundle.from_legacy.md)
* [export_legacy](api/Bundle.export_legacy.md)

### Initializing New Bundles

* [default_binary](api/Bundle.default_binary.md)
* [default_star](api/Bundle.default_star.md)
* [open](api/ParameterSet.open.md)
* [from_legacy](api/Bundle.from_legacy.md)

### Filtering

* [filter](api/ParameterSet.filter.md)
* [exclude](api/ParameterSet.exclude.md)
* [get_parameter](api/ParameterSet.get_parameter.md)

### Hierarchy

* [set_hierarchy](api/Bundle.set_hierarchy.md)
* [get_hierarchy](api/Bundle.get_hierarchy.md)

### Constraints

* [get_constraint](api/Bundle.get_constraint.md)
* [run_constraint](api/Bundle.run_constraint.md)
* [flip_constraint](api/Bundle.flip_constraint.md)

### Components

* [add_component](api/Bundle.add_component.md)
* [get_component](api/Bundle.get_component.md)
* [rename_component](api/Bundle.rename_component.md)
* [add_orbit](api/Bundle.add_orbit.md)
* [get_orbit](api/Bundle.get_orbit.md)
* [add_star](api/Bundle.add_star.md)
* [get_star](api/Bundle.get_star.md)
* [add_envelope](api/Bundle.add_envelope.md)
* [get_envelope](api/Bundle.get_envelope.md)

### Features

* [add_feature](api/Bundle.add_feature.md)
* [get_feature](api/Bundle.get_feature.md)
* [rename_feature](api/Bundle.rename_feature.md)
* [add_spot](api/Bundle.add_spot.md)
* [get_spot](api/Bundle.get_spot.md)

### Datasets

* [add_dataset](api/Bundle.add_dataset.md)
* [get_dataset](api/Bundle.get_dataset.md)
* [rename_dataset](api/Bundle.rename_dataset.md)
* [remove_dataset](api/Bundle.remove_dataset.md)
* [enable_dataset](api/Bundle.enable_dataset.md)
* [disable_dataset](api/Bundle.disable_dataset.md)

Dealing with time/phase:

* [get_ephemeris](api/Bundle.get_ephemeris.md)
* [to_time](api/Bundle.to_time.md)
* [to_phase](api/Bundle.to_phase.md)

### Compute

* [add_compute](api/Bundle.add_compute.md)
* [get_compute](api/Bundle.get_compute.md)
* [rename_compute](api/Bundle.rename_compute.md)
* [remove_compute](api/Bundle.remove_compute.md)
* [run_compute](api/Bundle.run_compute.md)

### Model

* [get_model](api/Bundle.get_model.md)
* [rename_model](api/Bundle.rename_model.md)
* [remove_model](api/Bundle.remove_model.md)

### Plotting

* [plot](api/ParameterSet.plot.md)
* [show](api/ParameterSet.show.md)
* [savefig](api/ParameterSet.savefig.md)
* [animate](api/ParameterSet.animate.md)
* [clf](api/ParameterSet.clf.md)
* [gcf](api/ParameterSet.gcf.md)
