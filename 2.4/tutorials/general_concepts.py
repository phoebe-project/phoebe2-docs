#!/usr/bin/env python
# coding: utf-8

# General Concepts: The PHOEBE Bundle
# ======================
# 
# **HOW TO RUN THIS FILE**: if you're running this in a Jupyter notebook or Google Colab session, you can click on a cell and then shift+Enter to run the cell and automatically select the next cell.  Alt+Enter will run a cell and create a new cell below it.  Ctrl+Enter will run a cell but keep it selected.  To restart from scratch, restart the kernel/runtime.
# 
# 
# All of these tutorials assume basic comfort with Python in general - particularly with the concepts of lists, dictionaries, and objects as well as basic comfort with using the numpy and matplotlib packages. This tutorial introduces all the general concepts of accessing parameters within the Bundle.
# 
# Setup
# ----------------------------------------------
# 

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# Let's get started with some basic imports:

# In[2]:


import phoebe
from phoebe import u # units


# If running in IPython notebooks, you may see a "ShimWarning" depending on the version of Jupyter you are using - this is safe to ignore.
# 
# PHOEBE 2 uses constants defined in the IAU 2015 Resolution which conflict with the constants defined in astropy.  As a result, you'll see the warnings as phoebe.u and phoebe.c "hijacks" the values in astropy.units and astropy.constants.
# 
# Whenever providing units, please make sure to use `phoebe.u` instead of `astropy.units`, otherwise the conversions may be inconsistent.

# ### Logger
# 
# Before starting any script, it is a good habit to initialize a logger and define which levels of information you want printed to the command line (clevel) and dumped to a file (flevel).  A convenience function is provided at the top-level via [phoebe.logger](../api/phoebe.logger.md) to initialize the logger with any desired level.
# 
# The levels from most to least information are:
# 
# * DEBUG
# * INFO
# * WARNING
# * ERROR
# * CRITICAL
# 

# In[3]:


logger = phoebe.logger(clevel='WARNING')


# All of these arguments are optional and will default to clevel='WARNING' if not provided.  There is therefore no need to provide a filename if you don't provide a value for flevel.
# 
# So with this logger, anything with INFO, WARNING, ERROR, or CRITICAL levels will be printed to the screen.  All messages of any level will be written to a file named 'tutorial.log' in the current directory.
# 
# Note: the logger messages are not included in the outputs shown below.
# 

# ## Overview
# 
# As a quick overview of what's to come, here is a quick preview of some of the steps used when modeling a binary system with PHOEBE.  Each of these steps will be explained in more detail throughout these tutorials.
# 
# First we need to create our binary system.  For the sake of most of these tutorials, we'll use the default detached binary available through the [phoebe.default_binary](../api/phoebe.default_binary.md) constructor.

# In[4]:


b = phoebe.default_binary()


# This object holds all the parameters and their respective values.  We'll see in this tutorial and the next tutorial on [constraints](constraints.ipynb) how to search through these parameters and set their values.

# In[5]:


b.set_value(qualifier='teff', component='primary', value=6500)


# Next, we need to define our datasets via [b.add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md).  This will be the topic of the following tutorial on [datasets](datasets.ipynb).  Datasets store observations to compare against the model, but also tell PHOEBE at what times to compute the forward model and store passband-dependent options.

# In[6]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,101))


# We'll then want to run our forward model to create a synthetic model of the observables defined by these datasets using [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md), which will be the topic of the [computing observables](compute.ipynb) tutorial.  The compute options tell PHOEBE how to create a synthetic model from the system parameters for the added datasets.

# In[7]:


b.run_compute()


# We can access the value of any parameter, including the arrays in the synthetic model just generated.  To export arrays to a file, we could call [b.export_arrays](../api/phoebe.parameters.ParameterSet.export_arrays.md)

# In[8]:


print(b.get_value(qualifier='fluxes', context='model'))


# We can then plot the resulting model with [b.plot](../api/phoebe.parameters.ParameterSet.plot.md), which will be covered in the [plotting](plotting.ipynb) tutorial.

