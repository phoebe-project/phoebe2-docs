#!/usr/bin/env python
# coding: utf-8

# # 2.3 - 2.4 Migration: new backends for Gaussian Processes
# 
# As of 2.4, the gaussian_process feature, which wrapped around `celerite`, has been replaced with the GP implementation in `scikit-learn` and `celerite2`. Adding a gaussian process feature now requires a `kind='sklearn'` or `kind='celerite2'` to be provided.
# 
# For more see the [GPs tutorial](gaussian_processes.ipynb)

# In[ ]:




