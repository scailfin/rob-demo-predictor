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

The demo requires an instance of the `ROB Web Service <https://github.com/scailfin/rob-webapi-flask/blob/master/README.rst>`_ and the `ROB Command Line Interface <https://github.com/scailfin/rob-client/blob/master/README.rst>`_. The following instructions can be used to setup the environment. The shown commands assume that the setup directory is ``~/projects/rob`` and that a `virtual environment <https://virtualenv.pypa.io/en/stable/>`_ is used:

.. code-block:: bash

    # -- Create the project directory and the virtual environment

    mkdir ~/projects/rob
    cd ~/projects/rob
    virtualenv ~/.venv/rob
    source ~/.venv/rob/bin/activate

    # -- Install the ROB core library

    git clone https://github.com/scailfin/rob-core.git
    cd rob-core/
    pip install -e .
    cd ..

    # --  Install anc configure Web service

    git clone https://github.com/scailfin/rob-webapi-flask.git
    cd rob-webapi-flask/
    pip install -e .
    export FLASK_APP=robflask.api
    export FLASK_ENV=development
    export ROB_API_DIR=~/projects/rob/.rob
    export ROB_ENGINE_CLASS=MultiProcessWorkflowEngine
    export ROB_ENGINE_MODULE=robcore.controller.backend.multiproc
    cd ..

    # -- Create the ROB database

    export ROB_DBMS=SQLITE3
    export SQLITE_ROB_CONNECT=~/projects/rob/.rob/db.sqlite
    robadm init

    # Install the ROB command line client
    git clone https://github.com/scailfin/rob-client.git
    cd rob-client/
    pip install -e .
    cd ..



Number Predictor Benchmark
--------------------------


The following commands will download the demo and register it as a new benchmark with the local ROB Web Service:

.. code-block:: bash

    cd ~/projects/rob
    git clone https://github.com/scailfin/rob-demo-predictor.git
    robadm benchmarks create -n "Number Predictor" \
        -d "Simple Number Predictor Demo" \
        -i rob-demo-predictor/instructions.txt \
        -s rob-demo-predictor/template/


Start the Web Service:

.. code-block:: bash

    flask run


Use a separate terminal to interact with the Web Service:

.. code-block:: bash

    # -- Register a new user and login

    rob register -u myuser -p mypwd
    eval $(rob login -u myuser -p mypwd)

    # -- List benchmarks
    rob benchmarks list
