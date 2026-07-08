# Tutorials

For a quick discussion on why PHOEBE 2 is designed the way it is and why the learning curve seems a little steep see the [General Design Concepts of PHOEBE 2](tutorials/design_concepts.ipynb).  Otherwise, feel free to jump in to the tutorials below.

Each of the following tutorials builds upon previous tutorials, so it will be most efficient to work through them sequentially at first. However, each should run independently, so feel free to jump in at any point to review a specific concept.  The advanced topics below each numbered-item go into more detail on related advanced topics, but are not required to continue to the next tutorial.

For more specific use-cases, see the [example scripts](./examples.md).

1. [The PHOEBE Bundle](tutorials/general_concepts.ipynb)
    * [Parameter Types](tutorials/parameters.ipynb)
    * [Parameter Units](tutorials/units.ipynb)
    * [Building a System](tutorials/building_a_system.ipynb)
    * [Contact Binary Hierarchy](tutorials/contact_binary_hierarchy.ipynb)
    * [Semi-Detached Systems](tutorials/requiv_crit_semidetached.ipynb)
    * [Saving, Loading, and Exporting](tutorials/saving_and_loading.ipynb)
2. [Constraints](tutorials/constraints.ipynb)
    * [Constraints and Changing Hierarchies](tutorials/constraints_hierarchies.ipynb)
    * [Built-In Constraints](tutorials/constraints_builtin.ipynb)
    * [Custom Constraints](tutorials/constraints_custom.ipynb)
3. [Datasets](tutorials/datasets.ipynb)
    * [Datasets (passband options, dealing with phases, removing datasets)](tutorials/datasets_advanced.ipynb)
4. [Computing Observables](tutorials/compute.ipynb)
    * [Compute Times & Phases](tutorials/compute_times_phases.ipynb)
    * [Phase Masking](tutorials/mask_phases.ipynb)
    * [Running Multiple Compute Options Simultaneously](tutorials/compute_multiple.ipynb)
    * [Alternate Backends](tutorials/alternate_backends.ipynb)
5. [Plotting](tutorials/plotting.ipynb)
    * [Plotting Options](tutorials/plotting_advanced.ipynb)
    * [Animations](tutorials/animations.ipynb)
    * [Accessing and Plotting Meshes](tutorials/meshes.ipynb)
6. [Features](tutorials/features.ipynb)
    * [Spots](tutorials/spots.ipynb)
    * [Example: Gaussian Processes](examples/minimal_GPs.ipynb)
    * [User-Defined Features](tutorials/user_defined_features.ipynb)
7. [Distributions](tutorials/distributions.ipynb)
    * [Distribution Types](tutorials/distribution_types.ipynb)
    * [Distribution Propagation](tutorials/distribution_propagation.ipynb)
    * [Latex Representations in Distribution Plots](tutorials/latex_repr.ipynb)
8. [Solving the Inverse Problem](tutorials/solver.ipynb)
    * [Solver Times](tutorials/solver_times.ipynb)
    * [LC Estimators](tutorials/LC_estimators.ipynb)
    * [RV Geometry Estimator](tutorials/RV_estimators.ipynb)
    * [Nelder-Mead Optimizer](tutorials/nelder_mead.ipynb)
    * [Differential Evolution Optimizer](tutorials/differential_evolution.ipynb)
    * [EMCEE Sampler](tutorials/emcee.ipynb)
    * [EMCEE Initializing Distribution Requirements](tutorials/emcee_init_from_requires.ipynb)
    * [Continuing EMCEE from a Previous Run](tutorials/emcee_continue_from.ipynb)
    * [Resampling EMCEE from a Previous Run](tutorials/emcee_resampling.ipynb)
    * [Convert Posterior Distributions from EMCEE](tutorials/emcee_distributions_convert.ipynb)
    * [Exporting Solver to an External Machine](tutorials/export_solver.ipynb)
    * [Fitting Limb Darkening Coefficients](tutorials/fitting_ld_coeffs.ipynb)
    * [Custom Cost Function](tutorials/emcee_custom_lnprob.ipynb)
9. [Running Jobs on External Compute Resources](tutorials/server.ipynb)


## Advanced Tutorials

The following set of advanced tutorials follow the same format as the tutorials above, but cover individual advanced topics that do not belong under any particular category, and do not depend on each other.

These all assume comfort with the tutorials listed above, but should not need to be read in any particular order.

* [Advanced: Running PHOEBE in MPI](tutorials/mpi.ipynb)
* [Advanced: Running PHOEBE with Multiprocessing](tutorials/multiprocessing.ipynb)
* [Advanced: Optimizing Performance](tutorials/optimizing.ipynb)
* [Advanced: Environment Variables](tutorials/envars.ipynb)
* [Advanced: Adding Custom Passband Tables](tutorials/passbands.ipynb)
* [Advanced: Passband Versioning & Updates](tutorials/passband_updates.ipynb)
* [Advanced: Settings](tutorials/settings.ipynb)
* [Advanced: Launching the UI from Jupyter](tutorials/ui_jupyter.ipynb)
