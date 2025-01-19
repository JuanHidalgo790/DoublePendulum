# DoublePendulumMasses
Code to simulate the dynamics of a double pendulum with two masses.

## Problem

A double pendulum consisting of two bars, without weight, linking two masses $m_{1}$ and $m_{2}$.


![figura_massas_thetas](https://github.com/user-attachments/assets/17d609ad-c9c4-4789-ab1c-304e018abe0f)


The dynamic of this system is given by two ODEs

$$(m_{1}+m_{2})L_{1} \ddot{\theta}_ {1} +m_{2} L_{2} \cos{(\theta _{1}-\theta _{2})} \ddot{\theta} _{2} +m _{2} L _{2} \sin{(\theta _{1}-\theta _{2})} \dot{\theta}^{2} _{2} +(m _{1} + m _{2})g\sin{\theta _{1}}=0$$

$$ m _{2} L _{1} \cos{(\theta _{1}-\theta _{2})} \ddot{\theta} _{1} + m _{2} L _{2} \ddot{\theta} _{2} -m _{2} L _{1} \sin{(\theta _{1}-\theta _{2})}\dot{\theta}^{2} _{1} + m _{2} g \sin{\theta _{2}}=0$$

Giving the parameters and the appropriate initial conditions, we get the animation, the dynamic plots, and the phase diagrams!

![DoublePendulumMassesAnimation](https://github.com/user-attachments/assets/9e7b548c-3c28-49f8-9782-f75d8fc9a157)


![DoublePendulumDynamicResponseMass1](https://github.com/user-attachments/assets/acc3b37d-76fb-4ac4-9e37-3c74dffe681a)
![DoublePendulumPhaseDiagramMass1](https://github.com/user-attachments/assets/90ff2668-cd6f-4d4f-bd68-a0536ed7fc35)
![DoublePendulumDynamicResponseMass2](https://github.com/user-attachments/assets/d8181a1a-b8c9-4884-b40d-c649e13655aa)
![DoublePendulumPhaseDiagramMass2](https://github.com/user-attachments/assets/a1ed7425-a9a7-4e71-bf17-3480bf7a8907)

## Input Parameters

### Constants

$m_{1}$ - mass 1 [kg]

$m_{2}$ - mass 2 [kg]

$l_{1}$ - length of bar 1 [m]

$l_{2}$ - length of bar 2 [m]

### Time of the simulation

$t_{0}$ - initial time [s]

$t_{f}$ - final time [s]

$\Delta t$ - timestep [s]

### Initial Conditions

$\theta_{1}^{0}$ - initial angle 1 [rad]

$\theta_{2}^{0}$ - initial angle 2 [rad]

$\dot{\theta}_{1}^{0}$ - initial angular velocity 1 [rad/s]

$\dot{\theta}_{2}^{0}$ - initial angular velocity 2 [rad/s]
