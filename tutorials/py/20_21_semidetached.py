#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: Semidetached
# ============================

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# In PHOEBE 2.1, [rpole and potential have been replaced with requiv](20_21_requiv).  That means that the constraint used to handle semidetached systems has also changed.

# In[1]:


import phoebe
b = phoebe.default_binary()


# ### requiv_max

# In PHOEBE 2.1, there is a new constrained Parameter that allows access to the critical value of requiv at which overflow would occur (for a detached system - contact systems have requiv_min and requiv_max).

# In[3]:


print b['requiv_max@primary@constraint']


# In order to create a semidetached system, you create a constraint as in PHOEBE 2.0, except instead of choosing 'critical_rpole' or 'critical_pot' constraints, use a new constraint called 'semidetached'.

# In[4]:


b.add_constraint('semidetached', 'primary')


# In[6]:


print b['requiv@primary@constraint']

