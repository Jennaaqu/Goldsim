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



| Parameter | Description | Value| Minimum/Maximum | Source| Phage Species| Host|
| ------ | ------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |$$7 \cdot 10^{-3} h^{-1}$$| $$2.95 \cdot 10^{-3}, 7 \cdot 10^{-3} h^{-1}$$ | (Silveira et. al, 2021)|  |             
| H | Hill functions      | $$[0,1]$$ |   | | | 
| d | Infection rate |$$1.06 \cdot 10^{-8} ml/hr$$| $$1.4 \cdot 10 ^{-9}, 3.7 \cdot 10^{-7} ml/h$$ |Luque and Silveira, 2020  | | |
| c | Burst size | $$11$$ | |(M.Middelboe et al.,2001) | Myoviridae | Vibrio sp. |
| m | Decay rate | $$0.528 hr^{-1}$$| |(C.A. Suttle,1994)   |Myoviridae |Vibrio sp. |
| $$\mathcal{P}(L)$$ | Probability of lysogeny | [0.1,0.7] |  |
| $$m$$ | Decay rate | $$0.012 h^{-1}$$| Da Paepe et al, 2006  | 
| $$\mu_i$$ | Induction rate |$$0.02 hr^{-1}$$| |Emily's thesis   | | |

Concentrations for lysogeny [0.01, 0.1]:

| Parameter | Description | Min | 1st Qu| Median| Mean| 3rd Qu| Max| Source| 
|------|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $$d$$ | Phage adsorption rate | $$1.4 \cdot 10^{-9} ml/h $$| $$4.6 \cdot 10^{-8} ml/h $$ | $$1.1 \cdot 10^{-7} ml/h $$ | $$1.4 \cdot 10^{-7} ml/h $$ | $$2.1 \cdot 10^{-7} ml/h $$ | $$3.7 \cdot 10^{-7} ml/h $$ | Luque et. al, 2020 |
| $$\tau_{ld}$$ | Commitment time | $$11 h $$| $$109 h $$ | $$262 h $$ | $$311 h $$ | $$489 $$ | $$807 h $$ | Luque et. al, 2020 |
| $$B_0$$ | Initial sensitive concentration | $$3.8 \cdot 10^4 cells/ml$$ | $$4.7 \cdot 10^{5} cells/ml$$ | $$1.5 \cdot 10^{6}  cells/ml $$| $$2.1 \cdot 10^{6}  cells/ml $$| $$3.4 \cdot 10^{6}  cells/ml $$| $$6.7 \cdot 10^{6}  cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$1.8 \cdot 10^5 phage/ml$$ | $$4.0 \cdot 10^{6} phage/ml$$ | $$9.1 \cdot 10^{6}  phage/ml $$| $$1.3 \cdot 10^{7}  phage/ml $$| $$1.9 \cdot 10^{7}  phage/ml $$| $$3.9 \cdot 10^{7}  phage/ml $$|  Luque et. al, 2020 |
| $$L_0$$ | Initial lysogen concentration | $$0.01 \cdot B_0 $$| $$0.0325 \cdot B0$$ | $$0.055 \cdot B0$$ | $$0.055 \cdot B0$$ | $$0.0775 \cdot B0$$ | $$0.1 \cdot B_0 $$ | inferred from Luque et. al, 2020 |
| $$I_{N0}$$ | Initial infected concentration |$$0 cells/ml $$| | | | | |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| | | | | |

Concentrations for lysogeny [0.1, ~0.5]:

| Parameter | Description | Min | 1st Qu| Median| Mean| 3rd Qu| Max| Source| 
|------|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $$d$$ | Phage adsorption rate | $$6.2 \cdot 10^{-9} ml/h $$| $$7.8 \cdot 10^{-8} ml/h $$ | $$1.6 \cdot 10^{-7} ml/h $$ | $$1.7 \cdot 10^{-7} ml/h $$ | $$2.5 \cdot 10^{-7} ml/h $$ | $$3.7 \cdot 10^{-7} ml/h $$ | Luque et. al, 2020 |
| $$\tau_{ld}$$ | Commitment time | $$13 h $$| $$183 h $$ | $$352 h $$ | $$376 h $$ | $$558 $$ | $$807 h $$ | Luque et. al, 2020 |
| $$B_0$$ | Initial sensitive concentration | $$3.8 \cdot 10^4 cells/ml$$ | $$7.9 \cdot 10^{5} cells/ml$$ | $$2.0 \cdot 10^{6}  cells/ml $$| $$2.5 \cdot 10^{6}  cells/ml $$| $$3.9 \cdot 10^{6}  cells/ml $$| $$6.7 \cdot 10^{6}  cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$6.2 \cdot 10^5 phage/ml$$ | $$6.3 \cdot 10^{6} phage/ml$$ | $$1.3 \cdot 10^{7}  phage/ml $$| $$1.6 \cdot 10^{7}  phage/ml $$| $$2.5 \cdot 10^{7}  phage/ml $$| $$3.9 \cdot 10^{7}  phage/ml $$|  Luque et. al, 2020 |
| $$L_0$$ | Initial lysogen concentration | $$0.1 \cdot B_0 $$| $$~0.2 \cdot B0$$ | $$~0.3 \cdot B0$$ | $$~0.3 \cdot B0$$ | $$~0.4 \cdot B0$$ | $$~0.5 \cdot B_0 $$ | inferred from Luque et. al, 2020 |
| $$I_{N0}$$ | Initial infected concentration |$$0 cells/ml $$| | | | | |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| | | | | |

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

| Parameter | Description | Value| Minimum/Maximum | Source| Phage Species|Host|
| ------ | ------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |$$7 \cdot 10^{-3} hr^{-1}$$| $$2.95 \cdot 10^{-3}, 7 \cdot 10^{-3} h^{-1}$$ | Silveira et. al, 2021|  |
| K | Carrying capacity |$$1 \cdot 10^9 cells/ml$$| |Toni's student  | | |
| d | Infection rate |$$1.06 \cdot 10^{-7} ml/hr$$| $$1.4 \cdot 10 ^{-9}, 3.7 \cdot 10^{-7} ml/h$$ |Luque and Silveira, 2020  | | |
| c | Burst size | $$11$$ | |(M.Middelboe et al.,2001) | Myoviridae | Vibrio sp. |
| m | Decay rate | $$0.528 hr^{-1}$$| |(C.A. Suttle,1994)   |Myoviridae |Vibrio sp. |
| $$\mu_{ld}$$ | Lysogenic decision rate window |$$0.0142 hr^-1$$ | |calculated   | | |
| $$\mu_{p}$$ | Time for phage to lyse |$$0.003551 hr^{-1}$$| |calculated   | | |
| $$\mu_i$$ | Induction rate |$$0.02 hr^{-1}$$| |Emily's thesis   | | |


Concentrations for lysogeny [0.01, 0.1]:

| Parameter | Description | Min | 1st Qu| Median| Mean| 3rd Qu| Max| Source| 
|------|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $$d$$ | Infection rate | $$1.4 \cdot 10^{-9} ml/h $$| $$4.6 \cdot 10^{-8} ml/h $$ | $$1.1 \cdot 10^{-7} ml/h $$ | $$1.4 \cdot 10^{-7} ml/h $$ | $$2.1 \cdot 10^{-7} ml/h $$ | $$3.7 \cdot 10^{-7} ml/h $$ | Luque et. al, 2020 |
| $$B_0$$ | Initial sensitive concentration | $$3.8 \cdot 10^4 cells/ml$$ | $$4.7 \cdot 10^{5} cells/ml$$ | $$1.5 \cdot 10^{6}  cells/ml $$| $$2.1 \cdot 10^{6}  cells/ml $$| $$3.4 \cdot 10^{6}  cells/ml $$| $$6.7 \cdot 10^{6}  cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$1.8 \cdot 10^5 phage/ml$$ | $$4.0 \cdot 10^{6} phage/ml$$ | $$9.1 \cdot 10^{6}  phage/ml $$| $$1.3 \cdot 10^{7}  phage/ml $$| $$1.9 \cdot 10^{7}  phage/ml $$| $$3.9 \cdot 10^{7}  phage/ml $$|  Luque et. al, 2020 |
| $$L_0$$ | Initial lysogen concentration | $$0.01 \cdot B_0 $$| $$0.0325 \cdot B0$$ | $$0.055 \cdot B0$$ | $$0.055 \cdot B0$$ | $$0.0775 \cdot B0$$ | $$0.1 \cdot B_0 $$ | inferred from Luque et. al, 2020 |
| $$I_{N0}$$ | Initial infected concentration |$$0 cells/ml $$| | | | | |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| | | | | |

Concentrations for lysogeny [0.1, ~0.5]:

| Parameter | Description | Min | 1st Qu| Median| Mean| 3rd Qu| Max| Source| 
|------|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $$d$$ | Infection rate | $$6.2 \cdot 10^{-9} ml/h $$| $$7.8 \cdot 10^{-8} ml/h $$ | $$1.6 \cdot 10^{-7} ml/h $$ | $$1.7 \cdot 10^{-7} ml/h $$ | $$2.5 \cdot 10^{-7} ml/h $$ | $$3.7 \cdot 10^{-7} ml/h $$ | Luque et. al, 2020 |
| $$\tau_{ld}$$ |Commitment Time | $$13 h $$| $$183 h $$ | $$352 h $$ | $$376 h $$ | $$558 $$ | $$807 h $$ | Luque et. al, 2020 |
| $$B_0$$ | Initial sensitive concentration | $$3.8 \cdot 10^4 cells/ml$$ | $$7.9 \cdot 10^{5} cells/ml$$ | $$2.0 \cdot 10^{6}  cells/ml $$| $$2.5 \cdot 10^{6}  cells/ml $$| $$3.9 \cdot 10^{6}  cells/ml $$| $$6.7 \cdot 10^{6}  cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$6.2 \cdot 10^5 phage/ml$$ | $$6.3 \cdot 10^{6} phage/ml$$ | $$1.3 \cdot 10^{7}  phage/ml $$| $$1.6 \cdot 10^{7}  phage/ml $$| $$2.5 \cdot 10^{7}  phage/ml $$| $$3.9 \cdot 10^{7}  phage/ml $$|  Luque et. al, 2020 |
| $$L_0$$ | Initial lysogen concentration | $$0.1 \cdot B_0 $$| $$~0.2 \cdot B0$$ | $$~0.3 \cdot B0$$ | $$~0.3 \cdot B0$$ | $$~0.4 \cdot B0$$ | $$~0.5 \cdot B_0 $$ | inferred from Luque et. al, 2020 |
| $$I_{N0}$$ | Initial infected concentration |$$0 cells/ml $$| | | | | |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| | | | | |



### Equilibrium concentrations of the coinfection model
This concentrations were obtained by:
1. Making the differential equations equal to zero.
2. Assuming on a first approximation exponential growth (i.e., there is no carrying capacity)
$$
\begin{align*}
B^{*}=\frac{m/d \big( r+ \mu_{ld} \big) \big(\mu_i -r \big) }{\mu_{ld}(c -1)(\mu_i - r) - 2r(\mu_i -r) + c \mu_i r} \\
P^{*}=r/d \\
I_n^{*}= \frac{r}{r + \mu_{ld}} B \\
I_p^{*}=\frac{rB}{\mu_p(r + \mu_{ld})} \bigg[ \mu_{ld} + \frac{\mu_i r}{\mu_i -r} \bigg] \\
L^{*}=\frac{r^2}{(r + \mu_{ld})(\mu_i -r)}B \\
\end{align*}
$$