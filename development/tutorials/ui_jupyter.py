#!/usr/bin/env python
# coding: utf-8

# Advanced: Interacting with the UI in Jupyter
# ============================
# 
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# ## Showing the Jupyter in-line UI
# 
# Whether you have the [UI Client](http://phoebe-project.org/clients) installed locally or not, calling [b.ui or PS.ui](../api/phoebe.parameters.ParameterSet.ui.md) will launch an inline-representation of that ParameterSet directly below the cell by default.  This allows you to interactively view and change parameter values without having to write code.
# 
# This can be super useful to create "interactive" scripts where you (or a student, etc) can change specific values at certain points throughout the script.  But do keep in mind that any values you change in the UI will not be reproduced when re-running the notebook (unless you manually do the exact same thing).
# 
# By default this is "blocking", which means that Jupyter will not continue to the next line until you click the blue "continue" button.  Once clicked, the UI will become "frozen" (and will show a "disconnected" note in the corner in place of the "continue" button) and Jupyter will continue to allow further entry and execution.
# 
# **NOTE**: The following lines are commented-out to avoid the error messages when viewing the notebook in read-only mode.  Below each commented line are a screenshot of the resulting UI.  To see the interactive versions, run this notebook locally and uncomment the calls to ui.

# In[3]:


#b.ui()


# ![ui](ui_jupyter_b_ui.png)

# In[4]:


#b.filter(qualifier='sma', context='component').ui()


# ![ui](ui_jupyter_b_filter_ui.png)

# Additionally, if you have figures attached to the Bundle (see [settings](settings.ipynb) for `auto_add_figure` and `auto_remove_figure` or [b.add_figure](../api/phoebe.frontend.bundle.Bundle.add_figure.md)), calling [b.ui_figures](../api/phoebe.frontend.bundle.Bundle.ui_figures.md) will launch the UI panel showing the figures.

# ## Launching the UI outside Jupyter
# 
# Calling [PS.ui](../api/phoebe.parameters.ParameterSet.ui.md) or [b.ui_figures](../api/phoebe.frontend.bundle.Bundle.ui_figures.md) from a Python or IPython instance will launch the desktop client (if installed) or the web-client in a browser.
# 
# This is still "blocking" by default, but by passing `blocking=False` to the UI call, you can interact with the bundle through the UI and Python simultaneously.  Similarly, you could have started in the UI and clicked the terminal button in the upper-right corner to launch a Python client.
# 
# Calling [b.ui_figures](../api/phoebe.frontend.bundle.Bundle.ui_figures.md) with `blocking=False` can be convenient to see the figures automatically update whenever there are changes to the datasets or models (for example, whenever calling [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md).

# In[ ]:





# In[ ]:




