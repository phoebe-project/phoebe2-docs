#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: xyz vs uvw coordinates
# ============================

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.1,<2.2"')


# In this tutorial we will review the changes in the coordinate conventions used for plane-of-sky vs Roche coordinates, which applies to both orbit and mesh datasets.

# In[1]:


import phoebe
b = phoebe.default_binary()


# In[2]:


b.add_dataset('orb', times=[0])
b.add_dataset('mesh', times=[0])


# In[3]:


b.run_compute()


# In PHOEBE 2.0, the orbit dataset had qualifiers x, y, z, vxs, vys, vzs which corresponded to the plane-of-sky coordinates (with z along the line-of-sight).  In PHOEBE 2.1, these plane-of-sky coordinates are now denoted by u, v, w - with w along the line-of-sight and with the corresponding velocities: vus, vvs, vws.

# In[4]:


print b.filter(context='model', kind='orb').qualifiers


# In PHOEBE 2.0, the protomesh was exposed with x, y, z signifying roche coordinates, but the mesh dataset or pbmesh with x, y, z signifying plane-of-sky coordinates.  Now in PHOEBE 2.1, this distinction is gone, with 'xyz' always signifying Roche coordinates and 'uvw' always plane-of-sky.  Note that the concept of the protomesh and pbmesh have also been removed and [replaced with a more flexible mesh dataset](./20_21_meshes.ipynb).

# In[5]:


print b.filter(context='model', kind='mesh').qualifiers

