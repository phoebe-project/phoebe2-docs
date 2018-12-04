#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: Meshes
# ============================

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# In this tutorial we will review the changes in the PHOEBE mesh structures. We will first explain the changes and then demonstrate them in code. As usual, let us import phoebe and create a default binary bundle:

# In[1]:


import phoebe
b = phoebe.default_binary()


# PHOEBE 2.0 had a mesh dataset along with `pbmesh` and `protomesh` options you could send to `b.run_compute()`.  These options were quite convenient, but had a few inherit problems:
# 
# * The protomesh was exposed at only t0 and was in Roche coordinates, despite using the same qualifiers 'x', 'y', 'z'.
# * Passband-dependent parameters were exposed in the mesh if `pbmesh=True`, but only if the times matched exactly with the passband (lc, rv, etc) dataset.
# * Storing more than a few meshes become very memory intensive due to their large size and the large number of columns.
# 
# Addressing these shortcomings required a complete redesign of the mesh dataset.  The most important changes are:
# 
# * `pbmesh` and `protomesh` are no longer valid options to `b.run_compute()`.  Everything is done through the mesh dataset itself, i.e. `b.add_dataset('mesh')`.
# * The default columns that are computed for each mesh include the elements in both Roche and plane-of-sky coordinate systems. These columns cannot be disabled.
# * The `columns` parameter in the mesh dataset lists additional columns to be exposed in the model mesh when calling `b.run_compute()`.  See the section on columns below for more details.
# * You can choose whether to expose coordinates in the Roche coordinate system ('xs', 'ys', 'zs') or the plane-of-sky coordinate system ('us', 'vs', 'ws').
# * When plotting, the default is the plane-of-sky coordinate system, and the axes will be correctly labeled as uvw, whereas in PHOEBE 2.0.x these were still labeled xyz. Note that this also applies to velocities ('vxs', 'vys', 'vzs' vs 'vus', 'vvs', 'vws').
# * The `include_times` parameter allows for importing timestamps from other datasets. It also provides support for important orbital times: 't0' (zero-point), 't0_perpass' (periastron passage), 't0_supconj' (superior conjunction) and 't0_ref' (zero-phase reference point).
# * By default, the `times` parameter is empty. If you do not set `times` or `include_times` before calling `b.run_compute()`, your model will be empty.

# ### The 'columns' parameter
# 
# This parameter is a SelectParameter (a new type of Parameter introduced in PHOEBE 2.1). Its value is one of the values in a list of allowed options. You can list the options by calling `param.get_choices()` (same as you would for a ChoiceParameter). The value also accepts wildcards, as long as the expression matches at least one of the choices. This allows you to easily select, say, `rvs` from all datasets, by passing `rvs@*`. To see the full list of matched options, use `param.expand_value()`.
# 
# To demonstrate, let us add a few datasets and look at the available choices for the `columns` parameter.

# In[2]:


b.add_dataset('mesh')
print b.get_parameter('columns').get_choices()


# In[3]:


b.add_dataset('lc')
print b.get_parameter('columns').get_choices()


# In[4]:


b['columns'] = ['*@lc01', 'teffs']
b.get_parameter('columns').get_value()


# In[5]:


b.get_parameter('columns').expand_value()


# ### The 'include_times' parameter
# 
# Similarly, the `include_times` parameter is a SelectParameter, with the choices being the existing datasets, as well as the t0s mentioned above.

# In[6]:


print b.get_parameter('include_times').get_value()


# In[7]:


print b.get_parameter('include_times').get_choices()


# In[8]:


b['include_times'] = ['lc01', 't0@system']


# In[9]:


print b.get_parameter('include_times').get_value()

