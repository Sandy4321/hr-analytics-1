# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 08:43:46 2017

@author: JJ Harrison
"""


from scipy import stats
import numpy as np
import math
import warnings

def twoPropZTtest(proportion_a, sample_size_a, proportion_b, sample_size_b):
    # Does a two-portion z-test when provided the portions and the sample size
    # returns a pvalue for the null that a and b have the same proportions (successes/samples)
    # See e.g. https://en.wikipedia.org/wiki/Statistical_hypothesis_testing#Common_test_statistics
    
    # Check that we've been passed proportions (successes/sample size)
    assert 0 <= proportion_a <= 1
    assert 0 <= proportion_b <= 1
    # Check that the sample sizes are as expected.
    assert type(sample_size_a) is int and sample_size_a > 0
    assert type(sample_size_b) is int and sample_size_b > 0
    
    #Check we have a reasonable number of samples so that the CLT applies
    if not (proportion_a*sample_size_a > 5 or proportion_b*sample_size_b > 5 or sample_size_a*(1-proportion_a) > 5 or sample_size_b*(1-proportion_b) > 5):
        warnings.warn("Sample size is too small for two proportion Z-test.")
        
    p_hat = (proportion_a + proportion_b)/(sample_size_a + sample_size_b)
    statistic = (proportion_a - proportion_b)/math.sqrt(p_hat*(1-p_hat)*(1/sample_size_a + 1/sample_size_b))
    pvalue = stats.norm.sf(abs(statistic))*2
    return [statistic, pvalue]

def twoPropZTtestData(a,b):
    # Does a two-portion z-test when provided with two data sets.
    # Assumes each of a and b has value 0 or 1. Proportion is then the mean of each.
    # returns a pvalue for the null that a and b have the same proportions (successes/samples)
    # See e.g. https://en.wikipedia.org/wiki/Statistical_hypothesis_testing#Common_test_statistics
    return twoPropZTtest(np.mean(a), len(a), np.mean(b), len(a))

