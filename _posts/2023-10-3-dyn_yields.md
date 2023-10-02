---
layout: post
title: Dynamic changes in the US government yield curve over the recent years
---

![about_fig.gif](/images/about_fig.gif)

- [code](https://github.com/econPreference/econPreference.github.io/blob/master/codes/dyn_yields.py)
- raw data source: [Filipović et al. 2022](https://www.discount-bond-data.org)

"representative yield curve over the last year" and "95% posterior interval" are derived from the Gaussian Process(GP) model. Specifically, suppose today is August 2023. Then, we can draw one scatter plot containing all observed yields from September 2022 to August 2023. The scatter plot would constitute a thick and sloping band if we put the X-axis as maturities. We can assume that the band comes from the Gaussian Process(GP), and the GP can be estimated using the band as data. The estimated GP is a representative of the yields over the last year. The above figure shows the mean and 95% quantile band of the predictive distribution of the GP. We should rely on the predictive distribution because we cannot observe some maturities.

## References

- Filipović, D., Pelger, M., and Ye, Y. (2022), “Stripping the Discount Curve - a Robust Machine Learning Approach,” SSRN Scholarly Paper, Rochester, NY. https://doi.org/10.2139/ssrn.4058150.
