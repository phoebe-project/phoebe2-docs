### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).export_compute (function)


```py

def export_compute(self, script_fname, out_fname=None, compute=None, model=None, dataset=None, pause=False, log_level=None, import_from_older=False, **kwargs)

```



Export a script to call run_compute externally (in a different thread
or on a different machine).  To automatically detach to a different
thread and load the results, see [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)
with `detach=True`.

After running the resulting `script_fname`, `out_fname` will be created,
which will contain a ParameterSet of the model parameters.  To attach
that model to this bundle, see [phoebe.frontend.bundle.Bundle.import_model](phoebe.frontend.bundle.Bundle.import_model.md).

Arguments
------------
* `script_fname` (string): the filename of the python script to be generated.
* `out_fname` (string, optional): the filename of the output file that `script_fname`
    will write when executed.  Once executed, pass this filename to
    [phoebe.frontend.bundle.Bundle.import_model](phoebe.frontend.bundle.Bundle.import_model.md) to load the resulting
    model.  If not provided, the script will automatically export
    to `script_fname`.out (where the filename is determined at runtime,
    so if you rename the script exported here, the resulting filename
    will reflect that change and be appended with '.out').
* `compute` (string, optional): name of the compute options to use.
    If not provided or None, run_compute will use an existing set of
    attached compute options if only 1 exists.  If more than 1 exist,
    then compute becomes a required argument.  If no compute options
    exist, then this will use default options and create and attach
    a new set of compute options with a default label.
* `model` (string, optional): name of the resulting model.  If not
    provided this will default to 'latest'.  NOTE: existing models
    with the same name will be overwritten depending on the value
    of `overwrite` (see below).   See also
    [phoebe.frontend.bundle.Bundle.rename_model](phoebe.frontend.bundle.Bundle.rename_model.md) to rename a model after
    creation.
* `dataset` (list, dict, or string, optional, default=None): filter for which datasets
    should be computed.  If provided as a dictionary, keys should be compute
    labels provided in `compute`.  If None, will use the `enabled` parameters in the
    `compute` options.  If not None, will override all `enabled` parameters.
* `pause` (bool, optional, default=False): whether to raise an input
    with instructions for running the exported script and calling
    [phoebe.frontend.bundle.Bundle.import_model](phoebe.frontend.bundle.Bundle.import_model.md).  Particularly
    useful if running in an interactive notebook or a script.
* `log_level` (string, optional, default=None): `clevel` to set in the
    logger in the exported script.  See [phoebe.logger](phoebe.logger.md).
* `import_from_older` (boolean, optional, default=False): whether to allow
    the script to run on a newer version of PHOEBE.  If True and executing
    the outputed script (`script_fname`) on a newer version of PHOEBE,
    the bundle will attempt to migrate to the newer version.  If False,
    an error will be raised when attempting to run the script.  See
    also: [phoebe.frontend.bundle.Bundle.open](phoebe.frontend.bundle.Bundle.open.md).
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md) before computing the model.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `**kwargs`:: any values in the compute options to temporarily
    override for this single compute run (parameter values will revert
    after run_compute is finished).

Returns
-----------
* `script_fname`, `out_fname`.  Where running `script_fname` will result
  in the model being written to `out_fname`.

