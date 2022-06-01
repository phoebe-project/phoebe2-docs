#!/usr/bin/env python
# coding: utf-8

# # Misaligned Rossiter-McLaughlin: phoebe and ellc
# 
# Setup
# --------------------
# 
# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# In[2]:


import phoebe

b = phoebe.default_binary()


# In[3]:


b.add_dataset('rv', compute_phases=phoebe.linspace(0,1,101))


# In[4]:


b.set_value_all('ld_mode', 'lookup')


# **NOTE**: ellc only supports flux-weighted RVs (needed to see Rossiter-McLaughlin) when irradiation is disabled and only supports misalgnment with spherical stars.  If these conditions aren't met, an error will be raised by [b.run_check_compute](../api/phoebe.frontend.bundle.Bundle.run_checks_compute.md) when trying to call [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md)

# In[5]:


b.add_compute('ellc', 
              rv_method='flux-weighted', 
              irrad_method='none',
              distortion_method='sphere')


# In[6]:


b.run_compute(kind='phoebe', irrad_method='none', model='phoebe2_aligned')


# In[7]:


b.run_compute(kind='ellc', model='ellc_aligned')


# In[8]:


print(b['ellc@compute'])


# In[9]:


_ = b.plot(context='model', show=True)


# In[10]:


b.set_value('yaw', component='primary', value=30)
b.set_value('yaw', component='secondary', value=50)


# In[11]:


b.run_compute(kind='phoebe', irrad_method='none', model='phoebe2_misaligned')


# In[12]:


b.run_compute(kind='ellc', model='ellc_misaligned', distortion_method='sphere')


# In[13]:


_ = b.plot(context='model', model=['phoebe2_aligned', 'phoebe2_misaligned'], show=True)


# In[14]:


_ = b.plot(context='model', model=['phoebe2_misaligned', 'ellc_misaligned'], show=True)


# In[ ]:




