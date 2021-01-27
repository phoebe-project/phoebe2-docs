#!/usr/bin/env python
# coding: utf-8

# # Advanced: Custom Constraints
# 
# **NOTE**: support for custom constraints was fixed in PHOEBE 2.3.18.  This notebook will fail to run on earlier versions.
# 
# [Built-in Constraints](./constraints_builtin.ipynb) are convenient as they automatically determine the correct expression and include support for multiple parameterizations via [b.flip_constraint](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).  However, for cases where a built-in constraint does not exist, PHOEBE provides a framework for easily creating your own expression to link multiple parameters via [b.add_constraint](../api/phoebe.frontend.bundle.Bundle.add_constraint.md).

# In[1]:


import phoebe

b = phoebe.default_binary()


# In this case, the two positional arguments to [b.add_constraint](../api/phoebe.frontend.bundle.Bundle.add_constraint.md) must be the left-hand side of the expression (which will become the constrained parameter) and the right-hand side of the expression (either another parameter or a [ConstraintParameter](../api/phoebe.parameters.ConstraintParameter.md)).
# 
# The easiest way to create a constraint parameter is via math operations on existing parameters.  For example, let's say we wanted the secondary temperature to always be half the primary temperature:

# In[4]:


print(b.filter(qualifier='teff'))


# In[5]:


lhs = b.get_parameter(qualifier='teff', component='secondary')
rhs = 0.5 * b.get_parameter(qualifier='teff', component='primary')


# In[8]:


rhs


# In[9]:


b.add_constraint(lhs, rhs)


# In[10]:


print(b.filter(qualifier='teff'))


# Now, as with any other constraint, if we change the value of a parameter in the constraint, the constrained value will automatically adjust.

# In[11]:


b.set_value(qualifier='teff', component='primary', value=7000)


# In[12]:


print(b.filter(qualifier='teff'))