# In[9]:


afig, mplfig = b.plot(show=True)


# And then lastly, if we wanted to solve the inverse problem and "fit" parameters to observational data, we may want to add [distributions](distributions.ipynb) to our system so that we can run [estimators, optimizers, or samplers](solver.ipynb).

# ## Default Binary Bundle

# For this tutorial, let's start over and discuss this `b` object in more detail and how to access and change the values of the input parameters.
# 
# Everything for our system will be stored in this single Python object that we call the [Bundle](../api/phoebe.frontend.bundle.Bundle.md) which we'll call `b` (short for bundle).

# In[10]:


b = phoebe.default_binary()


# The Bundle is just a collection of [Parameter](../api/phoebe.parameters.Parameter.md) objects along with some callable methods.  Here we can see that the default binary Bundle consists of over 100 individual parameters.

# In[11]:


b


# If we want to view or edit a Parameter in the Bundle, we first need to know how to access it.  Each Parameter object has a number of tags which can be used to [filter](../api/phoebe.parameters.ParameterSet.filter.md) (similar to a database query).  When filtering the Bundle, a [ParameterSet](../api/phoebe.parameters.ParameterSet.md) is returned - this is essentially just a subset of the Parameters in the Bundle and can be further filtered until eventually accessing a single Parameter.

# In[12]:


b.filter(context='compute')


# Here we filtered on the context tag for all Parameters with `context='compute'` (i.e. the options for computing a model).  If we want to see all the available options for this tag in the Bundle, we can use the plural form of the tag as a property on the Bundle or any ParameterSet.

# In[13]:


b.contexts


# Although there is no strict hierarchy or order to the tags, it can be helpful to think of the context tag as the top-level tag and is often very helpful to filter by the appropriate context first.
# 
# Other tags currently include:
# * kind
# * figure
# * component
# * feature
# * dataset
# * distribution
# * compute
# * model
# * solver
# * solution
# * time
# * qualifier

# Accessing the plural form of the tag as an attribute also works on a filtered ParameterSet

# In[14]:


b.filter(context='compute').components


# This then tells us what can be used to filter further.

# In[15]:


b.filter(context='compute').filter(component='primary')


# The qualifier tag is the shorthand name of the Parameter itself.  If you don't know what you're looking for, it is often useful to list all the qualifiers of the Bundle or a given ParameterSet.

# In[16]:


b.filter(context='compute', component='primary').qualifiers


# Now that we know the options for the qualifier within this filter, we can choose to filter on one of those.  Let's look filter by the 'ntriangles' qualifier.

# In[17]:


b.filter(context='compute', component='primary', qualifier='ntriangles')


# Once we filter far enough to get to a single Parameter, we can use [get_parameter](../api/phoebe.parameters.ParameterSet.get_parameter.md) to return the Parameter object itself (instead of a ParameterSet).

# In[18]:


b.filter(context='compute', component='primary', qualifier='ntriangles').get_parameter()


# As a shortcut, get_parameter also takes filtering keywords.  So the above line is also equivalent to the following:

# In[19]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# Each Parameter object contains several keys that provide information about that Parameter.  The keys "description" and "value" are always included, with additional keys available depending on the type of Parameter.

# In[20]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_value()


# In[21]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_description()


# We can also see a top-level view of the filtered parameters and descriptions (note: the syntax with @ symbols will be explained further in the section on twigs below.

# In[22]:


print(b.filter(context='compute', component='primary').info)


# Since the Parameter for `ntriangles` is a FloatParameter, it also includes a key for the allowable limits.

# In[23]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_limits()


# In this case, we're looking at the Parameter called `ntriangles` with the component tag set to 'primary'.  This Parameter therefore defines how many triangles should be created when creating the mesh for the star named 'primary'.  By default, this is set to 1500 triangles, with allowable values above 100.
# 
# If we wanted a finer mesh, we could change the value.

# In[24]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').set_value(2000)


# In[25]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# If we choose the `distortion_method` qualifier from that same ParameterSet, we'll see that it has a few different keys in addition to description and value.

