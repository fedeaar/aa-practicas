import numpy as np
from functools import reduce

#
# helpers
#

def attributes(S):
    attrs = reduce(lambda a, b: set.union(a, b), [set(x) for x in S])
    attrs.remove("label")
    return attrs

def unique_values(S, attr):
    out = set()
    for x in S:
        out.add(x[attr])
    return out

def split_values(S, attr):
    split = {}
    for x in S:
        value = x[attr]
        if value in split:
            split[value]["count"] += 1
            split[value]["values"].append(x)
        else:
            split[value] = { "count": 1, "values": [x]}
    return split

def split_by_cut(S, attr, c):
    split = {}
    leqc = "<=" + c
    gc = ">" + c
    for x in S:
        value = x[attr]
        key = leqc if value <= c else gc
        if key in split:
            split[key]["count"] += 1
            split[key]["values"].append(x)
        else:
            split[key] = { "count": 1, "values": [x]}
    return split

#
# metrics
#

def delta_metric(S, metric, split):
    n = len(S)
    result = metric(S)
    for x in split.values():
        result -= (x["count"] / n) * metric(x["values"])
    return result

def majority(split):
    max_count = 0 
    max_attr = None
    for attr in split:
        count = split[attr]["count"]
        if count > max_count:
            max_count = count
            max_attr = attr
    return max_attr

def gini(S):
    split = split_values(S, "label")
    n = len(S)
    res = 1
    for set in split:
        res -= (split[set]["count"] / n) ** 2
    return res

#
# categorical dta
#

def best_cut_cat(S, attrs, metric):
    max_gain = -np.inf
    max_split = None
    max_attr = None
    for attr in attrs:
        split = split_values(S, attr)
        gain = delta_metric(S, metric, split)
        if gain > max_gain:
            max_gain = gain
            max_split = split
            max_attr = attr
    return max_split, max_attr, max_gain

def ID3_cat(S, attrs, metric, max_height = None):
    split_label = split_values(S, "label")
    if (max_height == 1 or len(split_label) <= 1):
        return majority(split_label)
    split, attr, gain = best_cut_cat(S, attrs, metric)
    node = {
        "attr": attr,
        "gain": gain,
        "values": {}
    }
    subset_attrs = attrs.copy()
    subset_attrs.remove(attr)
    for value in split:
        subset = split[value]["values"]
        node["values"][value] = \
            ID3_cat(
                subset, 
                subset_attrs, 
                metric, 
                max_height - 1 if max_height != None else None)
    return node

#
# continuous dta
#

def best_cut_cont(S, attrs, metric):
    max_gain = -np.inf
    max_split = None
    max_attr = None
    for attr in attrs:
        values = unique_values(S, attr)
        for c in values:
            split = split_by_cut(S, attr, c)
            gain = delta_metric(S, metric, split)
            if gain > max_gain:
                max_gain = gain
                max_split = split
                max_attr = attr
    return max_split, max_attr, max_gain

def CART(S, attrs, metric, max_height = None): # no testeado
    split_label = split_values(S, "label")
    if (max_height == 1 or len(split_label) <= 1):
        return majority(split_label)
    split, attr, gain = best_cut_cont(S, attrs, metric)
    node = {
        "attr": attr,
        "gain": gain,
        "values": {}
    }
    subset_attrs = attrs.copy()
    subset_attrs.remove(attr)
    for value in split:
        subset = split[value]["values"]
        node["values"][value] = \
            CART(
                subset, 
                subset_attrs, 
                metric, 
                max_height - 1 if max_height != None else None)
    return node
