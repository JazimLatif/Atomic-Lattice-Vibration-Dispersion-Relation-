import numpy as np
from Particle import Particle
import copy
import random
from termcolor import colored
import matplotlib.pyplot as plt

a=25 #Lattice Constant (Space between adjacent M1 particles)
C=1 #Spring Constant (arbirtrary value)
Mass1 = 1 #Value of Mass for all monatomic particles and 3 M1 Diatomic particles
Mass2 = 0.5 #Diatomic M2 Mass
time = 0 #initial time


Monatomic_M1 = Particle(-2*a, (-2*a)-5,(-2*a)+5,'Test1', Mass1)
Monatomic_M2 = Particle(-1*a, (-1*a)-5, (-1*a)+5,'Test2', Mass1)
Monatomic_M3 = Particle(0*a,(0*a)-5, (0*a)+5,'Test3', Mass1)
Monatomic_M4 = Particle(1*a, (1*a)-5, (1*a)+5,'Test4', Mass1)
Monatomic_M5 = Particle(2*a, (2*a)-5, (2*a)+5,'Test5', Mass1)
#Monatomic particle values, equilibriums and displacement limits explained in report

Diatomic_M1 = Particle(-2*a,(-2*a)-5,(-2*a)+5,'Test1', Mass1)
Diatomic_M2 = Particle(-1*a, (-1*a)-5, (-1*a)+5,'Test2', Mass2)
Diatomic_M3 = Particle(0*a,(0*a)-5,(0*a)+5,'Test3', Mass1)
Diatomic_M4 = Particle(1*a,(1*a)-5,(1*a)+5,'Test4', Mass2)
Diatomic_M5 = Particle(2*a, (2*a)-5, (2*a)+5,'Test5', Mass1)
#Diatomic particle values, alternating mass with same positions and displacement limits.

#chain=[Monatomic_M1, Monatomic_M2, Monatomic_M3, Monatomic_M4, Monatomic_M5] #Monatomic chain 
chain=[Diatomic_M1, Diatomic_M2, Diatomic_M3, Diatomic_M4, Diatomic_M5] #Diatomic chain
 
 #When switching between simple monatomic and more advanced diatomic simulation, simply comment the undesired chain out.

data=[] #array to append values to for savedata plotting.

class nBodySystem:
    '''The nBodySystem class is similar to that of the 281 module for the solar system, instead of calculating the acceleration of the particles using the euler cromer method,
    it uses a sliding window to assign each particle an 'n' value for which the equations of motion attempt to be solved.
    it uses a chain of atoms given above as an array.'''
    def __init__(self, chain):
        self.chain = np.array(chain)
    def __repr__(self):
        result = ""
        for System in self.chain:
            result += f"{str(System)}\n"
        return result

    def simulate(self):
        '''Every time the chain is simulated, update its displacement and time (in the Particle class)
        The 2nd for loop 'zips' 3 chains together and takes the n-1, n and n+1 elements starting from the left where the second particle is n
        it then prints the information of the particle, where the middle 'n' particle is highlighted green
        it then calculates the omega value (same for all particles as modelled as infinite chain) using the k value which can be changed
        It then calculates the value of force acting on the nth particle using Hooke's Law 
        The last step would be to calculate the acceleration using the complex wave solution given in the report, this proved too challenging to code however, so is commented out for now'''
        for atom in self.chain:
            atom.update_displacement() 
            atom.update_time()
            #Every time 
        for Unminus1, Un, Unplus1 in zip(chain[0:-1], chain[1:-1], chain[2:]):
            print(Unminus1, colored(Un, 'green'), Unplus1)
            #This is the sliding window to move across the chain and print values of particles.
            k= 1*np.pi/a 
            omega=((4*C/Mass1)**0.5)*abs(np.sin(k*a/2))
            print ("\u03C9 =",omega)
            #This is the dispersion relation of the chain of infinite atoms, printing the omega value. The number N of Npi/A can be changed to any number to give the omega value at that point.
        

            Hooke=C*(Unplus1.displacement-(2*Un.displacement)+Unminus1.displacement)
            print(Hooke,"Newtons is the force equal to Hookes law\n" )
            #Using the randomly generated displacements of the particle, the force acting upon it to the left and right via Hookes law is calculated


            #Acceleration=omega**2(A*np.e**i(k*n*a-omega*time))
            #N2L=Mass1*Acceleration
            #print(N2L,"is the force equal to Newton's second law" )
            
            


system=nBodySystem(chain) #System is simulated below using the nBodySystem Class.

RUNTIME=10 #how many times the program should run
for i in range (RUNTIME):
    system.simulate()   
    item = [time,copy.deepcopy(chain)]
    data.append(item)
np.save('savechain',data,allow_pickle=True)   

#The above code runs the system for the desired length of time and saves the data to an array called 'data', which is stored in savechain to be read by the Graphs file.