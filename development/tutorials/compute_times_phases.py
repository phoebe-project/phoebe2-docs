#!/usr/bin/env python
# coding: utf-8

# Advanced: compute_times & compute_phases
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# Let's get started with some basic imports.

# In[2]:


import phoebe
from phoebe import u # units

b = phoebe.default_binary()


# In[3]:


b.add_dataset('lc', times=phoebe.linspace(0,10,101), dataset='lc01')


# Overriding Computation Times
# ----------------------------
# 
# If `compute_times` is not empty (by either providing `compute_times` *or* `compute_phases`), the provided value will be used to compute the model instead of those in the `times` parameter.
# 
# In the case of a [mesh dataset](MESH.ipynb) or [orbit dataset](ORB.ipynb), observations cannot be attached to the dataset, so a `times` parameter does not exist.  In this case `compute_times` or `compute_phases` will *always* be used.

# In[4]:


print(b.filter(qualifier=['times', 'compute_times'], context='dataset'))


# In[5]:


b.set_value('compute_times', phoebe.linspace(0,3,11))


# In[6]:


b.run_compute()


# In[7]:


print("dataset times: {}\ndataset compute_times: {}\nmodel times: {}".format(
    b.get_value('times', context='dataset'),
    b.get_value('compute_times', context='dataset'),
    b.get_value('times', context='model')
    ))


# `compute_times` (when not empty) overrides the value of `times` when computing the model.  However, passing `times` as a keyword argument to [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) will take precedence over either - and override the computed times across *all* enabled datasets.

# In[8]:


b.run_compute(times=[0,0.2])


# In[9]:


print("dataset times: {}\ndataset compute_times: {}\nmodel times: {}".format(
    b.get_value('times', context='dataset'),
    b.get_value('compute_times', context='dataset'),
    b.get_value('times', context='model')
    ))


# In[10]:


b.run_compute()


# In[11]:


print("dataset times: {}\ndataset compute_times: {}\nmodel times: {}".format(
    b.get_value('times', context='dataset'),
    b.get_value('compute_times', context='dataset'),
    b.get_value('times', context='model')
    ))


# Phase-Time Conversion
# ----------------------------------

# In addition to the ability to provide `compute_times`, we can alternatively provide `compute_phases`.  These two parameters are linked via a constraint (see the [constraints tutorial](./constraints.ipynb)), with `compute_phases` *constrained* by default.

# In[12]:


print(b.filter(qualifier=['times', 'compute_times', 'compute_phases', 'compute_phases_t0'], context='dataset'))


# Essentially, this constraint does the same thing as [b.to_phase](../api/phoebe.frontend.bundle.Bundle.to_phase.md) or [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md), using the appropriate t0 according to `phases_t0` from the **top-level** orbit in the hierarchy.

# In[13]:


print(b.get_constraint('compute_phases'))


# In[14]:


print(b.get_parameter('phases_t0').choices)


# In order to provide `compute_phases` instead of `compute_times`, we must call [b.flip_constraint](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).

# In[15]:


b.flip_constraint('compute_phases', solve_for='compute_times')


# In[16]:


b.set_value('compute_phases', phoebe.linspace(0,1,11))


# In[17]:


print(b.filter(qualifier=['times', 'compute_times', 'compute_phases', 'phases_t0'], context='dataset'))


# Note that under the hood, PHOEBE **always** works in time-space, meaning it is the *constrained* value of `compute_times` that is being passed under-the-hood.

# Also note that if directly passing `compute_phases` to [b.add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md), the constraint will be flipped on our behalf.  We would then need to flip the constraint in order to provide `compute_times` instead.

# Finally, it is important to make the distinction that this is **not** adding support for **observations** in phases.  If we have an old light curve that is only available in phase, we still must convert these to times manually (or via [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md)).  This restriction is intentional: we do not want the mapping between phase and time to change as the ephemeris is changed or fitted, rather we want to try to map from phase to time using the ephemeris that was originally used when the dataset was recorded (if possible, or the best possible guess).

# Interpolating the Model
# ------------------------------

# Whether or not we used `compute_times`/`compute_phases` or not, it is sometimes useful to be able to interpolate on the resulting model.  In the case where we provided `compute_times`/`compute_phases` to "down-sample" from a large dataset, this can be particularly useful.
# 
# We can call [interp_value](../api/phoebe.parameters.FloatArrayParameter.interp_value.md) on any [FloatArrayParameter](../api/phoebe.parameters.FloatArrayParameter.md).  

# In[18]:


b.get_parameter('fluxes', context='model').get_value()


# In[19]:


b.get_parameter('fluxes', context='model').interp_value(times=1.0)


# In[20]:


b.get_parameter('fluxes', context='model').interp_value(times=phoebe.linspace(0,3,101))


# In the case of times, this will *automatically* interpolate in phase-space if the provided time is outside the range of the referenced times array.  If you have a logger enabled with at least the 'warning' level, this will raise a warning and state the phases at which the interpolation will be completed.

# In[21]:


b.get_parameter('fluxes', context='model').interp_value(times=5)


# Determining & Plotting Residuals
# ----------------------------

# One particularly useful case for interpolating is to compare a model (perhaps computed in phase-space) to a dataset with a large number of datapoints.  We can do this directly by calling [compute_residuals](../api/phoebe.parameters.ParameterSet.compute_residuals.md), which will handle any necessary interpolation and compare the dependent variable between the dataset and models.
# 
# Note that if there are more than one dataset or model attached to the bundle, it may be necessary to pass `dataset` and/or `model` (or filter in advanced and call compute_residuals on the filtered [ParameterSet](../api/phoebe.paraemters.ParameterSet.md).
# 
# To see this in action, we'll first create a "fake" observational dataset, add some noise, recompute the model using `compute_phases`, and then calculate the residuals.

# In[22]:


b.add_dataset('lc', 
              times=phoebe.linspace(0,10,1000),
              dataset='lc01',
              overwrite=True)


# In[23]:


b.run_compute(irrad_method='none')


# In[24]:


fluxes = b.get_value('fluxes', context='model')
b.set_value('fluxes', context='dataset', value=fluxes)


# In[25]:


b.flip_constraint('compute_phases', solve_for='compute_times')


# In[26]:


b.set_value('compute_phases', phoebe.linspace(0,1,101))


# In[27]:


b.set_value('teff', component='primary', value=5950)


# In[28]:


b.run_compute(irrad_method='none')


# In[29]:


print(len(b.get_value('fluxes', context='dataset')), len(b.get_value('fluxes', context='model')))


# In[30]:


b.calculate_residuals()


# If we plot the dataset and model, we see that the model was only computed for one cycle, whereas the dataset extends further in time.

# In[31]:


afig, mplfig = b.plot(show=True)


# But we can also plot the residuals.  Here, [calculate_residuals](../api/phoebe.parameters.ParameterSet.calculate_residuals.md) is called internally, interpolating in phase-space, and then plotted in time-space.  See the options for `y` in the [plot API docs](../api/phoebe.parameters.ParameterSet.plot.md) for more details.

# In[32]:


afig, mplfig = b.plot(y='residuals', show=True)


# ## See Also
# 
# The following other advanced tutorials may interest you:
# * [Advanced: Phase Masking](./mask_phases.ipynb)
# * [Advanced: Solver Times](./solver_times.ipynb)
