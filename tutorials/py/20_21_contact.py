#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: Contact Systems
# ============================

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# In PHOEBE 2.1, [rpole and potential have been replaced with requiv](20_21_requiv).  That means that the constraint used to handle semidetached systems has also changed.

# In[1]:


import phoebe
b = phoebe.default_binary(contact_binary=True)


# ### requiv_max and requiv_min

# In PHOEBE 2.1, there is a new constrained Parameter for contact systems which tell the maximum value allowed for requiv before overflow occurs.

# In[4]:


print b['requiv_max@constraint']


# Similarly, there is another constrained Parameter that defines the minimum allowed value for requiv before the system would no longer be in contact.

# In[3]:


print b['requiv_min@constraint']


# ### requiv, pot, and fillout_factor

# Note that requiv and requiv_min exist for both the primary and secondary components.  If we look at requiv, we'll see that that is also defined for both components, with another constraint dictating that the secondary requiv must correspond to the same potential of the contact envelope.

# In[5]:


print b['requiv']


# The value of that potential as well as the corresponding fillout_factor is also exposed (and attached to the envelope object).  In PHOEBE 2.0, pot was the input Parameter for contacts, but is now constrained with requiv of the primary star the free parameter, by default.

# In[8]:


print b['pot']


# In[9]:


print b['fillout_factor']


# If desired, you can flip these constraints to allow any one of the three to be free (and the other two constrained).  For more information see the [critical radii: contact systems tutorial](./requiv_crit_contact.ipynb).
