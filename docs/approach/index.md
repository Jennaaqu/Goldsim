---
layout: default
title: Approach
nav_order: 4
---

# 1. The models

## 1.1. The metabolic model:

$$
\begin{align*}
\frac{dB}{dt}&=&\underbrace{r H_{O_2}H_{DOC}H_{eDAR}B}_{\text{growth}} -
\underbrace{dBP}_{\text{Infection}} \\      
\frac{dP}{dt}&=&\underbrace{c\mu_p \big[1 - \mathcal{P}(L)\big]I_n}_{burst} -
\underbrace{dBP}_{\text{infection}} - \underbrace{mP}_{\text{viral decay}} +
\underbrace{c\mu_i L}_{\text{burst induction}} \\ 
\frac{dI_n}{dt}&=&\underbrace{dBP}_{\text{Infection}} -
\underbrace{\big[1 -\mathcal{P}(L) \big] I_n}_{\text{lysis}} -
\underbrace{\mathcal{P}(L) I_n}_{lysogeny} \\ 
\frac{dL}{dt}&=&\underbrace{rH_{O_2}H_{DOC}H_{eDAR}L}_{\text{growth}} +
\underbrace{\mathcal{P}(L)I_n }_{\text{lysogeny}} -
\underbrace{\mu_i L}_{\text{induction}} \\
\end{align*}

$$

| Parameter | Description | Value| Source|
| ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |0.471 (wild type), 0.382 (spot- mutant)  | Experiment data |
| H | Hill functions |8.2x10 7 (Wild type), 1x10 8 (mutant)  | Concentrations of bacteria at the end of the experiments without CX  |
| d | Infection rate | 0 |  |
| $$\mu_p$$ | Lysis rate |  |   |
| c | Burst size | 125 |Da. Paepe et al, 2006  |
| $$\mathcal{P}(L)$$ | Probability of lysogeny | 0 |  |
| m | Decay rate | 0.012h<sup>-1</sup>| Da Paepe et al, 2006  |
| $$\mu_i$$ | Induction rate |  |   |



## 1.2. The coinfection model:

$$
\begin{align*} 
   \frac{dB}{dt}&=&\underbrace{r\big(1- \frac{N}{K}\big)B}_{\text{growth}} -
   \underbrace{dBP}_{\text{infection}} \\
   \frac{dP}{dt}&=&\underbrace{c\mu_p(B,L)I_p}_{\text{burst function}} - \underbrace{dBP}_{\text{Infection}} - \underbrace{dI_nP}_{\text{coinfection}} - \underbrace{mP}_{\text{viral decay}} \\
   \frac{dI_n}{dt}&=&\underbrace{dBP}_{\text{infection}} - \underbrace{dI_nP}_{\text{coinfection}} - \underbrace{\mu_{ld}(B,L)I_n}_{\text{Infected to $\Phi$ prod.}} \\
   \frac{dI_p}{dt}&=&\underbrace{\mu_{ld}(B,L)I_n}_{\text{Infected to $\Phi$ prod.}} - \underbrace{\mu_p(B,L)I_p}_{\text{lysed cells}} + \underbrace{\mu_i L}_{\text{induction}} \\
   \frac{dL}{dt}&=&\underbrace{r\big(1- \frac{N}{K}\big)L}_{\text{growth}} + \underbrace{dI_nP}_{\text{coinfection}} - \underbrace{\mu_i L}_{\text{induction}} \\
\end{align*}
$$

$$
\begin{equation*}
\mu_{ld}=\frac{1}{0.2 \Delta t_d}
\end{equation*}
$$

$$
\begin{equation*}
\mu_{ld}=\frac{1}{0.2 \Delta t_d}
\qquad
\mu_{p}=\frac{1}{0.8 \Delta t_d}
\qquad
\Delta t_{d}=\frac{\log 2}{r\big(1- \frac{N}{K}\big)B}}
\end{equation*}
$$


The processes considered in the model are controlled by the parameters shown in this table:

| Parameter | Description | Value| Source|
| ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |   |  |
| K | Carrying capacity |  |  |
| d | Infection rate | 0 |  |
| $$\mu_p$$ | Lysis rate |  |   |
| c | Burst size | 125 |Da. Paepe et al, 2006  |
| m | Decay rate | 0.012h<sup>-1</sup>| Da Paepe et al, 2006  |
| $$\mu_{ld}$$ | Induction rate |  |   |
| $$\mu_i$$ | Induction rate |  |   |


