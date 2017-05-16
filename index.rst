

Getting Started
==================================

The `PHOEBE 2.0 <https://github.com/phoebe-project/phoebe2/releases/tag/2.0>`_
release aims to provide fully-tested functionality that matches that of the
legacy `PHOEBE 1.0 <https://github.com/phoebe-project/phoebe1/>`_ (light curve
and radial velocity forward models of binary star systems) but with improved
precision and a python interface.

Although we have attempted to test as thoroughly as possible, please continue
to be skeptical of all results and `report any issues or bugs
<https://github.com/phoebe-project/phoebe2/issues>`_ or any `documentation
issues or bugs <https://github.com/phoebe-project/phoebe2-docs/issues>`_.

See below for installation instructions as well as a listing of all available
tutorials and example scripts.

Supported Physics (from PHOEBE 1.0)
----------------------------------------

* detached roche binaries
* keplerian orbits (including eccentric orbits with volume conservation)
* passbands/atmospheres
* limb-darkening
* gravity brightening
* reflection (heating without redistribution)
* finite integration time via oversampling
* circular spots
* contact systems (to mimic WD)

New Physics (not in PHOEBE 1.0)
----------------------------------------

* beaming/boosting
* single rotating stars


Unsupported Physics (from PHOEBE 1.0)
----------------------------------------

PHOEBE 2.0 can not yet handle:

* full support for contact systems
* semi-detached/single contact systems (planned future development)
* X-ray binaries


Unsupported Convenience Functionality
-----------------------------------------

* fitting (planned future development)
* GUI (in development)
* data in magnitudes (dropping support - convert manually)
* data in phases (dropping support - but function provided to convert during import)
* phase shifts


Planned Physics Support
------------------------------------------
More advanced physics can be found in the PHOEBE 2.0-alpha releases
and will be ported to future official releases as soon as they can be tested robustly.

Planned (new) future features include:

* heating (heat redistribution)
* triple and N-body systems (in development)
* N-body dynamics (in development)
* misaligned binaries (in development)
* pulsations (in development)
* bayesian (MCMC) fitting
* synthetic spectra
* synthetic eclipse timing variations (ETVs) (in development)
* synthetic interferometry


Download and Installation
===============================

Dependencies
--------------------------------

Note for **mac users**: it is suggested to use `homebrew to install a parallel version
of python <https://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/>`_.
PHOEBE has currently been tested to compile correctly using homebrew on El Capitan.

The C++ code in PHOEBE requires a compiler that supports C++11, either of the following
should build correctly:

* g++5 (or newer)
* clang3.3 (or newer)

Note for **Ubuntu 14.04 users**: g++5 is not installed by default.  You'll likely
need to to do the following in order to install PHOEBE:
::

   sudo add-apt-repository ppa:ubuntu-toolchain-r/test
   sudo apt-get install g++-5 gcc-5 libstdc++-5-dev
   export CXX=g++-5


PHOEBE requires python 2.7+ (not yet fully tested on python 3.x) with the following packages:

* numpy (may need 1.10+)
* scipy
* astropy (1.0+)

And suggested packages (required for some optional but commonly used features):

* matplotlib (suggested for plotting)
* sympy (for safer and more flexible constraints)

And optional packages (used for less commonly used features):

* mpld3 (alternate plotting - devel version only)
* bokeh (alternate plotting - devel version only)

From PIP
------------------------------

Installing PHOEBE from PIP is probably the easiest.  To install the latest version:

::

   pip install phoebe

To update a previous installation:

::

   pip install -U phoebe

And to uninstall:

::

   pip uninstall phoebe

If pip gives any problems automatically installing dependencies, install them manually first:

::

   pip install numpy scipy astropy matplotlib

Please check the version of PHOEBE you have installed to make sure you are using the corresponding version of the documentation.  You can check the version once PHOEBE is imported via :code:`phoebe.__version__`


Virtual Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If installing in a virtual environment, PHOEBE sets the matplotlib backend to 'TkAgg' instead of 'Agg' by default.  To override this, set the backend yourself before importing PHOEBE.  To use 'TkAgg', you may need to have python-tk installed on your system.  See `<http://matplotlib.org/faq/virtualenv_faq.html>`_ for more information.

To create a virtual environment and install PHOEBE, do the following, replacing "<myphoebedir>" with your (perferably empty or not existing) directory of choice:

::

   pip install virtualenv
   virtualenv <myphoebedir>
   source <myphoebedir>/bin/activate
   pip install numpy scipy astropy matplotlib phoebe



To leave the virtual environment:

::

   deactivate


And to destroy the virtual environment permanently:

::

   rm -rf <myphoebedir>



From Source
--------------------------------

Download Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download via the `github repository <https://github.com/phoebe-project/phoebe2/>`_:

::

   git clone --depth=1 https://github.com/phoebe-project/phoebe2.git


Note: developers should exclude the depth=1 to get the entire git history (download size will be larger).



Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NOTE:  PHOEBE 2.0 builds to a python module named 'phoebe' which may
conflict with the alpha version if you have that installed (but will not
conflict with PHOEBE 0.2x, 0.3x, or 1.0).  If you do have PHOEBE 2.0-alpha
installed, please uninstall before attempting to install PHOEBE 2.0.  If you
have a previous version of PHOEBE 2.x (including PHOEBE 2.0-beta), installing
will overwrite that version (unless you use a virtual environment).


To install without admin rights for a single-user:

::

   python setup.py build
   python setup.py install --user



or to install system-wide with admin rights:

::

   python setup.py build
   sudo python setup.py install


Testing
--------------------------------

The following additional dependencies are required
to run the nosetests:

* `nose <http://nose.readthedocs.io/en/latest/>`_
* `PHOEBE 1.0 <https://github.com/phoebe-project/phoebe1>`_ with the phoebe-py wrapper
* `photodynam <https://github.com/phoebe-project/photodynam>`_
* `rebound <https://github.com/hannorein/rebound>`_

To run all tests locally on your machine, run the following in the 'tests'
directory in the source.

::

   python run_tests nosetests


Please `report any issues or bugs <https://github.com/phoebe-project/phoebe2/issues>`_.


Tutorials
===============================

Each of the following tutorials builds upon previous tutorials, so it will be
most efficient to work through them sequentially at first.  However, each should
run independently, so feel free to jump in at any point to review a specific
concept.

For more specific use-cases, see the example scripts below.

Any of these tutorials can be downloaded as an IPython Notebook or a python script.
(see the link at the top of any tutorial).  To run these you'll need PHOEBE
installed on your system as well, and for the IPython notebooks you'll also need
IPython (sudo pip install jupyter; sudo apt-get install ipython-notebook).
Then simply start the notebook service (ipython notebook [downloaded_tutorial.ipynb]).
This will allow you to interact with the tutorial - running it line-by-line
and making alterations to see how they change the output.

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :numbered:

   General Concepts<tutorials/general_concepts>
   Building a System<tutorials/building_a_system>
   Saving and Loading<tutorials/saving_and_loading>
   Constraints<tutorials/constraints>
   Datasets<tutorials/datasets>
   Computing Observables<tutorials/compute>
   Plotting<tutorials/plotting>
   Accessing and Plotting Meshes<tutorials/meshes>
   Fitting<tutorials/fitting>


Advanced Tutorials
=======================

The following set of advanced tutorials follow the same format as the tutorials
above, but cover individual advanced topics and do not depend on each other.

These all assume comfort with the tutorials listed above, but should not need to
be read in any particular order.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Advanced: Settings<tutorials/settings>
   Advanced: Animations<tutorials/animations>
   Advanced: Alternate Plotting Backends<tutorials/alternate_plotting>
   Advanced: Alternate Backends<tutorials/alternate_backends>
   Advanced: Detaching from Run Compute<tutorials/detach>
   Advanced: Digging into the Backend<tutorials/backend>
   Advanced (coming soon): Creating Custom Parameters<tutorials/custom_parameters>
   Advanced (coming soon): Creating Custom Constraints<tutorials/constraint_create>
   Advanced (coming soon): Time Derivatives<tutorials/time_derivatives>
   Advanced (coming soon): Undo/Redo<tutorials/undo_redo>



Datasets and Observables
===============================

