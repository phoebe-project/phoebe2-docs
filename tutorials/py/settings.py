#!/usr/bin/env python
# coding: utf-8

# Advanced: Settings
# ============================
# 
# The Bundle also contains a few Parameters that provide settings for that Bundle.  Note that these are not system-wide and only apply to the current Bundle.  They are however maintained when [saving and loading](./saving_and_loading) a Bundle.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

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

# In[5]:


b['log_history@setting'].description


# This parameter can also be set by calling b.enable_history() or b.disable_history() and can be accessed with b.history_enabled.

# In[6]:


b['log_history@setting']


# In[7]:


b.history_enabled


# In[8]:


b.enable_history()


# In[9]:


b['log_history@setting']


# In[10]:


b.history_enabled


# ### dict_set_all
# 
# dict_set_all is a BooleanParameter (defaults to False) that controls whether attempting to set a value to a ParameterSet via dictionary access will set all the values in that ParameterSet (if True) or raise an error (if False)

# In[11]:


b['dict_set_all@setting']


# In[12]:


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

# In[13]:


b.set_value_all('teff@component', 4000)
print b['value@teff@primary@component'], b['value@teff@secondary@component']


# If you want dictionary access to use set_value_all instead of set_value, you can enable this parameter

# In[14]:


b['dict_set_all@setting'] = True
b['teff@component'] = 8000
print b['value@teff@primary@component'], b['value@teff@secondary@component']


# Now let's disable this so it doesn't confuse us while looking at the other options

# In[15]:


b['dict_set_all@setting'] = False


# ### dict_filter
# 
# dict_filter is a Parameter that accepts a dictionary.  This dictionary will then always be sent to the filter call which is done under-the-hood during dictionary access.

# In[16]:


b['incl']


# In our default binary, there are several inclination parameters - one for each component ('primary', 'secondary', 'binary') and one with the constraint context (to keep the inclinations aligned).
# 
# This can be inconvenient... if you want to set the value of the binary's inclination, you must always provide extra information (like '@component').
# 
# Instead, we can always have the dictionary access search in the component context by doing the following

# In[17]:


b['dict_filter@setting'] = {'context': 'component'}


# In[18]:


b['incl']


# Now we no longer see the constraint parameters.
# 
# All parameters are always accessible with method access:

# In[19]:


b.filter(qualifier='incl')


# Now let's reset this option... keeping in mind that we no longer have access to the 'setting' context through twig access, we'll have to use methods to clear the dict_filter

# In[20]:


b.set_value('dict_filter@setting', {})

