#!/usr/bin/env python
# coding: utf-8

# # Advanced: LC estimators

# ## Setup
# 
# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger()


# ## Generate data

# Let's first initialize a bundle and change some of the parameter values. We'll then export the computed models as "observables" to use with the [EBAI](../api/phoebe.parameters.solver.estimator.ebai.md) and [lc_geometry](../api/phoebe.parameters.solver.estimator.lc_geometry.md) estimators.
# 
# We'll use blackbody atmospheres with manual limb-darkening just to avoid any out-of-bounds errors if the estimates aren't perfectly physical.  Normally we would check these values to make sure they're reasonable before adopting and would definitely want to revert to physical atmospheres and appropriate limb-darkening when optimizing.

# In[3]:


b = phoebe.default_binary()
# set parameter values
b.set_value('q', value = 0.6)
b.set_value('incl', component='binary', value = 84.5)
b.set_value('ecc', 0.2)
b.set_value('per0', 63.7)
b.set_value('requiv', component='primary', value=1.)
b.set_value('requiv', component='secondary', value=0.6)
b.set_value('teff', component='secondary', value=5500.)

# add an lc dataset
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))
b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_mode_bol', 'manual')
b.set_value_all('atm', 'blackbody')

#compute the model
b.run_compute(irrad_method='none')

# extract the arrays from the model that we'll use as observables in the next step
times = b.get_value('times', context='model', dataset='lc01')
# here we're adding noise to the fluxes as well to make the fake data more "realistic"
np.random.seed(0) # to ensure reproducibility with added noise
fluxes = b.get_value('fluxes', context='model', dataset='lc01') + np.random.normal(size=times.shape) * 0.02
sigmas_lc = np.ones_like(times) * 0.04


# ## Initialize the bundle

# To showcase the estimators, we'll start with a fresh default bundle and set the `pblum_mode` to 'dataset-scaled' to simplify the comparison between the light curves.  Fore more information, see the [pblum tutorial](./pblum.ipynb).

# In[4]:


b = phoebe.default_binary()
b.add_dataset('lc', times=times, fluxes=fluxes, sigmas=sigmas_lc)
b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_mode_bol', 'manual')
b.set_value_all('atm', 'blackbody')
b.set_value('pblum_mode', 'dataset-scaled')

b.run_compute(model='default')
_ = b.plot(x='phase', show=True)


# ## EBAI

# Let's start with the [EBAI estimator](../api/phoebe.parameters.solver.estimator.ebai.md), which with the help of a trained neural network estimates of the time of superior conjunction, sum of equivalent radii, inclination,  temperature ratio, esinw and ecosw.  
# 
# **NOTE**: EBAI currently only works if the eclipse widths are less than 0.25 in phase.  If (either) eclipse is detected to be wider than 0.25, NANs will be returned and an error will be raised when attempting to adopt the solution. 
# 
# First we add the solver options via [add_solver](../api/phoebe.frontend.bundle.Bundle.add_solver.md):

# In[5]:


b.add_solver('estimator.ebai', solver='ebai01')
print(b.filter(solver='ebai01'))


# As we can see, by default it selects all available LC datasets and bins the light curves to 500 bins. We can change any of these in the 'ebai01' object or in the call to [run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md). If there are less points that bins, the phase binning is skipped. Just in case, let's turn off the phase binning for this example, since we already have only 100 data points.

# In[6]:


b['phase_bin@ebai01'] = False
print(b.filter(solver='ebai01'))


# In[7]:


b.run_solver('ebai01', solution='ebai_solution')


# Some of the parameters that the EBAI estimator returns are constrained, so to properly set their values through [adopt_solution](../api/phoebe.frontend.bundle.Bundle.adopt_solution.md), we need to flip the relevant constraints first. Note that simply running `b.adopt_solution()` without this step will result in an error.

# In[8]:


try:
    b.adopt_solution('ebai_solution')
except Exception as e:
    print(e)


# In[9]:


b.flip_constraint('requivsumfrac', solve_for='requiv@secondary')

b.flip_constraint('teffratio', solve_for='teff@secondary')
b.flip_constraint('esinw', solve_for='ecc')
b.flip_constraint('ecosw', solve_for='per0')


# Finally, we can adopt the EBAI solution and see how it has improved the model light curve:

# In[10]:


print(b.adopt_solution('ebai_solution'))


# In[11]:


b.run_compute(model='ebai_model')
_ = b.plot(x='phase', ls='-', legend=True, show=True)


# ## lc_geometry

# The EBAI estimator is known to have deficiencies in correctly estimating the eccentricity and argument of periastron, which can be seen in our solution too. To improve this, we can use the [lc_geometry estimator](../api/phoebe.parameters.solver.estimator.lc_geometry.md), which is specifically tailored to estimating eccentricty and argument of periastron by determining the eclipse separation and widths.

# In[12]:


b.add_solver('estimator.lc_geometry', solver='lcgeom')


# In[13]:


print(b.filter(solver='lcgeom'))


# The lc_geometry estimator takes similar inputs as EBAI, with two additions: `t0_near_times`, which will return the value of t0_supconj such that it falls within or near the provided times array (otherwise it will be a value in the range [0, period]) and `expose_model`, which if true returns the analytical, two-Gaussian model fit that's used to determine the eclipse parameters.

# In[14]:


b.run_solver('lcgeom', solution='lcgeom_solution')


# The resulting solution returns our values of interest: eccentricity and argument of periastron, as well as the analytical fluxes of all two-Gaussian models (since `expose_model = True`) and the eclipse parameters determined from the best fit:

# In[15]:


print(b.filter(solution='lcgeom_solution'))


# To update the values in the bundle, we need to reverse-flip the constraints for esinw and ecosw and adopt the solution.

# In[16]:


b.flip_constraint('per0', solve_for='ecosw')
b.flip_constraint('ecc', solve_for='esinw')


# In[17]:


print(b.adopt_solution('lcgeom_solution'))


# In[18]:


b.run_compute(model='lcgeom_model')
_ = b.plot(x='phases', ls='-', legend=True, show=True)


# ## phase masking

# For more details on phase-masking see [Advanced: Phase Masking](mask_phases.ipynb).
# 
# lc_geometry also returns suggested `mask_phases` computed from the eclipse widths, which we can notice in the list of `fitted_twigs`. However, by default it is excluded from the `adopt_parameters` list:

# In[19]:


print(b.get_value('fitted_twigs', solution='lcgeom_solution'))
print(b.get_value('adopt_parameters', solution='lcgeom_solution'))


# Therefore, we can set them in the bundle by either adding `mask_phases` the to the `adopt_parameters` list before calling `adopt_solution()`, or after, as:

# In[20]:


b.set_value('mask_phases', b.get_value('fitted_values', solution='lcgeom_solution')[-1])


# If we now plot the light curves, we'll see only the eclipses have been "masked out" of the data.

# In[21]:


_ = b.plot(x='phases', ls='-', legend=True, show=True)


# In[ ]:




