import random

class Particle:
    '''Simplified particle class from the template file provided, has parameters for Equilibrium, and max and min displacement values, between which the displacement is calculated 
    based on a random number generator, for the purpose of this it does not have to be truly random, as the range is small and values of displacement themselves are used to calculate force,
    not the randomness of the number.
    The update time function simply adds to the initial value of time of the particle which is 0, meaning every step of the simulation the time increases by 1.'''

    
    def __init__(self, Equilibrium=0 ,maxD=0 ,minD=0, Name='', Mass=1.0,Time=0):

        self.equilibrium = Equilibrium
        self.maxD=maxD
        self.minD=minD
        self.name = Name
        self.mass = Mass
        self.update_displacement()
        self.time= Time
    def __repr__(self):
        return ' Particle: {0}, Mass: {1}, Equilibrium: {2}, New Position: {3}, Time = {4}\n'.format(self.name,self.mass,self.equilibrium,self.displacement,self.time)
        #Format for output of the values of each atom in the chain in the nbodysystem file.
    def update_displacement(self):
        self.displacement= random.randrange(self.maxD, self.minD, 1)

    def update_time(self):
        self.time = self.time + 1