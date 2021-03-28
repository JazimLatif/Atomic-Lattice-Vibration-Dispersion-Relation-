HOW TO WORK THE SIMULATION:

RUN nBodySystem and you can see the particle data (main simulation) (can change from monatomic to diatomic by changing the chain on line 29 and 30)
RUN Graphs to see the graphs which use the nbody system data (also shown in report)
RUN test_sample to see the tests work for omega values as desired.
Running particle class does nothing

EXPLANATION OF EACH FILE:

First.py: Simple Hello World file to test github functioning as expected
Graphs.py: File to print the graphs used to show the expected dispersion relations for monatomic and diatomic system.
Particle.py: The particle class all of the atoms use to simulate their vibration and time in order to find the force acting on them.
nBodySystem.py: The simulation file which saves the sliding window calculations to a savedata deepcopy file in order to print the graph of particle vibration.
test_sample.py: 1 initial test to check pytest functioning as intended, function containing tests for numerical values for simple and more complex diatomic omega values.

Thank you