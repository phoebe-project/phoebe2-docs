# Physics Implemented in PHOEBE

The following tutorials aim to explain the implementation and usage of some of the physical effects that are incorporated in PHOEBE. These explain the relevant parameters and try to demonstrate how they affect the resulting synthetic models, but expect a comfortable understanding of using PHOEBE and Python.

## System Effects/Parameters:
* [Systemic Velocity (vgamma)](tutorials/vgamma.ipynb)
* [Rømer & Light Travel Time Effects (ltte)](tutorials/ltte.ipynb)
* [Third Light (l3_mode, l3, l3_frac)](tutorials/l3.ipynb)
* [Distance (distance)](tutorials/distance.ipynb)

## Orbital Effects/Parameters:
* [Various t0s (t0, t0_perpass, t0_supconj, t0_ref)](tutorials/t0s.ipynb)
* [Eccentricity & Volume Conservation (ecc)](tutorials/ecc.ipynb)
* [Apsidal Motion (dperdt)](tutorials/apsidal_motion.ipynb)
* [Misalignment (pitch & yaw)](tutorials/pitch_yaw.ipynb)
* [Rømer & Light Travel Time Effects (ltte)](tutorials/ltte.ipynb)
* [Beaming & Boosting (boosting_method)](tutorials/beaming_boosting.ipynb)

## Stellar Effects/Parameters:
* [Equivalent Radius (requiv)](tutorials/requiv.ipynb)
* [Potentials (replaced by Equivalent Radius in PHOEBE 2.1+)](tutorials/pot.ipynb)
* [Critical Radii: Detached Systems (requiv_max)](tutorials/requiv_crit_detached.ipynb)
* [Critical Radii: Semidetached Systems (requiv_max)](tutorials/requiv_crit_semidetached.ipynb)
* [Critical Radii: Contact Systems (requiv_min & requiv_max)](tutorials/requiv_crit_contact.ipynb)
* [Surface Gravities (logg)](tutorials/logg.ipynb)
* [Eccentricity & Volume Conservation (ecc)](tutorials/ecc.ipynb)
* [Spots](tutorials/spots.ipynb)
* [Eclipse Detection (eclipse_method)](tutorials/eclipse.ipynb)
* [Passband Luminosity (pblum_mode, pblum_component, pblum_dataset, pblum, pbflux)](tutorials/pblum.ipynb)
* [Gravity Brightening/Darkening (gravb_bol)](tutorials/gravb_bol.ipynb)
* [Reflection & Heating (irrad_frac_refl_bol, irrad_frac_lost_bol, ld_func_bol, ld_coeffs_bol)](tutorials/reflection_heating.ipynb)
* [Reflection & Heating: Lambert Scattering (irrad_method='horvat' vs 'wilson')](tutorials/irrad_method_horvat.ipynb)

## Passband/Atmosphere/Dataset Effects/Parameters:
* [Passbands & Atmospheres (passband & atm)](tutorials/atm_passbands.ipynb)
* [Passband Luminosity (pblum_mode, pblum_component, pblum_dataset, pblum, pbflux)](tutorials/pblum.ipynb)
* [Limb Darkening (ld_mode, ld_func, ld_coeffs_source, ld_coeffs)](tutorials/limb_darkening.ipynb)
* [Third Light (l3_mode, l3, l3_frac)](tutorials/l3.ipynb)
* [Extinction (ebv, Av, Rv)](tutorials/ebv_Av_Rv.ipynb)
* [Gravitational Redshift (rv_grav)](tutorials/grav_redshift.ipynb)
* [Intensity Weighting (intens_weighting)](tutorials/intens_weighting.ipynb)
* [Finite Time of Integration (exptime, fti_method, fti_oversample)](tutorials/fti.ipynb)
