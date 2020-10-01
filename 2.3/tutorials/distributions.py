#!/usr/bin/env python
# coding: utf-8

# Distributions
# ============================
# 
# Distributions are mostly useful when using samplers (which we'll see in the next tutorial on [solving the inverse problem](./solver.ipynb)) - but can also be useful to propagate any set of distributions (whether those be uncertainties in the literature, etc) through the forward model.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[ ]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[4]:


import phoebe

logger = phoebe.logger()

b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))


# Adding Distributions
# ----------------------
# 
# Distributions can be attached to most any FloatParameter in the Bundle.  To see a list of these available parameters, we can call [b.get_adjustable_parameters](../api/phoebe.frontend.bundle.Bundle.get_adjustable_parameters.md).  Note the `exclude_constrained` option which defaults to True: we can set distributions on constrained parameters (for priors, for example), but those will not be able to be sampled from in the forward model or while fitting.  We'll come back to this in the next tutorial when looking at priors.
# 

# In[5]:


b.get_adjustable_parameters()


# [add_distribution](../api/phoebe.frontend.bundle.Bundle.add_distribution.md) is quite flexible and accepts several different syntaxes to add multiple distributions in one line.  Here we'll just attach a distribution to a single parameter at a time.  Just like when calling [add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md) or [add_compute](../api/phoebe.frontend.bundle.Bundle.add_compute.md), [add_distribution](../api/phoebe.frontend.bundle.Bundle.add_distribution.md) optionally takes a `distribution` tag -- and in the cases of distributions, we can attach distributions to multiple parameters with the same `distribution` tag.
# 
# The values of the [DistributionParameters](../api/phoebe.parameters.DistributionParameter.md) are [distl](https://distl.readthedocs.io) distribution objects -- the most common of which are conveniently available at the top-level of PHOEBE:
# 
# * [phoebe.gaussian](../api/phoebe.gaussian.md)
# * [phoebe.gaussian_around](../api/phoebe.gaussian_around.md)
# * [phoebe.uniform](../api/phoebe.uniform.md)
# * [phoebe.uniform_around](../api/phoebe.uniform_around.md)
# 
# Now let's attach a gaussian distribution on the temperature of the primary star.

# In[6]:


b.add_distribution(qualifier='teff', component='primary', 
                   value=phoebe.gaussian(6000,100), 
                   distribution='mydist')


# As you probably can expect by now, we also have methods to:
# 
# * [get_distribution](../api/phoebe.frontend.bundle.Bundle.get_distribution.md)
# * [rename_distribution](../api/phoebe.frontend.bundle.Bundle.rename_distribution.md)
# * [remove_distribution](../api/phoebe.frontend.bundle.Bundle.remove_distribution.md)

# In[7]:


print(b.get_distribution(distribution='mydist'))


# Now let's add another distribution, with the same `distribution` tag, to the inclination of the binary.

# In[8]:


b.add_distribution(qualifier='incl', component='binary',
                   value=phoebe.uniform(80,90),
                   distribution='mydist')


# In[9]:


print(b.get_distribution(distribution='mydist'))


# Accessing & Plotting Distributions
# --------------------

# The parameters we've created and attached are [DistributionParameters](../api/phoebe.parameters.DistributionParameter.md) and live in `context='distribution'`, with all other tags matching the parameter they're referencing.  For example, let's filter and look at the distributions we've added.

# In[10]:


print(b.filter(context='distribution'))


# In[11]:


print(b.get_parameter(context='distribution', qualifier='incl'))


# In[12]:


print(b.get_parameter(context='distribution', qualifier='incl').tags)


# The "value" of the parameter, is the [distl](https://distl.readthedocs.io) distributon object itself.

# In[14]:


b.get_value(context='distribution', qualifier='incl')


# And because of that, we can call any method on the [distl](https://distl.readthedocs.io) object, including plotting the distribution.

# In[17]:


_ = b.get_value(context='distribution', qualifier='incl').plot(show=True)


# If we want to see how multiple individual distributions interact and are correlated with each other via a corner plot, we can access the combined "distribution collection" from any number of `distribution` tags. This may not be terribly useful now, but is very useful when trying to create multivariate priors.
# 
# * [b.get_distribution_collection](../api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
# * [b.plot_distribution_collection](../api/phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)

# In[18]:


_ = b.plot_distribution_collection(distribution='mydist', show=True)


# Sampling Distributions
# -------------------

# We can also sample from these distributions - either manually by calling sample on the [distl](https://distl.readthedocs.io) or in bulk by respecting any covariances in the "distributon collection" via:
# 
# * [b.sample_distribution_collection](../api/phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)

# In[19]:


b.sample_distribution_collection(distribution='mydist')


# By default this just returns a dictionary with the twigs and sampled values.  But if we wanted, we could have these applied immediately to the face-values by passing `set_value=True`, in which case a [ParameterSet](../api/phoebe.parameters.ParameterSet.md) of changed parameters (including those via constraints) is returned instead.

# In[21]:


changed_params = b.sample_distribution_collection(distribution='mydist', set_value=True)


# In[22]:


print(changed_params)


# Propagating Distributions through Forward Model
# -------------------

# Lastly, we can have PHOEBE automatically draw from a "distribution collection" multiple times and expose the distribution of the model itself.

# In[24]:


print(b.get_parameter(qualifier='sample_from', context='compute'))


# Once `sample_from` is set, `sample_num` and `sample_mode` are exposed as visible parameters

# In[25]:


b.set_value('sample_from', value='mydist')


# In[26]:


print(b.filter(qualifier='sample*'))


# Now when we call [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md), 10 different instances of the forward model will be computed from 10 random draws from the "distribution collection" but only the median and 1-sigma uncertainties will be exposed in the model.

# In[27]:


b.run_compute(irrad_method='none')


# In[28]:


_ = b.plot(show=True)


# Next
# ----------
# 
# Next up: let's learn about [solving the inverse problem](./solver.ipynb)
