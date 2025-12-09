'''
Created on 18:52:39
author @ram86
'''

import graphviz
import sys
sys.path.append(r'D:\Graphvis\bin')
for path in sys.path:
    print(path)

temp = r"""
digraph{
broadcaster -> a, b, c
a -> b
b -> c
c -> inv
inv -> a}
"""

dot = graphviz.Source(temp,filename = 'test.dot',format= 'svg')
print(dot.source)
dot.view()