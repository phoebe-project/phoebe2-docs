#!/usr/bin/env python
# coding: utf-8

# # 2.3 - 2.4 Migration: using ligeor as a built-in dependency
# 
# The lc_geometry estimator now uses [ligeor](https://github.com/gecheline/ligeor) as a built-in dependency, which allows for estimates of additional parameters, compared to 2.3. In addition to `ecc` and `per0`, lc_geometry now returns estimates of `requivsumfrac`, `teffratio`, and if ellc is available as a backend, can also quickly optimize for `requivratio` and `incl@binary`.

# In[ ]:




