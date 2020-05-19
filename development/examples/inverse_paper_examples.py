#!/usr/bin/env python
# coding: utf-8

# # Inverse Problem: General Workflow and Examples
# 
# In this example script, we'll reproduce many of the plots from the fitting release paper ([Conroy et al. 2020](http://phoebe-project.org/publications/2020Conroy+)).

# # Setup
# 
# First we'll import, set our plotting options, and set a fixed random seed so that our noise model is reproducible between runs.

# In[1]:


import matplotlib.pyplot as plt

plt.rc('font', family='serif')


# In[2]:


import phoebe
import numpy as np

logger = phoebe.logger('error')

# we'll set the random seed so that the noise model is reproducible
np.random.seed(123456789)


# # Create fake "observations"
# 
# Now we'll create a fake set of observations by setting some parameter values, running a forward model, and adding some simple random noise on both the fluxes and RVs.

# In[3]:


b = phoebe.default_binary()
b.set_value('ecc', 0.2)
b.set_value('per0', 25)
b.set_value('teff@primary', 7000)
b.set_value('teff@secondary', 6000)
b.set_value('sma@binary', 7)
b.set_value('incl@binary', 80)
b.set_value('q', 0.3)
b.set_value('t0_supconj', 0.1)
#b.set_value('requiv@primary', 0.95*b.get_value('requiv_max@primary@component'))  # rv_geometry fails to converge
b.set_value('requiv@primary', 2.0)

lctimes = phoebe.linspace(0, 10, 1005)
rvtimes = phoebe.linspace(0, 10, 105)
b.add_dataset('lc', compute_times=lctimes)
b.add_dataset('rv', compute_times=rvtimes)
b.set_value_all('ld_mode', 'lookup')
b.run_compute(irrad_method='none')

fluxes = b.get_value('fluxes@model') + np.random.normal(size=lctimes.shape) * 0.01
fsigmas = np.ones_like(lctimes) * 0.02

rvsA = b.get_value('rvs@primary@model') + np.random.normal(size=rvtimes.shape) * 10
rvsB = b.get_value('rvs@secondary@model') + np.random.normal(size=rvtimes.shape) * 10
rvsigmas = np.ones_like(rvtimes) * 20


# In[4]:


# TESTING to compare to ebai - REMOVE 
b.add_constraint('teffratio')
b.add_constraint('requivsumfrac')
print(b.filter(qualifier=['teffratio', 'requivsumfrac'], context='component'))


# # Create a new bundle/system
# 
# Now we'll start over "blind" with a fresh bundle and import our "fake" observations in datasets.

# In[5]:


b = phoebe.default_binary()
b.add_dataset('lc', times=lctimes, fluxes=fluxes, sigmas=fsigmas, dataset='lc01')
b.add_dataset('rv', times=rvtimes, rvs={'primary': rvsA, 'secondary': rvsB}, sigmas=rvsigmas, dataset='rv01')
b.set_value_all('ld_mode', 'lookup')


# For the sake of this example, we'll assume that we know the orbital period _exactly_, and so can see that our observations phase nicely.  

# In[6]:


afig, mplfig = b.plot(x='phases', show=True)


# # Run `rv_geometry` estimator
# 
# First we'll run the `rv_geometry` estimator.

# In[7]:


b.add_solver('estimator.rv_geometry',
             rv='rv01')


# In[8]:


b.run_solver(kind='rv_geometry', solution='rv_geom_sol')


# By calling [b.adopt_solution](../api/phoebe.frontend.bundle.Bundle.adopt_solution.md) with `trial_run=True`, we can see the proposed values by the estimator.

# In[9]:


print(b.adopt_solution('rv_geom_sol', trial_run=True))


# And by plotting the solution, we can see the underlying Keplerian orbit that was fitted to the RVs to determine these values.  
# 
# This reproduces Figure ??? ...

# In[10]:


afig, mplfig = b.plot(solution='rv_geom_sol',
                      show=True, save='figure_rv_geometry.eps')


# # Run `lc_geometry` estimator
# 
# Next we'll run the `lc_geometry` estimator.

# In[11]:


b.add_solver('estimator.lc_geometry',
             lc='lc01')


# In[12]:


b.run_solver(kind='lc_geometry', solution='lc_geom_sol')


# Again, calling [b.adopt_solution](../api/phoebe.frontend.bundle.Bundle.adopt_solution.md) with `trial_run=True` shows the proposed values.

# In[13]:


print(b.adopt_solution('lc_geom_sol', trial_run=True))


# By plotting the solution, we get Figure ???, which shows the best two gaussian model as well as the detected positions of mid-eclipse, ingress, and egress which were used to compute the proposed values.

# In[14]:


afig, mplfig = b.plot(solution='lc_geom_sol',
                      show=True, save='figure_lc_geometry.eps')


# Figure ??? in the paper which shows the seven underlying two gaussian models cannot directly be generated from the plotting functionality within PHOEBE, but the arrays are stored in the solution and can be plotted manually, as shown below.

# In[15]:


from phoebe.dependencies.autofig.cyclers import _mplcolors as cmap

input_phases = b.get_value('input_phases', solution='lc_geom_sol')
input_fluxes = b.get_value('input_fluxes', solution='lc_geom_sol')
input_sigmas = b.get_value('input_sigmas', solution='lc_geom_sol')

analytic_phases = b.get_value('analytic_phases', solution='lc_geom_sol')
analytic_fluxes_dict = b.get_value('analytic_fluxes', solution='lc_geom_sol')
analytic_best_model = b.get_value('analytic_best_model', solution='lc_geom_sol')

plt.figure(figsize=(8,6))
plt.plot(input_phases, input_fluxes, ls='None', marker='.', c='gray',)
for i, (model, analytic_fluxes) in enumerate(analytic_fluxes_dict.items()):
    plt.plot(analytic_phases, analytic_fluxes, 
             label="{} - best fit".format(model) if model==analytic_best_model else model, 
             lw=4 if model==analytic_best_model else 3, 
             c='k' if model==analytic_best_model else cmap[i+1])
    
plt.xlabel('phase')
plt.ylabel('flux (normalized)')
plt.legend()
plt.savefig('figure_lc_geometry_models.eps')


# Figure ??? exhibits eclipse masking by adopting `mask_phases` from the `lc_geometry` solution.  Note that by default, `mask_phases` is not included in `adopt_parameters`, which is why it was not included when calling [b.adopt_solution](../api/phoebe.frontend.bundle.Bundle.adopt_solution.md) with `trial_mode=True` (all available proposed parameters could be shown by passing `adopt_parameters='*'`.  For the sake of this figure, we'll only adopt the `mask_phases`, plot the dataset with that mask applied, but then disable the mask for the rest of this example script.

# In[16]:


b.adopt_solution('lc_geom_sol', adopt_parameters='mask_phases')


# In[17]:


_ = b.plot(context='dataset', dataset='lc01', x='phases', xlim=(-0.55,0.55),
           save='figure_lc_geometry_mask.eps', show=True)


# In[18]:


b.set_value('mask_enabled@lc01', False)


# # Run `ebai` estimator
# 
# And finally, we'll do the same for the `ebai` estimator.

# In[19]:


b.add_solver('estimator.ebai',
             lc='lc01')


# In[20]:


b.run_solver(kind='ebai', solution='ebai_sol')


# In[21]:


print(b.adopt_solution('ebai_sol', trial_run=True))


# By plotting the `ebai` solution, we reproduce Figure ???, which shows the normalized light curve observations and the resulting sample two gaussian model that is sent to the neural network.

# In[22]:


afig, mplfig = b.plot(solution='ebai_sol',
                      show=True, save='figure_ebai.eps')


