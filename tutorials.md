# Tutorials

For a quick discussion on why PHOEBE 2 is designed the way it is and why the learning curve seems a little steep see the [General Design Concepts of PHOEBE 2](tutorials/design_concepts.ipynb).  Otherwise, feel free to jump in to the tutorials below.

Each of the following tutorials builds upon previous tutorials, so it will be most efficient to work through them sequentially at first. However, each should run independently, so feel free to jump in at any point to review a specific concept.  The advanced topics below each numbered-item go into more detail on related advanced topics, but are not required to continue to the next tutorial.

For more specific use-cases, see the example scripts below.

1. [The PHOEBE Bundle](tutorials/general_concepts.ipynb)
    * [Advanced: Parameter Types](tutorials/parameters.ipynb)
    * [Advanced: Parameter Units](tutorials/units.ipynb)
    * [Advanced: Building a System](tutorials/building_a_system.ipynb)
    * [Advanced: Contact Binary Hierarchy](tutorials/contact_binary_hierarchy.ipynb)
    * [Advanced: Saving, Loading, and Exporting](tutorials/saving_and_loading.ipynb)
2. [Constraints](tutorials/constraints.ipynb)
    * [Advanced: Constraints and Changing Hierarchices](tutorials/constraints_hierarchies.ipynb)
    * [Advanced: Built-In Constraints](tutorials/constraints_builtin.ipynb)
3. [Datasets](tutorials/datasets.ipynb)
    * [Advanced: Datasets (passband options, dealing with phases, removing datasets)](tutorials/datasets_advanced.ipynb)
4. [Features](tutorials/features.ipynb)
    * [Advanced: Spots](tutorials/spots.ipynb)
    * [Example: Gaussian Processes](examples/minimial_gps.ipynb)
5. [Computing Observables](tutorials/compute.ipynb)
    * [Advanced: Compute Times & Phases](tutorials/compute_times_phases.ipynb)
    * [Advanced: Phase Masking](tutorials/mask_phases.ipynb)
    * [Advanced: Running Multiple Compute Options Simulataneously](tutorials/compute_multiple.ipynb)
    * [Advanced: Alternate Backends](tutorials/alternate_backends.ipynb)
    * [Advanced: Detaching from Run Compute](tutorials/detach.ipynb)
6. [Plotting](tutorials/plotting.ipynb)
    * [Advanced: Plotting Options](tutorials/plotting_advanced.ipynb)
    * [Advanced: Animations](tutorials/animations.ipynb)
    * [Advanced: Accessing and Plotting Meshes](tutorials/meshes.ipynb)
7. [Distributions](tutorials/distributions.ipynb)
8. [Solving the Inverse Problem](tutorials/solver.ipynb)
    * [Advanced: Solver Times](tutorials/solver_times.ipynb)
    * [Advanced: LC Estimators](tutorials/LC_estimators.ipynb)
    * [Advanced: RV Geometry Estimator](tutorials/RV_estimators.ipynb)

## Migrating from PHOEBE 2.2 to PHOEBE 2.3

These tutorials highlight the major changes between versions 2.2.x and 2.3+ in the following topics:

* [Extinction: per-dataset to system-level](tutorials/22_23_extinction.ipynb)
* [Checks: run_checks at system, compute, solver, and solution levels](tutorials/22_23_run_checks.ipynb)
* [Read Only and Constrained Notation](tutorials/22_23_readonly.ipynb)
* [requivsumfrac constraint: replaces requivsum](tutorials/22_23_requivsumfrac.ipynb)
* [Scipy dependency: updated to 1.7+](tutorials/22_23_scipy.ipynb)


## Advanced Tutorials

The following set of advanced tutorials follow the same format as the tutorials above, but cover individual advanced topics that do not belong under any particular category, and do not depend on each other.

These all assume comfort with the tutorials listed above, but should not need to be read in any particular order.

* [Advanced: Running PHOEBE in MPI](tutorials/mpi.ipynb)
* [Advanced: Optimizing Performance](tutorials/optimizing.ipynb)
* [Advanced: Environment Variables](tutorials/envars.ipynb)
* [Advanced: Adding Custom Passband Tables](tutorials/passbands.ipynb)
* [Advanced: Passband Versioning & Updates](tutorials/passband_updates.ipynb)
* [Advanced: Settings](tutorials/settings.ipynb)
