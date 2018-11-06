## Tutorials

Each of the following tutorials builds upon previous tutorials, so it will be most efficient to work through them sequentially at first. However, each should run independently, so feel free to jump in at any point to review a specific concept.

For more specific use-cases, see the example scripts below.

Any of these tutorials can be downloaded as an IPython/Jupyter Notebook or a python script. (see the link at the top of any tutorial). To run these you’ll need PHOEBE installed on your system as well, and for the IPython/Jupyter notebooks you’ll also need IPython (`sudo pip install jupyter; sudo apt-get install ipython-notebook`). Then simply start the notebook service (`ipython notebook` or `jupyter notebook`). This will allow you to interact with the tutorial - running it line-by-line and making alterations to see how they change the output.

1. [General Concepts](tutorials/general_concepts.ipynb)
2. [Building a System](tutorials/building_a_system.ipynb)
3. [Saving and Loading](tutorials/saving_and_loading.ipynb)
4. [Constraints](tutorials/constraints.ipynb)
5. [Datasets](tutorials/datasets.ipynb)
6. [Computing Observables](tutorials/compute.ipynb)
7. [Plotting](tutorials/plotting.ipynb)
8. [Accessing and Plotting Meshes](tutorials/meshes.ipynb)

### Migrating from PHOEBE 2.0 to PHOEBE 2.1

These tutorials highlight the major changes between versions 2.0.x and 2.1+ in the following topics:

* [Potential/Rpole to Requiv](tutorials/20_21_requiv.ipynb)
* [Semidetached Constraints](tutorials/20_21_semidetached.ipynb)
* [Plotting](tutorials/20_21_plotting.ipynb)
* [Meshes](tutorials/20_21_meshes.ipynb)
* [nparray](tutorials/20_21_nparray.ipynb)

### Advanced tutorials

The following set of advanced tutorials follow the same format as the tutorials above, but cover individual advanced topics and do not depend on each other.

These all assume comfort with the tutorials listed above, but should not need to be read in any particular order.

* [Advanced: Settings](tutorials/settings.ipynb)
* [Advanced: Animations](tutorials/animations.ipynb)
* [Advanced: Alternate Backends](tutorials/alternate_backends.ipynb)
* [Advanced: Detaching from Run Compute](tutorials/detach.ipynb)
* [Advanced: Adding Custom Passband Tables](tutorials/passbands.ipynb)

### Datasets and Observables
The following tutorials aim to both explain the general logic that PHOEBE uses to compute observables as well as explaining the parameters, fields, and options for each observable type.

These aim to be quite thorough and may not be best for light-reading. They expect a comfortable understanding of using PHOEBE and python

* [How does PHOEBE compute observables](tutorials/phoebe_logic.ipynb)
* [Orbits (orb)](tutorials/ORB.ipynb)
* [Meshes (mesh)](tutorials/MESH.ipynb)
* [Light Curves (lc)](tutorials/LC.ipynb)
* [Radial Velocities (rv)](tutorials/RV.ipynb)
* [Line Profiles (lp)](tutorials/LP.ipynb)

### Explanations of Individual Parameters

The following tutorials aim to explain the implementation and usage of some of the physical effects that are incorporated in PHOEBE. These explain the relevant parameters and try to demonstrate how they affect the resulting synthetic models, but expect a comfortable understanding of using PHOEBE and python

* [Various t0s](tutorials/t0s.ipynb)
* [Equivalent Radius](tutorials/requiv.ipynb)
* [Potentials (replaced by Equivalent Radius in PHOEBE 2.1+)](tutorials/pot.ipynb)
* [Eccentricity (Volume Conservation)](tutorials/ecc.ipynb)
* [Apsidal Motion](tutorials/apsidal_motion.ipynb)
* [Systemic Velocity (vgamma)](tutorials/vgamma.ipynb)
* [Passband Luminosity](tutorials/pblum.ipynb)
* [Third Light](tutorials/l3.ipynb)
* [Distance](tutorials/distance.ipynb)
* [Limb Darkening](tutorials/limb_darkening.ipynb)
* [Gravitational Redshift (RVs)](tutorials/grav_redshift.ipynb)
* [Reflection and Heating](tutorials/reflection_heating.ipynb)
* [Beaming and Boosting (not yet implemented)](tutorials/beaming_boosting.ipynb)
* [Eclipse Detection](tutorials/eclipse.ipynb)
* [Intensity Weighting](tutorials/intens_weighting.ipynb)


## Example Scripts

These example scripts are generally focused to show a single advanced feature or a specific science use-case. They are generally less verbose than the tutorials and assume you’re comfortable with the general concepts and syntax of both Python and PHOEBE. Some scripts may be listed under different sections if they fall under multiple categories.

### Single Stars

* [Sun (rotating single star)](examples/sun.ipynb)


### Detached Binary Stars

* [Minimal Example to Produce a Synthetic Light Curve](examples/minimal_synthetic.ipynb)
* [Complete Binary Animation](examples/animation_binary_complete.ipynb)
* [Rossiter-McLaughlin Effect (RVs)](examples/rossiter_mclaughlin.ipynb)
* [Wilson-Devinney Style Meshing](examples/mesh_wd.ipynb)
* [Detached Binary: Roche vs Rotstar](examples/detached_rotstar.ipynb)
* [Binary with Spots](examples/binary_spots.ipynb)


### Contact Binary Stars

* [Minimal Contact Binary System](examples/minimal_contact_binary.ipynb)
* [Comparing Contact Binary System PHOEBE 2 vs PHOEBE Legacy](examples/legacy_contact_binary.ipynb)

### Spots

* [Binary with Spots](examples/binary_spots.ipynb)
* [Single Star with Spots](examples/single_spots.ipynb)
* [Comparing Spots in PHOEBE 2 vs PHOEBE Legacy](examples/legacy_spots.ipynb)

### Advanced Plotting

* [Complete Binary Animation](examples/animation_binary_complete.ipynb)

### Alternate Backends

* [Comparing PHOEBE 2 vs PHOEBE Legacy](examples/legacy.ipynb)
* [Comparing Contact Binary System PHOEBE 2 vs PHOEBE Legacy](examples/legacy_contact_binary.ipynb)
* [Comparing Spots in PHOEBE 2 vs PHOEBE Legacy](examples/legacy_spots.ipynb)



## API Documentation

[API Docs](api.md)