# # Adopt from estimators
# 
# Now we'll adopt the proposed values from the two geometry estimators.

# In[23]:


b.flip_constraint('asini@binary', solve_for='sma@binary')
b.adopt_solution('rv_geom_sol')


# In[24]:


b.adopt_solution('lc_geom_sol')


# We'll keep the eccentricity and per0 estimates from the lc geometry, but use the ebai results to adopt the values for the temperature ratio, sum of fractional radii, and inclination.  Note that since we flipped the asini constraint earlier, that value from the rv geometry will remain fixed and the semi-major axis will be adjusted based on asini from rv geometry and incl from ebai.

# In[25]:


b.flip_constraint('teffratio', solve_for='teff@primary')
b.flip_constraint('requivsumfrac', solve_for='requiv@primary')
b.adopt_solution('ebai_sol', adopt_parameters=['teffratio', 'requivsumfrac', 'incl'])


# In[26]:


print(b.filter(qualifier=['ecc', 'per0', 'teff', 'sma', 'incl', 'q', 'requiv'], context='component'))


# Now we can run a forward model with these adopted parameters to see how well the results from the estimators agree with the observations.

# In[27]:


b.run_compute(irrad_method='none', model='after_estimators', overwrite=True)


# In[28]:


_ = b.plot(x='phases', show=True)


# In[29]:


# TESTING to compare ebai to original values at top
print(b.filter(qualifier=['teffratio', 'requivsumfrac'], context='component'))


# # Optimize with `nelder_mead` using `ellc`
# 
# To avoid a long burnin during sampling, we'll use the `nelder_mead` optimizer to try to achieve better agreement with the observations.

# In[30]:


b.add_compute('ellc', compute='fastcompute')


# For the sake of optimizing, we'll use `pblum_mode='dataset-scaled'` which will automatically re-scale the light curve to the observations at each iteration - we'll disable this later for sampling to make sure we account for any degeneracies between the luminosity and other parameters.

# In[31]:


b.set_value_all('pblum_mode', 'dataset-scaled')


# In[32]:


b.add_solver('optimizer.nelder_mead',
             fit_parameters=['teffratio', 'requivsumfrac', 'incl', 'q', 'ecc', 'per0'],
             compute='fastcompute')


# In[33]:


print(b.get_solver(kind='nelder_mead'))


# In[34]:


b.run_solver(kind='nelder_mead', maxfev=1000, solution='nm_sol')


# In[35]:


print(b.get_solution('nm_sol'))


# In[36]:


print(b.adopt_solution('nm_sol', trial_run=True))


# We'll adopt all the proposed values, and run the forward model with a new `model` tag so that we can overplot the "before" and "after".  

# In[39]:


b.adopt_solution('nm_sol')


# In[37]:


b.run_compute(compute='phoebe01', model='after_nm')


# Figure ?? shows the forward-models from the parameters we adopted after estimators to those after optimization.

# In[38]:


_ = b.plot(x='phases', 
           c={'after_estimators': 'red', 'after_nm': 'green', 'dataset': 'black'}, 
           linestyle={'after_estimators': 'dashed', 'after_nm': 'solid'},
           marker={'dataset': '.'},
           save='figure_optimizer_nm.eps', show=True)


# # Determine uncertainties with `emcee`

# So that we don't ignore any degeneracies between parameters and the luminosities, we'll turn off the dataset-scaling we used for optimizing and make sure we have a reasonable value of `pblum@primary` set to roughly obtain the out-of-eclipse flux levels of the observations.

# In[40]:


b.set_value_all('pblum_mode', 'component-coupled')


# In[41]:


print(b.compute_pblums(compute='fastcompute', dataset='lc01', pbflux=True))


# We'll now create our initializing distribution, including gaussian "balls" around all of the optimized values and a generous boxcar on `pblum@primary`.

# In[42]:


# TODO: remove @primary@lc01 once bug fixed
b.add_distribution({'teffratio': phoebe.gaussian_around(0.1),
                    'requivsumfrac': phoebe.gaussian_around(0.1),
                    'incl@binary': phoebe.gaussian_around(3),
                    'q': phoebe.gaussian_around(0.1),
                    'ecc': phoebe.gaussian_around(0.05),
                    'per0': phoebe.gaussian_around(5),
                    'pblum@primary@lc01': phoebe.uniform_around(2)},
                    distribution='ball_around_optimized_solution')


# We can look at this combined set of distributions, which will be used to sample the initial values of our walkers in `emcee`.

# In[43]:


_ = b.plot_distribution_collection('ball_around_optimized_solution', show=True)


# In[44]:


b.add_solver('sampler.emcee',
             init_from='ball_around_optimized_solution',
             compute='fastcompute',
             solver='emcee_solver')


# Since we'll need a lot of iterations, we'll export the solver to an HPC cluster and import the solution.  We'll save the bundle first so that we can interrupt the notebook and return to the following line, if needed.

# In[45]:


b.save('figure_examples_before_emcee.bundle')
b.export_solver('figure_examples_run_emcee.py', 
                solver='emcee_solver',
                niters=2000, progress_every_niters=250, 
                nwalkers=16,
                solution='emcee_sol',
                pause=True)


# In[2]:


b = phoebe.load('figure_examples_before_emcee.bundle')
b.import_solution('figure_examples_run_emcee.py.out.progress', solution='emcee_sol')


# Alternatively, we could run the solver locally as we've seen before, but probably would want to run less iterations:
# 
# ```
# b.run_solver('emcee_solver', niters=300, nwalkers=16, solution='emcee_sol')
# ```
# 
# in which case calling `b.import_solution` is not necessary.

# In[3]:


_ = b.plot('emcee_sol', style='failed', 
           save='figure_emcee_failed_samples.eps', show=True)


# In[62]:


_ = b.plot('emcee_sol', style='walks', c='black', 
           adopt_parameters=['q', 'ecc', 'per0', 'incl@binary'],
           save='figure_emcee_walks.eps', show=True)


# In[63]:


_ = b.plot('emcee_sol', style='lnprobabilities', c='black',
           burnin=0, thin=1,
           save='figure_emcee_lnprobabilities_all.eps', show=True)


# In[64]:


_ = b.plot('emcee_sol', style='lnprobabilities', c='black',
           save='figure_emcee_lnprobabilities.eps', show=True)


# # Accessing posteriors from `emcee` run
# 
# **TODO**: explain the difference between `parameters` and `adopt_parameters`, or consider merging in the code so this isn't possible (or rename to be more self-explanatory).

# In[65]:


#_ = b.plot('emcee_sol', style='corner', show=True)


# In[66]:


_ = b.plot('emcee_sol', style='corner', parameters=['teffratio', 'requivsumfrac', 'incl@binary'], 
           save='figure_posteriors_mvsamples.eps', show=True)


# In[67]:


_ = b.plot('emcee_sol', style='corner', parameters=['teffratio', 'requivsumfrac', 'incl@binary'], 
           distributions_convert='mvgaussian',
           save='figure_posteriors_mvgaussian.eps', show=True)


# In[68]:


_ = b.plot('emcee_sol', style='corner', parameters=['ecc', 'per0'], 
           save='figure_posteriors_ew.eps', show=True)


# In[69]:


_ = b.plot('emcee_sol', style='corner', parameters=['esinw', 'ecosw'], 
           save='figure_posteriors_ecs.eps', show=True)


# In[5]:


b.run_compute(compute='fastcompute', 
              sample_from='emcee_sol', sample_num=100, sample_mode='3-sigma',
              model='emcee_posts')


# In[7]:


b.save('figure_examples_after_sample_from.bundle')


# In[1]:


#### REMOVE THIS CELL ONCE DONE TESTING - THIS JUST ALLOWS TO START THE SCRIPT HERE


