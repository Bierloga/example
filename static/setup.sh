#!/bin/sh
cd /home/actions-runner/example/example/example
pkill gunicorn
gunicorn main:app
systemctl enable --now example
systemctl restart nginx