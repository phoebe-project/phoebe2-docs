#!/usr/bin/env python
# coding: utf-8

# PHOEBE Logic for Computing Observables
# ============================
# 
# The general logic steps that PHOEBE uses for each observable type are as follows:
# 
# 1. Dynamics - each star or body in the system hierarchy needs to be placed in the correct position in the orbit at any given time.  Some observables (dynamical RVs and ETVs) simply use information from the dynamics and do not use any of the following steps.
# 2. Meshing - each star or body in the system needs to be discretized (if applicable), creating a mesh of triangles that describe the shape of the surface.
# 3. Local Quantities - at any given time, each surface element needs to have its local quantities populated.  These include things like effective temperature and intensity.
# 4. Eclipse Detection - each star needs to detect which of its surface elements are eclipsed, and handle subdivision if necessary to increase the resolution along the eclipse edge.
# 5. Integration - lastly, the local quantities need to be integrated over all visible surface elements to compute a single observable value at the given time

# Dynamics
# -------------------
# 
# See more information about options for dynamics in the section on the [ORB dataset](ORB.ipynb)

# Meshing
# ----------------------
# 
# See more information about options for meshing as well as the returned columns in the section on the [MESH dataset](MESH.ipynb)
# 
# Related example scripts:
#   * [Wilson-Devinney Style Meshing Example Script](../examples/mesh_wd.ipynb)
#   
#   
# 

# Local Quantities
# --------------------
# 
# See more information about the options and parameters for computing flux-related local quantities in the section on the [LC dataset](LC.ipynb)
# 
# See more information about the options and parameters for computing local radial-velocities in the section on the [RV dataset](RV.ipynb) (note that flux-weighted RVs also use flux-related local quantities described in the [LC dataset](LC.ipynb) section).
# 
# Related Example scripts:
#   * [Reflection and Heating](../tutorials/reflection_heating.ipynb)
#   * [Beaming and Boosting](../tutorials/beaming_boosting.ipynb)
#   
# 
# 

# Eclipse Detection
# ----------------------
# 
# See more information about the options for eclipse detection and subdivision in the section on the [MESH dataset](MESH.ipynb)

# Integration
# -----------------
# 
