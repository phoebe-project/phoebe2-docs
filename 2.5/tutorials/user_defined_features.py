#!/usr/bin/env python
# coding: utf-8

# User Defined Features
# ============================
# 
# User Defined Features allow writing custom code that hooks into various locations in PHOEBE's logic.  These "features" are then attached to the bundle in the same way as built-in features, with full distribution, fitting, and server support.
# 
# Setup
# -----------------------------
# 
# Let's first make sure we have the latest version of PHOEBE 2.5 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.5"


# In[2]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# ## Types of User-Defined Features
# 
# User-Defined Features fall under two different categories:
# 
# 1. `DatasetFeature`: these allow modifying the synthetic model of a dataset _after_ PHOEBE has completed its calculation (across all times) but _before_ being exposed in the model or before any merit function is calculated (when calling [solvers](./solver.ipyng)).  Because of this, these can also be used across any [alternate backend](./alternate_backends.ipynb).  These can also modify the data that is being sent to estimators.  These are useful when wanting to add some independent effect to the model (some offset or third-light contribution, etc).
# 
# 2. `ComponentFeature`: these allow modifying PHOEBE's internal computation at the mesh-level within the time-loop for a single component, and are useful for anything that depends on internal quantities at a given time to expose (mimicing pulsations or modifying [spots](./spots.ipynb) to migrate, etc).

# ## Limitations and Caveats
# 
# Before we get started showing how to write and attach a custom feature, there are a few caveats to keep in mind:
# 
# * Inheritance from other features (including built-in features) is supported, but using `super` is not and will result in an error.
# * Any referenced packages must be exported in each method that uses it
# * The custom feature is "copied" when calling `add_feature` and changes made to the class outside PHOEBE are ignored.
# 
# These will make more sense as we come across them.

# ## Defining Custom Features
# 
# ### Dataset Feature
# 
# To create a `DatasetFeature`, create a class that inherits from `phoebe.features.DatasetFeature`, and optionally override the following attributes & methods (the return statements below are the defaults for any method that is not defined):

# In[3]:


from phoebe.features import DatasetFeature
from phoebe.parameters import FloatParameter, ParameterSet, constraint

class CustomDatasetFeature(DatasetFeature):
    # define which kinds of dataset are supported by the feature
    allowed_dataset_kinds = ['lc', 'rv', 'lp']

    @classmethod
    def create_feature_parameters(self, feature, **kwargs):
        """
        returns a ParameterSet of parameters that defines how the features act
        as well as a list of constraints between those parameters (or an empty list)
        """
        return ParameterSet([]), []

    @classmethod
    def parse_bundle(cls, b, feature_ps):
        """
        cache any internal information from the bundle or feature (current parameter
        values, etc) to use in either of the later methods.  Note that the user
        may have changed units from those defined in `create_feature_parameters`
        """
        return {}

    @classmethod
    def run_checks_compute(cls, b, feature_ps, compute_ps):
        """
        optionally check for self-consistent or physicality of the values of parameters
        these will be run at each forward model and can prevent the rest of the model
        running to raise an error if it can be predicted in advance
        """
        return [{}]

    def modify_data_for_estimators(self, b, data_ps, **data_arrays):
        """
        Modify the data parameters for the estimators.
        This is called before the data is passed to the estimators.
        """
        return {}

    def modify_model(self, b, model_ps):
        """
        Modify the model parameters (of this dataset) before being stored
        in the bundle or to the merit function of estimators/samplers.
        """
        return None


# ### Component Features
# 
# Similarly, to create a `ComponentFeature`, create a class that inherits from `phoebe.features.ComponentFeature`, and optionally override the following attributes & methods (the return statements below are the defaults for any method that is not defined):

# In[4]:


from phoebe.features import ComponentFeature
from phoebe.parameters import FloatParameter, ParameterSet, constraint


