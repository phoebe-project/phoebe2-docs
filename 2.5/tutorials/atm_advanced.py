#!/usr/bin/env python
# coding: utf-8

# Adavanced: Model Atmospheres
# ============================
# 
# Setup
# -----------------------------

# ##### Let's first make sure we have the latest version of PHOEBE 2.5 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.5"


# As of v2.5, model atmospheres in PHOEBE are handled by a new ModelAtmosphere class which provides a framework both for handling model spectra when creating (or updating) PHOEBE passband files, as well as registering the parameters covered by the model atmosphere (such as effective temperature and surface gravity) that are referred to as 'basic_axes'

# Let's load the models and see which are currently incorporated

# In[2]:


import phoebe
from phoebe.atmospheres import models
import matplotlib.pyplot as plt

models._atmtable


# This tells us that, for example, the PHOEBE default atmosphere 'ck2004' corresponds to the 'CK2004ModelAtmosphere' class
# 
# Now let's look more closely at the properties of the 'CK2004ModelAtmosphere' class

# In[3]:


dir(models.CK2004ModelAtmosphere)


# The two most interesting of these are (probably) 'basic_axis_names' and 'mus'
# 
# 'basic_axis_names' defines the parameter axes that span the model atmosphere grid.

# In[4]:


models.CK2004ModelAtmosphere.basic_axis_names


# In[5]:


models.TMAPsdOModelAtmosphere.basic_axis_names


# As seen above, these can be different for different atmospheres which require different parameterisations.  Here, the 'ck2004' grid spans a range of effective temperatures ('teffs'), surface gravities ('loggs') and metallicities ('abuns'), while 'tmap_sdO' covers effective temperatures, surface gravities and the logarithmic He/H fraction by mass ('loghefrac').
# 
# Model atmosphere grids can, in principle, span any number of basic axes but effective temperature could be considered a bare minimum.

# In[6]:


models.BlackbodyModelAtmosphere.basic_axis_names


# 'mus' contains the hard-coded range of angles (where mu=cos(theta)) across the stellar limb for which model spectra are available.  These are essentially the anchor points at which the limb-darkening of the model atmosphere is measured.  These again vary from atmosphere to atmosphere, and may sometimes be useful when attempting to understand the fidelity of model atmosphere limb-darkening for a given use case.

# In[7]:


models.CK2004ModelAtmosphere.mus


# In[8]:


models.TMAPsdOModelAtmosphere.mus


# Atmosphere models that do not contain limb-darkening information ('blackbody', for example), will not have the 'mus' attribute and thus require the 'ld_func' to be set to something other than 'interp' as described in the [Atmospheres & Passbands](./atm_passbands.ipynb) tutorial.

# In[9]:


models.BlackbodyModelAtmosphere.mus


# Returning to the basic axes, in order to access the actual values that the grid spans, we will need to load a passband file.

# In[10]:


pb=phoebe.get_passband("Johnson:V")


# The ndpolator then allows us to see the various tables contained within the passband, where N tells us the number of basic axes.

# In[11]:


pb.ndp


# We can then access the grid points of the basic axes via the 'axes' property of a given model atmosphere

# In[12]:


pb.ndp['ck2004'].axes


# This shows that the default 'ck2004' grid spans 3500 to 50000 K in effective temperature ('teffs'), 0.0 to 5.0 in surface gravity ('loggs') and -2.5 to 0.5 in metallicity ('abuns').

# Now let's iteratively access the model atmosphere axes to make a Kiel diagram (effective temperature versus surface gravity) showing the coverage of the various atmosphere models.

# In[13]:


cmap = plt.get_cmap('tab20', len(models._atmtable))

atmindex=0
for atmosphere in models._atmtable:
    if set(['teffs', 'loggs']).issubset(models._atmtable[atmosphere].basic_axis_names) and 'extern' not in atmosphere:
        atmteffs=pb.ndp[atmosphere].axes[models._atmtable[atmosphere].basic_axis_names.index('teffs')]
        atmloggs=pb.ndp[atmosphere].axes[models._atmtable[atmosphere].basic_axis_names.index('loggs')]
        for i in range(0,len(atmteffs)):
            if i==0:
                plt.scatter([atmteffs[i]] * len(atmloggs), atmloggs, label=atmosphere, color=cmap(atmindex))
            else:
                plt.scatter([atmteffs[i]] * len(atmloggs), atmloggs, color=cmap(atmindex))
        atmindex+=1
        plt.legend()
        plt.xlabel('Teff')
        plt.ylabel('Logg')
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()



# In[ ]:




