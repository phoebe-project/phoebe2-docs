#!/usr/bin/env python
# coding: utf-8

# Advanced: Optimizing Performance with PHOEBE
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# In[1]:


import phoebe


# In[2]:


b = phoebe.default_binary()


# Interactivity Options
# --------------------------

# When running in an interactive Python session, PHOEBE updates all constraints and runs various checks after **each** command.  Although this is convenient, it does take some time, and it can sometimes be advantageous to disable this to save computation time.
# 
# ### Interactive Checks
# 
# By default, interactive checks are **enabled** when PHOEBE is being run in an interactive session (either an interactive python, IPython, or Jupyter notebook session), but **disabled** when PHOEBE is run as a script directly from the console.  When enabled, PHOEBE will re-run the system checks after every single change to the bundle, raising warnings via the logger as soon as they occur.
# 
# This default behavior can be changed via [phoebe.interactive_checks_on()](../api/phoebe.interactive_checks_on.md) or [phoebe.interactive_checks_off()](../api/phoebe.interactive_checks_off.md).  The current value can be accessed via phoebe.conf.interactive_checks.

# In[3]:


print(phoebe.conf.interactive_checks)


# In[4]:


phoebe.interactive_checks_off()


# In[5]:


print(phoebe.conf.interactive_checks)


# If disabled, you can always manually run the checks via [b.run_checks()](../api/phoebe.frontend.bundle.Bundle.run_checks.md).

# In[6]:


print(b.run_checks())


# In[7]:


b.set_value('requiv', component='primary', value=50)


# In[8]:


print(b.run_checks())


# ### Interactive Constraints
# 
# By default, interactive constraints are **always enabled** in PHOEBE, unless explicitly disabled.  Whenever a value is changed in the bundle that affects the value of a constrained value, that constraint is immediately executed and all applicable values updated.  The ensures that all constrained values are "up-to-date".
# 
# If disabled, constraints are delayed and only executed when needed by PHOEBE (when calling run_compute, for example).  This can save significant time, as each value that needs updating only needs to have its constraint executed once, instead of multiple times.
# 
# This default behavior can be changed via [phoebe.interactive_constraints_on()](../api/phoebe.interactive_constraints_on.md) or [phoebe.interactive_constraints_off()](../api/phoebe.interactive_constraints_off.md).  The current value can be accessed via phoebe.conf.interactive_constraints.
# 
# Let's first look at the default behavior with interactive constraints on.

# In[9]:


print(phoebe.conf.interactive_constraints)


# In[10]:


print(b.filter('mass', component='primary'))


# In[11]:


b.set_value('sma@binary', 10)


# In[12]:


print(b.filter('mass', component='primary'))


# Note that the mass has already updated, according to the constraint, when the value of the semi-major axes was changed.  If we disable interactive constraints this will not be the case.

# In[13]:


phoebe.interactive_constraints_off()


# In[14]:


print(phoebe.conf.interactive_constraints)


# In[15]:


print(b.filter('mass', component='primary'))


# In[16]:


b.set_value('sma@binary', 15)


# In[17]:


print(b.filter('mass', component='primary'))


# No need to worry though - all constraints will be run automatically before passing to the backend.  If you need to access the value of a constrained parameter, you can explicitly ask for all delayed constraints to be executed via [b.run_delayed_constraints()](../api/phoebe.frontend.bundle.Bundle.run_delayed_constraints).

# In[18]:


b.run_delayed_constraints()


# In[19]:


print(b.filter('mass', component='primary'))


# In[20]:


phoebe.reset_settings()


# Filtering Options
# -------------------------
# 
# ### check_visible
# 
# By default, everytime you call filter or set_value, PHOEBE checks to see if the current value is visible (meaning it is relevant given the value of other parameters).  Although not terribly expensive, these checks can add up... so disabling these checks can save time.  Note that these are automatically *temporarily* disabled during [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md).  If disabling these checks, be aware that changing the value of some parameters may have no affect on the resulting computations.  You can always manually check the visibility/relevance of a parameter by calling [parameter.is_visible](../api/phoebe.parameters.Parameter.is_visible.md).
# 
# This default behavior can be changed via [phoebe.check_visible_on()](../api/phoebe.check_visible_on.md) or [phoebe.check_visible_off()](../api/phoebe.check_visible_off.md).
# 
# Let's first look at the default behavior with check_visible on.

# In[21]:


b.add_dataset('lc')


# In[22]:


print(b.get_dataset())


