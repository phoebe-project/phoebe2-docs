## Getting Started

The [PHOEBE 2.1](https://github.com/phoebe-project/phoebe2/releases/tag/2.1.0) release aims to provide fully-tested functionality that matches that of the legacy [PHOEBE 1.0](https://github.com/phoebe-project/phoebe1/) (light curve and radial velocity forward models of binary star systems) but with improved precision and a python interface.

Although we have attempted to test as thoroughly as possible, please continue to be skeptical of all results and [report any issues or bugs](https://github.com/phoebe-project/phoebe2/issues) or any [documentation issues or bugs](https://github.com/phoebe-project/phoebe2-docs/issues).

See below for installation instructions as well as a listing of all available tutorials and example scripts.





## Download and Installation

download and installation instructions here

## Tutorials

Each of the following tutorials builds upon previous tutorials, so it will be most efficient to work through them sequentially at first. However, each should run independently, so feel free to jump in at any point to review a specific concept.

For more specific use-cases, see the example scripts below.

Any of these tutorials can be downloaded as an IPython Notebook or a python script. (see the link at the top of any tutorial). To run these you’ll need PHOEBE installed on your system as well, and for the IPython notebooks you’ll also need IPython (sudo pip install jupyter; sudo apt-get install ipython-notebook). Then simply start the notebook service (ipython notebook [downloaded_tutorial.ipynb]). This will allow you to interact with the tutorial - running it line-by-line and making alterations to see how they change the output.

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

## Example Scripts

These example scripts are generally focused to show a single advanced feature or a specific science use-case. They are generally less verbose than the tutorials and assume you’re comfortable with the general concepts and syntax of both Python and PHOEBE. Some scripts may be listed under different sections if they fall under multiple categories.


### Single Stars

* [Sun (rotating single star)](examples/sun.ipynb)


## API Documentation

[API Docs](api.md)

## FAQ

Q: Is PHOEBE 2.x backwards compatible with PHOEBE 2.0 alpha releases?

A: Unfortunately, no. We simply learned too much from the alpha-release that we decided that a complete rewrite was needed. However, many of the syntax concepts should be very familiar if you’ve used the frontend in the alpha releases.

Q: Can I speed up plotting in any way?

A: You could try changing your backend, e.g via matplotlib.rcParams['backend'] = 'Agg' but do this before importing Phoebe.

Q: How do I add a custom passband to PHOEBE 2?

A: You will need a table of intensities that you can download from the PHOEBE homepage. Then you should follow the instructions available phoebe.atmospheres.passbands.Passband

Q: Is PHOEBE 2.x Python 3.x ready?

A: PHOEBE has been tested on Python 2.7 with various compilers. We are working towards testing PHOEBE on Python 3.x.

Q: Is it safe to use Phoebe?

A: For the most part, yes. If you do not have sympy installed, then constraints will be evaluated using the ‘eval’ command - which could potentially be dangerous if you blindly open a bundle from an untrusted source. To avoid this, simply install the sympy optional dependency.
