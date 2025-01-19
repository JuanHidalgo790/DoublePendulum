import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

## Double Pendulum System 

###########################################################################################################
# Coded by Juan Andrés Santisteban Hidalgo, PhD
###########################################################################################################
############### Parameters ################################################################################

L1 = 1   # length of bar 1 [m]
L2 = 1   # length of bar 2 [m]
m1 = 1   # mass 1 [kg]
m2 = 1   # mass 2 [kg]
g = 9.81 # gravity [m/s^2]

## Simulation time ########################################################################################
t0 = 0  # initial time [s]
tf = 10 # final time [s]
delta_t = 0.01                          # time step [s]
nt = int(np.round(tf/delta_t))          # number of time steps
tspan = np.linspace(t0, tf, nt)         # time span [s]

## Initial Conditions ######################################################################################
theta1 = np.pi/4        # initial angle of bar 1 [rad]
theta2 = 2*np.pi/4      # initial angle of bar 2 [rad]
dtheta1 = 0             # initial angular velocity of bar 1 [rad/s]
dtheta2 = -np.pi/4      # initial angular velocity of bar 2 [rad/s]

Y0 = [theta1, theta2, dtheta1, dtheta2]                       # initial conditions vector
###########################################################################################################
###########################################################################################################

def doublePendulum(t, y):

    n = 2
    M = np.array([[(m1+m2)*L1, m2*L2*np.cos(y[0]-y[1])],[m2*L1*np.cos(y[0]-y[1]), m2*L2]])
    G = np.array([[0, m2*L2*y[3]*np.sin(y[0]-y[1])],[-m2*L1*y[2]*np.sin(y[0]-y[1]), 0]])
    A = np.block([[np.zeros((n,n)), np.eye(n)],[np.zeros((n,n)), -np.matmul(np.linalg.inv(M),G)]])
    B = np.block([[np.zeros((n,n))],[np.linalg.inv(M)]])
    F = np.array([-(m1+m2)*g*np.sin(y[0]), -m2*g*np.sin(y[1])])
    dy = np.matmul(A,y)+np.matmul(B,F)

    return np.transpose(dy)

Y = np.zeros((len(tspan), len(Y0)))   # array for solution
Y[0, :] = Y0

r = integrate.ode(doublePendulum).set_integrator("dopri5")  # choice of method
r.set_initial_value(Y0, tspan[0])   # initial values
for i in range(1, tspan.size):
   Y[i, :] = r.integrate(tspan[i]) # get one more value, add it to the array
   if not r.successful():
       raise RuntimeError("Could not integrate")

## Animation of the double pendulum
def pendulum_animation(T1, Y1):
    global L1, L2
    N = len(T1)

    plt.figure()
    for i in range(N):
        plt.plot([0, L1 * np.sin(Y1[i, 0])], [0, -L1 * np.cos(Y1[i, 0])], 'r', linewidth=2)
        plt.plot([L1 * np.sin(Y1[i, 0]), L1 * np.sin(Y1[i, 0]) + L2 * np.sin(Y1[i, 1])],
                 [-L1 * np.cos(Y1[i, 0]), -L1 * np.cos(Y1[i, 0]) - L2 * np.cos(Y1[i, 1])], 'r', linewidth=2)
        plt.xlim([-(L1 + L2), (L1 + L2)])
        plt.ylim([-(L1 + L2), 0])
        plt.pause(0.05)
        plt.clf()

pendulum_animation(tspan,Y)

# plot of the dynamic response of mass 1
fig, ax = plt.subplots()
plt.plot(tspan, Y[:,0],'r')
ax.set_title('Dynamic Response of Mass 1')
ax.set_xlabel('t [s]')
ax.set_ylabel('x(t) [m]')
ax.grid()
ax.set_axisbelow(True)

# plot of the phase diagram of mass 1
fig, ax = plt.subplots()
plt.plot(Y[:,0], Y[:,2], 'g')
ax.set_title('Phase Diagram of Mass 1')
ax.set_xlabel('x(t) [m]')
ax.set_ylabel('xdot(t) [m/s]')
ax.grid()
ax.set_axisbelow(True)

# plot of the dynamic response of mass 2
fig, ax = plt.subplots()
plt.plot(tspan, Y[:,1],'r')
ax.set_title('Dynamic Response of Mass 2')
ax.set_xlabel('t [s]')
ax.set_ylabel('x(t) [m]')
ax.grid()
ax.set_axisbelow(True)

# plot of the phase diagram of mass 2
fig, ax = plt.subplots()
plt.plot(Y[:,1], Y[:,3], 'g')
ax.set_title('Phase Diagram of Mass 2')
ax.set_xlabel('x(t) [m]')
ax.set_ylabel('xdot(t) [m/s]')
ax.grid()
ax.set_axisbelow(True)

plt.show()
