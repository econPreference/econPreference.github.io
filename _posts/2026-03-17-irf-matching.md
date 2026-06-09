---
layout: post
title: How Can SVARs Use More of Economic Theory? Matching Theoretical IRFs
excerpt_separator: <!--more-->
---

Identifying monetary policy shocks in SVARs has always been about bringing economic theory to the data. But most conventional identification schemes use only a limited part of what theory says. Recursive restrictions use assumptions about timing. Sign restrictions use assumptions about directions. These restrictions are useful, but they often ignore the richer dynamic information contained in theoretical impulse response functions.

That missing information matters. In monetary SVARs, standard restrictions can still produce responses that are difficult to reconcile with theory. One classic example is the **price puzzle**, where prices fail to fall after a contractionary monetary policy shock. Another is the puzzling result that output can rise after monetary tightening, even though standard New Keynesian models predict a contraction.

In [our latest paper](https://github.com/econPreference/econPreference.github.io/blob/master/papers/IRF_Matching.pdf) co-authored with Myunghyun Kim and Inhwan So, **"Identifying Monetary Policy Shocks by Matching Theoretical IRFs,"** we propose a new identification scheme: the **matching restriction**. The idea is simple. If a theoretical model implies a particular dynamic response to a monetary policy shock, then SVAR rotations that generate empirical IRFs closer to that theoretical IRF should receive higher prior density. We show that this restriction helps resolve both the price puzzle and the positive output response puzzle in two benchmark monetary SVARs.

 <!--more-->

### 1. A Restriction on the Shape of the Response

The matching restriction is different from a standard sign restriction. A sign restriction says that a variable must move in a particular direction, usually over a pre-specified set of horizons. The matching restriction instead uses the **shape** of a theoretical IRF: its persistence, hump-shaped dynamics, timing, and decay.

Formally, the restriction constructs a prior over the rotation matrix in a set-identified SVAR. For each rotation, we evaluate how compatible the implied empirical IRF distribution is with the theoretical IRF from a New Keynesian DSGE model. Rotations that generate empirical IRFs closer to the theoretical benchmark receive higher prior density. The reduced-form likelihood and prior remain unchanged; the restriction operates through the prior over rotations.

This is useful because the restriction does not require the empirical IRF to match the theoretical IRF exactly. It also does not require every SVAR variable to appear in the DSGE model. In our applications, we match only one theoretically disciplined response at a time and then ask whether the rest of the SVAR dynamics become more consistent with theory.

### 2. Matching Output: Eliminating the Price Puzzle

> <p style="text-align: center;">
>   <a href="https://econpreference.github.io/images/2026-3-17-irf-matching-fig3.png"><img src="https://econpreference.github.io/images/2026-3-17-irf-matching-fig3.png"></a>
> </p>
> <center> Figure 1. IRFs to a contractionary monetary policy shock in the Arias, Caldara, and Rubio-Ramírez (2019) SVAR. The lighter area uses only the sign restriction, while the darker area adds the matching restriction based on the theoretical IRF of output. </center>

The first application uses the monetary SVAR framework of Arias, Caldara, and Rubio-Ramírez (2019). In this setup, the sign restrictions imply that a contractionary monetary policy shock lowers output, but they do not generate a clear decline in prices. The price puzzle remains.

We add a matching restriction based only on the theoretical IRF of output from a New Keynesian DSGE model. In the model, a contractionary monetary policy shock generates a hump-shaped decline in output. The matching restriction therefore favors SVAR rotations whose GDP response looks closer to this theoretical output response. Importantly, we do **not** match the price response.

Even though prices are not directly targeted, Figure 1 shows that the price puzzle disappears. With the sign restriction alone, the GDP deflator response is inconclusive and its credible set remains wide. Once the matching restriction is added, the GDP deflator falls persistently after the shock, and the credible sets become much tighter. The responses of commodity prices, total reserves, and nonborrowed reserves also become more consistent with a contractionary monetary policy shock.

This result is the key empirical payoff of the approach. By disciplining the output dynamics toward a theoretical benchmark, the SVAR identifies a monetary policy shock whose broader macroeconomic effects also line up better with theory.

### 3. Matching Prices: Making Tightening Contractionary

> <p style="text-align: center;">
>   <a href="https://econpreference.github.io/images/2026-3-17-irf-matching-fig5.png"><img src="https://econpreference.github.io/images/2026-3-17-irf-matching-fig5.png"></a>
> </p>
> <center> Figure 2. IRFs to a contractionary monetary policy shock in the Uhlig (2005) SVAR. The lighter area uses only the sign restriction, while the darker area adds the matching restriction based on the theoretical IRF of prices. </center>

The second application uses the SVAR framework of Uhlig (2005). This model imposes sign restrictions directly on prices, commodity prices, nonborrowed reserves, and the federal funds rate. By construction, the price puzzle is ruled out. But output is left unrestricted, and the identified shock can generate a positive output response after monetary tightening.

Here we add a matching restriction based only on the theoretical IRF of prices. The New Keynesian DSGE model predicts that prices should fall persistently after a contractionary monetary policy shock, so the matching restriction favors rotations whose GDP deflator response follows that theoretical price path. Again, we do **not** match the output response.

Figure 2 shows that this restriction makes the monetary tightening contractionary. Under the sign restriction alone, the GDP response is positive and highly uncertain. After adding the matching restriction, GDP falls, and its credible set becomes much narrower. The credible sets for commodity prices, total reserves, and nonborrowed reserves also tighten.

The lesson is that matching one theoretically informative IRF can discipline the whole structural shock. Matching prices helps identify a monetary policy shock that produces the output response theory predicts, even though output itself is not directly restricted.

### Conclusion: Theory as Quantitative Information

The main message of the paper is that theoretical IRFs contain information that standard SVAR restrictions usually leave unused. Sign restrictions use the direction of selected responses. The matching restriction uses more of the dynamic content of theory by assigning more prior mass to rotations that produce empirical IRFs close to theoretical benchmarks.

This approach provides a bridge between theoretical models and SVAR identification. It remains compatible with the Bayesian machinery used for sign-restricted SVARs, but it makes the source of additional identifying information explicit. In our monetary policy applications, this additional information resolves the price puzzle in one benchmark model and the positive output response puzzle in another.

More broadly, whenever theory gives a clear prediction about the dynamic response of at least one variable to a shock, the matching restriction provides a natural way to use that prediction in SVAR identification without forcing every response to satisfy a long list of horizon-by-horizon restrictions.

For more details, please check out [our full paper](https://github.com/econPreference/econPreference.github.io/blob/master/papers/IRF_Matching.pdf).

## References

Kim, M., Lee, S., and So, I. (2026), "Identifying Monetary Policy Shocks by Matching Theoretical IRFs," Working Paper.

Arias, J. E., Caldara, D., and Rubio-Ramírez, J. F. (2019), "The systematic component of monetary policy in SVARs: An agnostic identification procedure," Journal of Monetary Economics, 101, 1-13.

Christiano, L. J., Eichenbaum, M., and Evans, C. L. (2005), "Nominal rigidities and the dynamic effects of a shock to monetary policy," Journal of Political Economy, 113, 1-45.

Giacomini, R. and Kitagawa, T. (2021), "Robust Bayesian inference for set-identified models," Econometrica, 89, 1519-1556.

Rubio-Ramírez, J. F., Waggoner, D. F., and Zha, T. (2010), "Structural vector autoregressions: Theory of identification and algorithms for inference," Review of Economic Studies, 77, 665-696.

Uhlig, H. (2005), "What are the effects of monetary policy on output? Results from an agnostic identification procedure," Journal of Monetary Economics, 52, 381-419.
