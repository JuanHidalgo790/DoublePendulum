# DoublePendulum
Code to simulate the dynamics of a double pendulum with two masses.

## Problem

A double pendulum consisting of two bars, without weight, linking two masses $m_{1}$ and $m_{2}$.

![DoublePendulumFigure](https://github.com/user-attachments/assets/6b5305c5-9738-41c6-831c-0379659b78f8)


The dynamic of this system is given by two ODEs

$$(m_{1}+m_{2})(l_{1} \ddot{\theta}_ {1}+g\sin{\theta_{1}})+m_{2} l_{2}\[\ddot{\theta} _{2} cos{(\theta _{1}-\theta _{2})}+\dot{\theta}^{2} _{2} \sin{(\theta _{1}-\theta _{2})}\]=0$$

$$m _{2} l _{2} \ddot{\theta} _{1} +m _{2} l _{1} \[\ddot{\theta} _{1} cos{(\theta _{1}-\theta _{2})}-\dot{\theta}^{2} _{1} \sin{(\theta _{1}-\theta _{2})}\]+ m _{2} g\sin{\theta _{2}}=0$$

Giving the parameters and the appropriate initial conditions, we get the animation, the dynamic plots, and the phase diagrams!



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
