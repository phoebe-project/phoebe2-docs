#!/usr/bin/env python
# coding: utf-8

# Advanced: Settings
# ============================
# 
# The Bundle also contains a few Parameters that provide settings for that Bundle.  Note that these are not system-wide and only apply to the current Bundle.  They are however maintained when [saving and loading](./saving_and_loading.ipynb) a Bundle.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# Accessing Settings
# ---------------------------

# Settings are found with their own context in the Bundle and can be accessed through the get_setting method

# In[2]:


b.get_setting()


# or via filtering/twig access

# In[3]:


b['setting']


# and can be set as any other Parameter in the Bundle

# Available Settings
# --------------------------
# 
# Now let's look at each of the available settings and what they do

# ### log_history
# 
# log_history is a BooleanParameter (defaults to False) that controls whether undo/redo ability is enabled.

# In[4]:


b['log_history@setting'].description


# This parameter can also be set by calling b.enable_history() or b.disable_history() and can be accessed with b.history_enabled.

# In[5]:


b['log_history@setting']


# In[6]:


b.history_enabled


# In[7]:


b.enable_history()


# In[8]:


b['log_history@setting']


# In[9]:


b.history_enabled


# ### dict_set_all
# 
# dict_set_all is a BooleanParameter (defaults to False) that controls whether attempting to set a value to a ParameterSet via dictionary access will set all the values in that ParameterSet (if True) or raise an error (if False)

# In[10]:


b['dict_set_all@setting']


# In[11]:


b['teff@component']


# In our default binary there are temperatures ('teff') parameters for each of the components ('primary' and 'secondary').  If we were to do:
# 
# b['teff@component'] = 6000
# 
# this would raise an error.  Under-the-hood, this is simply calling:
# 
# b.set_value('teff@component', 6000)
# 
# which of course would also raise an error.
# 
# In order to set both temperatures to 6000, you would either have to loop over the components or call the set_value_all method:

# In[12]:


b.set_value_all('teff@component', 4000)
print(b['value@teff@primary@component'], b['value@teff@secondary@component'])


# If you want dictionary access to use set_value_all instead of set_value, you can enable this parameter

# In[13]:


b['dict_set_all@setting'] = True
b['teff@component'] = 8000
print(b['value@teff@primary@component'], b['value@teff@secondary@component'])


# Now let's disable this so it doesn't confuse us while looking at the other options

# In[14]:


b.set_value_all('teff@component', 6000)
b['dict_set_all@setting'] = False


# ### dict_filter
# 
# dict_filter is a Parameter that accepts a dictionary.  This dictionary will then always be sent to the filter call which is done under-the-hood during dictionary access.

# In[15]:


b['incl']


# In our default binary, there are several inclination parameters - one for each component ('primary', 'secondary', 'binary') and one with the constraint context (to keep the inclinations aligned).
# 
# This can be inconvenient... if you want to set the value of the binary's inclination, you must always provide extra information (like '@component').
# 
# Instead, we can always have the dictionary access search in the component context by doing the following

# In[16]:


b['dict_filter@setting'] = {'context': 'component'}


# In[17]:


b['incl']


# Now we no longer see the constraint parameters.
# 
# All parameters are always accessible with method access:

# In[18]:


b.filter(qualifier='incl')


# Now let's reset this option... keeping in mind that we no longer have access to the 'setting' context through twig access, we'll have to use methods to clear the dict_filter

# In[19]:


b.set_value('dict_filter@setting', {})


# ### run_checks_compute
# 
# The run_checks_compute option allows setting the default compute option(s) sent to [b.run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md), including warnings in the logger raised by interactive checks (see [phoebe.interactive_checks_on](../api/phoebe.interactive_checks_on.md)).

# In[20]:


b['run_checks_compute@setting']


# In[21]:


b.add_dataset('lc')
b.add_compute('legacy')
print(b.run_checks())


# In[22]:


b['run_checks_compute@setting'] = ['phoebe01']


# In[23]:


print(b.run_checks())


# In[ ]:




