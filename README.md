# LEEM Image Simulation with Fourier Optics

This is a simulation program written in python that help user to simulate sample viewed in Low Energy Electron Microscopy (LEEM) using Fourier Optics (FO). The method and mathematical derivation are documented at [here](https://www.sciencedirect.com/science/article/abs/pii/S0304399118304418).


# Package Requirements
- Python 3.6+
- joblib 0.13.2+
- numba 0.41.0+
- scipy 1.3.1+
- numpy 1.16.4+

# Simulation Setup
Users can match the simulation with their LEEM setting by tuning constants and sample in the program.

## 2D FO Simulation Setup
In 2D FO Simulation, user can setup the constants in `FO2Dconstants.py`.  
Documentation of constants are listed [here](https://github.com/klwlau/LEEM-Fourier-Optics/blob/master/docs/FO2Dconstants.md).

To setup the sample in the simulation user can specify in `FO2Dsample.py`.  
Documentation of sample setup are listed [here](https://github.com/klwlau/LEEM-Fourier-Optics/blob/master/docs/FO2Dsample.md).

## 1D FO Simulation Setup
In 1D FO Simulation, user can setup the constants in `FO1Dconstants.py`.  
Documentation of constants are listed [here](https://github.com/klwlau/LEEM-Fourier-Optics/blob/master/docs/FO1Dconstants.md).

To setup the sample in the simulation user can specify in `runFO1DSimulation.py`.  
Documentation of sample setup are listed [here](https://github.com/klwlau/LEEM-Fourier-Optics/blob/master/docs/FO1Dsample.md).


## Program Execution

After the config, user can run the software in terminal ***or by other editor/IDE***:

```
python runFO2DSimulation.py
```

or, running 1D FO simulation

```
python runFO1DSimulation.py
```


## Simulation Output
Two `.npy` files are saved after the simulation. 
- `simObject_<Time Stamp>.npy` for simulated sample.
- `result_<User Note>_<TimeStamp>.npy` for simulated result.

# Terms of use