import matplotlib.pyplot as plt

plt.rc('font', family='serif')

import phoebe
import numpy as np

logger = phoebe.logger('error')

# we'll set the random seed so that the noise model is reproducible
np.random.seed(123456789)


# In[2]:


b = phoebe.load('figure_examples_after_sample_from.bundle')


# In[10]:


# TODO: fix this so that passing model to plot doesn't exclude the observations
_ = b.plot(kind='lc', model='emcee_posts', x='phases', y='fluxes', 
           c={'dataset': 'black', 'model': 'blue'},
           s={'dataset': 0.005},
           marker={'dataset': '.'})
_ = b.plot(kind='lc', model='emcee_posts', x='phases', y='residuals', 
           c={'dataset': 'black', 'model': 'blue'},
           save='figure_posteriors_sample_from_lc.eps', show=True)


# In[11]:


# TODO: fix this so model and dataset are in same panel for residuals 
# and so observations are included in top-panel (problem seems to be units on phase)
_ = b.plot(kind='rv', model='emcee_posts', x='phases', y='rvs',
          c={'dataset': 'black', 'model': 'blue'},
          marker={'dataset': '.'})
_ = b.plot(kind='rv', model='emcee_posts', x='phases', y='residuals', 
           c={'dataset': 'black', 'model': 'blue'},
           save='figure_posteriors_sample_from_rv.eps', show=True)


# # Sampling with `dynesty`

# The posterior plots in the paper were all created from the `emcee` results, but we'll also run the `dynesty` sampler on the same system.
# 
# `dynesty` samples directly from the priors, so we shouldn't use the same gaussian balls we did for `emcee`.  Instead, we'll create a narrow box around the solution with widths somewhat estimated from the `emcee` cornerplot.  We can do this to save time for this example because we know the solution, but in practice these would likely need to be much more conservatively set.

# In[3]:


b.add_distribution({'teffratio': phoebe.uniform_around(0.1),
                    'requivsumfrac': phoebe.uniform_around(0.1),
                    'incl@binary': phoebe.uniform_around(0.5),
                    'q': phoebe.uniform_around(0.1),
                    'ecc': phoebe.uniform_around(0.05),
                    'per0': phoebe.uniform_around(6),
                    'pblum@primary@lc01': phoebe.uniform_around(0.5)},
                    distribution='dynesty_uninformative_priors')


# In[4]:


b.add_solver('sampler.dynesty',
             compute='fastcompute',
             priors='dynesty_uninformative_priors',
             solver='dynesty_solver'
            )


# In[5]:


b.save('figure_examples_before_dynesty.bundle')
b.export_solver('figure_examples_run_dynesty.py', 
                solver='dynesty_solver',
                maxiter=10000, maxcall=int(1e6), progress_every_niters=100, 
                solution='dynesty_sol',
                pause=True)


# In[ ]:


#### REMOVE THIS CELL ONCE DONE TESTING - THIS JUST ALLOWS TO START THE SCRIPT HERE


import matplotlib.pyplot as plt

plt.rc('font', family='serif')

import phoebe
import numpy as np

logger = phoebe.logger('error')

# we'll set the random seed so that the noise model is reproducible
np.random.seed(123456789)


# In[6]:


b = phoebe.load('figure_examples_before_dynesty.bundle')
b.import_solution('figure_examples_run_dynesty.py.out', solution='dynesty_sol')


# In[10]:


afig, mplfig = _ = b.plot('dynesty_sol', style='trace', 
           savefig='figure_dynesty_trace.eps', show=True)


# In[12]:


mplfig.tight_layout()
mplfig.savefig('figure_dynesty_trace.eps')


# In[8]:


_ = b.plot('dynesty_sol', style='run', 
           show=True)


# In[9]:


_ = b.plot('dynesty_sol', style='corner', 
           show=True)


# In[ ]:



