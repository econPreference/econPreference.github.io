---
layout: post
title: Why Do Sign-Restricted SVARs Still Struggle? Conditional Correlations as a New Identification Restriction
excerpt_separator: <!--more-->
---

Since Uhlig (2005), sign restrictions have become one of the most widely used tools for identifying structural shocks in SVARs. Their appeal is clear: compared with recursive orderings or exact zero restrictions, they are relatively weak and often viewed as less controversial. But this flexibility comes at a cost. In many applications, sign restrictions alone leave the model too agnostic, so the identified set remains wide and the implied impulse responses can still look economically unsatisfying.

This is particularly clear in two classic applications. In monetary SVARs, sign-restricted models often struggle with the **price puzzle**, the result that prices fail to fall after a contractionary monetary policy shock. In oil market SVARs, sign restrictions can also leave the price response to an oil supply shock too weak or too uncertain to line up cleanly with theory.

In [our latest paper](https://github.com/econPreference/econPreference.github.io/blob/master/papers/Conditional_Correlation.pdf) co-authored with Myunghyun Kim, **"Restrictions on Conditional Correlations in SVARs,"** we propose a new type of restriction that is both simple and theoretically transparent: the **correlation restriction**. The idea is straightforward. Conditional on a demand shock, output and prices should move together, so their conditional correlation should be positive. Conditional on a supply shock, output and prices should move in opposite directions, so their conditional correlation should be negative. We show that this restriction materially sharpens identification of both monetary policy shocks and oil supply shocks.

 <!--more-->

### 1. A Restriction on Comovement, Not on Every Horizon

The key point is that the correlation restriction is not just another version of a long sequence of sign restrictions. If one imposes sign restrictions on both output and prices for several horizons, one must pre-specify when the two variables should move together. Our restriction does something different. It requires only that the **overall conditional comovement** between output and prices have the theoretically correct sign.

To implement this idea, we simulate the SVAR under only the shock of interest, shutting down the other structural shocks, and then compute the conditional correlation between the simulated paths of output and prices. This makes the restriction a direct function of the structural parameters, so it can be incorporated into the standard Bayesian machinery already used for sign-restricted SVARs.

This distinction matters. Under the correlation restriction, output and prices can temporarily move in opposite directions at some horizons, including early ones, as long as their overall conditional correlation is theory-consistent. In other words, the restriction disciplines the broad economic comovement implied by the model without over-disciplining the short-run shape of the impulse responses.

### 2. Monetary Policy Shocks: Making the Price Puzzle Disappear

> <p style="text-align: center;">
>   <a href="url"><img src="https://econpreference.github.io/images/2026-3-17-correlation-restriction-fig1.png"></a>
> </p>
> <center> Figure 1. IRFs to a contractionary monetary policy shock. The lighter area uses only the sign restriction, while the darker area adds the correlation restriction. </center>

We first apply the correlation restriction to a monetary SVAR in the spirit of Arias, Caldara, and Rubio-Ramírez (2019). Monetary policy shocks are demand shocks, so the theoretical implication is unambiguous: conditional on a contractionary monetary policy shock, output and prices should be positively correlated because both should decline.

This simple idea has large empirical consequences. When we impose only the standard sign restriction on the policy equation, the posterior median of the conditional correlation between output and prices is essentially zero, and its credible interval is extremely wide. Once we add the correlation restriction, the median conditional correlation becomes strongly positive. More importantly, the impulse response of prices changes in an economically meaningful way. With sign restrictions alone, prices do not fall significantly after a contractionary monetary shock. With the correlation restriction, prices fall with high posterior probability. In short, the price puzzle disappears.

Figure 1 shows that the gain is not limited to the price response. The credible sets for the impulse responses become visibly narrower, especially for output and prices. Therefore, the correlation restriction does not simply force a textbook result. It meaningfully reduces the set of admissible structural models while remaining grounded in an uncontroversial theoretical implication of demand shocks.

### 3. Oil Supply Shocks

> <p style="text-align: center;">
>   <a href="url"><img src="https://econpreference.github.io/images/2026-3-17-correlation-restriction-fig2.png"></a>
> </p>
> <center> Figure 2. IRFs to an oil supply shock. The lighter area uses only the sign restriction, while the darker area adds the correlation restriction. </center>

The same logic also works on the supply side. An adverse oil supply shock reduces world oil production and raises the real oil price. Since oil is a pervasive input in production, this increase in oil prices raises production costs, depresses aggregate supply, lowers output, and raises consumer prices. Therefore, output and prices should be negatively correlated conditional on an oil supply shock.

This second application is important because it shows that the correlation restriction is not just a device for fixing the monetary policy price puzzle. It also sharpens identification in a supply shock setting where sign restrictions alone still leave too much uncertainty.

Figure 2 shows exactly that. Without the correlation restriction, the model already produces a negative median conditional correlation, but the credible interval remains very wide. Once the correlation restriction is imposed, the conditional correlation becomes much more tightly negative. The responses of world oil production and the real oil price remain broadly similar, but the responses of output and prices become much more informative. Output is estimated more precisely, and consumer prices rise more clearly and with much higher posterior probability. That is exactly the response implied by standard economic theory for an adverse oil supply shock.

### Conclusion: A Small Restriction with Large Payoff

The main message of the paper is that a very simple theoretical distinction can be turned into a very useful empirical restriction. Demand shocks make output and prices move together. Supply shocks make them move in opposite directions. Encoding that implication as a restriction on conditional correlations substantially sharpens SVAR identification.

What I find especially appealing is that the same idea works in two very different applications. In the monetary policy case, it helps the model get rid of the price puzzle. In the oil supply case, it restores a price response that is much more consistent with standard theory. More broadly, whenever economic theory gives a clear prediction about comovement across variables under a particular shock, the correlation restriction provides a natural way to use that information without forcing the entire impulse response path to satisfy a long list of horizon by horizon sign restrictions.

For more details, please check out [our full paper](https://github.com/econPreference/econPreference.github.io/blob/master/papers/Conditional_Correlation.pdf).

## References

Kim, M. and Lee, S. (2026), "Restrictions on Conditional Correlations in SVARs," Working Paper.

Arias, J. E., Caldara, D., and Rubio-Ramírez, J. F. (2019), "The systematic component of monetary policy in SVARs: An agnostic identification procedure," Journal of Monetary Economics, 101, 1–13.

Baumeister, C. and Peersman, G. (2013), "Time-varying effects of oil supply shocks on the US economy," American Economic Journal: Macroeconomics, 5, 1–28.

Rubio-Ramírez, J. F., Waggoner, D. F., and Zha, T. (2010), "Structural vector autoregressions: Theory of identification and algorithms for inference," Review of Economic Studies, 77, 665–696.

Uhlig, H. (2005), "What are the effects of monetary policy on output? Results from an agnostic identification procedure," Journal of Monetary Economics, 52, 381–419.
