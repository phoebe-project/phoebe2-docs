#!/usr/bin/env python
# coding: utf-8

# Solvers: The Inverse Problem
# ============================
# 
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger()


# General "Fitting" Workflow
# ---------------------------------------
# 
# PHOEBE includes wrappers around several different inverse-problem "algorithms" with a common interface.  These available "algorithms" are divided into three categories:
# 
# * estimators: provides proposed values for a number of parameters from the datasets as input alone, not requiring full forward-models via [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md).
# * optimizers: runs off-the-shelf optimizers to attempt to find the local (or global) solution.
# * samplers: samples the local parameter space to estimate uncertainties and correlations.
# 
# To see the currently implemented set of solvers, we can call [phoebe.list_available_solvers](../api/phoebe.list_available_solvers.md)

# In[3]:


print(phoebe.list_available_solvers())


# Solving an eclipsing binary is a very time-intensive task (both for you as well as your computer).  There is no one-size-fits-all recipe to follow, but in general you might find the following workflow useful:
# 
# 1. Create a bundle with the appropriate configuration (single star, detached binary, semi-detached, contact, etc).
# 2. Attach observational datasets
# 3. Flip constraints as necessary to parameterize the system in the way that makes sense for any information you know in advance, types of data, and scientific goals.  For example: if you have an SB2 system with RVs, it might make sense to reparameterize to "fit" for `asini` instead of `sma` and `incl`.
# 4. Manually set known or approximate values for parameters wherever possible.
# 5. Run the appropriate estimators, checking to see if the proposed values make sense before adopting them.
# 6. Try to optimize the forward model.  See which expensive effects can be disabled without affecting the synthetic model (to some precision tolerance).  Make sure to revisit these assumptions as optimizers may move the system to different areas of parameter space where they are no longer valid.
# 7. Run optimizers to find (what you hope and assume to be) the global solution.  Start with just a few parameters that are most sensitive to the remaining residuals and add more until the residuals are flat (no systematics).  Check all read-only constrained parameters to make sure that they make sense, are consistent with known information, and are physical.
# 8. Run samplers around the global solution found by the optimizers to explore that local parameter space and the correlations between parameters.  Check for convergence before interpreting the resulting posteriors.

# For the sake of a simple crude example, we'll just use the synthetic light curve of a default binary with a bit of noise as our "observations".   See the [inverse problem example scripts](../examples.md) for more realistic examples.

# In[4]:


b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))
b.run_compute(irrad_method='none')

times = b.get_value('times', context='model')
fluxes = b.get_value('fluxes', context='model') + np.random.normal(size=times.shape) * 0.01
sigmas = np.ones_like(times) * 0.02

b = phoebe.default_binary()
b.add_dataset('lc', times=times, fluxes=fluxes, sigmas=np.full_like(fluxes, fill_value=0.1))


# Adding Solver Options
# ----------------------------------
# 
# As there are quite a few different solvers implemented in PHOEBE and each have their own available options, we won't get in to the details here.  See [LC esimators](./LC_estimators.ipynb), [RV estimators](./RV_estimators.ipynb), [Nelder-Mead Optimizer](./nelder_mead.ipynb), and [emcee sampler](./emcee.ipynb) for details on some of the most commonly-used solver.  The [solver API docs](../api/phoebe.parameters.solver.md) or [solver example scripts](../examples.md) may also help.
# 
# As you may expect, to use a solver you must first call [b.add_solver](../api/phoebe.frontend.bundle.Bundle.add_solver.md), set the desired options, and then call [b.run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md) (or [b.export_solver](../api/phoebe.frontend.bundle.Bundle.export_solver.md) and [b.import_solution](../api/phoebe.frontend.bundle.Bundle.import_solution.md)).

# In[5]:


b.add_solver('estimator.lc_geometry', solver='my_lcgeom_solver')


# In[6]:


print(b.get_solver(solver='my_lcgeom_solver'))


# In addition to the [solver API docs](../api/phoebe.parameters.solver.md), remember that each parameter has a description and possibly a set of available choices (if its a [ChoiceParameter](../api/phoebe.parameters.ChoiceParameter.md) or [SelectParameter](../api/phoebe.parameters.SelectParameter.md)).

# In[7]:


print(b.get_parameter('expose_model').description)


# In[8]:


print(b.get_parameter('lc_datasets').description)


# In[9]:


print(b.get_parameter('lc_datasets').choices)


# run_solver
# ---------------

# [b.run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md) (or [b.export_solver](../api/phoebe.frontend.bundle.Bundle.export_solver.md) and [b.import_solution](../api/phoebe.frontend.bundle.Bundle.import_solution.md)) allows optionally setting a `solution` tag (if not provided, one will be created automatically), just as [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) allows setting a `model` tag.  

# In[10]:


