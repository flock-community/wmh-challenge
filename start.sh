#!/usr/bin/env bash
xvfb-run -s "-screen 0 1400x900x24" jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token=''
