import pytest
from nbodysystem import nBodySystem
from nbodysystem import a,C,Mass1,Mass2
import numpy as np 

def increase(x):
    return x + 1

def test_answer():
    assert increase(3)==4
# above 2 functions testing if pytest works, when 4 is changed to 5 the test fails as expected.
def dispersion(k):
    omega=((4*C/Mass1)**0.5)*abs(np.sin(k*a/2))
    return omega
    #function to return omega values for different values of k tested below
def test_omega1():
    assert dispersion(np.pi/a)==2.0
    #2 is the value we expect as Root(4*1/1) is root 4 ==2
def test_omega2():
    assert dispersion(np.pi/a)==2.5
    #we still expect 2, so this test should fail, which it does telling us that the correct value is being tested.
def test_omega3():
    assert dispersion(2*np.pi/a)==0
    #For this value of k we expect 0, as it is a trough in the sin curve. This test surprisingly fails due to pi not being a floating point number, talked about in the report.
def diatomic_dispersion1(k2):
    inverse_sum_mass = (1/Mass1)+(1/Mass2)
    omega2=((C*inverse_sum_mass)+C*((inverse_sum_mass**2-((4*(np.sin(k2*a/2))**2)/(Mass1*Mass2)))**0.5))**0.5
    return omega2
    #Returns the acoustic branch of diatomic lattice
def diatomic_dispersion2(k2):
    inverse_sum_mass = (1/Mass1)+(1/Mass2)
    omega3=((C*inverse_sum_mass)-C*((inverse_sum_mass**2-((4*(abs(np.sin(k2*a/2)))**2)/(Mass1*Mass2)))**0.5))**0.5
    return omega3
    #Returns the optical branch of diatomic lattice
def test_diatomic_omega_acoustic1():
    assert diatomic_dispersion2(0)==0
    #Testing the trough of the acoustic branch
def test_diatomic_omega_optical1():
    assert diatomic_dispersion1(0)==6**0.5
    #Testing the trough of the optical branch
def test_diatomic_omega_acoustic2():
    assert diatomic_dispersion2(np.pi/a)==2**0.5
    #Testing the peak of the acoustic branch
def test_diatomic_omega_optical2():
    assert diatomic_dispersion1(np.pi/a)==2
    #Testing the peak of the optical branch



