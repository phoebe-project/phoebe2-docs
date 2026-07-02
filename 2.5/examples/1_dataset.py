#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('science')
plt.rcParams.update({'font.size': 6})
# plt.rc('xlabel', fontsize=8) 
# plt.rc('ylabel', fontsize=8) 
get_ipython().run_line_magic('matplotlib', 'inline')

phoebe_c = {'black': "#131313",
             'blue': "#2B71B1",
             'orange': "#FF702F",
             'green': "#22B77F",
             'red': '#F92E3D',
             'purple': '#6D2EB8',
             'pink': "#ED3170",
             'yellow': "#FFCD2F"}


# In[15]:


lcV = np.loadtxt('data/lc.V.data')
lcB = np.loadtxt('data/lc.B.data')
rv1 = np.loadtxt('data/rv1.data')
rv2 = np.loadtxt('data/rv2.data')


# In[16]:


fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(7.25,3))
axes[0].errorbar(x=lcV[:,0], y=lcV[:,1], yerr=lcV[:,2], fmt='.', ms=1, c=phoebe_c['black'], label='Johnson:V')
axes[0].errorbar(x=lcB[:,0], y=lcB[:,1], yerr=lcB[:,2], fmt='.', ms=1, c='0.65', label='Johnson:B')
axes[1].errorbar(x=rv1[:,0], y=rv1[:,1], yerr=rv1[:,2], fmt='.', ms=2.5, c=phoebe_c['black'], label='primary RV')
axes[1].errorbar(x=rv2[:,0], y=rv2[:,1], yerr=rv2[:,2], fmt='.', ms=2.5, c='0.65', label='secondary RV')
axes[0].set_xlabel('Time [d]')
axes[0].set_ylabel('Flux [W/m$^2$]')
axes[1].set_xlabel('Time [d]')
axes[1].set_ylabel('Radial velocity [m/s$^2$]')
axes[0].legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, fancybox=True, frameon=False)
axes[1].legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, fancybox=True, frameon=False)
fig.tight_layout()
fig.savefig('figs/1_data.pdf')


# In[ ]:




