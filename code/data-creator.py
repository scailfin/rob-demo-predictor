# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB).
#
# Copyright (C) 2019 NYU.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Create random sequences of predition data together with ground truth."""

from __future__ import absolute_import, division, print_function

import argparse
import errno
import os
import random
import statistics
import sys


def main(seq_length, seq_count):
    """Generate seq_count random sequences of seq_length values (containing
    values between 1 and 100) together with ground truth generated using one of
    the five functions. Output sequences and ground truth.

    Parameters
    ----------
    seq_length: int
    seq_count: int
    """
    gt = dict()
    funcs = [0] * 5
    for i in range(seq_count):
        seq = set()
        while len(seq) < seq_length:
            val = random.randint(1, 100)
            if not val in seq:
                seq.add(val)
        seq = sorted(seq)
        func = random.randint(0, 4)
        funcs[func] += 1
        if func == 0:
            gt[i] = max(seq) + 1
        elif func == 1:
            gt[i] = max(seq) + 5
        elif func == 2:
            gt[i] = seq[-1] + (seq[-1] - seq[-2])
        elif func == 3:
            gt[i] = seq[int(len(seq) / 2)] + 1
        elif func == 4:
            gt[i] = seq[-1] + seq[0]
        else:
            raise RuntimeError('invalid function identifier {}'.format(func))
        print('{}:{}'.format(i, ','.join([str(v) for v in seq])))
    print()
    for seq_id in gt:
        print('{}:{}'.format(seq_id, gt[seq_id]))
    print()
    print(funcs)


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", default=5, type=int, required=True)
    parser.add_argument("-n", "--sequences", default=5, type=int, required=True)

    parsed_args = parser.parse_args(args)

    main(
        seq_length=parsed_args.length,
        seq_count=parsed_args.sequences
    )
