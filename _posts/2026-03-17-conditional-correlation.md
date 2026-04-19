---
layout: post
title: Why Do Sign-Restricted SVARs Still Struggle? Conditional Correlations as a New Identification Restriction
excerpt_separator: <!--more-->
---

Since Uhlig (2005), sign restrictions have become one of the most widely used tools for identifying structural shocks in SVARs. Their appeal is clear: compared with recursive orderings or exact zero restrictions, they are relatively weak and often viewed as less controversial. But this flexibility comes at a cost. In many applications, sign restrictions alone leave the model too agnostic, so the identified set remains wide and the implied impulse responses can still look economically unsatisfying.

This is particularly clear in two classic applications. In monetary SVARs, sign-restricted models often struggle with the **price puzzle**, the result that prices fail to fall after a contractionary monetary policy shock. In oil market SVARs, sign restrictions can also leave the price response to an oil supply shock too weak or too uncertain to line up cleanly with theory.

In [our latest paper](url) co-authored with Myunghyun Kim, **"Restrictions on Conditional Correlations in SVARs,"** we propose a new type of restriction that is both simple and theoretically transparent: the **correlation restriction**. The idea is straightforward. Conditional on a demand shock, output and prices should move together, so their conditional correlation should be positive. Conditional on a supply shock, output and prices should move in opposite directions, so their conditional correlation should be negative. We show that this restriction materially sharpens identification of both monetary policy shocks and oil supply shocks.

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

### 3. Oil Supply Shocks: Recovering the Theory-Consistent Price Response

We then turn to oil supply shocks using the framework of Baumeister and Peersman (2013). Here the relevant theoretical implication reverses. An adverse oil supply shock reduces output but raises prices because higher oil prices increase production costs. Therefore, output and prices should be negatively correlated conditional on the oil supply shock.

Again, the correlation restriction substantially sharpens identification. Without it, the conditional correlation between output and prices is already negative at the posterior median, but the credible interval is still wide enough to allow economically implausible cases. Once the correlation restriction is imposed, the conditional correlation becomes much more tightly negative. The resulting impulse responses are also more sensible. In particular, prices rise more clearly and with much higher posterior probability after an oil supply shock, which is exactly what standard economic theory would predict.

This is important because it shows that the correlation restriction is useful not only for the famous monetary-policy price puzzle, but also for supply-side applications where sign restrictions alone can leave too much ambiguity in the price response.

### Conclusion: A Small Restriction with Large Payoff

Our paper argues that SVAR identification can be improved by exploiting one of the most basic distinctions in macroeconomics: demand shocks move output and prices together, while supply shocks move them in opposite directions. Translating that idea into a restriction on **conditional correlations** turns out to be both easy to implement and empirically powerful.

The broader message is that the correlation restriction offers a middle ground between overly weak identification and heavy-handed short-run sign restrictions. It does not force output and prices to move in a particular direction at every horizon. Instead, it imposes the economically meaningful requirement that the model generate the right pattern of comovement overall. In the applications we study, that is enough to make the identified shocks substantially more credible.

For monetary policy shocks, the restriction sharpens inference and makes the price puzzle disappear. For oil supply shocks, it tightens the identified set and yields a price response that is much more consistent with theory. More generally, whenever a researcher has a clear theoretical prediction about the sign of conditional comovement across variables, the correlation restriction provides a natural way to use that information in SVARs.

For more details, please check out our full paper.

## References

Kim, M. and Lee, S. (2026), "Restrictions on Conditional Correlations in SVARs," Working Paper.

Arias, J. E., Caldara, D., and Rubio-Ramírez, J. F. (2019), "The systematic component of monetary policy in SVARs: An agnostic identification procedure," Journal of Monetary Economics, 101, 1–13.

Baumeister, C. and Peersman, G. (2013), "Time-varying effects of oil supply shocks on the US economy," American Economic Journal: Macroeconomics, 5, 1–28.

Rubio-Ramírez, J. F., Waggoner, D. F., and Zha, T. (2010), "Structural vector autoregressions: Theory of identification and algorithms for inference," Review of Economic Studies, 77, 665–696.

Uhlig, H. (2005), "What are the effects of monetary policy on output? Results from an agnostic identification procedure," Journal of Monetary Economics, 52, 381–419.
