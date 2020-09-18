#!/usr/bin/env python
# coding: utf-8

# Advanced: Settings
# ============================
# 
# The Bundle also contains a few Parameters that provide settings for that Bundle.  Note that these are not system-wide and only apply to the current Bundle.  They are however maintained when [saving and loading](./saving_and_loading.ipynb) a Bundle.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# As always, let's do imports and initialize a longger and a new Bundle.

# In[2]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# Accessing Settings
# ---------------------------

# Settings are found with their own context in the Bundle and can be accessed through the get_setting method

# In[3]:


b.get_setting()


# or via filtering/twig access

# In[4]:


b['setting']


# and can be set as any other Parameter in the Bundle

# Available Settings
# --------------------------
# 
# Now let's look at each of the available settings and what they do

# ### phoebe_version
# 
# `phoebe_version` is a read-only parameter in the settings to store the version of PHOEBE used.

# ### dict_set_all
# 
# `dict_set_all` is a BooleanParameter (defaults to False) that controls whether attempting to set a value to a ParameterSet via dictionary access will set all the values in that ParameterSet (if True) or raise an error (if False)

# In[5]:


b['dict_set_all@setting']


# In[6]:


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

# In[7]:


b.set_value_all('teff@component', 4000)
print(b['value@teff@primary@component'], b['value@teff@secondary@component'])


# If you want dictionary access to use set_value_all instead of set_value, you can enable this parameter

# In[8]:


b['dict_set_all@setting'] = True
b['teff@component'] = 8000
print(b['value@teff@primary@component'], b['value@teff@secondary@component'])


# Now let's disable this so it doesn't confuse us while looking at the other options

# In[9]:


b.set_value_all('teff@component', 6000)
b['dict_set_all@setting'] = False


# ### dict_filter
# 
# `dict_filter` is a Parameter that accepts a dictionary.  This dictionary will then always be sent to the filter call which is done under-the-hood during dictionary access.

# In[10]:


b['incl']


# In our default binary, there are several inclination parameters - one for each component ('primary', 'secondary', 'binary') and one with the constraint context (to keep the inclinations aligned).
# 
# This can be inconvenient... if you want to set the value of the binary's inclination, you must always provide extra information (like '@component').
# 
# Instead, we can always have the dictionary access search in the component context by doing the following

# In[11]:


b['dict_filter@setting'] = {'context': 'component'}


# In[12]:


b['incl']


# Now we no longer see the constraint parameters.
# 
# All parameters are always accessible with method access:

# In[13]:


b.filter(qualifier='incl')


# Now let's reset this option... keeping in mind that we no longer have access to the 'setting' context through twig access, we'll have to use methods to clear the dict_filter

# In[14]:


b.set_value('dict_filter@setting', {})


# ### run_checks_compute (/figure/solver/solution)
# 
# The `run_checks_compute` option allows setting the default compute option(s) sent to [b.run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md), including warnings in the logger raised by interactive checks (see [phoebe.interactive_checks_on](../api/phoebe.interactive_checks_on.md)).
# 
# Similar options also exist for checks at the figure, solver, and solution level.

# In[15]:


b['run_checks_compute@setting']


# In[16]:


b.add_dataset('lc')
b.add_compute('legacy')
print(b.run_checks())


# In[17]:


b['run_checks_compute@setting'] = ['phoebe01']


# In[18]:


print(b.run_checks())


# ### auto_add_figure, auto_remove_figure
# 
# The `auto_add_figure` and `auto_remove_figure` determine whether new figures are automatically added to the Bundle when new datasets, distributions, etc are added.  This is False by default within Python, but True by default within the [UI clients](http://phoebe-project.org/clients).

# In[19]:


b['auto_add_figure']


# In[20]:


b['auto_add_figure'].description


# In[21]:


b['auto_remove_figure']


# In[22]:


b['auto_remove_figure'].description


# ### web_client, web_client_url
# 
# The `web_client` and `web_client_url` settings determine whether the [client](http://phoebe-project.org/clients) is opened in a web-browser or with the installed desktop client whenever calling [b.ui](../api/phoebe.parameters.ParameterSet.ui.md) or [b.ui_figures](../api/phoebe.frontend.bundle.Bundle.ui_figures.md).  For more information, see the [UI from Jupyter tutorial](./ui_jupyter.ipynb).

# In[23]:


b['web_client']


# In[24]:


b['web_client'].description


# In[25]:


b['web_client_url']


# In[26]:


b['web_client_url'].description

