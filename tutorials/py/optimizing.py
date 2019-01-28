#!/usr/bin/env python
# coding: utf-8

# Advanced: Optimizing Performance with PHOEBE
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


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


passed, msg = b.run_checks()
print(passed, msg)


# In[7]:


b.set_value('requiv', component='primary', value=50)


# In[8]:


passed, msg = b.run_checks()
print(passed, msg)


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
