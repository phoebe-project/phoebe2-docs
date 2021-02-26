#!/usr/bin/env python
# coding: utf-8

# # Advanced: Fitting Limb Darkening Coefficients
# 
# **NOTE**: support for fitting `ld_coeffs` as well as custom constraints was fixed in PHOEBE 2.3.30.  This notebook will fail to run on earlier versions.

# ## Create Fake Example Observations
# 
# Here we'll create fake observations (ignoring noise or reasonable uncertainties) to demonstrate how to fit limb-darkening coefficients for multiple light curve datasets, including two that we want to keep in sync due to having a shared passband.
# 
# Note that limb-darkening coefficients parameters (`ld_coeffs`) are not visible by default as `ld_mode` defaults to 'interp'.  See the [limb-darkening tutorial](./limb_darkening.ipynb) for more details.

# In[1]:


import phoebe
import numpy as np

phoebe.logger('error') # just to ignore many limb-brightening warnings

b = phoebe.default_binary()

b.add_dataset('lc', times=phoebe.linspace(0,1,51), passband='Johnson:V', dataset='Vband1')
b.add_dataset('lc', times=phoebe.linspace(1,2,51), passband='Johnson:B', dataset='Bband1')
b.add_dataset('lc', times=phoebe.linspace(2,3,51), passband='Johnson:B', dataset='Bband2')

b.set_value_all('ld_mode', 'manual')

b.set_value_all('ld_coeffs', dataset='Vband1', value=[0.3, 0.7])
b.set_value_all('ld_coeffs', dataset='Bband*', value=[0.4, 0.6])

b.set_value_all('irrad_method', 'none')

b.run_compute()

for ds in b.datasets:
    b.set_value('fluxes', dataset=ds, context='dataset', value=b.get_value('fluxes', dataset=ds, context='model'))
    b.set_value('sigmas', dataset=ds, context='dataset', value=0.1*np.ones_like(b.get_value('fluxes', dataset=ds, context='model')))

b.set_value_all('ld_coeffs', [0.5, 0.5])
b.set_value('incl@binary', 90)

b.remove_model(model='latest')


# In[2]:


_ = b.plot(show=True)


# ## Optional: Constraining Limb-Darkening Coefficients
# 
# In this case, we have three datasets, so 6 different `ld_coeffs` parameters (and would have 2 `ld_coeffs_bol` parameters, but we'll leave `ld_mode_bol` to be 'lookup')

# In[3]:


print(b.filter(qualifier='ld_coeffs'))


# There are 2 different `ld_coeffs` parameters (one for each component) for each dataset, as limb-darkening is passband dependent.  However, in this case, two of the datasets are the same passband, so when fitting, we want to ensure these are always using the same value and kept in sync.  
# 
# To do that, we can create a custom constraint via [b.add_constraint](../api/phoebe.frontend.bundle.Bundle.add_constraint.md) (for more details see [Advanced: Custom Constraints](constraints_custom.ipynb)).

# In[4]:


for component in ['primary', 'secondary']:
    lhs = b.get_parameter(qualifier='ld_coeffs', component=component, dataset='Bband2')
    rhs = b.get_parameter(qualifier='ld_coeffs', component=component, dataset='Bband1') 
    b.add_constraint(lhs, rhs)


# In[5]:


print(b.filter(qualifier='ld_coeffs'))


# ## Optimizing
# 
# For optimizers, we need to set the `fit_parameters`.  Each index in the referenced `ld_coeffs` parameters will be fitted separately.  If wanting to only fit a subset of the indices, those can be referenced with square brackets in the twigs sent to `fit_parameters` (i.e. `'ld_coeffs[0]@Vband1@primary'`), otherwise all will be included when expanding to the available parameters.
# 
# Here we'll fit all `ld_coeffs` for the unconstrained datasets (Vband1 and Bband1) and allow Bband2 to be handled by their constraints.

# In[6]:


b.add_solver('optimizer.nelder_mead', 
             maxiter=50, maxfev=200, xatol=1e-2, 
             solver='nm_solver')


# In[7]:


b.set_value('fit_parameters', ['ld_coeffs@Vband1', 'ld_coeffs@Bband1'])


# In[8]:


b.get_value('fit_parameters')


# In[9]:


b.get_value('fit_parameters', expand=True)


# In[10]:


b.run_solver(solver='nm_solver', solution='nm_sol')


# In[11]:


print(b.get_value(qualifier='message', solution='nm_sol'))


# We can now see when adopting the solution that the Bband2 coefficients will also be adopted, according to the constraints we created.

# In[12]:


print(b.adopt_solution(solution='nm_sol'))


# ## Attaching and Plotting Distributions
# When attaching distributions, each (applicable) index in the `ld_coeffs` array must have its own attached distribution.
# 
# When calling [b.add_distribution](../api/phoebe.frontend.bundle.Bundle.add_distribution.md), the index must be included using the square bracket notation.  Alternatively, to add a copy of the same distribution to all matching parameters, `allow_multiple_matches=True` can be passed.
# 
# Here we'll show several different syntaxes that are valid to attach distribution to the `ld_coeffs` parameters.

# In[13]:


b.add_distribution('ld_coeffs[0]@primary@Vband1', phoebe.gaussian_around(0.1), 
                   distribution='mydist')


# In[14]:


b.add_distribution({'ld_coeffs[1]@primary@Vband1': phoebe.gaussian_around(0.1),
                    'ld_coeffs[0]@secondary@Vband1': phoebe.gaussian_around(0.1),
                    'ld_coeffs[1]@secondary@Vband1': phoebe.gaussian_around(0.1)}, 
                   distribution='mydist')


# In[15]:


try:
    b.add_distribution('ld_coeffs@secondary@Vband', phoebe.gaussian_around(0.1), 
                       distribution='mydist')
except Exception as err:
    print(err)


# In[16]:


b.add_distribution('ld_coeffs@Bband1', phoebe.gaussian_around(0.1), 
                   distribution='mydist', allow_multiple_matches=True)


# In[17]:


print(b.get_distribution('mydist'))


# In[18]:


_ = b.plot_distribution_collection('mydist', show=True)


# ## Samplers
# 
# Once distributions are attached, we can now initialize our `init_from` distribution as in any other case.  Here we'll show a quick example using just several iterations and the emcee sampler.

# In[19]:


b.add_solver('sampler.emcee', solver='emcee_solver', init_from='mydist', niters=10, nwalkers=16)


# In[20]:


b.run_solver('emcee_solver', solution='emcee_sol')


# Note that the posteriors from the solution do not include the propagated distributions from the constraints, but if applied or sampled, the constraints will continue to be respected.

# In[21]:


_ = b.plot(solution='emcee_sol', style='corner', show=True)


# When inspecting/plotting the solution, the individual elements in the `ld_coeffs` can be referenced (and are expanded to all matches) using the same notation as above, for example:

# In[22]:


_ = b.plot(solution='emcee_sol', style='corner', 
           adopt_parameters=['ld_coeffs@Vband1', 'ld_coeffs[0]@primary@Bband1'], show=True)


# If we now adopt the solution, the posteriors will be stored in a new tagged distribution collection (we'll name it 'emcee_posts') and the central values will be adopted, including those for the constrained Bband2 dataset.

# In[23]:


b.adopt_solution('emcee_sol', distribution='emcee_posts')

