#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        Enter description
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""



date_range = ['2019-03-19 00:07:01', '2019-03-19 18:07:47', '2019-03-19 19:07:23', '2019-03-19 20:07:42', '2019-03-20 00:07:32',
              '2019-03-22 00:07:50', '2019-03-22 17:07:30', '2019-03-22 23:07:14', '2019-03-26 00:07:14', '2019-03-31 17:07:42',
              '2019-04-02 00:07:46', '2019-04-05 23:07:15', '2019-04-07 15:07:49', '2019-04-07 16:07:01', '2019-04-07 22:07:28',
              '2019-04-07 23:07:24', '2019-04-08 00:07:33', '2019-04-15 17:07:27', '2019-04-15 18:07:44', '2019-04-15 19:07:19',
              '2019-04-16 18:07:17', '2019-04-17 00:07:35', '2019-04-17 19:07:09', '2019-04-17 20:07:13', '2019-04-18 00:07:34',
              '2019-04-28 00:07:44']

exchange_rate = [3388.16, 3369.15, 3339.89, 3284.94, 3232.45, 3183.02, 3303.95, 3389.11, 3401.45, 3298.21, 3528.76, 3753.34, 3594.35,
                 3805.21, 3655.81, 3602.21, 3647.28, 5087.34, 5009.63, 5015.26, 5139.24, 5262.07, 5350.22, 5494.85, 5129.30, 5814.15]

# We have similar dates with different time stamps
# Using data time select 5 day range starting from the end of the list
# count the number of records
# use count to select the number of rates exchange startin from the end of the list



""" Dev Notes:
        functions

        
        def data_sort():  # takes full list of dates and exchange rates
        calculate range for the last five days
        select exchange rate based on date count
        return exchange rate data range

        def stats():  # takes return values from data_sort()
        Generate list of daily currency exchange rate
        extract the last five days data
        calculate the days min(), max()
        calculate the ranges min(), max()
        calculate the mean()
            - sum(range)/len(range)
        retrun mean, max, min

    format data and display
    Ref links:
    Enter link
"""