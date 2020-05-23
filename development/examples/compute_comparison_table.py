#!/usr/bin/env python
# coding: utf-8

# # Compute Backends Comparison Table
# 
# This is an extended version of Table 2 from [Conroy et al. 2020](http://phoebe-project.org/publications/2020Conroy+) and provides an overview of the capabilities and features of the available backends **as implemented by the wrappers**.  Note that some of these codes provide additional or slightly different functionality if run natively.
# 
# The API docs for each of the creation functions through [b.add_compute](../api/phoebe.frontend.bundle.Bundle.add_compute.md) can be found at:
# 
# * [phoebe](../api/phoebe.parameters.compute.phoebe.md)
# * [legacy](../api/phoebe.parameters.compute.legacy.md)
# * [ellc](../api/phoebe.parameters.compute.ellc.md)
# * [jktebop](../api/phoebe.parameters.compute.jktebop.md)

# <table style="width:100%">
#     <tr style="border-bottom:2px solid black">
#         <th></th>
#         <th>PHOEBE</th>
#         <th>legacy</th>
#         <th>ellc</th>
#         <th>jktebop</th>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b style="text-decoration:underline;text-decoration-style:dotted" title="the wrappers are tested on the versions stated, compatibility with newer versions is not guaranteed, but will be updated as possible">Supported Versions</b></td>
#         <td><a href="http://phoebe-project.org/releases/2.3">2.3</a></td>
#         <td><a href="http://phoebe-project.org/1.0">1.0</a></td>
#         <td><a href="https://github.com/pmaxted/ellc/tree/c04c17b0bd657e41e2315daa70e5aed380bd8094">1.8.2</a></td>
#         <td><a href="https://www.astro.keele.ac.uk/jkt/codes/jktebop.html">v34</a></td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/LC.ipynb">LCs</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/pblum.ipynb">LCs (absolute fluxes)</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="fluxes re-scaled by phoebe based on pblum_method, may not be exact">re-scaled</td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="fluxes re-scaled by phoebe based on pblum_method, may not be exact">re-scaled</td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/RV.ipynb">RVs (dynamical)</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#     </tr>
#     <tr>
#         <td><b><a href="../examples/rossiter_mclaughlin.ipynb">RVs (flux-weighted)</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="ellc does natively support flux-weighted with a three parameter irradiation model, but not with the lambert irradiation which is used when mapped from PHOEBE">yes (no irradiation)</td>
#         <td>no</td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/LP.ipynb">Spectral Line Profiles</a></b></td>
#         <td>forward-model</td>
#         <td>no</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/ORB.ipynb">Orbits</a></b></td>
#         <td>forward-model</td>
#         <td>no</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/MESH.ipynb">Access to Underlying Meshes</a></b></td>
#         <td>forward-model</td>
#         <td>forward-model (limited)</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/requiv_crit_detached.ipynb">Detached Systems</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#     </tr>
#     <tr>
#         <td><b><a href="../tutorials/requiv_crit_semidetached.ipynb">Semi-detached Systems</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="the semi-detached radius is determined by PHOEBE and passed to ellc.  ellc does also natively support semi-detached systems by passing a radius of -1, but this is not used by the backend wrapper in PHOEBE.">yes</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/requiv_crit_contact.ipynb">Contact Systems</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="The wrapper will pass the values in the backend parameterization via PHOEBE's constraints, allowing the user to use any parameterization supported by PHOEBE"><b>(Native) Parameterization</b></td>
#         <td>period<br/>mass-ratio<br/>semi-major axis<br/>synchronicities<br/>equivalent radii<br/>Teffs<br/>eccentricity<br/>argument of periastron</td>
#         <td>period<br/>mass-ratio<br/>semi-major axis<br/>synchronicities<br/>equipotentials<br/>Teffs<br/>eccentricity<br/>argument of periastron</td>
#         <td>period<br/>mass-ratio<br/><br/>syncrhonicities<br/>fractional radii<br/>surface-brightness ratio<br/>&#8730;ecosw<br/>&#8730;esinw</td>
#         <td>period<br/>mass-ratio<br/>sum of fractional radii<br/>ratio of radii<br/>surface-brightness ratio<br/><span style="text-decoration:underline;text-decoration-style:dotted" title="jktebop also natively supports passing eccentricity and argument of periastron">ecosw<br/>esinw</span></td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b>Surface Distortion</b></td>
#         <td>roche<br/>rotating star<br/>sphere</td>
#         <td>roche</td>
#         <td>roche<br/>sphere<br/>roche_v<br/>poly1p5<br/>poly3p0<br/>love</td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="biaxial-spherioid used for ellipsoidal and irradiation contributions, but spheres still used for eclipse shapes">biaxial-spheroid<br/>sphere</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b>Asynchronous Rotation</b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/atm_passbands.ipynb">Atmospheres</a></b></td>
#         <td>blackbody<br/><span style="text-decoration:underline;text-decoration-style:dotted" title="(atm=ck2004)">Castelli-Kurucz</span><br/>phoenix</td>
#         <td><span style="text-decoration:underline;text-decoration-style:dotted" title="(atm=extern_planckint)">blackbody</span><br/><span style="text-decoration:underline;text-decoration-style:dotted" title="(atm=extern_atmx)">Catelli-Kurucz</span><br/><br/></td>
#         <td></td>
#         <td></td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/atm_passbands.ipynb">Number of Supported Passbands</a></b></td>
#         <td><a href="../api/phoebe.list_online_passbands.md" title="full available list can be accessed with phoebe.list_online_passbands">30</a></td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="PHOEBE legacy natively supports approximately 100, but only those available in PHOEBE 2 are available directly through the backend wrapper">30</td>
#         <td>0</td>
#         <td>0</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/reflection_heating.ipynb">Irradiation</a></b></td>
#         <td>Horvat/Lambert<br/>Wilson</td>
#         <td>Wilson</td>
#         <td>Lambert</td>
#         <td>biaxial-spheroid</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/limb_darkening.ipynb">Limb-Darkening</a></b></td>
#         <td>interpolated<br/>linear<br/>logarithmic<br/>quadratic<br/>sqrt<br/>power</td>
#         <td>linear<br/>logarithmic<br/>sqrt</td>
#         <td>linear<br/>logarithmic<br/>quadratic<br/>sqrt<br/><span style="text-decoration:underline;text-decoration-style:dotted" title="ellc natively refers to this as power-2, but is mapped from PHOEBE's ld_func=power">power</span></td>
#         <td>linear<br/>logarithmic<br/>quadratic<br/>sqrt</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/gravb_bol.ipynb">Gravity Brightening/Darkening<a/></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/spots.ipynb">Spots</a></b></td>
#         <td>circular</td>
#         <td>circular</td>
#         <td>circular</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/ltte.ipynb">Romer (ltte) Delay</a></b></td>
#         <td>yes (optional)</td>
#         <td>no</td>
#         <td>yes (optional)</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/apsidal_motion.ipynb">Apsidal Motion</a></b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b>Period Time-Derivative</b></td>
#         <td>yes</td>
#         <td>yes</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/pitch_yaw.ipynb">Spin-Orbit Misalignment</a></b></td>
#         <td>yes</td>
#         <td>no</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/ebv_Av_Rv.ipynb">Extinction/Reddening</a></b></td>
#         <td>yes</td>
#         <td>no</td>
#         <td>no</td>
#         <td>no</td>
#     </tr>
#     <tr style="border-bottom:1px solid black">
#         <td><b><a href="../tutorials/beaming_boosting.ipynb">Doppler Beaming/Boosting</a></b></td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="beaming/boosting was disabled in PHOEBE 2.2 but will hopefully be re-implemented in a future release">no</td>
#         <td>no</td>
#         <td style="text-decoration:underline;text-decoration-style:dotted" title="ellc does natively support beaming/boosting, but is not currently available through PHOEBE">no</td>
#         <td>no</td>
#     </tr>
# </table>
