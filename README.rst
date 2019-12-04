====================================================
Reproducible Open Benchmarks - Number Predictor Demo
====================================================

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://github.com/scailfin/benchmark-templates/blob/master/LICENSE



About
=====

The **Number Predictor Benchmark Demo** is part of the *Reproducible Open Benchmarks for Data Analysis Platform (ROB)*. The aim of this demo is to show the basic features of the benchmark engine and the command line interface.

The source code and input files for the demo are included in this repository. The idea is very simple. The predictor takes a sequence of numbers as input and outputs the predicted next value for the sequence. The benchmark includes 25 sequences in total. The benchmark result is computed as the deviation of the predicted values from the actual values.



Getting Started
===============

The demo requires an instance of the `ROB Web Service <https://github.com/scailfin/rob-webapi-flask/>`_ and the `ROB Command Line Interface <https://github.com/scailfin/rob-client/>`_. You can follow the instructions on the `Flask Web API - Demo Setup site <https://github.com/scailfin/rob-webapi-flask/blob/master/docs/demo-setup.rst>`_ to setup and run the Web API. The `ROB Command Line Interface <https://github.com/scailfin/rob-client/>`_ page contains information to install the client.

Use the ``robadm`` command line client from the Web API to create a new benchmark. Make sure to set the environment variables that configure the database accordingly, e.g.,:

.. code-block:: bash

    export ROB_DBMS=SQLITE3
    export SQLITE_ROB_CONNECT=./.rob/db.sqlite


If the Web API is running on your local machine with the default settings there is no need to configure additional environment variables. If the Web API is running on a different machine or port, for example, set the environment variables **ROB_API_HOST**, **ROB_API_PORT**, and **ROB_API_PATH** accordingly (see `the documentation <https://github.com/scailfin/rob-core/blob/master/docs/configuration.rst>`_ for details).



Number Predictor Benchmark
--------------------------

The following commands will download the demo and register it as a new benchmark with the local ROB Web Service:

.. code-block:: bash

    git clone https://github.com/scailfin/rob-demo-predictor.git
    robadm benchmarks create -n "Number Predictor" \
        -d "Simple Number Predictor Demo" \
        -i rob-demo-predictor/instructions.txt \
        -s rob-demo-predictor/template/


To confirm that everything worked as expected use the ``rob`` command line tool to list available benchmarks:

.. code-block:: bash

    rob benchmarks list


The output should contain at least the created benchmark. Note that the benchmark identifier will likely be different every time you register a benchmark.


.. code-block:: console

    ID       | Name             | Description
    ---------|------------------|-----------------------------
    2a0f6059 | Number Predictor | Simple Number Predictor Demo


Run the Benchmark
=================

The repository provides several different implementations for the predictor:

- `max-value.py <https://github.com/scailfin/rob-demo-predictor/blob/master/solutions/max-value.py>`_: Uses the maximum value in a given sequence as the prediction result.
- `max-n-value.py <https://github.com/scailfin/rob-demo-predictor/blob/master/solutions/max-n-value.py>`_: Uses the maximum value in a given sequence and adds a given constant value as the prediction result.
- `last-two-diff.py <https://github.com/scailfin/rob-demo-predictor/blob/master/solutions/last-two-diff.py>`_: Uses the difference between last two values in a given sequence a the prediction result.
- `add-first.py <https://github.com/scailfin/rob-demo-predictor/blob/master/solutions/add-first.py>`_: Uses the sum of the first value and the last value in a given sequence to determine the result.
- `AddDiffOfLastTwoValues.java <https://github.com/scailfin/rob-demo-predictor/blob/master/solutions/java-predictor/src/main/java/org/rob/demo/predictor/AddDiffOfLastTwoValues.java>`_: Implementation of the predictor that uses Java as the programming language instead of Python. Uses the sum of the last value and the difference between the last value and the next-to-last value in a given sequence as the prediction result.


In the following we register a new user **alice** and create a submission for the *Predictor* benchmark.

.. code-block:: bash

    # Register new user
    rob register -u alice -p mypwd
    # Login as alice
    eval $(rob login -u alice -p mypwd)
    # Set predictor benchmark as the default benchmark
    export ROB_BENCHMARK=2a0f6059
    # Create a new submission for the benchmark.
    rob submissions create -n 'Team Alice'


We use the *max-value.py* predictor to run the benchmark. This requires us to first upload the code file. We then use the unique file identifier as the argument when running the benchmark.


A look at the current leader board shows the result of the benchmark run.

.. code-block:: bash

    rob benchmark leaders

.. code-block:: console

    Rank | User  | Deviation | Exact Predictions
    -----|-------|-----------|------------------
       1 | bob   |       2.2 |                 2
       2 | alice |       4.8 |                 0
