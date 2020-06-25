#!/usr/bin/env python
# coding: utf-8

# # Propagating Distributions through Constraints
# 
# In this example script, we'll reproduce Figure 4 from the fitting release paper ([Conroy et al. 2020](http://phoebe-project.org/publications/2020Conroy+)).
# 
# <img src="http://phoebe-project.org/images/figures/2020Conroy+_fig4.png" alt="Figure 4" width="800px"/>

# # Setup

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import matplotlib.pyplot as plt

plt.rc('font', family='serif', size=14, serif='STIXGeneral')
plt.rc('mathtext', fontset='stix')


# In[3]:


import phoebe
logger = phoebe.logger('warning')


# In[4]:


b = phoebe.default_binary()


# In[5]:


b.set_value('latex_repr', component='binary', value='orb')
b.set_value('latex_repr', component='primary', value='1')
b.set_value('latex_repr', component='secondary', value='2')


# In[6]:


b.add_distribution({'sma@binary': phoebe.uniform(5,8), 'incl@binary': phoebe.gaussian(75,10)}, 
                   distribution='mydist')


# # Plotting Distributions

# In[7]:


dist = b.get_parameter('sma', component='binary', context='component').get_distribution('mydist')

plt.clf()
figure = plt.figure(figsize=(4,4))
_ = dist.plot(plot_uncertainties=False)
_ = plt.tight_layout()
_ = plt.savefig('figure_priors_sma.pdf')


# In[8]:


dist = b.get_parameter('incl', component='binary', context='component').get_distribution('mydist')

plt.clf()
figure = plt.figure(figsize=(4,4))
_ = dist.plot(plot_uncertainties=False)
_ =plt.tight_layout()
_ = plt.savefig('figure_priors_incl.pdf')


# In[9]:


dist = b.get_parameter('asini', component='binary', context='component').get_distribution('mydist')

plt.clf()
figure = plt.figure(figsize=(4,4))
_ = dist.plot(plot_uncertainties=False)
_ = plt.tight_layout()
_ = plt.savefig('figure_priors_asini.pdf')


# In[ ]:




