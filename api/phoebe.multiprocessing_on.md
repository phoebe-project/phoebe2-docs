### [phoebe](phoebe.md).multiprocessing_on (function)


```py

def multiprocessing_on()

```



Enable multiprocessing to use all CPUs available (this is the state by default).
MPI will always take preference over multiprocessing.  See [phoebe.mpi_on](phoebe.mpi_on.md)
and [phoebe.mpi_off](phoebe.mpi_off.md).

Multiprocessing is used by
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md) (for some solvers) and
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) when `sample_from` is used.

See also:
* [phoebe.multiprocessing_off](phoebe.multiprocessing_off.md)
* [phoebe.multiprocessing_get_nprocs](phoebe.multiprocessing_get_nprocs.md)
* [phoebe.multiprocessing_set_nprocs](phoebe.multiprocessing_set_nprocs.md)
