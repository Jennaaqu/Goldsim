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
\end{align*}
$$

| Parameter | Description | Value| Source|
| ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |0.471 (wild type), 0.382 (spot- mutant)  | Experiment data |
| H | Hill functions |8.2x10 7 (Wild type), 1x10 8 (mutant)  | Concentrations of bacteria at the end of the experiments without CX  |
| d | Infection rate | 0 |  |
| $$\mathcal{P}(L)$$ | Probability of lysogeny | 0 |  |
| $$\mu_i$$ | Induction rate |  |   |
| $$\delta$$ | Probability of lysogen infection | 0 |  |
| c | Burst size | 125 |Da. Paepe et al, 2006  |
| m | Decay rate | 0.012h<sup>-1</sup>| Da Paepe et al, 2006  |

## 1.2. The coinfection model:

$$
\begin{align*} 
   \frac{dB}{dt}&=&\underbrace{r H_{O_2}H_{DOC}H_{eDAR}B}_{\text{growth}} - \underbrace{dBP}_{\text{Infection}} \\
   \frac{dP}{dt}&=&\underbrace{c\mu_p \big[1 - \mathcal{P}(L)\big]I_n}_{burst} - \underbrace{dBP}_{\text{infection}} - \underbrace{mP}_{\text{viral decay}} + \underbrace{c\mu_i L}_{\text{burst induction}} \\
   \frac{dI_n}{dt}&=&\underbrace{dBP}_{\text{Infection}} - \underbrace{\big[1 - \mathcal{P}(L) \big] I_n}_{\text{lysis}} - \underbrace{\mathcal{P}(L) I_n}_{lysogeny} \\
   \frac{dL}{dt}&=&\underbrace{rH_{O_2}H_{DOC}H_{eDAR}L}_{\text{growth}} + \underbrace{\mathcal{P}(L)I_n }_{\text{lysogeny}} - \underbrace{\mu_i L}_{\text{induction}} \\
\end{align*}   
$$


The processes considered in the model are controlled by the parameters shown in this table:

| Parameter | Description | Value| Source|
| ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |   |  |
| K | Carrying capacity |  |  |
| $$\mu_i$$ | Induction rate |  |   |
| d | Infection rate | 0 |  |
| c | Burst size | 125 |Da. Paepe et al, 2006  |
| m | Decay rate | 0.012h<sup>-1</sup>| Da Paepe et al, 2006  |


