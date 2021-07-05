#!/usr/bin/env python
# coding: utf-8

# Advanced: Building a System
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.Bundle()


# Default Systems
# ------------------------
# 
# Although the default empty Bundle doesn't include a system, there are available
# constructors that create default systems.  To create a simple binary with component tags
# 'binary', 'primary', and 'secondary' (as above), you could call [default_binary](../api/phoebe.frontend.bundle.Bundle.default_binary.md):

# In[3]:


b = phoebe.Bundle.default_binary()


# or for short:

# In[4]:


b = phoebe.default_binary()


# In[5]:


print(b.hierarchy)


# To build the same binary but as a contact system, you would call:

# In[6]:


b = phoebe.default_binary(contact_binary=True)


# In[7]:


print(b.hierarchy)


# For more details on dealing with contact binary systems, see the [Contact Binary Hierarchy Tutorial](contact_binary_hierarchy.ipynb) and the [Contact Binary Example Script](../examples/minimal_contact_binary.ipynb).

# Adding Components Manually
# --------------------
# 
# **IMPORTANT**: in the vast majority of cases, starting with one of the default systems is sufficient.  Below we will discuss the alternative method of building a system from scratch.
# 
# By default, an empty [Bundle](../api/phoebe.frontend.bundle.Bundle.md) does not contain any information about our system.
# 
# So, let's first start by adding a few stars.  Here we'll call the generic [add_component](../api/phoebe.frontend.bundle.Bundle.add_component.md) method.  This method works for any type of component in the system - stars, orbits, planets, disks, rings, spots, etc.  The first argument needs to be a callable or the name of a callable in [phoebe.parameters.component](../api/phoebe.parameters.component.md) which include the following options:
# 
# * orbit
# * star
# * envelope
# 
# add_component also takes a keyword argument for the 'component' tag.  Here we'll give them component tags 'primary' and 'secondary' - but note that these are merely convenience labels and do not hold any special roles.  Some tags, however, are forbidden if they clash with other tags or reserved values - so if you get error stating the component tag is forbidden, try using a different string.

# In[8]:


b = phoebe.Bundle()


# In[9]:


b.add_component(phoebe.component.star, component='primary')
b.add_component('star', component='secondary')


# But there are also shortcut methods for [add_star](../api/phoebe.frontend.bundle.Bundle.add_star.md) and [add_orbit](../api/phoebe.frontend.bundle.Bundle.add_orbit.md).  In these cases you don't need to provide the function, but only the component tag of your star/orbit.
# 
# Any of these functions also accept values for any of the qualifiers of the created parameters.

# In[10]:


b.add_star('extrastarforfun', teff=6000)


# Here we call the add_component method of the bundle with several arguments:
# 
# * a function (or the name of a function) in phoebe.parameters.component.  This 
#   function tells the bundle what parameters need to be added.
# * component: the tag that we want to give this component for future reference.
# * any additional keyword arguments: you can also provide initial values for Parameters 
#   that you know will be created.  In the last example you can see that the
#   effective temperature will already be set to 6000 (in default units which is K).
# 
# and then we'll do the same to add an orbit:

# In[11]:


b.add_orbit('binary')


# ## Defining the Hierarchy
# 
# 
# At this point all we've done is add a bunch of Parameters to our Bundle, but 
# we still need to specify the hierarchical setup of our system.
# 
# Here we want to place our two stars (with component tags 'primary' and 'secondary') in our
# orbit (with component tag 'binary').  This can be done with several different syntaxes sent to [b.set_hierarchy](../api/phoebe.frontend.bundle.Bundle.set_hierarchy.md):

# In[12]:


b.set_hierarchy(phoebe.hierarchy.binaryorbit, b['binary'], b['primary'], b['secondary'])


# or

# In[13]:


b.set_hierarchy(phoebe.hierarchy.binaryorbit(b['binary'], b['primary'], b['secondary']))


# If you access the value that this set via [get_hierarchy](../api/phoebe.frontend.bundle.Bundle.get_hierarchy.md), you'll see that it really just resulted
# in a simple string representation:

# In[14]:


b.get_hierarchy()


# We could just as easily have used this string to set the hierarchy:

# In[15]:


b.set_hierarchy('orbit:binary(star:primary, star:secondary)')


# If at any point we want to flip the primary and secondary components or make
# this binary a triple, its seriously as easy as changing this hierarchy and
# everything else will adjust as needed (including cross-ParameterSet constraints, 
# and datasets)

# The Hierarchy Parameter
# -----------------------------
# 
# Setting the hierarchy just sets the value of a single parameter (although it may take some time because it also does a lot of paperwork and manages constraints between components in the system).  You can access that parameter as usual:

# In[16]:


b['hierarchy@system']


# or through any of these shortcuts:

# In[17]:


b.get_hierarchy()


# In[18]:


b.hierarchy


# This [HierarchyParameter](../api/phoebe.parameters.HierarchyParameter.md) then has several methods unique to itself.  You can, for instance, list the component tags of all the stars or orbits in the hierarchy via [get_stars](../api/phoebe.parameters.HierarchyParameter.get_stars.md) or [get_orbits](../api/phoebe.parameters.HierarchyParameter.get_orbits.md), respectively:

# In[19]:


print(b.hierarchy.get_stars())


# In[20]:


print(b.hierarchy.get_orbits())


# Or you can ask for the component tag of the top-level item in the hierarchy via [get_top](../api/phoebe.parameters.HierarchyParameter.get_top.md).

# In[21]:


print(b.hierarchy.get_top())


# And request the parent, children, child, or sibling of any item in the hierarchy via [get_parent_of](../api/phoebe.parameters.HierarchyParameter.get_parent_of.md), [get_children_of](../api/phoebe.parameters.HierarchyParameter.get_children_of.md), or [get_sibling_of](../api/phoebe.parameters.HierarchyParameter.get_sibling_of.md).

# In[22]:


print(b.hierarchy.get_parent_of('primary'))


# In[23]:


print(b.hierarchy.get_children_of('binary'))


# In[24]:


print(b.hierarchy.get_child_of('binary', 0))  # here 0 means primary component, 1 means secondary


# In[25]:


print(b.hierarchy.get_sibling_of('primary'))


# We can also check whether a given component (by component tag) is the primary or secondary component in its parent orbit via [get_primary_or_secondary](../api/phoebe.parameters.HierarchyParameter.get_primary_or_secondary.md).  Note that here its just a coincidence (although on purpose) that the component tag is also 'secondary'.

# In[26]:


print(b.hierarchy.get_primary_or_secondary('secondary'))

