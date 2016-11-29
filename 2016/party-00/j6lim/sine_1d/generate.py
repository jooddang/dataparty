#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
sine_1d.py
---
f(x) = sin(2*pi*x), where -1.0 <= x < 1.0
Let's see whether NN can learn this function
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(np.pi * x)

def generate(N):
    X = np.random.uniform(size=N, low=-1.0, high=1.0)
    Y = f(X)
    return (X, Y)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate sine 1d data")
    parser.add_argument("-v", "--visualize", action='store_true', help="Visualize data")
    parser.add_argument('data_size', type=int, help="Numer of data")
    parser.add_argument('input_filename', type=str, help="Input data CSV filename")
    parser.add_argument('output_filename', type=str, help="Output data CSV filename")

    args = parser.parse_args()

    X, Y = generate(args.data_size)

    if args.visualize:
        plt.scatter(X, Y)
        plt.show()

    np.savetxt(args.input_filename, X, delimiter=',')
    np.savetxt(args.output_filename, Y, delimiter=',')



