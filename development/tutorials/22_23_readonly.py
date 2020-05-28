#!/usr/bin/env python
# coding: utf-8

# 2.2 - 2.3 Migration: Read Only and Constrained Notation
# ============================
# 
# In the string representation of a [ParameterSet](../api/phoebe.parameters.ParameterSet.md), constrained parameters were notated with a `\*` symbol in the far left.  
# 
# In version 2.3, this is replaced with a `C`.  Parameters that are read-only for other reasons (i.e. exposed model parameters) are noted with an `R`.

# In[1]:


import phoebe


# In[2]:


b = phoebe.default_binary()


# In[3]:


print(b.filter(qualifier=['sma', 'incl', 'asini']))

