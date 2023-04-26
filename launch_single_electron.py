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

# Velocity of CM frame relative to lab frame
v_CM = get_v_CM_to_lab(E_beam, mass_scatteringcenter)
# Gamma which is boost of CM frame relative to lab frame
gamma_CM = getGammaFromV(v_CM)
print("Gamma of CM frame is",gamma_CM)


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
print("angle_lab_to_CM for initial beamline particle is:",angle_lab_to_CM(0,E_beam,me,v_CM))
print("angle_lab_to_CM for a test outgoing particle of 10 MeV and 20 degrees in lab is:",angle_lab_to_CM(20,0.01,me, v_CM))
print("Backwards: angle_CM_to_lab for outgoing particle along beamline is:",angle_CM_to_lab(0, 0.01, me, v_CM))
print("Backwards: angle_CM_to_lab for outgoing 10 MeV particle at 26 degrees in CM frame is:",angle_CM_to_lab(26.,0.01,me, v_CM))

print("\n\n")
p_testlabtocm = momentum_lab_to_CM(20.,0.01,me,v_CM)
e_lab = getE(0.01,me)
print("Momentum of p = 10 MeV electron at 20 degrees in lab frame, in CM frame:",p_testlabtocm)
print("And its angle in CM frame:",angle_lab_to_CM(20,0.01,me, v_CM))
print("Which gives it an energy of",getE(p_testlabtocm,me))
print("From scaling energy function, get that it should be:",energy_lab_to_CM(20.,e_lab,me,v_CM))
p_testcmtolab = momentum_CM_to_lab(27., 0.008, me, v_CM)
e_cm = getE(0.008,me)
print("Momentum of 8 MeV electron at 27 degrees in CM frame, in lab frame:",p_testcmtolab)
print("And its angle in lab frame:",angle_CM_to_lab(27.,0.008, me, v_CM))
print("Which gives it an energy of",getE(p_testcmtolab,me))
print("From scaling energy function, get that it should be:",energy_CM_to_lab(27.,e_cm,me,v_CM))
