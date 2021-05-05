### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).export_solver (function)


```py

def export_solver(self, script_fname, out_fname=None, solver=None, solution=None, pause=False, autocontinue=False, import_from_older=False, log_level=None, **kwargs)

```



Export a script to call run_solver externally (in a different thread
or on a different machine).

After running the resulting `script_fname`, `out_fname` will be created,
which will contain a ParameterSet of the solution parameters.  To attach
that solution to this bundle, see [phoebe.frontend.bundle.Bundle.import_solution](phoebe.frontend.bundle.Bundle.import_solution.md).

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
* `solver` (string, optional, default=None):
* `solution` (string, optional, default=None):
* `pause` (bool, optional, default=False): whether to raise an input
    with instructions for running the exported script and calling
    [phoebe.frontend.bundle.Bundle.import_solution](phoebe.frontend.bundle.Bundle.import_solution.md).  Particularly
    useful if running in an interactive notebook or a script.
* `autocontinue` (bool, optional, default=False): **NEW IN 2.3.33** override `continue_from`
    in `solver` to continue from `out_fname` (or `script_fname`.out or
    .progress files) if those files exist.  This is useful to set to True
    and then resubmit the same script if not converged (although care should
    be taken to ensure multiple scripts aren't reading/writing from the
    same filenames).  `continue_from` must be a parameter in `solver` options,
    or an error will be raised if `autocontinue=True`
* `import_from_older` (boolean, optional, default=False): whether to allow
    the script to run on a newer version of PHOEBE.  If True and executing
    the outputed script (`script_fname`) on a newer version of PHOEBE,
    the bundle will attempt to migrate to the newer version.  If False,
    an error will be raised when attempting to run the script.  See
    also: [phoebe.frontend.bundle.Bundle.open](phoebe.frontend.bundle.Bundle.open.md).
* `log_level` (string, optional, default=None): `clevel` to set in the
    logger in the exported script.  See [phoebe.logger](phoebe.logger.md).
* `custom_lnprobability_callable` (callable, optional, default=None):
    custom callable function which takes the following arguments:
    `b, model, lnpriors, priors, priors_combine` and returns the lnprobability
    to override the built-in lnprobability of [phoebe.frontend.bundle.Bundle.calculate_lnp](phoebe.frontend.bundle.Bundle.calculate_lnp.md) (on priors)
    + [phoebe.parameters.ParameterSet.calculate_lnlikelihood](phoebe.parameters.ParameterSet.calculate_lnlikelihood.md).  For
    optimizers that minimize, the negative returned values will be minimized.
    NOTE: if defined in an interactive session and inspect.getsource fails,
    this will raise an error.
* `**kwargs`:: any values in the solver or compute options to temporarily
    override for this single solver run (parameter values will revert
    after run_solver is finished).

Returns
-----------
* `script_fname`, `out_fname`.  Where running `script_fname` will result
  in the model being written to `out_fname`.
