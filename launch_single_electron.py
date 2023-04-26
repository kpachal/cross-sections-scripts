import sys, os
from relativistic_kinematics import *

################
# Everything that absolutely has to be tuned is here.
# Mass and energy units are GeV to align with what is fed to FormCalc.
mTa = 160.631 # tantalum nucleus
#mu = 2.2e-3 # up quark. Why is mass in this code so different?
mu = 7.3559471591835346E-002 # Value in FormCalc
me = 5.1099892800000001E-004 # electron
mp = 0.938 # proton

# Set which of the above (or something else) we will use to determine scattering kinematics
mass_scatteringcenter = mu

E_beam = 0.030 # 30 MeV e- beam

# This path must be set to point at the Fortran code from FormCalc in a location where it can compile with LoopTools.
path_fortran = "/Users/katherinepachal/Code/Mathematica-projects/DarkLight-backgrounds/scattered-electron.fortran"

# This is a template run script that will be copied with line by line changes to add the cuts needed for our single electron scattering across a full grid of angles.
run_template = "run.F"

################

# Get sqrt(s) for e- beam hitting stationary target with mass chosen above.
sqrtS = getSqrtS(E_beam, mass_scatteringcenter)
print("Tantalum target, 30 MeV beam: sqrt(s) =",getSqrtS(E_beam,mTa))
print("Proton target, 30 MeV beam: sqrt(s) =",getSqrtS(E_beam,mp))
print("Up quark target, 30 MeV beam: sqrt(s) =",getSqrtS(E_beam,mu))
print("Using sqrt(S) =",sqrtS)

print("Velocity of CM relative to lab frame is", get_v_CM_to_lab(E_beam, mass_scatteringcenter),"c")

print("Validations")
print("V (or beta) of beam electron",getBetaFromEM(E_beam, me))
print("V, second estimate:",getBetaFromEP(E_beam,getP(E_beam,me)))
print("Gamma of beam electron, function 1:",getGammaFromEM(E_beam,me))
print("Beta from that gamma:",getBetaFromGamma(getGammaFromEM(E_beam,me)))
print("Gamma from beta using E and m:",getGammaFromBeta(getBetaFromEM(E_beam, me)))
print("Gamma of beam electron, from V:",getGammaFromV(getV(E_beam, me)))
print("Beta from gamma from EM",getBetaFromGamma(getGammaFromEM(E_beam,me)))