# In[26]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method')


# In[27]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_value()


# In[28]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_description()


# Since the distortion_method Parameter is a [ChoiceParameter](../api/phoebe.parameters.ChoiceParameter.md), it contains a key for the allowable choices.

# In[29]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_choices()


# We can only set a value if it is contained within this list - if you attempt to set a non-valid value, an error will be raised.

# In[30]:


try:
    b.get_parameter(context='compute', component='primary', qualifier='distortion_method').set_value('blah')
except Exception as e:
    print(e)


# In[31]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').set_value('rotstar')


# In[32]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_value()


# [Parameter](../api/phoebe.parameters.Parameter.md) types include:
# * [IntParameter](../api/phoebe.parameters.IntParameter.md)
# * [FloatParameter](../api/phoebe.parameters.FloatParameter.md)
# * [FloatArrayParameter](../api/phoebe.parameters.FloatArrayParameter.md)
# * [BoolParameter](../api/phoebe.parameters.BoolParameter.md)
# * [StringParameter](../api/phoebe.parameters.StringParameter.md)
# * [ChoiceParameter](../api/phoebe.parameters.ChoiceParameter.md)
# * [SelectParameter](../api/phoebe.parameters.SelectParameter.md)
# * [DictParameter](../api/phoebe.parameters.DictParameter.md)
# * [ConstraintParameter](../api/phoebe.parameters.ConstraintParameter.md)
# * [DistributionParameter](../api/phoebe.parameters.DistributionParameter.md)
# * [HierarchyParameter](../api/phoebe.parameters.HierarchyParameter.md)
# * [UnitParameter](../api/phoebe.parameters.UnitParameter.md)
# * [JobParameter](../api/phoebe.parameters.JobParameter.md)
# 
# these Parameter types and their available options are all described in great detail in [Advanced: Parameter Types](parameters.ipynb)

# ### Twigs

# As a shortcut to needing to filter by all these tags, the Bundle and ParameterSets can be filtered through what we call "twigs" (as in a Bundle of twigs).  These are essentially a single string-representation of the tags, separated by `@` symbols.
# 
# This is very useful as a shorthand when working in an interactive Python console, but somewhat obfuscates the names of the tags and can make it difficult if you use them in a script and make changes earlier in the script.
# 
# For example, the following lines give identical results:

# In[33]:


b.filter(context='compute', component='primary')


# In[34]:


b['primary@compute']


# In[35]:


b['compute@primary']


# However, this dictionary-style twig access will never return a ParameterSet with a single Parameter, instead it will return the Parameter itself.  This can be seen in the different output between the following two lines:

# In[36]:


b.filter(context='compute', component='primary', qualifier='distortion_method')


# In[37]:


b['distortion_method@primary@compute']


# Because of this, this dictionary-style twig access can also set the value directly:

# In[38]:


b['distortion_method@primary@compute'] = 'roche'


# In[39]:


print(b['distortion_method@primary@compute'])


# And can even provide direct access to the keys/attributes of the Parameter (value, description, limits, etc)

# In[40]:


print(b['value@distortion_method@primary@compute'])


# In[41]:


print(b['description@distortion_method@primary@compute'])


# As with the tags, you can call .twigs on any ParameterSet to see the "smallest unique twigs" of the contained Parameters

# In[42]:


b['compute'].twigs


# Since the more verbose method without twigs is a bit clearer to read, most of the tutorials will show that syntax, but feel free to use twigs if they make more sense to you.

# Next
# ----------
# 
# Next up: let's learn about [constraints](constraints.ipynb).
# 
# Or look at any of the following advanced topics:
# * [Advanced: Parameter Types](parameters.ipynb)
# * [Advanced: Parameter Units](units.ipynb)
# * [Advanced: Building a System](building_a_system.ipynb)
# * [Advanced: Contact Binary Hierarchy](contact_binary_hierarchy.ipynb)
# * [Advanced: Saving, Loading, and Exporting](saving_and_loading.ipynb)
