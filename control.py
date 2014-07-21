#!/usr/bin/env python
"""Simple projector control script

This is written to control power on a Canon SX6000 projector

Usage:
  control.py power (--off | --on)
  control.py (-h | --help)
  control.py --version

Options:
  power --on         Power on
  power --off        Power off
  -h --help          Show this screen.
  --version          Show version

"""
from docopt import docopt
import time
import serial

# Configure the serial connection
ser = serial.Serial(
    # We're using a KeySpan USB to Serial Adapter and the provided driver
    # This will be different for different adapters and drivers
    port='/dev/cu.KeySerial1',
    # Canon projector serial communication specifications
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)
