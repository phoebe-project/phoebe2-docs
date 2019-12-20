#!/usr/bin/env python
# coding: utf-8

# Atmospheres & Passbands
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll add a single light curve dataset to expose all the passband-dependent options.

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')


# Relevant Parameters
# -----------------------
# 
# An 'atm' parameter exists for each of the components in the system (for each set of compute options) and defines which atmosphere table should be used.
# 
# By default, these are set to 'ck2004' (Castelli-Kurucz) but can be set to 'blackbody' as well as 'extern_atmx' and 'extern_planckint' (which are included primarily for direct comparison with PHOEBE legacy).

# In[4]:


b['atm']


# In[5]:


b['atm@primary']


# In[6]:


b['atm@primary'].description


# In[7]:


b['atm@primary'].choices


# Note that if you change the value of 'atm' to anything other than 'ck2004', the corresponding 'ld_func' will need to be changed to something other than 'interp' (warnings and errors will be raised to remind you of this).

# In[8]:


b['ld_func@primary']


# In[9]:


b['atm@primary'] = 'blackbody'


# In[10]:


print(b.run_checks())


# In[12]:


b['ld_mode@primary'] = 'manual'
b['ld_func@primary'] = 'logarithmic'


# In[13]:


print(b.run_checks())


# A 'passband' parameter exists for each passband-dependent-dataset (i.e. not meshes or orbits, but light curves and radial velocities).  This parameter dictates which passband should be used for the computation of all intensities.

# In[14]:


b['passband']


# The available choices will include both locally installed passbands as well as passbands currently available from the online PHOEBE repository.  If you choose an online-passband, it will be downloaded and installed locally as soon as required by [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md).

# In[15]:


print(b['passband'].choices)


# To see your current locally-installed passbands, call [phoebe.list_installed_passbands()](../api/phoebe.list_installed_passbands.md).

# In[16]:


print(phoebe.list_installed_passbands())


# These installed passbands can be in any of a number of directories, which can be accessed via [phoebe.list_passband_directories()](../api/phoebe.list_passband_directories.md).
# 
# The first entry is the global location - this is where passbands can be stored by a server-admin to be available to all PHOEBE-users on that machine.
# 
# The second entry is the local location - this is where individual users can store passbands and where PHOEBE will download and install passbands (by default).

# In[17]:


print(phoebe.list_passband_directories())


# To see the passbands available from the [online repository](http://github.com/phoebe-project/phoebe2-tables), call [phoebe.list_online_passbands()](../api/phoebe.list_online_passbands.md).

# In[18]:


print(phoebe.list_online_passbands())


# Lastly, to manually download and install one of these online passbands, you can do so explicitly via [phoebe.download_passband](../api/phoebe.download_passband.md) or by visiting [tables.phoebe-project.org](http://phoebe-project.org/tables).  See also the tutorial on [updating passbands](./passband_updates.ipynb).
# 
# Note that this isn't necessary unless you want to explicitly download passbands before needed by run_compute (perhaps if you're expecting to have unreliable network connection in the future and want to ensure you have all needed passbands).

# In[20]:


phoebe.download_passband('Cousins:Rc')


# In[21]:


print(phoebe.list_installed_passbands())


# In[ ]:




