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


def get_power_state():
    """Get the projector's current power state

    Returns:
        A string containing the projector control code for the current
        power state.

        'g:POWER=OFF'    = OFF
        'g:POWER=OFF2ON' = OFF -> ON in transition
        'g:POWER=ON'     = ON
        'g:POWER=ON2PMM' = ON -> Standby in transition
        'g:POWER=PMM'    = Standby
        'g:POWER=PMM2ON' = Standby -> ON in transition
        'g:POWER=ON2OFF' = ON-> OFF in transition
    """
    print "Getting current power state"
    power_state = send_serial_command('GET POWER')
    return power_state


def send_serial_command(string):
    """Send a serial command

    Returns:
        A string of the serial response to the command
    """
    # Write the command
    print 'Command: ' + string
    ser.write(string + '\r\n')

    # Wait a second and then listen for the response until the receive
    # buffer is fully empty
    time.sleep(1)
    response = ''
    while ser.inWaiting() > 0:
        response += ser.read(1)

    print 'Response: ' + response
    return response
