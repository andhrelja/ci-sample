#!/bin/bash

export REPOSITORY_IO_PATH=$(pwd)/data
export CONFIG_JSON_PATH=$(pwd)/config.json

pip install git+https://github.com/andhrelja/price_scraper.git
python -m price_scraper --config-json-path $CONFIG_JSON_PATH