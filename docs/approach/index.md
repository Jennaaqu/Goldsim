---
layout: default
title: Approach
nav_order: 4
---

# 1. The models

## 1.1. The metabolic model:

$$
\begin{align*}
   \frac{dB}{dt}&=&r_{max}H_{O_2}H_{DOC}H_{eDAR}B - dBP \\
   \frac{dP}{dt}&=&c\mu_p \big[1 - \mathcal{P}(L)\big]I - dBP - mP + c\mu_i L \\
   \frac{dI_n}{dt}&=&dBP - \big[1 - \mathcal{P}(L) \big] I - \mathcal{P}(L)I \\
   \frac{dL}{dt}&=&rH_{O_2}H_{DOC}H_{eDAR}L + dI_nP - \mu_i L \\
\end{eqnarray*}
$$

## 1.2. The coinfection model:

$$
\begin{align*} 
   \frac{dB}{dt}&=&\underbrace{r\big(1- \frac{N}{K}\big)B}_{\text{growth}} - \underbrace{dBP}_{\text{infection}} \\
   \frac{dP}{dt}&=&\underbrace{c\mu_p(B,L)I_p}_{\text{burst function}} - \underbrace{dBP}_{\text{Infection}} - \underbrace{dI_nP}_{\text{coinfection}} - \underbrace{mP}_{\text{viral decay}} \\
   \frac{dI_n}{dt}&=&\underbrace{dBP}_{\text{infection}} - \underbrace{dI_nP}_{\text{coinfection}} - \underbrace{\mu_{ld}(B,L)I_n}_{\text{Infected to $\Phi$ prod.}} \\
   \frac{dI_p}{dt}&=&\underbrace{\mu_{ld}(B,L)I_n}_{\text{Infected to $\Phi$ prod.}} - \underbrace{\mu_p(B,L)I_p}_{\text{lysed cells}} + \underbrace{\mu_i L}_{\text{induction}} \\
   \frac{dL}{dt}&=&\underbrace{r\big(1- \frac{N}{K}\big)L}_{\text{growth}} + \underbrace{dI_nP}_{\text{coinfection}} - \underbrace{\mu_i L}_{\text{induction}} \\
\end{align*}
$$

$$
\begin{align*} 
\frac{dL}{dt}&=\underbrace{r\bigg(1 - \frac{L}{K}\bigg)}_{\text{Logistic growth}} - \underbrace{\mu_i L}_{\text{Induction}} - \underbrace{\delta dT}_{\text{Infection}}& \\
\frac{dT}{dt}&=\underbrace{\mu_i L}_{\text{Induction}} - \underbrace{m T}_{\text{Decay}} - \underbrace{d TL}_{\text{Infection}}&
\end{align*} $$

This model assumes the existence of two bioagents (Lysogens and Temperate phages) that can undergo the following processes: Lysogen logistic growth, lysogen induction, lysogen reinfection, viral burst, and viral decay. As a first approximation, let us assume that lysogens are totally immune against infections ($$\delta=0$$). This yields the simplified model:

$$
\begin{align*} 
\frac{dL}{dt}&=\underbrace{r\bigg(1 - \frac{L}{K}\bigg)}_{\text{Logistic growth}} - \underbrace{\mu_i L}_{\text{Induction}}& \\
\frac{dT}{dt}&=\underbrace{\mu_i L}_{\text{Induction}} - \underbrace{m T}_{\text{Decay}}&
\end{align*}$$

The processes considered in the model are controlled by the parameters shown in this table:

| Parameter | Description | Value| Source|
| ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |0.471 (wild type), 0.382 (spot- mutant)  | Experiment data |
| K | Carrying capacity |8.2x10 7 (Wild type), 1x10 8 (mutant)  | Concentrations of bacteria at the end of the experiments without CX  |
| $$\mu_i$$ | Induction rate |spoT-: 8.481e-12, WT + CX: 5.793e-09, spoT- + CX: 1.814e-09, WT: 3.993e-11 | Experiment results  |
| $$\delta$$ | Probability of lysogen infection | 0 |  |
| d | Infection rate | 0 |  |
| c | Burst size | 125 |Da. Paepe et al, 2006  |
| m | Decay rate | 0.012h<sup>-1</sup>| Da Paepe et al, 2006  |

Our first step will be to try to fit the experimental data to this model.
