#!/usr/bin/env python
# coding: utf-8

# Advanced: passband versioning & updates
# ==============================

# As of the 2.2 release, PHOEBE allows you to check for online updates to local install passbands.  If we add a new atmosphere table or feature (extinction as in this release, for example) to a passband table, you can now update directly from the python interface of PHOEBE.
# 
# If you try using extinction in a version of a table that does not support extinction, an error will be raised (either during [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) or you can check by calling [run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md) manually) with instructions on how to update the passband.
# 
# If you'd like to manually check for updates, you can use [phoebe.list_all_update_passbands_available](../api/list_all_update_passbands_available.md) or [phoebe.update_passband_available](../api/update_passband_available.md).

# In[1]:


import phoebe

print(phoebe.list_installed_passbands())


# In[2]:


print(phoebe.list_all_update_passbands_available())


# In[3]:


print(phoebe.update_passband_available('Johnson:V'))


# If there are updates available that you'd like to apply, you can apply them all via [phoebe.update_all_passbands](../api/update_all_passbands.md)

# In[4]:


phoebe.update_all_passbands()


# To update a single passband to the latest online version, call [phoebe.download_passband](../api/phoebe.download_passband.md)

# In[5]:


phoebe.download_passband('Johnson:V')


# In[ ]:




