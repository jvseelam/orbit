import math
import numpy as np
import matplotlib.pyplot as plt


# Initial time, x,y position and x,y velocities
t = 0.0
x = 5.0
y = 0.0
u = 0.0
v = 50.0

steps = 127  # Number of points along the orbit
dt = 1/100  # Change in time or time step
tttl = steps*dt  # Total time of integration

"""
Sources:
http://farside.ph.utexas.edu/teaching/336k/Newtonhtml/node28.html
http://www.astro.utu.fi/~cflynn/galdyn/lecture6.html

Consider a particle of mass $m$ moving in the two-dimensional 
harmonic potential 

U(x,y) = U(r) = 1/2*k*r^2, 
where r = sqrt(x^2+y^2), k>0 constant.


The particle is subject to this force:
F(r) = $nabla$(U) = m*(d²r/dt²) = -k*r


Then written in component form (x, y components individually):
d²x/dt² = -$omega$²x = -kx/m

similarly for y, where
$omega$ = sqrt(k/m) (units are kg(¹/²)metres⁻(¹/²)second⁻¹ )

The period T = 2*pi/omega
 
 """

omega = 5.0
# The period would be 2*pi/5 =1.257 seconds


""" Simple harmonic oscillator potential energy gives forces in
x, -y directions. Note, strictly speaking, this is actually
force/mass or acceleration rather than just force."""


def fx(x):
    return -x*omega**2


def fy(y):
    return -y*omega**2


# Arrays which store our numerical approximation points
xs = np.zeros(steps)
ys = np.zeros(steps)


for i in range(0, steps):
    xs[i] = x
    ys[i] = y

    t += dt
    x += dt*u
    u += dt*fx(x)  # Actually it's dt*acceleration
    y += dt*v
    v += dt*fy(y)

lines = plt.plot(xs, ys)
plt.setp(lines, color='r', marker='.')  # , mew='0.001')
# mew is markeredgewidth


"""The following three lines define parameters which
define the actual ellipse path"""
# eps_x, eps_y = -math.pi/2
# Ax = 5.0
# Ay = 10.0

"""These are each points which lie on the actual ellipse"""
# xtrue = Ax * math.sin(omega * t - eps_x)
# ytrue = -Ay * math.cos(omega * t - eps_y)
