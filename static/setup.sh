#!/bin/sh
cd /home/actions-runner/example/example/example
pkill gunicorn
systemctl enable --now example
systemctl restart nginx