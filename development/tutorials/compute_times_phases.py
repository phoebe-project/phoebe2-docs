#!/usr/bin/env python
# coding: utf-8

# Advanced: compute_times & compute_phases
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# In[2]:


b.add_dataset('lc', times=phoebe.linspace(0,10,101), dataset='lc01')


# Overriding Computation Times
# ----------------------------
# 
# If `compute_times` is not empty (by either providing `compute_times` *or* `compute_phases`), the provided value will be used to compute the model instead of those in the `times` parameter.

# In[3]:


print(b.filter(qualifier=['times', 'compute_times'], context='dataset'))


# In[4]:


b.set_value('compute_times', phoebe.linspace(0,3,11))


# In[5]:


b.run_compute()


# In[6]:


print("dataset times: {}\ndataset compute_times: {}\nmodel times: {}".format(
    b.get_value('times', context='dataset'),
    b.get_value('compute_times', context='dataset'),
    b.get_value('times', context='model')
    ))


# Phase-Time Conversion
# ----------------------------------

# In addition to the ability to provide `compute_times`, we can alternatively provide `compute_phases`.  These two parameters are linked via a constraint (see the [constraints tutorial](./constraints.ipynb)), with `compute_phases` *constrained* by default.

# In[7]:


print(b.filter(qualifier=['times', 'compute_times', 'compute_phases'], context='dataset'))


# If we look at the constraint itself, we see that this translation is rudimentary and does not include all the same complexity as [b.to_phase](../api/phoebe.frontend.bundle.Bundle.to_phase.md) or [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md), but it will immediately react to a change in the orbital period (of the top-level orbit in the hierarchy).

# In[8]:


print(b.get_constraint('compute_phases'))


# In order to provide `compute_phases` instead of `compute_times`, we must call [b.flip_constraint](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).

# In[9]:


b.flip_constraint('compute_phases', solve_for='compute_times')


# In[10]:


b.set_value('compute_phases', phoebe.linspace(0,1,11))


# In[11]:


print(b.filter(qualifier=['times', 'compute_times', 'compute_phases'], context='dataset'))


# Note that under the hood, PHOEBE **always** works in time-space, meaning it is the *constrained* value of `compute_times` that is being passed under-the-hood... even if those will result in slightly different phase-values due to the values of t0, dperdt, etc.

# Also note that if directly passing `compute_phases` to [b.add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md), the constraint will be flipped on our behalf.  We would then need to flip the constraint in order to provide `compute_times` instead.

# Interpolating the Model
# ------------------------------

# Whether or not we used `compute_times`/`compute_phases` or not, it is sometimes useful to be able to interpolate on the resulting model.  In the case where we provided `compute_times`/`compute_phases` to "down-sample" from a large dataset, this can be particularly useful.
# 
# We can call [interp_value](../api/phoebe.parameters.FloatArrayParameter.interp_value.md) on any [FloatArrayParameter](../api/phoebe.parameters.FloatArrayParameter.md).  

# In[12]:


b.get_parameter('fluxes', context='model').get_value()


# In[13]:


b.get_parameter('fluxes', context='model').interp_value(times=1.0)


# In[14]:


b.get_parameter('fluxes', context='model').interp_value(times=np.linspace(0,3,101))


# In the case of times, this will *automatically* interpolate in phase-space if the provided time is outside the range of the referenced times array.  If you have a logger enabled with at least the 'warning' level, this will raise a warning and state the phases at which the interpolation will be completed.

# In[15]:


b.get_parameter('fluxes', context='model').interp_value(times=5)


# Determining & Plotting Residuals
# ----------------------------

# One particularly useful case for interpolating is to compare a model (perhaps computed in phase-space) to a dataset with a large number of datapoints.  We can do this directly by calling [compute_residuals](../api/phoebe.parameters.ParameterSet.compute_residuals.md), which will handle any necessary interpolation and compare the dependent variable between the dataset and models.
# 
# Note that if there are more than one dataset or model attached to the bundle, it may be necessary to pass `dataset` and/or `model` (or filter in advanced and call compute_residuals on the filtered [ParameterSet](../api/phoebe.paraemters.ParameterSet.md).
# 
# To see this in action, we'll first create a "fake" observational dataset, add some noise, recompute the model using `compute_phases`, and then compute the residuals.

# In[16]:


b.add_dataset('lc', 
              times=phoebe.linspace(0,10,1000),
              dataset='lc01',
              overwrite=True)


# In[17]:


b.run_compute(irrad_method='none')


# In[18]:


fluxes = b.get_value('fluxes', context='model')
b.set_value('fluxes', context='dataset', value=fluxes)


# In[19]:


b.flip_constraint('compute_phases', solve_for='compute_times')


# In[20]:


b.set_value('compute_phases', phoebe.linspace(0,1,101))


# In[21]:


b.set_value('teff', component='primary', value=5950)


# In[22]:


b.run_compute(irrad_method='none')


# In[23]:


print(len(b.get_value('fluxes', context='dataset')), len(b.get_value('fluxes', context='model')))


# In[24]:


b.compute_residuals()


# If we plot the dataset and model, we see that the model was only computed for one cycle, whereas the dataset extends further in time.

# In[25]:


afig, mplfig = b.plot(show=True)


# But we can also plot the residuals.  Here, [compute_residuals](../api/phoebe.parameters.ParameterSet.compute_residuals.md) is called internally, interpolating in phase-space, and then plotted in time-space.  See the options for `y` in the [plot API docs](../api/phoebe.parameters.ParameterSet.plot.md) for more details.

# In[26]:


afig, mplfig = b.plot(y='residuals', show=True)


# In[ ]:




