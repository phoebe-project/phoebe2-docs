### [phoebe](phoebe.md).multiprocessing_set_nprocs (function)


```py

def multiprocessing_set_nprocs(nprocs)

```



Set a custom number of processors to use within multiprocessing.
MPI will always take preference over multiprocessing.  See [phoebe.mpi_on](phoebe.mpi_on.md)
and [phoebe.mpi_off](phoebe.mpi_off.md).

Multiprocessing is used by
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md) (for some solvers) and
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) when `sample_from` is used.

See also:
* [phoebe.multiprocessing_on](phoebe.multiprocessing_on.md)
* [phoebe.multiprocessing_off](phoebe.multiprocessing_off.md)
* [phoebe.multiprocessing_get_nprocs](phoebe.multiprocessing_get_nprocs.md)
