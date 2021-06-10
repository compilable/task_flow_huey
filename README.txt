# set the py env.
python3 -m venv local


# load the env
source local/bin/activate

# start the worker
huey_consumer.py main.huey --logfile='/home/aeronx/workspace_files/DEV/huey/log.log'

# start the worker - debug mode
huey_consumer.py -v main.huey

# dependencies
pip install huey
pip install redis
pip install gevent

# docs
https://huey.readthedocs.io/en/latest/installation.html
https://docs.python.org/3/tutorial/venv.html