class CustomComponentFeature(ComponentFeature):
    """
    Note that for all features, each of the methods below will be called.  So
    changing the coordinates WILL affect the original/intrinsic loggs which
    will then be used as input for that method call.

    In other words, its probably safest if each feature only overrides a
    SINGLE one of the methods.  Overriding multiple methods should be done
    with great care.

    Each feature may or may not require recomputing a mesh, depending on the
    kind of change it exacts to the mesh. For example, pulsations will require
    recomputing a mesh while spots will not. By default, the mesh will be
    recomputed (set in this superclass' `__init__()` method) but inherited
    classes should overload `self.remeshing_required`.
    """
    # define which kinds of components are supported by the feature
    allowed_component_kinds = ['star', 'envelope', 'orbit']

    @classmethod
    def create_feature_parameters(self, feature, **kwargs):
        """
        returns a ParameterSet of parameters that defines how the features act
        as well as a list of constraints between those parameters (or an empty list)
        """
        params = []
        # NOTE here that the string in qualifier and kwargs.get for value should match!
        params += [FloatParameter(qualifier='test_param',
                                  latexfmt=r'T_\mathrm{{ {feature} }}',
                                  value=kwargs.get('test_param', 1),
                                  default_unit=u.dimensionless_unscaled,
                                  description='Just a test parameter!')]
        return ParameterSet(params), []

    @classmethod
    def parse_bundle(cls, b, feature_ps):
        """
        cache any internal information from the bundle or feature (current parameter
        values, etc) to use in either of the later methods.  Note that the user
        may have changed units from those defined in `create_feature_parameters`
        """
        return {}

    @classmethod
    def run_checks_compute(cls, b, feature_ps, compute_ps):
        """
        optionally check for self-consistent or physicality of the values of parameters
        these will be run at each forward model and can prevent the rest of the model
        running to raise an error if it can be predicted in advance
        """
        return [{}]

    def requires_remeshing(self):
        """
        define whether this feature (with its current parameter values) requires
        the mesh to be recomputed at each time.
        """
        return True

    def modify_coords_for_computations(self, coords_for_computations, s, t):
        """
        Method for a feature to modify the coordinates.  Coordinates are
        modified AFTER scaling but BEFORE being placed in orbit.

        NOTE: coords_for_computations affect physical properties only and
        not geometric properties (areas, eclipse detection, etc).  If you
        want to override geometric properties, use the hook for
        modify_coords_for_observations as well.

        Features that affect coordinates_for_computations should override
        this method
        """
        return coords_for_computations

    def modify_coords_for_observations(self, coords_for_computations, coords_for_observations, s, t):
        """
        Method for a feature to modify the coordinates.  Coordinates are
        modified AFTER scaling but BEFORE being placed in orbit.

        NOTE: coords_for_observations affect the geometry only (areas of each
        element and eclipse detection) but WILL NOT affect any physical
        parameters (loggs, teffs, intensities).  If you want to override
        physical parameters, use the hook for modify_coords_for_computations
        as well.

        Features that affect coordinates_for_observations should override this method.
        """
        return coords_for_observations

    def modify_rvs(self, rvs, orbit_vel, roche_coords, s=[0., 0., 1.], t=None):
        """
        Method for a feature to modify the radial velocities.

        Features that affect radial velocities (RV+LP datasets) should override this method

        NOTE: orbit_vel[2] is in the OPPOSITE direction of the radial velocity
        """
        return rvs

    def modify_loggs(self, loggs, roche_coords, s=[0., 0., 1.], t=None):
        """
        Method for a feature to modify the loggs.

        Features that affect loggs should override this method
        """
        return loggs

    def modify_teffs(self, teffs, roche_coords, s=[0., 0., 1.], t=None):
        """
        Method for a feature to modify the teffs.

        Features that affect teffs should override this method
        """
        return teffs

    def modify_intensities(self, abs_normal_intensities, abs_intensities,
                           mus, pblum_scale, extinct_factors, boost_factors,
                           roche_coords, s=[0., 0., 1.], t=None):
        """
        Method for a feature to modify the intensities.
        Features that affect intensities should override this method

        Arguments
        ----------
        * `abs_normal_intensities` (ndarray): Absolute normal intensities, already multiplied
            by `extinct_factors`.
        * `abs_intensities` (ndarray): Absolute projected intensities, already multiplied by
            `extinct_factors` and `boost_factors`.
        * `mus` (ndarray): Cosine of the angle between the normal vector and the line of sight
        * `pblum_scale` (ndarray): Scale factor for the pblum, that will be applied to the abs_intensities
            AFTER modify_intensities to result in the scaled intensities
        * `extinct_factors` (ndarray): Extinction factors for the intensities, already applied
        * `boost_factors` (ndarray): Boost factors for the intensities, already applied
        * `roche_coords` (ndarray): Roche coordinates for the computations
        * `s` (array-like): Spin vector in Roche coordinates
        * `t` (float): Current time
        """
        return abs_normal_intensities, abs_intensities


