import matplotlib.pyplot as plt
import numpy as np
import math
from nbodysystem import nBodySystem

#######################################################################################################################################################################''
#CONSTANTS AND EMPTY LISTS

a=25
C=1
Mass1=1
Mass2=0.5

positions=[]
#######################################################################################################################################################################
#Graph 1 Monatomic Dispersion Relation (plots the graph we should see for an infinite monatomic chain with dotted lines at multiples of k)

k= np.arange(-2.5*np.pi/a, 2.5*np.pi/a, 0.001)
omega=((4*C/Mass1)**0.5)*abs(np.sin(k*a/2))
plt.grid(True, which='both')
plt.xlabel('k (wave number)')
plt.ylabel('\u03C9 (frequency)')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.axvline(x=np.pi/a, color='k', linestyle='--')
plt.axvline(x=-1*np.pi/a, color='k', linestyle='--')
plt.axvline(x=2*np.pi/a, color='k', linestyle='--')
plt.axvline(x=-2*np.pi/a, color='k', linestyle='--')
plt.plot(k,omega)
plt.savefig('Monatomic Dispersion Relation')
plt.show()
#######################################################################################################################################################################
#Graph 1 Diatomic Dispersion Relation (plots the graph we should see for an infinite diatomic chain with dotted lines at multiples of k)

k2= np.arange(-2*np.pi/a, 2*np.pi/a, 0.01)
inverse_sum_mass = (1/Mass1)+(1/Mass2)
omega2=((C*inverse_sum_mass)+C*((inverse_sum_mass**2-((4*(np.sin(k2*a/2))**2)/(Mass1*Mass2)))**0.5))**0.5
omega3=((C*inverse_sum_mass)-C*((inverse_sum_mass**2-((4*(abs(np.sin(k2*a/2)))**2)/(Mass1*Mass2)))**0.5))**0.5
plt.grid(True, which='both')
plt.title("Diatomic Dispersion Relation")
plt.xlabel('k (wave number)')
plt.ylabel('\u03C9 (frequency)')
plt.xlim(-2*np.pi/a, 2*np.pi/a)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.axvline(x=np.pi/a, color='k', linestyle='--')
plt.axvline(x=-1*np.pi/a, color='k', linestyle='--')
plt.axhspan(((2*C/Mass1)**0.5),((2*C/Mass2)**0.5), color='green', alpha=0.5)
plt.plot(k2,omega2,k2,omega3)
plt.savefig('Dispersion Relation Diatomic.jpg')
plt.show()

#######################################################################################################################################################################
#Graph 3 Particle Vibration 

Data=np.load('savechain.npy',allow_pickle=True)

def findPosition(Data,index):
    positions=[]    
    for atom in iteration[1]:
        positions.append(atom.displacement)
    return(positions)
#this was to find the location of the displacements when looking through the file, appending it to the positions list which is below.

for iteration in Data:
    positions.append(findPosition(Data,iteration))



plt.plot(positions,list(range(1,11)))

for equilibriumlines in range(3):
    plt.axvline(x=-1*equilibriumlines*a, color='k', linestyle='--')
    plt.axvline(x=+1*equilibriumlines*a, color='k', linestyle='--')
    equilibriumlines+=equilibriumlines
#This chunk of code saves copy pasting the same line multiple times for different values of equilibrium, to expand to an infinite chain would simply be changing the range number
#It puts a dotted line at negative and positive multiples of a
#Just more efficient than having 5 lines of code for 5 particles, this makes it easier to expand the chain.
plt.title("Graph showing the vibration of atoms")
plt.xlabel("position of atom")
plt.ylabel("time")
plt.savefig('PositionGraph.jpg')
plt.show()



#######################################################################################################################################################################

#Graph to visualise complex wave function obtained from https://notebook.community/JoseGuzman/myIPythonNotebooks/SignalProcessing/Sine%20waves%20and%20complex%20waves
#this was for my own understanding, included for completeness.

t = np.arange(0,np.pi, 1/30000)

freq = 2 # in Hz
phi = 0
amp = 1
k = 2*np.pi*freq*t + phi

cwv = amp * np.exp(-1j* k) # complex sine wave

fig, ax = plt.subplots(2,1, figsize=(8,4), sharex=True)
ax[0].plot(t, np.real(cwv), lw=1.5)
ax[0].plot(t, np.imag(cwv), lw=0.5, color='orange')
ax[0].set_title('real (cosine)', color='C0')

ax[1].plot(t, np.imag(cwv), color='orange', lw=1.5)
ax[1].plot(t, np.real(cwv), lw=0.5, color='C0')
ax[1].set_title('imaginary (sine)', color='orange')

for myax in ax:
    myax.set_yticks(range(-2,2,1))
    myax.set_xlabel('Time (sec)')
    myax.set_ylabel('Amplitude (AU)')

plt.show()