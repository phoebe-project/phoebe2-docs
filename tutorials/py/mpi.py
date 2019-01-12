#!/usr/bin/env python
# coding: utf-8

# Advanced: Running PHOEBE in MPI
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# In[1]:


import phoebe


# MPI Modes
# ------------

# As of the 2.1 release, PHOEBE officially support parallelization using MPI.  Note that the 2.1.1 release fixed a bug related to using PHOEBE within non-openmpi environments.

# There are several "modes of operation" depending on your settings and whether you're running your script within python or mpirun.  You can enable/disable MPI within phoebe by placing [phoebe.mpi_on()](../api/phoebe.mpi_on.md) or [phoebe.mpi_off()](../api/phoebe.mpi_off.md) at the top of your script.  If you do not do this, MPI will be enabled by default if within mpirun and disabled otherwise.
# 
# When MPI is enabled, PHOEBE will do the following:
# * if within mpirun: uses PHOEBE's built-in per-dataset or per-time parallelization.  The main code you write in your script is executed on a single processor, but during [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) the task is divided among the available resources.
# * if not within mpirun (ie. in a serial python environment): will spawn a separate thread at phoebe.frontend.bundle.Bundle.run_compute, using number of processors sent to [phoebe.mpi_on](../api/phoebe.mpi_on.md) (for example: phoebe.mpi_on(nprocs=4)). 
# 
# When MPI is disabled, PHOEBE will do the following:
# * if within mpirun: PHOEBE will run equally on all processors. The user can customize parallelization with access to phoebe.mpi.nprocs, phoebe.mpi.myrank.  Your script runs equally on each processor, meaning you have multiple (separate) copies of the bundle.
# * if not within mpirun (ie. in a serial python environment): PHOEBE will run on a single processor in serial-mode. 

# Accessing/Changing MPI Settings
# --------------------

# To check the currently adopted settings, as well as quickly access information needed for manually doing your own parallelization, access the phoebe.mpi object.

# In[3]:


print(phoebe.mpi.enabled)


# In[4]:


print(phoebe.mpi.mode)


# In[5]:


phoebe.mpi_on()


# In[6]:


print(phoebe.mpi.enabled)


# In[7]:


print(phoebe.mpi.mode)


# In[8]:


print(phoebe.mpi.myrank)


# In[9]:


print(phoebe.mpi.nprocs)


# PHOEBE determines whether the current script is running within an MPI environment by checking for environment variables set by mpirun/mpiexec.  If you run into any issues with PHOEBE not behaving as expected, check to see whether PHOEBE thinks its within mpirun.

# In[10]:


print(phoebe.mpi.within_mpirun)


# If this gives False when you're calling PHOEBE within mpirun, please contact us and we'll do our best to add support for your MPI setup.
