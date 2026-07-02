#!/usr/bin/env python
# coding: utf-8

# General Design Concepts of PHOEBE 2
# ======================
# 
# This document aims to introduce the design concepts for PHOEBE 2 and explain **why** it is designed in a slightly non-pythonic way.  Hopefully understanding the rationale for these decisions will help to make the learning curve a little less steep - but feel free to skip straight to the tutorials as all the concepts will be re-explained there within the context of PHOEBE.
# 
# General Goals of PHOEBE 2
# ------------------------------------------
# 
# Many eclipsing binary codes exist in the field, each with their own strenghts and weaknesses.  The major motivation for *re-writing* PHOEBE into PHOEBE 2 was to address the improvement in photometric precision in the Kepler-era.  As such, we try to emphasize the following goals even when at the cost of others:
# 
# * **Precision**: achieve a precision (both numerical and in terms of advanced physics) necessary to adequately model observations from Kepler and future space missions;
# * **Flexibility**: build a framework that is modular and allows for future expansion to include new physics and observables;
# * **Self-Consistency**: re-use the same frameworks and concepts within the code so that once the basics are mastered, more advanced functionality should be easy to learn;
# * **User-friendly**: replace the custom scripting language used in PHOEBE legacy with the widely-adopted Python scripting language.
# 
# Whenever possible, without sacrificing the above goals, we also aim to achieve:
# 
# * **Efficiency**: optimize the code to minimize computation time;
# * **Simplicity**: don't overcomplicate things and try to keep the learning-curve manageable.

# Why not use simple function calls?
# -----------------------------------------------
# 
# Placing yourself in the shoes of a developer designing a code to model observables of eclipsing binary systems in Python, you would probably first consider the simplest option which is to have simple functions for each observable type to generate synthetic models.
# 
# So for example, something like:
# 
# ```
# fluxes = phoebe.lc(times=[...], teffA=6000, teffB=5500, massA=1.1, ...)
# rvs = phoebe.rv(times=[...], ...)
# ```
# 
# Although this is easy to learn and very intuitive, it does have several significant drawbacks for our use-case:
# * Gets unwieldy if you want to pass a lot of (non-default) options
# * Using A and B suffixes (ie. `teffA` vs `teffB`) for two stars in a binary makes sense, but becomes much more complicated if we want to extend to triples, quadruples, etc.
# * Does not allow for any optimizations between observables/datasets.  One of the more expensive steps in numerical modeling of EBs is creating the mesh of the star.  Here if we want a light curve and radial velocity curve at the same time, we are unnecessarily duplicating that step.

# Ok, so why not objects with attributes and methods?
# ------------------------------------------------------
# 
# Any Python developer considering these drawbacks above will immediately realize that classes/objects will solve them.  We can now have a `Orbit` and `Star` class and instantiate one `Orbit` and two `Stars` (for a binary system).
# 
# Imagine something like:
# 
# ```
# primary = Star(teff=6000, mass=1.2)
# primary.requiv = 1.1
# 
# secondary = Star(teff=5500, mass=0.9, requiv=0.9)
# 
# orbit = Orbit(period=3.14, primary=primary, secondary=secondary)
# print(orbit.primary.mass)
# ```
# 
# Now dealing with a lot of non-default options is a lot cleaner, as they can either be passed to the instantiation of the respective `Orbit` or `Star`, *or* we can change the attribute on the object later.
# 
# A framework like this also adds a built-in object hierarchy.  We no longer have `teffA` vs `teffB` but rather `orbit.primary.teff` vs `orbit.secondary.teff`, which will extend much nicer to higher-ordered systems.
# 
# We could pass this `orbit` object to the functions above, but then we still have the optimization issue.  So instead, we would also want include our dataset information (passbands, etc) so that we can compute all of our datasets at once.  Maybe something like:
# 
# ```
# orbit.add_lc(LC(times=[...], passband='Johnson:V', ...))
# orbit.add_rv(RV(times=[...], ...))
# 
# fluxes, rvs = phoebe.create_synthetics(orbit)
# ```
# 
# We've now addressed all of the drawbacks from the simple function design, but we have uncovered a few more:
# * Some parameters needed to define a dataset are still star-dependent - so where are these stored?  For example, would we expect access limb-darkening as `orbit.lcs[0].ld.primary` or `orbit.primary.lcs[0].ld` or `orbit.lcs[0].primary.ld`?
# * Do we define a mass-ratio `q` in the `Orbit` class or individual masses in the `Star` class?
# 
# The two points above have really driven the design of the PHOEBE 2 interface and add significant power and flexibility, but it has come at the cost of a somewhat non-pythonic and a steep learning curve.

# Introducing the Bundle
# ----------------------------------------------
# 
# ### a database-like store of parameters
# 
# What we really need to address the first point above is a *database* of options, where each *parameter* is tagged with the *dataset* and *component/star* that it is associate with.  This would then remove the fixed, ambiguous, hierarchy of the parameters and allow the user to access the parameters through any order of "drilling-down" (what we call *filtering* in PHOEBE 2).
# 
# In pseudo-code, this will look something like:
# 
# ```
# b = phoebe.default_binary()
# b.get_parameter(qualifier='teff', component='primary')
# b.get_value(qualifier='teff', component='primary')
# ```
# 
# for the case of `teffA` vs `teffB` from before.  Or for the case of limb-darkening:
# 
# ```
# b.get_value(qualifier='ld', component='primary', dataset='mylc')
# ```
# 
# The first tutorial on [general concepts](general_concepts.ipynb) discusses the actual implementation and syntax in detail.
# 
# ### support for custom parameterizations via "constraints"
# 
# What we would really like to do for the second point (mass-ratio vs individual masses, semi-major axis and inclination vs asini, etc) is to have a framework that supports any *combination* of parameterizations by telling the parameters the equations that relate them to each other.  These are what we call *constraints* in PHOEBE 2.
# 
# In pseudo-code, this will look something like:
# 
# ```
# b.get_value(qualifier='mass', component='primary')
# 1.2
# b.set_value(qualifier='q', component='binary', value=0.8)
# b.get_value(qualifier='mass', component='primary')
# 1.4
# ```
# 
# Here the masses of the individual stars are *read-only* parameters which know how to be computed from `q` (and the orbital period and semi-major axis - following Kepler's third law).  If you wanted to provide (or fit for) the primary mass instead of q, we can have PHOEBE re-arrange the equations to make q read-only instead.  This looks something like:
# 
# ```
# b.flip_constraint(qualifier='mass', component='primary', solve_for='q')
# 
# b.set_value(qualifier='mass', component='primary', value=1.2)
# b.get_value(qualifier='q', component='binary')
# 1.2
# ```
# 
# The tutorial on [constraints](constraints.ipynb) covers these concepts in detail.  Although the advanced functionality can somewhat be ignored unless you want the flexibility to change the default parameterization, it is still important to be aware of constraints, how they work, and the fact that some parameters are "read-only" by default.  However, once you learn how to use (and perhaps abuse) constraints, a large number of advanced use-cases are opened up.
# 

# In[ ]:




