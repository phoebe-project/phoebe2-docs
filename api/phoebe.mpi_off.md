### [phoebe](phoebe.md).mpi_off (function)


```py

def mpi_off()

```



Run PHOEBE in Serial Mode.

Default case:
* If PHOEBE is run within an mpirun environment, MPI is ENABLED by default.
* If PHOEBE is not run within an mpirun environment, MPI is DISABLED by default.

When MPI is disabled, PHOEBE will do the following:
* if within mpirun: PHOEBE will run equally on all processors.  The user can
    customize parallelization with access to `phoebe.mpi.nprocs`,
    `phoebe.mpi.myrank`.
* if not within mpirun (ie. in a serial python environment): PHOEBE will
    run on a single processor in serial-mode.  Compute jobs can still
    be detached from the main thread by sending `detach=True` to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) but will stll run
    on a single processor.

See also:
* [phoebe.mpi_on](phoebe.mpi_on.md)

