#!/usr/bin/env python
# coding: utf-8

# Advanced: Undo/Redo
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# Enabling/Disabling Logging History
# ---------------------------------------------

# Undo and redo support is built directly into the bundle.  Every time you make a change to a parameter or call a method, a new Parameter is created with the 'history' context.  These parameters then know how to undo or redo that action.  Of course, this can result in a large list of Parameters that you may not want - see the tutorial on [Settings](settings) for more details on how to change the log size or enable/disable history entirely.
# 
# By default history logging is off, so let's first enable it.

# In[3]:


b.enable_history()


# Undoing
# ---------------

# First let's set a value so we know what we're expecting to undo

# In[4]:


b['ra@system']


# In[5]:


b['ra@system'] = 10
b['ra@system']


# The history context contains a list of parameters, all numbered and ugly.  But there is a convenience method which allows you to get history items by index - including reverse indexing.  This is probably the most common way to get a history item... and you'll most likely want the LATEST item.

# In[6]:


b.get_history(-1)


# In[7]:


print b.get_history(-1)['redo_func'], b.get_history(-1)['redo_kwargs']


# Here you can see that redo_func and redo_kwargs shows exactly the last call we made to the bundle that actually changed something (we did b['ra@system'] = 10).  
# 
# We can also look at what will be called when we undo this item

# In[8]:


print b.get_history(-1)['undo_func'], b.get_history(-1)['undo_kwargs']


# If we want, we can then automatically call that undo method (note that you can also pass the index to undo, but it does assume -1 by default)

# In[9]:


b.undo()


# And we can see that it did exactly what we expected.

# In[10]:


b['ra@system']

