#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Daniel Fuchs

CS3001: Data Science - Homework #1 Main File
"""

import math
import numpy
import random
import matplotlib.pyplot as plt

import merge_sort
import summary_stats


def main():
    print("Executing full-task output routine")
    ###########################

    # These functions are fairly robust; feel free to change
    # the input list sizes. The function names relate to the
    # respective homework problem.

    task_2_a()

    listA = [random.randint(0, 9) for _ in range(1000)]
    listB = [random.gauss(5, 3) for _ in range(1000)]
    listC = [math.exp(random.gauss(1, 0.5)) for _ in range(1000)]

    ssA = []
    ssB = []
    ssC = []

    task_2_b([listA, listB, listC], [ssA, ssB, ssC])

    countA = []
    countB = []
    countC = []

    task_2_c([listA, listB, listC], [countA, countB, countC])

    task_3_a([ssA, ssB, ssC], show_graph=True)

    task_3_b([countA, countB, countC], show_graph=True)

    task_4()

    ###########################
    print("Execution complete!")


def task_2_a():
    print("\n>>>EXECUTING TASK 2-A \n")
    a = [random.randint(0, 9) for _ in range(10)]
    b = merge_sort.df_merge_sort(a)
    print('Custom Merge-Sort is', 'correct!' if b == sorted(b) else 'incorrect!')
    print("")


def task_2_b(input_lists, storage_lists):
    print("\n>>>EXECUTING TASK 2-B \n")
    if len(input_lists) <= len(storage_lists):
        for i in range(len(input_lists)):
            print("Generating Summary Statistics...")
            storage_lists[i].extend(summary_stats.df_build_summary_stats(input_lists[i]))
            summary_stats.df_print_summary_stats(input_lists[i], show_values=False)
            print("")


def task_2_c(input_lists, storage_lists):
    print("\n>>>EXECUTING TASK 2-C \n")
    if len(input_lists) <= len(storage_lists):
        for i in range(len(input_lists)):
            print("Scaling / Counting Values...")
            storage_lists[i].extend(summary_stats.df_scaled_int_count(input_lists[i], 9))
            print("Complete! Values:", storage_lists[i])
            print("")


def task_3_a(data_sets, show_graph=True):
    print("\n>>>EXECUTING TASK 3-A \n")

    if len(data_sets) != 3:
        print("This task expects three data-sets to be given.")
        return

    labels = ['max', 'min', 'mean', 'median', 'mean+std', 'mean-std', '75 perc', '25 perc']
    icons = ['kv', 'k^', 'b+', 'bx', 'gv', 'g^', 'rv', 'r^']

    for j in range(len(data_sets[0])):
        plt.plot(['Data 1', 'Data 2', 'Data 3'],
                 [data_sets[0][j], data_sets[1][j], data_sets[2][j]],
                 icons[j],
                 label=labels[j])
    plt.xticks([-.5, 0, 1, 2, 3.5], ['', 'Data 1', 'Data 2', 'Data 3', ''])
    plt.legend()
    if show_graph:
        plt.show()
    plt.clf()


def task_3_b(data_sets, show_graph=True):
    print("\n>>>EXECUTING TASK 3-B \n")

    if len(data_sets) != 3:
        print("This task expects three data-sets to be given.")
        return

    labels = ['Rescaled Data %i' % (i+1) for i in range(len(data_sets))]
    icons = ['ro-', 'g+-.', 'bx:']

    for i in range(len(data_sets)):
        plt.plot(range(0, 10), data_sets[i], icons[i], label=labels[i])
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    if show_graph:
        plt.show()
    plt.clf()


def task_4():
    print("\n>>>EXECUTING TASK 4 \n")
    x = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print("Numpy Results:")
    print('a:\n', x[:, 2])
    print('b:\n', x[-1, :2])
    print('c:\n', x[:, [True, False, False, True]])
    print('d:\n', x[0:2, 0:2])
    print('e:\n', x[[0, 1, 2], [0, 1, 2]])
    print('f:\n', x[0] ** 2)
    print('g:\n', x.max(axis=1))
    print('h:\n', x[:2, :2] + x[:2, 2:])
    print('i:\n', x[:2, :3].T)
    print('j:\n', x[:2, :3].reshape((3, 2)))
    print('k:\n', x[:, :2].dot([1, 1]))
    print('l:\n', x[:, :2].dot([[3, 0], [0, 2]]))


if __name__ == '__main__':
    main()
