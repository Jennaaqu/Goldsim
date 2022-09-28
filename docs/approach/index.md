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
| r | Maximum Growth Rate |0.17 1/hr | (Silveira et. al, 2021)  |
| H | Hill functions | |   |
| d | Infection rate | |  |
| $$\mu_p$$ | Time for phage to lyse | 1/hr|unit conversion factor   |
| c | Burst size | 5 |  |
| $$\mathcal{P}(L)$$ | Probability of lysogeny |0.6 | calculated  |
| m | Decay rate |0.08 1/hr |   |
| $$\mu_i$$ | Induction rate | 0.02 1/hr | Toni's student   |



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

with:

$$
\begin{equation*}
\mu_{ld}=\frac{1}{0.2 \Delta t_d} \qquad
\mu_{p}=\frac{1}{0.8 \Delta t_d} \qquad
\Delta t_{d}=\frac{\log 2}{r\big(1- \frac{N}{K}\big)B} 
\end{equation*}
$$


The processes considered in the model are controlled by the parameters shown in this table:

| Parameter | Description | Value| Source| Phage Species|Host|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |0.17 hr^-1| (Silveira et. al, 2021)|  |
| K | Carrying capacity |1e9 items/ml|Toni's student  | | |
| d | Infection rate |1.06e-8 ml/hr| (Luque and Silveira, 2020)  | | |
| c | Burst size | 11 | (M.Middelboe et al.,2001) | Myoviridae | Vibrio sp. |
| m | Decay rate | 0.528 hr^-1| (C.A. Suttle,1994)   |Myoviridae |Vibrio sp. |
| $$\mu_{ld}$$ | Lysogenic decision rate window |0.5354 hr^-1 | calculated   | | |
| $$\mu_{p}$$ | Time for phage to lyse |0.1338 hr^-1| calculated   | | |
| $$\mu_i$$ | Induction rate |0.02 hr^-1| Toni's student   | | |


### Equilibrium concentrations of the coinfection model
This concentrations were obtained by:
1. Making the differential equations equal to zero.
2. Assuming on a first approximation exponential growth (i.e., there is no carrying capacity)
$$
\begin{align*}
B^{*}=\frac{m/d \big( r+ \mu_{ld} \big) \big(\mu_i -r \big) }{\mu_{ld}(c -1)(\mu_i - r) - 2r(\mu_i -r) + c \mu_i} \\
P^{*}=r/d \\
I_n^{*}= \frac{r}{r + \mu_{ld}} B \\
I_p^{*}=\frac{rB}{\mu_p(r + \mu_{ld}} \bigg[ \mu_{ld} + \frac{\mu_i r}{\mu_i -r} \bigg] \\
L^{*}=\frac{r^2}{(r + \mu_{ld})(\mu_i -r)}B \\
\end{align*}
$$