#!/usr/bin/env python3

from distutils.core import setup

setup(name='prox-sensors',
      version='0.3',
      description='library for reading prox outputs',
      py_modules=['prox_reader', 'prox_interface', 'sensor_switch']
    )
