#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        international currency exchange rate analyser
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""

exchange_rate = [3388.16, 3369.15, 3339.89, 3284.94, 3232.45, 3183.02, 3303.95, 3389.11, 3401.45, 3298.21, 3528.76, 3753.34, 3594.35,
                 3805.21, 3655.81, 3602.21, 3647.28, 5087.34, 5009.63, 5015.26, 5139.24, 5262.07, 5350.22, 5494.85, 5129.30]


def stats(list_name):
    """Takes a list of an international currency,
    retrives the 10 most recent entries, five days
    calculates the max(), the min() and finally the mean
    it returns all three plus the generated list
    Arguments:
        list_name {float} -- List of exchange rates
    """
    n_range = list_name[-10:]
    max_value = max(n_range)
    mea_value = round(float(sum(n_range)) / len(n_range), 2)
    min_value = min(n_range)
    return n_range, max_value, mea_value, min_value


stats = stats(exchange_rate)
srange = stats[0]
smax = stats[1]
smean = stats[2]
smin = stats[3]

print()
print("+---- exchange rate analysis ----+")
print("|")
print("| Max:\t" + str(smax))
print("| Mea:\t" + str(smean))
print("| Mim:\t" + str(smin))
print("|")
print("+-------------------------------+")
