### [phoebe](phoebe.md).mpi_on (function)


```py

def mpi_on(nprocs=None)

```



ENABLE PHOEBE to use MPI (parallelization).

Default case:
* If PHOEBE is run within an mpirun environment, MPI is ENABLED by default.
* If PHOEBE is not run within an mpirun environment, MPI is DISABLED by default.

When MPI is enabled, PHOEBE will do the following:
* if within mpirun: uses PHOEBE's built-in per-dataset or per-time
    parallelization
* if not within mpirun (ie. in a serial python environment): will spawn a
    separate thread at [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md),
    using `nprocs` processors.  This separate thread will be detached
    from the main thread if sending `detach=True` to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

See also:
* [phoebe.mpi_off](phoebe.mpi_off.md)

Arguments
----------
* `nprocs` (int, optional): number of processors.  Only applicable if **NOT**
    within mpirun (see above).