The following tutorials aim to both explain the general logic that PHOEBE
uses to compute observables as well as explaining the parameters, fields, and options
for each observable type.

These aim to be quite thorough and may not be best for light-reading.  They
expect a comfortable understanding of using PHOEBE and python

.. toctree::
   :maxdepth: 1
   :titlesonly:

   How does PHOEBE compute observables<tutorials/phoebe_logic>
   Orbits (orb)<tutorials/ORB>
   Meshes (mesh)<tutorials/MESH>
   Light Curves (lc)<tutorials/LC>
   Radial Velocities (rv)<tutorials/RV>
   Eclipse Timing Variations (etv)<tutorials/ETV>


Explanations of Individual Parameters
========================================

The following tutorials aim to explain the implementation and usage of
some of the physical effects that are incorporated in PHOEBE.  These explain
the relevant parameters and try to demonstrate how they affect the resulting
synthetic models, but expect a comfortable understanding of using PHOEBE and python

.. toctree::
   :maxdepth: 1
   :titlesonly:


   Potentials<tutorials/pot>
   Eccentricity (Volume Conservation)<tutorials/ecc>
   Apsidal Motion<tutorials/apsidal_motion>
   Systemic Velocity<tutorials/vgamma>
   Passband Luminosity<tutorials/pblum>
   Third Light<tutorials/l3>
   Distance<tutorials/distance>
   Limb Darkening<tutorials/limb_darkening>
   Gravitational Redshift (RVs)<tutorials/grav_redshift>
   Reddening and Extinction (not yet implemented)<tutorials/reddening_extinction>
   Reflection and Heating<tutorials/reflection_heating>
   Beaming and Boosting (not yet implemented)<tutorials/beaming_boosting>
   Eclipse Detection<tutorials/eclipse>
   Intensity Weighting<tutorials/intens_weighting>

COMING SOON (differences between various t0s and phasing)


Example Scripts
===============================

These example scripts are generally focussed to show a single advanced feature
or a specific science use-case.  They are generally less verbose than the tutorials
and assume you're comfortable with the general concepts and syntax of both
Python and PHOEBE.  Some scripts may be listed under different sections if they
fall under multiple categories.


Single Stars
------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Sun (rotating single star)<examples/sun>
   Single Star with Pulsations (TESTING - not yet supported)<examples/rotstar_pulsations>



Detached Binary Stars
------------------------------


.. toctree::
   :maxdepth: 1
   :titlesonly:

   Minimal Example to Produce a Synthetic Light Curve<examples/minimal_synthetic>
   Complete Binary Animation<examples/animation_binary_complete>
   Rossiter-McLaughlin Effect (RVs)<examples/rossiter_mclaughlin>
   Wilson-Devinney Style Meshing<examples/mesh_wd>
   Detached Binary: Roche vs Rotstar <examples/detached_rotstar>
   Binary with Spots<examples/binary_spots>
   Binary with Pulsations (TESTING - not yet supported)<examples/binary_pulsations>



Contact Binary Stars (NOT YET SUPPORTED)
----------------------------------------------------------


.. toctree::
   :maxdepth: 1
   :titlesonly:

   Minimal Contact Binary System (TESTING - not yet supported)<examples/minimal_contact_binary>
   Comparing Contact Binary System PHOEBE 2.0 vs PHOEBE Legacy (TESTING - not yet supported)<examples/legacy_contact_binary>



Triple Stars (NOT YET SUPPORTED)
-------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Minimal Hierarchical Triple (TESTING - not yet supported)<examples/hierarchical_triple>
   Minimal Dynamical Triple (TESTING - not yet supported)<examples/dynamical_triple>
   Hierarchical Triple vs Photodynam (TESTING - not yet supported) <examples/hierarchical_triple_pd>
   LTTE ETVs in a Hierarchical Triple (TESTING - not yet supported) <examples/hierarchical_triple_etvs>
   KOI 126 (TESTING - not yet supported)<examples/koi126>
   Comparing Roche Distortion for Nbody vs Keplerian (Binary) <examples/hybrid_binary>




Planetary System (NOT YET SUPPORTED)
-------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Sun-Earth (TESTING - not yet supported)<examples/sun_earth>



