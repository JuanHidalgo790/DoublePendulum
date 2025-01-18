# DoublePendulum
Code to simulate the dynamics of a double pendulum with two masses.

## Problem

A double pendulum consisting of two bars, without weight, linking two masses $m_{1}$ and $m_{2}$.

![DoublePendulumFigure](https://github.com/user-attachments/assets/6b5305c5-9738-41c6-831c-0379659b78f8)


The dynamic of this system is given by two ODEs

$$(m_{1}+m_{2})l_{1}(l_{1} \ddot{\theta}_ {1}+g\sin{\theta_{1}})+m_{2} l_{1} l_{2}\[\ddot{\theta} _{2} cos{(\theta _{1}-\theta _{2})}+\dot{\theta}^{2} _{2} \sin{(\theta _{1}-\theta _{2})}\]=0$$

$$m _{2} L _{2} \ddot{\theta} _{1} +m _{2} l _{1} l _{2}\[\ddot{\theta} _{1} cos{(\theta _{1}-\theta _{2})}-\dot{\theta}^{2} _{1} \sin{(\theta _{1}-\theta _{2})}\]+ m _{2} l _{2}g\sin{\theta _{2}}=0$$

Giving the parameters and the appropriate initial conditions, we get the animation, the dynamic plots, and the phase diagrams!

![DoublePendulumAnimation](https://github.com/user-attachments/assets/a4c06ce3-de69-459f-8b84-a8531d59c398)


![DoublePendulumDynamicResponseBar1](https://github.com/user-attachments/assets/a8655ed6-88c0-42d9-ae98-6fce0f142d78)
![DoublePendulumPhaseDiagramBar1](https://github.com/user-attachments/assets/f5cb7a36-de21-44b0-b6ab-c9fc9c8ef8b5)
![DoublePendulumDynamicResponseBar2](https://github.com/user-attachments/assets/a63df65a-4b0f-421a-b070-db172b53f855)
![DoublePendulumPhaseDiagramBar2](https://github.com/user-attachments/assets/fc2da819-7a95-4237-bd3b-486d4777c706)

## Input Parameters

$m_{1}$ - mass 1 [kg]

$m_{2}$ - mass 2 [kg]

$l_{1}$ - length of bar 1 [m]

$l_{2}$ - length of bar 2 [m]

## Time of the simulation

$t_{0}$ - initial time [s]

$t_{f}$ - final time [s]

$\Delta t$ - timestep [s]

## Initial Conditions

$\theta_{1}^{0}$ - initial angle 1 [rad]

$\theta_{2}^{0}$ - initial angle 2 [rad]

$\dot{\theta}_{1}^{0}$ - initial angular velocity 1 [rad/s]

$\dot{\theta}_{2}^{0}$ - initial angular velocity 2 [rad/s]