b.run_solver(solver='my_lcgeom_solver', solution='my_lcgeom_solution')


# In many cases, the `solution` itself is plottable - showing some sort of diagnostic figures.  In some cases, such as [sampler.emcee](../api/phoebe.parameters.solver.sampler.emcee.md) or [sampler.dynesty](../api/phoebe.parameters.solver.sampler.dynesty.md), there are several different diagnostic figures available which can be chosen by passing the available options to `style`.

# In[11]:


_ = b.plot(solution='my_lcgeom_solution', show=True)


# The proposed values can be viewed via [b.adopt_solution](../api/phoebe.frontend.bundle.Bundle.adopt_solution.md).
# 
# By passing `trial_run=True` the proposed changed parameters will be shown, but not changed in the bundle itself.

# In[12]:


print(b.adopt_solution(trial_run=True))


# Otherwise, the changes will be made and all changed parameters (including those changed via [constraints](constraints.ipynb)) will be returned.

# In[13]:


print(b.adopt_solution())


# The Merit Function
# -----------------
# 
# Both [optimizers](../api/phoebe.parameters.solver.optimizer.md) and [samplers](../api/phoebe.parameters.solver.sampler.md) require running a forward model and use a merit function to compare the synthetic model to the observational data.  This merit function is described in detail in the 2.3 release paper ([Conroy+ 2020](http://phoebe-project.org/publications/2020Conroy+)).
# 
# Several bundle methods allow for accessing the values used in the merit function:
# 
# * [b.calculate_residuals](../api/phoebe.parameters.ParameterSet.calculate_residuals.md)
# * [b.calculate_chi2](../api/phoebe.parameters.ParameterSet.calculate_chi2.md)
# * [b.calculate_lnlikelihood](../api/phoebe.parameters.ParameterSet.calculate_lnlikelihood.md)
# * [b.calculate_lnp](../api/phoebe.frontend.bundle.Bundle.calculate_lnp.md)
# 
# The log-probability used as the merit function within optimizers and samplers is defined as [calculate_lnp](../api/phoebe.frontend.bundle.Bundle.calculate_lnp.md)`(priors, combine=priors_combine)` + [calculate_lnlikelihood](../api/phoebe.parameters.ParameterSet.calculate_lnlikelihood).
# 
# To see the affect of `priors_combine`, we can pass the `solver` tag directly to [b.get_distribution_collection](../api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md), [b.plot_distribution_collection](../api/phoebe.frontend.bundle.Bundle.plot_distribution_collection.md), or [b.calculate_lnp](../api/phoebe.frontend.bundle.Bundle.calculate_lnp.md).

# In[14]:


b.add_distribution('teff@primary', phoebe.gaussian(6000,100), distribution='mydist01')
b.add_distribution('teff@secondary', phoebe.gaussian(5500,600), distribution='mydist01')

b.add_distribution('teff@primary', phoebe.uniform(5800,6200), distribution='mydist02')


# In[15]:


b.add_solver('sampler.emcee', priors=['mydist01', 'mydist02'], solver='myemceesolver')


# In[16]:


print(b.filter(qualifier='prior*'))


# Now we'll look at the affect of `priors_combine` on the resulting priors distributions that would be sent to the merit function.

# In[17]:


print(b.get_parameter('priors_combine').description)


# In[18]:


_ = b.plot_distribution_collection('priors@myemceesolver', show=True)


# In[19]:


b.calculate_lnp('priors@myemceesolver')


# In[20]:


b.set_value('priors_combine', 'first')


# In[21]:


_ = b.plot_distribution_collection('priors@myemceesolver', show=True)


# In[22]:


b.calculate_lnp('priors@myemceesolver')


# As with the example above, to run an `emcee` run, just set all the desired options in the `solver` parameters, and then call [b.run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md).  This will then expose the resulting chains in the solution, which are available for plotting and adopting.  See the  [solver example scripts](../examples.md) or the individual [API docs for solvers](../api/phoebe.parameters.solver.md) for more details on each available algorithm.

# Next
# ----------
# 
# Solver jobs can be quite computationally expensive, and so you may wish to set up the job locally and then [submit it on external compute resources](./server.ipynb).
# 
# 
# Or look at any of these advanced topics related to running solvers:
# * [Advanced: Solver Times](./solver_times.ipynb)
# * [Advanced: LC Estimators](./LC_estimators.ipynb)
# * [Advanced: RV Estimators](./RV_estimators.ipynb)
# * [Advanced: Nelder-Mead Optimizer](./nelder_mead.ipynb)
# * [Advanced: Emcee Sampler](./emcee.ipynb)
# * [Advanced: Running Solvers on an External Machine](./export_solver.ipynb)
# * [Advanced: Fitting Limb Darkening Coefficients](./fitting_ld_coeffs.ipynb)
