#! /usr/bin/python3.21

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent.parent}/logs/Python-s-__repr__-And-__str__.log'
)