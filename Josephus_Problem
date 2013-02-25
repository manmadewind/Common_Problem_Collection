# -*- coding: utf-8 -*-

'''
Josephus Problem
Time comsuming: O(n)
'''

def getSurvive(n, m):
  if n == 1:
    return 0

  return (getSurvive(n - 1, m) + m) % n
