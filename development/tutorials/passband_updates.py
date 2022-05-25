#!/usr/bin/env python
# coding: utf-8

# Advanced: passband versioning & updates
# ==============================

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# PHOEBE allows you to check for online updates to local install passbands.  If we add a new atmosphere table or feature (extinction as in this release, for example) to a passband table, you can now update directly from the python interface of PHOEBE.
# 
# If you try using extinction in a version of a table that does not support extinction, for example, an error will be raised (either during [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) or you can check by calling [run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md) manually).  If extinction tables are available in the online version of the passband (from [tables.phoebe-project.org](http://phoebe-project.org/tables)), then the local installed version will automatically be updated if the timestamps on the passbands match, otherwise a message will be raised with instructions to manually call [phoebe.update_passband](../api/update_passband.md).
# 
# If you'd like to manually check for updates, you can use [phoebe.list_all_update_passbands_available](../api/list_all_update_passbands_available.md) or [phoebe.update_passband_available](../api/update_passband_available.md).

# In[2]:


import phoebe

print(phoebe.list_installed_passbands())


# In[3]:


print(phoebe.list_all_update_passbands_available())


# In[4]:


print(phoebe.update_passband_available('Johnson:V'))


# If there are updates available that you'd like to apply, you can apply them all via [phoebe.update_all_passbands](../api/update_all_passbands.md)

# In[5]:


phoebe.update_all_passbands()


# To update a single passband to the latest online version with the same contents as the locally installed version (or with new tables, see the `content` argument), call [phoebe.update_passband](../api/phoebe.update_passband.md).  

# In[6]:


phoebe.update_passband('Johnson:V')


# In[ ]:




