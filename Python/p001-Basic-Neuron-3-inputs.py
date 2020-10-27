#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:27:29 2020

@author: pranjal27bhardwaj
"""

import numpy as np


#print(inputs)
inputs_1 = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3.0

output_1 = inputs_1[0]*weights[0] + inputs_1[1]*weights[1] + inputs_1[2]*weights[2] + bias
print(output_1)

'''
inputs_2 = np.random.rand(3, 1)
weights_2 = np.random.rand(3,1)


output_2 = inputs_2[0]*weights[0] + inputs_2[1]*weights[1] + inputs_2[2]*weights[2] + bias
print(output_2)'''