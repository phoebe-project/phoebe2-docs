### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[server](phoebe.parameters.server.md).awsec2 (function)


```py

def awsec2(server, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for an awsec2 server.

The server referenced by `crimpl_name` must be configured on the local
machine with [crimpl](<a href="http://crimpl.readthedocs.io">http://crimpl.readthedocs.io</a>).

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_server](phoebe.frontend.bundle.Bundle.add_server.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_server](phoebe.frontend.bundle.Bundle.add_server.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Arguments
----------
* `crimpl_name` (string, optional): Name of server saved in crimpl.  Must be
    available on the local machine.  See docs for more details.
* `conda_env` (string, optional, default='default'): Name of conda
    environment on remote machine to run jobs.  Will be created and
    necessary deps installed (if `install_deps=True`) if does not exist.
* `isolate_env` (bool, optional, default=False): Whether to clone the
    conda_env environment per-job.
* `nprocs` (int, optional, default=4): Number of processors to allocate to
    each job
* `use_mpi` (bool, optional, default=True): Whether to use mpi on the remote
   machine
* `install_deps` (bool, optional, default=True): Whether to ensure required
    dependencies are installed in conda_env on the remote machine (adds some
    overhead)
* `terminate_on_complete` (bool, optional, default=True): Whether to
    terminate the server after the job is completed for detached jobs only.
    This will override to False for jobs to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)
    or [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md) with `detach=False`.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