# Now if we disable check_visible, we'll see the same thing as if we passed `check_visible=False` to any filter call.

# In[23]:


phoebe.check_visible_off()


# In[24]:


print(b.get_dataset())


# Now the same filter is returning additional parameters.  For example, `ld_coeffs_source` parameters were initially hidden because `ld_mode` is set to 'interp'.  We can see the rules that are being followed:

# In[25]:


print(b.get_parameter(qualifier='ld_coeffs_source', component='primary').visible_if)


# and can still manually check to see that it shouldn't be visible (isn't currently relevant given the value of `ld_func`):

# In[26]:


print(b.get_parameter(qualifier='ld_coeffs_source', component='primary').is_visible)


# In[27]:


phoebe.reset_settings()


# ### check_default
# 
# Similarly, PHOEBE automatically excludes any parameter which is tagged with a '\_default' tag.  These parameters exist to provide default values when a new component or dataset are added to the bundle, but can usually be ignored, and so are excluded from any filter calls.  Although not at all expensive, this too can be disabled at the settings level or by passing `check_default=False` to any filter call.  
# 
# This default behavior can be changed via [phoebe.check_default_on()](../api/phoebe.check_default_on.md) or [phoebe.check_default_off()](../api/phoebe.check_default_off.md).

# In[28]:


print(b.get_dataset())


# In[29]:


print(b.get_dataset(check_default=False))


# In[30]:


phoebe.check_default_off()


# In[31]:


print(b.get_dataset())


# In[32]:


phoebe.reset_settings()


# Passband Options
# ----------------------------
# 
# PHOEBE automatically fetches necessary tables from [tables.phoebe-project.org](http://tables.phoebe-project.org).  By default, only the necessary tables for each passband are fetched (except when calling [download_passband](../api/phoebe.download_passband.md) manually) and the fits files are fetched uncompressed.
# 
# 
# For more details, see the API docs on [download_passband](../api/phoebe.download_passband.md) and [update_passband](../api/phoebe.update_passband.md) as well as the [passband updating tutorial](./passband_updates.ipynb).
# 
# The default values mentioned in the API docs for `content` and `gzipped` can be exposed via [phoebe.get_download_passband_defaults](../api/phoebe.get_download_passband_defaults.md) and changed via [phoebe.set_download_passband_defaults](../api/phoebe.set_download_passband_defaults.md).  Note that setting `gzipped` to True will minimize file storage for the passband files and will result in faster download speeds, but take significantly longer to load by PHOEBE as they have to be uncompressed each time they are loaded.  If you have a large number of installed passbands, this could significantly slow importing PHOEBE.

# In[34]:


phoebe.get_download_passband_defaults()


# ## Environment Variables

# Some settings cannot be changed after importing PHOEBE, so they are available via environment variables.  These can be set in a variety of ways:
# 
# Setting inline before calling python will set for that single session of PHOEBE:
# ```
# PHOEBE_ENABLE_PLOTTING=FALSE python [script.py]
# ```
# 
# Setting via the os package in python **before** importing PHOEBE allows you to set the setting everytime you run a given script:
# ```py
# import os
# os.environ['PHOEBE_ENABLE_PLOTTING'] = 'FALSE'
# import phoebe
# ```
# 
# Note for all boolean settings, the string is converted to uppercase and compared to 'TRUE'.

# ### PHOEBE_ENABLE_PLOTTING
# 
# PHOEBE_ENABLE_PLOTTING (TRUE by default) allows for disabling plotting within PHOEBE and therefore skipping the import of all plotting libraries (which take up a significant amount of the time it takes to import phoebe).

# ### PHOEBE_ENABLE_ONLINE_PASSBANDS
# 
# PHOEBE_ENABLE_ONLINE_PASSBANDS (TRUE by default) dictates whether online passbands are queried and available for on-the-fly downloading.  If you are sure you have all the local passbands you need, set this to False to save some time.

# ### PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_CONTENT
# 
# PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_CONTENT ('all' by default, use comma separate for a list: 'ck2004,phoenix') allows setting the value for `content` in [phoebe.set_download_passband_defaults](../api/phoebe.set_download_passband_defaults.md).  For more details, see the section above.

# ### PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_GZIPPED
# 
# PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_GZIPPED (FALSE by default) allows setting the value for `gzipped` in [phoebe.set_download_passband_defaults](../api/phoebe.set_download_passband_defaults.md).  For more details, see the section above.

# In[ ]:




