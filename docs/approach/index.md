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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======

=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
| $$B_0$$ | Initial sensitive concentration | $$B0 cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$P0 cells/ml $$|  Luque et. al, 2020 |
| $$I_{N0}$$ | Initial infected concentration | $$In0 cells/ml $$|   |
| $$L_0$$ | Initial lysogen concentration | $$L0 cells/ml $$|  Silveira et. al, 2021 | 

=======

=======
>>>>>>> 1a80513f998553593a0a42ee16d5a6bd4bd4602a
>>>>>>> Stashed changes
=======
=======
>>>>>>> e1216730fcb06441fc58a46e79b9bc4b182118c2
| Parameter | Description | Value| Minimum/Maximum | Source| Phage Species| Host|
| ------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |$$7 \cdot 10^{-3} hr^{-1}$$| $$2.95 \cdot 10^{-3}, 7 \cdot 10^{-3} h^{-1}$$ | (Silveira et. al, 2021)|  |             
| H | Hill functions      | $$[0,1]$$ |   | | | 
| d | Infection rate |$$1.06 \cdot 10^{-8} ml/hr$$| $$7.2 \cdot 10 ^{-10}, 3.7 \cdot 10^{-7} ml/h$$ |(Luque and Silveira, 2020)  | | |
| c | Burst size | $$11$$ | |(M.Middelboe et al.,2001) | Myoviridae | Vibrio sp. |
| m | Decay rate | $$0.528 hr^{-1}$$| |(C.A. Suttle,1994)   |Myoviridae |Vibrio sp. |
| $$\mathcal{P}(L)$$ | Probability of lysogeny | [0.1,0.7] |  |
| $$m$$ | Decay rate | $$0.012 h^{-1}$$| Da Paepe et al, 2006  | 
| $$\mu_i$$ | Induction rate |$$0.02 hr^{-1}$$| |Emily's thesis   | | |
| $$B_0$$ | Initial sensitive concentration | $$2.5 \cdot 10^6 cells/ml$$ | $$3.78 \cdot 10^{4}, 1.54 \cdot 10^{6}  cells/ml $$|  Silveira et. al, 2021 |
| $$P_0$$ | Initial phage concentration |$$1.6 \cdot 10^7$$ | $$1.4 \cdot 10^{5}, 1.17 \cdot 10^{7} phage/ml $$ |Silveira et. al, 2021 |
| $$I_{N0}$$ | Initial infected concentration | $$0 cells/ml $$| |  |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| |  |
| $$L_0$$ | Initial lysogen concentration | $$0.1 B_0 $$| $$[0.0001, 0.1]$$ | inferred from Silveira et. al, 2021 |
<<<<<<< HEAD
>>>>>>> parent of 99d2083 (Update index.md)
=======
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
| $$B_0$$ | Initial sensitive concentration | $$B0 cells/ml $$|  Silveira et. al, 2021 |
| $$P_0$$ | Initial phage concentration | $$P0 cells/ml $$|  Silveira et. al, 2021 |
| $$I_{N0}$$ | Initial infected concentration | $$In0 cells/ml $$|   |
| $$L_0$$ | Initial lysogen concentration | $$L0 cells/ml $$|  Silveira et. al, 2021 | 

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> parent of 1a80513 (Update index.md)
=======
>>>>>>> e1216730fcb06441fc58a46e79b9bc4b182118c2

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
| ------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| r | Maximum Growth Rate |$$7 \cdot 10^{-3} hr^{-1}$$| $$2.95 \cdot 10^{-3}, 7 \cdot 10^{-3} h^{-1}$$ | (Silveira et. al, 2021)|  |
| K | Carrying capacity |$$1 \cdot 10^9 cells/ml$$| |Toni's student  | | |
| d | Infection rate |$$1.06 \cdot 10^{-8} ml/hr$$| $$7.2 \cdot 10 ^{-10}, 3.7 \cdot 10^{-7} ml/h$$ |(Luque and Silveira, 2020)  | | |
| c | Burst size | $$11$$ | |(M.Middelboe et al.,2001) | Myoviridae | Vibrio sp. |
| m | Decay rate | $$0.528 hr^{-1}$$| |(C.A. Suttle,1994)   |Myoviridae |Vibrio sp. |
| $$\mu_{ld}$$ | Lysogenic decision rate window |$$0.5354 hr^-1$$ | |calculated   | | |
| $$\mu_{p}$$ | Time for phage to lyse |$$0.1338 hr^{-1}$$| |calculated   | | |
| $$\mu_i$$ | Induction rate |$$0.02 hr^{-1}$$| |Emily's thesis   | | |
| $$B_0$$ | Initial sensitive concentration | $$2.5 \cdot 10^6 cells/ml$$ | $$3.78 \cdot 10^{4}, 1.54 \cdot 10^{6}  cells/ml $$|  Silveira et. al, 2021 |
| $$P_0$$ | Initial phage concentration |$$1.6 \cdot 10^7$$ | $$1.4 \cdot 10^{5}, 1.17 \cdot 10^{7} phage/ml $$ |Silveira et. al, 2021 |
| $$I_{N0}$$ | Initial infected concentration | $$0 cells/ml $$| |  |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| |  |
| $$L_0$$ | Initial lysogen concentration | $$0.1 B_0 $$| $$[0.0001, 0.1]$$ | inferred from Silveira et. al, 2021 | 

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