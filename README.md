# Planar 2-DOF Robot Arm Control
### Approximate model of a 2-segment prosthetic limb

---

## Overview

This project simulates the control of a **planar 2-DOF robot arm** as an approximate model of a prosthetic limb (forearm + hand) reaching a target point in 2D space — for example, grasping an object on a table.

The arm solves the **inverse kinematics problem** using **gradient descent** on a cost function defined as the squared Euclidean distance between the current end-effector position and the target.

---

## How it works

```
Initial configuration → Forward Kinematics → Cost Function → Gradient → Update angles → Repeat
```

1. **Forward Kinematics** — computes the end-effector (TCP) position from joint angles
2. **Cost Function** — measures squared distance between TCP and target
3. **Jacobian** — analytical partial derivatives of TCP position w.r.t. joint angles
4. **Gradient Descent** — iteratively updates joint angles to minimize the cost
5. **Stopping Criterion** — algorithm stops when cost < tolerance

---

## System Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| L1 | 0.30 m | Forearm length |
| L2 | 0.18 m | Hand length |
| Max reach | 0.48 m | L1 + L2 |
| Target | [0.35, -0.10] m | Object on table |
| Learning rate | 0.08 | Gradient descent step size |
| Tolerance | 0.001 | Stopping criterion |

---

## Results

| | Value |
|---|---|
| Initial distance² | ~0.15 |
| Final distance² | <0.001 |
| Convergence | ✓ |

**Initial configuration** — arm in resting position, far from target

**Final configuration** — arm reaches the target point

---

## Requirements

```
Python 3.x
matplotlib
math (standard library)
my_functions.py (plot_robot_arm utility)
```

---

## Run

```bash
python robotic_arm_control.py
```

---

## Author

**Simone Palazzi**
BSc Automation & Control Engineering — Politecnico di Milano

