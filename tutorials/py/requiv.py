#!/usr/bin/env python
# coding: utf-8

# Equivalent Radius
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Now let's add a mesh dataset at a few different times so that we can see how the potentials affect the surfaces of the stars.

# In[3]:


b.add_dataset('mesh', times=np.linspace(0,1,11), dataset='mesh01')


# Relevant Parameters
# ------------------------
# 
# The 'requiv' parameter defines the stellar surface to have a constant volume of 4./3 pi requiv^3.

# In[4]:


print b['requiv@component']


# Critical Potentials and System Checks
# --------------------------------------------
# 
# Additionally, for each detached component, there is an requiv_max Parameter which shows the critical value at which the Roche surface will overflow.  Setting requiv to a larger value will fail system checks and raise a warning.

# In[5]:


print b['requiv_max@primary@component']


# In[6]:


print b['requiv_max@primary@constraint']


# In[8]:


b.set_value('requiv@primary@component', 3)


# In[ ]:





# At this time, if you were to call run_compute, an error would be thrown.  An error isn't immediately thrown when setting requiv, however, since the overflow can be recitified by changing any of the other relevant parameters.  For instance, let's change sma to be large enough to account for this value of rpole and you'll see that the error does not occur again.

# In[10]:


b.set_value('sma@binary@component', 10)


# These logger warnings are handy when running phoebe interactively, but in a script its also handy to be able to check whether the system is currently computable /before/ running run_compute.
# 
# This can be done by calling run_checks which returns a boolean (whether the system passes all checks) and a message (a string describing the first failed check).

# In[13]:


passed, message = b.run_checks()
print passed, message


# In[14]:


b.set_value('sma@binary@component', 5)


# In[15]:


passed, message = b.run_checks()
print passed, message


# Semi-Detached Systems
# -----------------------------
# 
# Semi-detached systems are implemented by constraining the value of requiv to be the same as requiv_max by appyling the 'semidetached' constraint on the 'primary' component.
# 

# In[17]:


b.add_constraint('semidetached', 'primary')


# We can view the constraint on requiv by accessing the constraint:

# In[21]:


b['requiv@constraint@primary']


# Now whenever any of the relevant parameters (q, ecc, syncpar, sma) are changed, the value of requiv will change to match the critical value as defined by requiv_max.

# In[20]:


b['requiv_max@constraint@primary']

