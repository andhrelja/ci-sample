#!/bin/bash

DATA_DIR=$(pwd)/data
INPUT_CONFIG_PATH=$(pwd)/config.json

pip install git+https://github.com/andhrelja/price_scraper.git
python -m price_scraper --input-config-path $INPUT_CONFIG_PATH