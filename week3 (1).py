# -*- coding: utf-8 -*-
"""week3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/songqsh/19ma573qingshuo/blob/master/src/week3-1.ipynb

BSM formula
"""

import numpy as np
import scipy.stats as ss

"""We reload the european option class created before."""

'''=========
option class init
=========='''
class VanillaOption:
    def __init__(
        self,
        otype = 1, # 1: 'call'
                  # -1: 'put'
        strike = 110.,
        maturity = 1.,
        market_price = 10.):
      self.otype = otype
      self.strike = strike
      self.maturity = maturity
      self.market_price = market_price #this will be used for calibration
      
        
    def payoff(self, s): #s: excercise price
      otype = self.otype
      k = self.strike
      maturity = self.maturity
      return np.max([0, (s - k)*otype])