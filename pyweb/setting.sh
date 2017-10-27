#!/bin/bash

export PATH=$PATH:../google-cloud-sdk/bin
export PYTHONPATH=../google_appengine/:./lib
cp -p app_dev.yaml app.yaml
