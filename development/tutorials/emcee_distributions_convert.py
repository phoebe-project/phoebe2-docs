#!/usr/bin/env python
# coding: utf-8

# # Advanced: Convert Posterior Distributions from EMCEE
# 
# **IMPORTANT**: this tutorial assumes basic knowledge (and uses a file resulting from) the [emcee tutorial](./emcee.ipynb).
# 
# **NOTE**: a bug in the latex labels when *converting to univariate distributions* was fixed in 2.3.12.  Running this notebook on earlier versions will raise an error near the end.

# ## Setup
# 
# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger('error')


# We'll then start with the bundle from the end of the [emcee tutorial](./emcee.ipynb).  If you're running this notebook locally, you will need to run that first to create the `emcee_advanced_tutorials.bundle` file that we will use here.

# In[3]:


b = phoebe.load('emcee_advanced_tutorials.bundle')


# # how posteriors are represented
# 
# The emcee solution object contains all the samples from all chains during the MCMC run.  This is then "trimmed" based on the set or passed values of `burnin`, `thin`, and `lnprob_cutoff` to create a [distl MVSamples](https://distl.readthedocs.io/en/latest/api/MVSamples/) object - which is capable of plotting the histogram representation of all these samples as a corner plot, while still retaining (and ultimately drawing from) the full underlying set of samples.  This is the most "true" representation of the underlying information, but requires maintaining the full set of "trimmed" samples and can be expensive for a large number of walkers/iterations.
# 
# We can access the underlying [distl MVSamples](https://distl.readthedocs.io/en/latest/api/MVSamples/) object with [b.get_distribution_collection](../api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md) and can see that it has a [dc.samples](https://distl.readthedocs.io/en/latest/api/MVSamples.samples/) property containing this underlying data.

# In[4]:


dc, twigs = b.get_distribution_collection(solution='emcee_sol')


# In[5]:


dc


# We could convert this object manually using distl, using [dc.to_mvgaussian](https://distl.readthedocs.io/en/latest/api/MVSamples.to_mvgaussian/), for example.  This is much more lightweight, as it only stores the means and covariance matrix, but is really only fair if the samples can be well-represented by a multivariate gaussian.

# In[6]:


dc.to_mvgaussian()


# PHOEBE provides an interface to do these conversions (using distl) under-the-hood so that all the plotting and adopting infrastructure still works seemlesly.  This brings us to the `distributions_convert` parameter.

# # distributions_convert parameter
# 
# The `distributions_convert` parameter (or as an override keyword argument) will convert the underlying [distl MVSamples](https://distl.readthedocs.io/en/latest/api/MVSamples/) object to the desired distribution type whenever calling [adopt_solution](../api/phoebe.frontend.bundle.Bundle.adopt_solution.md), [get_distribution_collection](../api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md), [sample_distribution_collection](../api/phoebe.frontend.bundle.Bundle.sample_distribution_collection.md), [uncertainties_from_distribution_collection](../api/phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection.md), [plot_distribution_collection](../api/phoebe.frontend.bundle.Bundle.plot_distribution_collection.md), or [plot](../phoebe.parameters.ParameterSet.plot.md) (with `style='corner'` or `'failed'`).
# 
# If we examine the `distributions_convert` parameter (in the emcee solution), we can see its description and available choices.

# In[7]:


print(b.get_parameter(qualifier='distributions_convert', solution='emcee_sol'))


# If we don't pass `distributions_convert` to `plot`, then the value from the parameter will be used.  In this case, it will keep the distribution as a multivariate samples.

# In[8]:


_ = b.plot(solution='emcee_sol', style='corner', show=True)


# By converting to [MVHistogram](https://distl.readthedocs.io/en/latest/api/MVHistogram/), the data is stored as an N-dimensional histogram.  In this case, with a 6 parameters and a default of 20 bins per dimension (when `distributions_convert` is set to `'mvhistogram'` or `'histogram'`, a new `distributions_bins` parameter becomes visible to override the default), this is actually more expensive to store than the underlying samples.  But in cases with few parameters and a large number of walkers/iterations, the binned version may be cheaper to manage.

# In[9]:


_ = b.plot(solution='emcee_sol', style='corner', 
           distributions_convert='mvhistogram', show=True)


# By converting to [MVGaussian](https://distl.readthedocs.io/en/latest/api/MVGaussian/), the data is stored as means and a covariance matrix.  This is extremely cheap to store, but should **only** be used if the underlying distribution is gaussian (probably not the case here, especially for the last parameter).

# In[10]:


_ = b.plot(solution='emcee_sol', style='corner', 
           distributions_convert='mvgaussian', show=True)


# Even cheaper yet, we can convert to non-multivariate distribution types and drop information about the covariances between parameters.  Here if we convert to a collection of [Gaussian](https://distl.readthedocs.io/en/latest/api/Gaussian/) distributions, only the means and sigmas are stored.
# 
# **NOTE**: a bug in the latex labels when *converting to univariate distributions* was fixed in 2.3.12.  Running this notebook on earlier versions will raise an error near the end

# In[11]:


_ = b.plot(solution='emcee_sol', style='corner', 
           distributions_convert='gaussian', show=True)


# If we look at the actual [distl DistributionCollection](https://distl.readthedocs.io/en/latest/api/DistributionCollection/) object, we can see that it now contains a list of independent gaussian distributions.

# In[12]:


dc, twigs = b.get_distribution_collection(solution='emcee_sol', distributions_convert='gaussian')


# In[13]:


print(dc)


# In[14]:


print(dc.dists)


# ## See Also
# 
# See the following for even more advanced use cases of emcee.
# 
# * [Advanced: EMCEE Initializing Distribution Requirements](./emcee_init_from_requires.ipynb)
# * [Advanced: continuing emcee from a previous run](./emcee_continue_from.ipynb)
# * [Advanced: resampling emcee from a previous run](./emcee_resample.ipynb)
