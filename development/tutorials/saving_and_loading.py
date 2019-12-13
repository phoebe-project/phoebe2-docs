#!/usr/bin/env python
# coding: utf-8

# Saving and Loading
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# Saving a Bundle
# -----------------------
# 
# 

# In[2]:


b['incl@orbit'] = 56.789


# To save the Bundle to a file, we can call the [save](../api/phoebe.parameters.ParameterSet.save.md) method of the Bundle and pass a filename.

# In[3]:


print(b.save('test.phoebe'))


# We can now inspect the contents of the created file.
# 
# This file is in the JSON-format and is simply a list of dictionaries - where each dictionary represents the attributes of a single Parameter.
# 
# You could edit this file in a text-editor - but do be careful if changing any of the tags.  For example: if you want to change the component tag of one of your stars, make sure to change ALL instances of the component tag to match (as well as the hierarchy Parameter).

# In[4]:


get_ipython().system('head -n 30 test.phoebe')


# Loading a Bundle
# ----------------------

# To open an existing Bundle from the file we just created, call [Bundle.open](../api/phoebe.frontend.bundle.Bundle.open.md) and pass the filename.

# In[5]:


b2 = phoebe.Bundle.open('test.phoebe')


# Just to prove this worked, we can check to make sure we retained the changed value of inclination.

# In[6]:


print(b2.get_value('incl@orbit'))


# Support for Other Codes
# ------------------------------
# 
# ### Legacy
# 
# Importing from a PHOEBE Legacy file is as simple as passing the filename to [from_legacy](../api/phoebe.frontend.bundle.Bundle.from_legacy.md):

# In[7]:


b = phoebe.Bundle.from_legacy('legacy.phoebe')


# Exporting to a PHOEBE Legacy file is also possible (although note that some parameters don't translate exactly or are not supported in PHOEBE Legacy), via [b.export_legacy](../api/phoebe.frontend.bundle.Bundle.export_legacy.md).

# In[8]:


b.export_legacy('legacy_export.phoebe')


# For the parameters that could not be directly translated, you should see a warning message (if you have warning messages enabled in your logger).
# 
# We can now look at the beginning of the saved file and see that it matches the PHOEBE Legacy file-format.

# In[9]:


get_ipython().system('head -n 30 legacy_export.phoebe')


# Next
# ---------
# 
# Next up: let's learn all about [constraints](constraints.ipynb)
