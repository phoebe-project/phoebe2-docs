#!/usr/bin/env python
# coding: utf-8

# Advanced: Environment Variables
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[ ]:


#!pip install -I "phoebe>=2.3,<2.4"


# ## Setting Environment Variables

# Some settings cannot be changed after importing PHOEBE, so they are available via environment variables.  These can be set in a variety of ways:
# 
# Setting inline before calling python will set for that single session of PHOEBE:
# ```
# PHOEBE_ENABLE_PLOTTING=FALSE python [script.py]
# ```
# 
# Setting via the os package in python **before** importing PHOEBE allows you to set the setting everytime you run a given script:
# ```py
# import os
# os.environ['PHOEBE_ENABLE_PLOTTING'] = 'FALSE'
# import phoebe
# ```
# 
# Note for all boolean settings, the string is converted to uppercase and compared to 'TRUE'.

# ## Plotting Options

# ### PHOEBE_ENABLE_PLOTTING
# 
# PHOEBE_ENABLE_PLOTTING (TRUE by default) allows for disabling plotting within PHOEBE and therefore skipping the import of all plotting libraries (which take up a significant amount of the time it takes to import phoebe).

# ## Passband Options

# ### PHOEBE_ENABLE_ONLINE_PASSBANDS
# 
# PHOEBE_ENABLE_ONLINE_PASSBANDS (TRUE by default) dictates whether online passbands are queried and available for on-the-fly downloading.  If you are sure you have all the local passbands you need, set this to False to save some time.

# ### PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_CONTENT
# 
# PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_CONTENT ('all' by default, use comma separate for a list: 'ck2004,phoenix') allows setting the value for `content` in [phoebe.set_download_passband_defaults](../api/phoebe.set_download_passband_defaults.md).  For more details, see the section above.

# ### PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_GZIPPED
# 
# PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_GZIPPED (FALSE by default) allows setting the value for `gzipped` in [phoebe.set_download_passband_defaults](../api/phoebe.set_download_passband_defaults.md).  For more details, see the section above.

# ### PHOEBE_UPDATE_PASSBAND_IGNORE_VERSION
# 
# PHOEBE_UPDATE_PASSBAND_IGNORE_VERSION (FALSE by default) allows disabling the timestamp check used to require manually updating passbands when required content is missing.  See [phoebe.update_passband_ignore_version_on](../api/phoebe.update_passband_ignore_version_on.md) and [phoebe.update_passband_ignore_version_off](../api/phoebe.update_passband_ignore_version_off.md)

# ### PHOEBE_PBDIR
# 
# PHOEBE_PBDIR (empty by default) allows setting an additional custom directory to query for passbands, in addition to [phoebe.list_passband_directories](../api/phoebe.list_passband_directories.md)

# ## MPI Options

# ### PHOEBE_ENABLE_MPI
# 
# PHOEBE_ENABLE_MPI (defaults to TRUE if within mpirun/mpiexec, otherwise FALSE): whether to use internal parallelization.  See also [phoebe.mpi_on](../api/phoebe.mpi_on.md) and [phoebe.mpi_off](../api/phoebe.mpi_off.md)

# ### PHOEBE_MPI_NPROCS
# 
# PHOEBE_MPI_NPROCS (defaults to 4) allows setting the number of processors to spawn if MPI is enabled but **not** running within mpirun/mpiexec.  See also: [phoebe.mpi_on](../api/phoebe.mpi_on.md).

# ## Multiprocessing Options
# 
# ### PHOEBE_MULTIPROCESSING_NPROCS  (NEW IN 2.3.26)
# 
# PHOEBE_MULTIPROCESSING_NPROCS (defaults to using all available CPUs, when supported, and only if not within MPI): number of processors to expose to multiprocessing.  See also [phoebe.multiprocessing_on](../api/phoebe.multiprocessing_on.md), [phoebe.multiprocessing_off](../api/phoebe.multiprocessing_off.md), and [phoebe.multiprocessing_set_nprocs](../api/phoebe.multiprocessing_set_nprocs.md).

# In[ ]:




