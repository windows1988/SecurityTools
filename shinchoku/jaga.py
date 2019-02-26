#!/usr/bin/env python3

from math import* 

def jaccard_similarity(x,y): 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)])) 
    union_cardinality = len(set.union(*[set(x), set(y)])) 
    return intersection_cardinality/float(union_cardinality) 


list1 = [0.5300699300699301, 0.9300699300699301, 1.0, 0.5986013986013986, 0.2895104895104895, 0.17902097902097902, 0.17062937062937064, 0.36643356643356645, 0.17342657342657342, 0.13706293706293707, 0.11888111888111888, 0.6937062937062937, 0.36923076923076925, 0.5300699300699301, 0.0, -0.002797202797202797]

list2 = [0.38741258741258744, 0.8125874125874126, 0.8601398601398601, 0.4307692307692308, 0.5776223776223777, 0.4167832167832168, 0.2965034965034965, 0.36643356643356645, 0.4251748251748252, 0.2629370629370629, 0.3146853146853147, 0.7356643356643356, 0.2573426573426573, 0.558041958041958, 0.13986013986013987, 0.025174825174825177]
print(jaccard_similarity(list1,list2))