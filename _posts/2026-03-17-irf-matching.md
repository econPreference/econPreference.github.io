---
layout: post
title: "Beyond Signs: Matching Theoretical IRFs in SVARs"
excerpt_separator: <!--more-->
---

Structural VARs are often identified by translating economic theory into restrictions. A recursive ordering says which variables can react within the period. A sign restriction says whether a response should be positive or negative. These restrictions are useful, but they use only a small part of what many theoretical models provide.

Theoretical models usually say more than "prices should fall" or "output should decline." They also imply a dynamic path: when the response starts, how persistent it is, whether it is hump-shaped, and how quickly it fades out. Standard SVAR restrictions often leave this quantitative information unused.

That omission matters in monetary policy applications. Even widely used identification schemes can produce responses that are hard to reconcile with theory. Prices may fail to fall after a contractionary monetary policy shock, producing the price puzzle. Output may even rise after monetary tightening, despite the contractionary response predicted by standard New Keynesian models.

In [our latest paper](https://github.com/econPreference/econPreference.github.io/blob/master/papers/IRF_Matching.pdf), co-authored with Myunghyun Kim and Inhwan So, **"Identifying Monetary Policy Shocks by Matching Theoretical IRFs,"** we propose a new identification scheme: the **matching restriction**. The restriction uses theoretical impulse response functions (IRFs) to construct a prior over rotations in a set-identified SVAR. Rotations receive higher prior density when they generate empirical IRF distributions that place more mass near the theoretical IRF.

The idea is to let theory discipline the shape of selected responses without forcing the entire SVAR to mirror a DSGE model. In our applications, matching only one theoretically informative response is enough to improve the behavior of several other variables.

<!--more-->

### 1. Matching More Than the Sign

The matching restriction differs from a standard sign restriction. A sign restriction keeps rotations that produce responses with the desired direction. The matching restriction instead ranks rotations according to how well their implied empirical IRFs line up with a theoretical benchmark.

This does not mean that the empirical IRF must trace the theoretical IRF exactly at every horizon. The restriction is probabilistic. For each rotation, we use the distribution of the empirical IRF implied by that rotation and evaluate how compatible it is with the theoretical IRF from a New Keynesian DSGE model. Rotations that make the theoretical IRF more plausible under this empirical distribution receive more prior weight.

This design has two useful features. First, the reduced-form VAR is left intact; the restriction operates through the prior over rotations. Second, it does not restrict the SVAR to include only variables that appear in the DSGE model. We can match the response of one variable and then ask whether the resulting structural shock also produces more plausible responses for variables that are not directly matched.

### 2. Matching Output: Eliminating the Price Puzzle

> <p style="text-align: center;">
>   <a href="https://econpreference.github.io/images/2026-3-17-irf-matching-fig3.png"><img src="https://econpreference.github.io/images/2026-3-17-irf-matching-fig3.png"></a>
> </p>
> <center> Figure 1. IRFs to a contractionary monetary policy shock in the Arias, Caldara, and Rubio-Ramírez (2019) SVAR. The lighter area uses only the sign restriction, while the darker area adds the matching restriction based on the theoretical IRF of output. </center>

Our first application builds on the monetary policy SVAR of Arias, Caldara, and Rubio-Ramírez (2019). Their identification scheme produces a contractionary output response, but the price response remains inconclusive. The price puzzle is not fully resolved.

We add a matching restriction based on the theoretical IRF of output. In the New Keynesian DSGE model, a contractionary monetary policy shock generates a persistent, hump-shaped decline in output. The matching restriction therefore favors rotations whose GDP response is more compatible with that theoretical output path.

Importantly, we do not match prices. Prices are left to respond according to the structural shock identified after disciplining output.

Figure 1 shows the result. Under the sign restriction alone, the GDP deflator response remains wide and inconclusive. After adding the matching restriction, the GDP deflator falls persistently after the shock, and the credible sets become much tighter. Commodity prices, total reserves, and nonborrowed reserves also move in directions more consistent with a contractionary monetary policy shock.

The key point is that disciplining output changes the identified shock. Once the output response is made more consistent with theory, the broader macroeconomic responses also become more coherent.

### 3. Matching Prices: Making Tightening Contractionary

> <p style="text-align: center;">
>   <a href="https://econpreference.github.io/images/2026-3-17-irf-matching-fig5.png"><img src="https://econpreference.github.io/images/2026-3-17-irf-matching-fig5.png"></a>
> </p>
> <center> Figure 2. IRFs to a contractionary monetary policy shock in the Uhlig (2005) SVAR. The lighter area uses only the sign restriction, while the darker area adds the matching restriction based on the theoretical IRF of prices. </center>

Our second application uses the SVAR framework of Uhlig (2005). This model imposes sign restrictions directly on prices, commodity prices, nonborrowed reserves, and the federal funds rate. By construction, the price puzzle is ruled out. But output is left unrestricted, and the identified shock can generate a positive output response after monetary tightening.

Here we match prices rather than output. The New Keynesian DSGE model predicts that prices should fall gradually after a contractionary monetary policy shock, so the matching restriction favors rotations whose GDP deflator response is more compatible with that theoretical price path.

Again, output is not directly matched.

Figure 2 shows that matching prices makes the monetary tightening contractionary. Under the sign restriction alone, the GDP response is positive and highly uncertain. After adding the matching restriction, GDP falls, and its credible set becomes much narrower. The credible sets for commodity prices, total reserves, and nonborrowed reserves also tighten.

This result illustrates the main advantage of the approach. A theoretical IRF for one variable can help identify the structural shock in a way that improves the responses of variables that are not themselves restricted.

### Conclusion: Theory as Quantitative Information

The main message of the paper is simple: theoretical IRFs contain identifying information that standard SVAR restrictions often leave on the table.

Sign restrictions use the direction of selected responses. The matching restriction uses more of the dynamic content of theory by giving more prior weight to rotations that make empirical IRFs more compatible with theoretical benchmarks. It therefore provides a way to bring quantitative theory into SVAR identification without restricting the SVAR to variables that are included in the DSGE model.

In our monetary policy applications, this additional information resolves the price puzzle in one benchmark SVAR and the positive output response puzzle in another. More broadly, whenever theory provides a clear prediction for the dynamic response of at least one variable, the matching restriction offers a practical way to use that prediction in set-identified SVARs.

For more details, please check out [our full paper](https://github.com/econPreference/econPreference.github.io/blob/master/papers/IRF_Matching.pdf).

## References

Kim, M., Lee, S., and So, I. (2026), "Identifying Monetary Policy Shocks by Matching Theoretical IRFs," Working Paper.

Arias, J. E., Caldara, D., and Rubio-Ramírez, J. F. (2019), "The systematic component of monetary policy in SVARs: An agnostic identification procedure," Journal of Monetary Economics, 101, 1-13.

Christiano, L. J., Eichenbaum, M., and Evans, C. L. (2005), "Nominal rigidities and the dynamic effects of a shock to monetary policy," Journal of Political Economy, 113, 1-45.

Giacomini, R. and Kitagawa, T. (2021), "Robust Bayesian inference for set-identified models," Econometrica, 89, 1519-1556.

Rubio-Ramírez, J. F., Waggoner, D. F., and Zha, T. (2010), "Structural vector autoregressions: Theory of identification and algorithms for inference," Review of Economic Studies, 77, 665-696.

Uhlig, H. (2005), "What are the effects of monetary policy on output? Results from an agnostic identification procedure," Journal of Monetary Economics, 52, 381-419.
