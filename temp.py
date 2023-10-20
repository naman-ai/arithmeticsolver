# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools
from collections import Counter


def solver(my_list, answer):
    if len(my_list)==1:
        if my_list[0]==answer:
            return True
        else:
            return False
    else:
        for pair in itertools.combinations(my_list, 2):
            new_element = pair[0]+pair[1]
            addition = solver(list((Counter(my_list)-Counter(list(pair))).elements())+[new_element], answer)
            if addition:
                print(f"add{pair}")
                return True
                
            new_element = pair[0]*pair[1]
            multiplication = solver(list((Counter(my_list)-Counter(list(pair))).elements())+[new_element], answer)
            if multiplication:
                print(f"mul{pair}")
                return True
            
            if pair[0]!=0 and (pair[1]/pair[0])%1==0:
                new_element = pair[1]/pair[0]
                div = solver(list((Counter(my_list)-Counter(list(pair))).elements())+[new_element], answer)
                if div:
                    print(f"div{pair}")
                    return True
            
            if pair[1]!=0 and (pair[0]/pair[1])%1==0:
                new_element = pair[0]/pair[1]
                div = solver(list((Counter(my_list)-Counter(list(pair))).elements())+[new_element], answer)
                if div:
                    print(f"div{pair}")
                    return True
                    
            new_element = abs(pair[0]-pair[1])
            sub = solver(list((Counter(my_list)-Counter(list(pair))).elements())+[new_element], answer)
            if sub:
                print(f"sub{pair}")
                return True
            
            
        
my_list = [6,7,9,12]
answer = 24
a=(solver(my_list, answer))
        
        