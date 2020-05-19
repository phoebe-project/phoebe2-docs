# Tutorials

For a quick discussion on why PHOEBE 2 is designed the way it is and why the learning curve seems a little steep see the [General Design Concepts of PHOEBE 2](tutorials/design_concepts.ipynb).  Otherwise, feel free to jump in to the tutorials below.

Each of the following tutorials builds upon previous tutorials, so it will be most efficient to work through them sequentially at first. However, each should run independently, so feel free to jump in at any point to review a specific concept.

For more specific use-cases, see the example scripts below.

1. [General Concepts](tutorials/general_concepts.ipynb)
2. [Building a System](tutorials/building_a_system.ipynb)
3. [Saving and Loading](tutorials/saving_and_loading.ipynb)
4. [Constraints](tutorials/constraints.ipynb)
5. [Datasets](tutorials/datasets.ipynb)
6. [Computing Observables](tutorials/compute.ipynb)
7. [Plotting](tutorials/plotting.ipynb)
8. [Accessing and Plotting Meshes](tutorials/meshes.ipynb)
9. Solving the Inverse Problem

## Migrating from PHOEBE 2.2 to PHOEBE 2.3

These tutorials highlight the major changes between versions 2.2.x and 2.3+ in the following topics:

* Extinction: per-dataset to system-level
* Checks: run_checks at system, compute, solver, and solution levels
* requivsumfrac constraint: replaces requivsum
* Scipy dependency: updated to 1.7+


## Advanced tutorials

The following set of advanced tutorials follow the same format as the tutorials above, but cover individual advanced topics and do not depend on each other.

These all assume comfort with the tutorials listed above, but should not need to be read in any particular order.

* [Advanced: Contact Binary Hierarchy](tutorials/contact_binary_hierarchy.ipynb)
* [Advanced: Compute Times & Phases](tutorials/compute_times_phases.ipynb)
* [Advanced: Animations](tutorials/animations.ipynb)
* [Advanced: Alternate Backends](tutorials/alternate_backends.ipynb)
* [Advanced: Running PHOEBE in MPI](tutorials/mpi.ipynb)
* [Advanced: Optimizing Performance](tutorials/optimizing.ipynb)
* [Advanced: Detaching from Run Compute](tutorials/detach.ipynb)
* [Advanced: Adding Custom Passband Tables](tutorials/passbands.ipynb)
* [Advanced: Passband Versioning & Updates](tutorials/passband_updates.ipynb)
* [Advanced: Settings](tutorials/settings.ipynb)
