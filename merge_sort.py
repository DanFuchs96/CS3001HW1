#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Daniel Fuchs

CS3001: Data Science - Homework #1 Module (Merge sort)
"""


def df_merge_sort(val_list):
    if len(val_list) <= 1:
        return val_list
    else:
        mid = len(val_list) // 2
        l_part = df_merge_sort(val_list[:mid])
        r_part = df_merge_sort(val_list[mid:])
        return df_merge(l_part, r_part)


def df_merge(l_part, r_part):
    result_list = []
    while l_part and r_part:
        l_val = l_part[0]
        r_val = r_part[0]
        if r_val < l_val:
            result_list.append(r_val)
            r_part.remove(r_val)
        else:
            result_list.append(l_val)
            l_part.remove(l_val)
    if l_part:
        result_list.extend(l_part)
    if r_part:
        result_list.extend(r_part)
    return result_list
