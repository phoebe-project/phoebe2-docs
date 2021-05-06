#!/usr/bin/env python
# coding: utf-8

# # Advanced: Custom Cost Funtion (with emcee)
# 
# **IMPORTANT**: this tutorial assumes basic knowledge (and uses a file resulting from) the [emcee tutorial](./emcee.ipynb), although the custom cost function itself can be used for any optimizer or sampler.

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


# ## Defining the custom cost function
# 
# As is described in the [b.run_solver API docs](../api/phoebe.frontend.bundle.Bundle.run_solver.md), a custom function can be passed which overrides the internal default cost function.  This function must accept `b, model, lnpriors, priors, priors_combine` as arguments and return the `lnprobability` (cost function).  The arguments are as follows:
# * `b`: the bundle with the current face-values for this forward model
# * `model`: the name of the forward model in `b`
# * `lnpriors`: the pre-computed value of the log-priors by passing `priors` and `priors_combine` to [b.calculate_lnp](../api/phoebe.frontend.bundle.Bundle.calculate_lnp.md)
# * `priors`: the name(s) of the prior distributions
# * `priors_combine`: the choice for how to combine priors if `priors` includes more than one distribution for any single parameter.
# 
# If a custom function is not passed, the default cost function is the sum of the lnlikelihood (from [b.calculate_lnlikelihood](../api/phoebe.parameters.ParameterSet.calculate_lnlikelihood.md)) and the probability of drawing the current face-values from the passed priors.
# 
# Let's reproduce this default case for the sake of this example.  We'll include a print statement just for confirmation that our function is being called.  In practice, you could do any modifications here with access to parameter values, distributions, synthetic models, and observations.

# In[4]:


def default_lnprob(b, model, lnpriors, priors, priors_combine):
    print("* calling default_lnprob")
    return lnpriors + b.calculate_lnlikelihood(model=model)


# ## run_solver
# 
# In order to swap out the default cost function with our custom cost function, we must pass the function itself to `custom_lnprobability_callable` when calling [b.run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md)

# In[5]:


b.run_solver('emcee_solver',
             custom_lnprobability_callable=default_lnprob,
             niters=1,
             solution='emcee_sol_custom_lnprob', overwrite=True)