Circumbinary Planets (NOT YET SUPPORTED)
------------------------------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Kepler 16 (TESTING - not yet supported)<examples/kepler16>



Spots
------------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Binary with Spots<examples/binary_spots>
   Comparing Spots in PHOEBE 2.0 vs PHOEBE Legacy<examples/legacy_spots>



Pulsations (NOT YET SUPPORTED)
------------------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Single Star with Pulsations (TESTING - not yet supported)<examples/rotstar_pulsations>
   Binary with Pulsations (TESTING - not yet supported)<examples/binary_pulsations>



Advanced Constraints (NOT YET SUPPORTED)
------------------------------

COMING SOON (creating custom constraints, main-sequence, etc)



Advanced Plotting
------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Complete Binary Animation<examples/animation_binary_complete>



Alternate Backends
------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Comparing PHOEBE 2.0 vs PHOEBE Legacy<examples/legacy>
   Comparing Contact Binary System PHOEBE 2.0 vs PHOEBE Legacy (TESTING - not yet supported)<examples/legacy_contact_binary>
   Comparing Spots in PHOEBE 2.0 vs PHOEBE Legacy (TESTING - not yet supported)<examples/legacy_spots>
   Comparing PHOEBE 2.0 vs Photodynam (Binary)<examples/photodynam>
   Comparing PHOEBE 2.0 vs Photodynam (Hierarchical Triple)<examples/hierarchical_triple_pd>
   Comparing PHOEBE 2.0 vs JKTEBOP <examples/jktebop>


Frontend API Docs
===============================

.. toctree::
   :maxdepth: 2

   Frontend <api/phoebe.frontend>
   Parameters <api/phoebe.parameters>


Backend (Advanced) API Docs
===============================

.. toctree::
   :maxdepth: 2

   Backend <api/phoebe.backend>
   Atmospheres <api/phoebe.atmospheres>
   Constraints <api/phoebe.constraints>
   Dynamics <api/phoebe.dynamics>
   Distortions <api/phoebe.distortions>


Development Information
================================

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Style Guidelines (coming soon)<development/style>
   Development in the Frontend (coming soon)<development/devel_frontend>
   Development in the Backend (coming soon)<development/devel_backend>
   Tutorials and Scripts<development/tutorials_scripts>
   API Documentation (coming soon)<development/api>
   Testing (coming soon)<development/testing>
   Benchmarking (coming soon)<development/benchmark>
   Committing Code (coming soon)<development/committing>
   Releasing a New Version (coming soon)<development/release>

Citing PHOEBE 2.0
================================

If using PHOEBE 2.0, please consider citing the following papers, as appropriate:

* `PHOEBE 2.0 release paper <http://adsabs.harvard.edu/abs/2016ApJS..227...29P>`_
* `PHOEBE 1.0 release paper <http://adsabs.harvard.edu/abs/2005ApJ...628..426P>`_

See also the full up-to-date list of `PHOEBE publications <http://phoebe-project.org/publications>`_

FAQ
================================


*Q: Is PHOEBE 2.0 backwards compatible with PHOEBE 2.0 alpha releases?*

A: Unfortunately, no.  We simply learned too much from the alpha-release that
we decided that a complete rewrite was needed.  However, many of the syntax
concepts should be very familiar if you've used the frontend in the alpha releases.

*Q: Can I speed up plotting in any way?*

A: You could try changing your backend, e.g via ``matplotlib.rcParams['backend'] = 'Agg'``
but do this before importing Phoebe.

*Q: How do I add a custom passband to PHOEBE 2?*

A: You will need a table of intensities that you can download from the PHOEBE homepage.
Then you should follow the instructions available :class:`phoebe.atmospheres.passbands.Passband`

*Q: Is PHOEBE 2.x Python 3.x ready?*

A: PHOEBE has been tested on Python 2.7 with various compilers.  We are working
towards testing PHOEBE on Python 3.x.

*Q: Is it safe to use Phoebe?*

A: For the most part, yes.  If you do not have sympy installed, then constraints
will be evaluated using the 'eval' command - which could potentially be dangerous
if you blindly open a bundle from an untrusted source.  To avoid this, simply
install the sympy optional dependency.
