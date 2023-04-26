## A set of functions for calculations required in converting various reference frames
# and calculating overall kinematics.
# Basing boost calculations on here: http://www.phys.ufl.edu/~avery/course/4390/f2015/lectures/relativistic_kinematics_1.pdf
# Also these are really helpful: https://uspas.fnal.gov/materials/10MIT/Review_of_Relativity.pdf 
import math
import numpy as np

# A few shared fixed quantities
me = 5.1099892800000001E-004 # electron

def getP(E, m) :
    return np.sqrt(E**2 - m**2)

def getE(p, m) :
    return np.sqrt(p**2 + m**2)

def getV(E, m) :
    return getBetaFromEM(E, m)

# Considering c = 1, so v = beta = fraction of speed of light.

def getSqrtS(E_beam, m_target) :
    sum = 2.*E_beam**2 + 2.*m_target*E_beam + m_target**2 - me**2
    return math.sqrt(sum)

def getGammaFromEM(E, m) :
    return E/m

def getGammaFromBeta(beta) :
    return 1./np.sqrt(1 - beta**2)

def getGammaFromV(v) :
    return 1./np.sqrt(1 - v**2)

def getBetaFromEM(E, m) :
    return getP(E,m)/E

def getBetaFromGamma(gamma) :
    return np.sqrt(1 - pow(gamma,-2))

def getBetaFromEP(E, p) :
    return p/E


# Following https://phys.libretexts.org/Bookshelves/Nuclear_and_Particle_Physics/Book%3A_Nuclear_and_Particle_Physics_(Walet)/09%3A_Relativistic_Kinematics/9.03%3A_Transformations_between_CM_and_lab_frame
def get_v_CM_to_lab(E_beam, m_target) :
    mom_electron_lab = getP(E_beam, me)
    # So p_electron_lab = (mom_electron_lab, 0, 0, E_beam)
    # And p_target_lab = (0, 0, 0, m_target**2)
    v = mom_electron_lab/(m_target + E_beam)
    return v

# Following http://www.phys.ufl.edu/~avery/course/4390/f2015/lectures/relativistic_kinematics_1.pdf 
def angle_lab_to_CM(theta_lab, E_lab, mass, v_frame) :
    p_lab = getP(E_lab,mass)
    gamma_frame = getGammaFromV(v_frame)
    tan_theta_CM = (p_lab * math.sin(math.radians(theta_lab)))/(gamma_frame*(p_lab * math.cos(math.radians(theta_lab)) - v_frame * E_lab))
    return math.degrees(math.atan(tan_theta_CM))

def angle_CM_to_lab() :
    return

def momentum_lab_to_CM() :
    return

def momentum_CM_to_lab() :
    return