# In addition, instances of `ComponentFeature` have access to `ComponentFeature.cartesian_to_spherical(roche_coords)` which returns `r, colat, longitude`.

# ## Attaching Custom Features to Bundle
# 
# Attaching a custom user-defined feature to the bundle works very similarly to built-in features.  Here, instead of passing a string of the kind of feature as the first argument, we will pass the _class_ itself.
# 
# Component Features require a valid `component` label to be passed, whereas Dataset Features require a valid `dataset` label to be passed (according to the `allowed_component_kinds`/`allowed_dataset_kinds`, respectively).  Any parameters that were defined by `create_feature_parameters` can be passed as keyword arguments (so long as the `value` defined in the parameter appropriately checked for the same name from `kwargs`), or filtered/retrieved/set after as any other parameter.

# In[5]:


b.add_feature(CustomComponentFeature,
              component='primary',
              test_param=2,
              feature='my_custom_component_feature')


# Now if we filter for parameter taggged with the feature name, we can see our custom "test_param" parameter (with the passed value that overrode the default) as well as a read-only parameter containing a reference to the code itself.

# In[6]:


print(b.filter(feature='my_custom_component_feature'))


# This code is serialized and stored with the bundle, which makes it portable to run on other systems (but also means that you should treat bundles from other people the same as you would treat python scripts and run them only if you trust and read the source code!).

# In[7]:


print(b.get_parameter(qualifier='custom_code', feature='my_custom_component_feature').get_source_code())


# This also means that the code is "frozen" at the time in which you call `add_feature`, and changes to your class will not be picked up by the bundle (effectively the bundle holds a copy, not a reference - this is the same as loading data into the bundle from an array or file).
# 
# This does allow saving the feature to the same bundle file and sending to an external machine or colleague without also having to send a python script or install some plugin in order to run forward models or solvers with the feature enabled:

# In[8]:


b.save('custom_feature.bundle')


# In[10]:


b2 = phoebe.load('custom_feature.bundle')


# In[11]:


print(b2.filter(feature='my_custom_component_feature'))


# ## Examples
# 
# In order to better understand the functionality and flexibility of user-defined features, see some of the following examples (and _please_ consider reaching out if you create a feature yourself that you would be willing to have featured here for others to learn):
# * [Example: Sinusoidal Third Light (DatasetFeature)](../examples/user_defined_features_sinusoidal_l3.ipynb)
# * [Example: Sinusoidal Intensities (ComponentFeature)](../examples/user_defined_features_sinusoidal_intens.ipynb)
# * [Example: Differential Rotation (ComponentFeature)](../examples/user_defined_features_diff_rotation.ipynb)
# * [Example: Migrating Spot (ComponentFeature)](../examples/user_defined_features_migrating_spot.ipynb)

# In[ ]:




