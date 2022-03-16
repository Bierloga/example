#!/bin/sh
cd /home/actions-runner/example
pkill gunicorn
gunicorn main:app