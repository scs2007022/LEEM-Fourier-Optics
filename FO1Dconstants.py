import numpy as np

if __name__ == '__main__':
    print("")
else:
    print("Loading Constants")

taskName = "ACSinObject"

numberOfThreads = -1  # number of threads used in the simulation with -1 means using all threads, -2 means using all threads minus 1.

simulatingSpaceSize = 100  # total simulating space in nm
simulatingSpaceTotalStep = 400 # total simulating steps

##################### Basic setting ####################
U_a = 18e3      # eV    Accelerating Voltage
U_o = 10        # ev    Electron Voltage
C_c = 59.8e-3   # m     1st order, 1st degree Chromatic Aberration Coefficient   
C_3c = 0        # m     3rd order, 1st degree Chromatic aberration coefficient
C_cc = 0        # m     1st order, 2nd degree Chromatic aberration coefficient
C_3 = 55.8e-3   # m     3rd order Spherical Aberration Coefficient
C_5 = 0         # m     5th order Spherical Aberration Coefficient
#
alpha_ap = 4.15e-3      # rad   Acceptance Angle of the Contrast Aperture
alpha_ill = 0.25e-3     # rad   Illumination Divergence Angle
#
delta_E = 0.5     # eV    Energy Spread
M_L = 1         #       Lateral Magnification
##################### Basic setting ####################

##################### AC Constants######################
# U_a = 10.01e3  # eV  Accelerating Voltage
# U_o = 10  # eV  Electron Voltage
# C_c = 0  # m   Chromatic Aberration Coefficient
# C_3c = -67.4
# C_cc = 27.9
# C_3 = 0  # m   Spherical Aberration Coefficient
# C_5 = 92.8
#
# alpha_ap = 7.37E-3  # rad Acceptance Angle of the Contrast Aperture
# alpha_ill = 0.1E-3  # rad Illumination Divergence Angle
#
# delta_E = 0.25  # eV  Energy Spread
# M_L = 0.653  # Lateral Magnification
##################### AC Constants######################


# ##################### NAC Constants######################
# U_a = 15.01e3  # eV  Accelerating Voltage
# U_o = 10  # eV  Electron Voltage
# C_c = -0.075  # m   Chromatic Aberration Coefficient
# C_3c = -59.37
# C_cc = 23.09
# C_3 = 0.345  # m   Spherical Aberration Coefficient
# C_5 = 39.4
#
# alpha_ap = 2.34E-3  # rad Acceptance Aangle of the Contrast Aperture
# alpha_ill = 0.1E-3  # rad Illumination Divergence Angle
#
# delta_E = 0.25  # eV  Energy Spread
# M_L = 0.653  # Lateral Magnification
# ##################### NAC Constants######################

#############convert defocus_current into delta_z#############
# defocus_current_series = np.linspace(-7, 7, 71)  # mA
# delta_zo_series = defocus_current_series * 5.23 * 10 ** -6
# delta_z_series = delta_zo_series * 3.2
#############convert defocus_current into delta_z#############

##################directly use delta_z#############
delta_z_series = np.linspace(-200E-6, 200E-6, 101)
##################directly use delta_z#############

##################single delta_z#################
# delta_z_series = [0]
##################single delta_z#################
# print(delta_z_series)
    
###################################################################
delta_fc = C_c * (delta_E / U_a)
delta_f3c = C_3c * (delta_E / U_a)
delta_fcc = C_cc * (delta_E / U_a) ** 2

lamda = 6.6262e-34 / np.sqrt(2 * 1.6022e-19 * 9.1095e-31 * U_a)
lamda_o = 6.6262e-34 / np.sqrt(2 * 1.6022e-19 * 9.1095e-31 * U_o)
q_max = alpha_ap / lamda
q_ill = alpha_ill / lamda
