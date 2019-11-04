# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB).
#
# Copyright (C) 2019 NYU.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Analytics code for the predictor examples. Reads a text file (as produced by
the predictor code) and outputs the average distance of the predicted values
from the expected values and the number of exact predictions.
"""

from __future__ import absolute_import, division, print_function

import argparse
import errno
import math
import os
import json
import sys


def read(inputfile):
    """Read prediction results and ground truth. Expects a file where each line
    is a pair of sequence identifier and value, separated by ':'

    Parameters
    ----------
    inputfile: file
        Input text file

    Returns
    -------
    dict
    """
    results = dict()
    with open(inputfile, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            id, value = line.strip().split(':')
            results[int(id)] = int(value)
    return results


def main(resultfile, gtfile, outputfile):
    """Expects an input file where each row contains the sequence identifier
    and the predicted value. If the result file does not contain a prediction
    for an input sequence the default value of 0 is assumed.
    Outputs JSON object that contains the average distance of the predicted
    value from the expected value and the total number of exact predictions.

    Parameters
    ----------
    resultfile: file
        Text file containing prediction results
    gtfile: file
        Text file containing ground truth data
    outputfile: file
        Output file that will contain he result in Json format
    """
    # Read results and ground truth.
    results = read(resultfile)
    gt = read(gtfile)
    # Compute exact matches and average diff.
    exact_match_count = 0
    total_diff = 0
    for seq_id in gt:
        if seq_id in results:
            prediction = results[seq_id]
        else:
            prediction = 0
        diff = abs(prediction - gt[seq_id])
        if diff == 0:
            exact_match_count += 1
        else:
            total_diff += (diff * diff)
    # Create results object
    results = {
        'avg_diff': math.sqrt(total_diff / len(gt)),
        'exact_match': exact_match_count
    }
    # Write analytics results. Ensure that output directory exists:
    # influenced by http://stackoverflow.com/a/12517490
    dir_name = os.path.dirname(outputfile)
    if dir_name != '':
        if not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
            except OSError as exc:  # guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
    with open(outputfile, 'w') as f:
        json.dump(results, f)


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resultfile", required=True)
    parser.add_argument("-g", "--gtfile", required=True)
    parser.add_argument("-o", "--outputfile", required=True)

    parsed_args = parser.parse_args(args)

    main(
        resultfile=parsed_args.resultfile,
        gtfile=parsed_args.gtfile,
        outputfile=parsed_args.outputfile
    )
