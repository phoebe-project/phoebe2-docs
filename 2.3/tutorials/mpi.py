#!/usr/bin/env python
# coding: utf-8

# Advanced: Running PHOEBE in MPI
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[ ]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[1]:


import phoebe


# MPI Modes
# ------------

# As of the 2.1 release, PHOEBE officially support parallelization using MPI within [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md).  The 2.3 release introduced support for [run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md), including support for both MPI and multiprocessing.

# There are several "modes of operation" depending on your settings and whether you're running your script within python or mpirun.  You can enable/disable MPI within phoebe by placing [phoebe.mpi_on()](../api/phoebe.mpi_on.md) or [phoebe.mpi_off()](../api/phoebe.mpi_off.md) at the top of your script.  If you do not do this, MPI will be enabled by default if within mpirun and disabled otherwise.
# 
# When MPI is enabled, PHOEBE will do the following:
# * if within mpirun: 
#     * `run_compute`: uses PHOEBE's built-in per-dataset or per-time parallelization.  The main code you write in your script is executed on a single processor, but during [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) the task is divided among the available resources.
#     * `run_solver`: when applicable, PHOEBE will parallelize over the individual models within the solver and serialize `run_compute`.  For [sampler.emcee](../api.phoebe.parameters.solver.sampler.emcee.md), this will only be done if `nwalkers` <= `nprocs`.
# * if not within mpirun (ie. in a serial python environment): will spawn a separate thread at [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) or [run_solver](../api/phoebe.frontend.bundle.Bundle.run_solver.md), using number of processors sent to [phoebe.mpi_on](../api/phoebe.mpi_on.md) (for example: phoebe.mpi_on(nprocs=4)). 
# 
# When MPI is disabled, PHOEBE will do the following:
# * if within mpirun: PHOEBE will run equally on all processors. The user can customize parallelization with access to phoebe.mpi.nprocs, phoebe.mpi.myrank.  Your script runs equally on each processor, meaning you have multiple (separate) copies of the bundle. USE WITH CAUTION.
# * if not within mpirun (ie. in a serial python environment): 
#     * `run_compute`: If `sample_from` is used, PHOEBE will make use of multiprocessing across all available processors to parallize across sampled models.  In all other cases, PHOEBE will run on a single processor in serial-mode. 
#     * `run_solver`: PHOEBE will make use of multiprocessing across all available processors whenever the solver backend support multiprocessing, otherwise will fallback on serial-model

# Accessing/Changing MPI Settings
# --------------------

# To check the currently adopted settings, as well as quickly access information needed for manually doing your own parallelization, access the phoebe.mpi object.

# In[2]:


print(phoebe.mpi.enabled)


# In[3]:


print(phoebe.mpi.mode)


# In[4]:


phoebe.mpi_on()


# In[5]:


print(phoebe.mpi.enabled)


# In[6]:


print(phoebe.mpi.mode)


# In[7]:


print(phoebe.mpi.myrank)


# In[8]:


print(phoebe.mpi.nprocs)


# PHOEBE determines whether the current script is running within an MPI environment by checking for environment variables set by mpirun/mpiexec.  If you run into any issues with PHOEBE not behaving as expected, check to see whether PHOEBE thinks its within mpirun.

# In[9]:


print(phoebe.mpi.within_mpirun)


# If this gives False when you're calling PHOEBE within mpirun, please contact us and we'll do our best to add support for your MPI setup.
# 
# Note that some of these options can also be set via [environment variables](./envars.ipynb)
