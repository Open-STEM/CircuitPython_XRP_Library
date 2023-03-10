"""
`WPILib`
================================================================================

Library for programming XRP roobts


* Author(s): Open STEM Authors

Implementation Notes
--------------------

**Hardware:**

- TODO Add links to any specific hardware product page(s), or category page(s).

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

import board as _board
from . import _drivetrain
from . import _ultrasonic_wrapper
from . import _reflectance_wrapper
from . import _servo
from . import _buttons
from . import _encoded_motor
from . import _led


from ._drivetrain import Drivetrain
from ._buttons import Buttons
from ._reflectance_wrapper import ReflectanceWrapper
from ._ultrasonic_wrapper import UltrasonicWrapper
from ._led import RGBLED
from ._servo import Servo


import time


class XRPBot:
    """
    If you need to change the encoder counts, alter the ticksPerRev values in the following two constructors.
    Most robots have either 144 or 288 ticks per revolution, depending on which motors are used.
    """

    def __init__(self, is_prototype: bool = False, ticks_per_rev: int = 288):
        self._leftMotor = _drivetrain._encoded_motor.EncodedMotor(
            encoderPinA=_board.GP4,
            encoderPinB=_board.GP5,
            motorPin1=_board.GP8,
            motorPin2=_board.GP9,
            doFlip=True,
            ticksPerRev=ticks_per_rev,
        )
        self._rightMotor = _drivetrain._encoded_motor.EncodedMotor(
            encoderPinA=_board.GP2,
            encoderPinB=_board.GP3,
            motorPin1=_board.GP10,
            motorPin2=_board.GP11,
            doFlip=False,
            ticksPerRev=ticks_per_rev,
        )

        # Publicly-accessible objects
        self.drivetrain = _drivetrain.Drivetrain(
            self._leftMotor, self._rightMotor
        )  # units in cm
        self.reflectance = _reflectance_wrapper.ReflectanceWrapper()
        self.sonar = _ultrasonic_wrapper.UltrasonicWrapper()
        self.led = _led.RGBLED(_board.GP18)
        self.servo = _servo.Servo(_board.GP12, actuationRange=135)
        self.buttons = _buttons.Buttons()

        if is_prototype:
            drivetrain.set_legacy_mode(True)
            sonar.set_legacy_mode(True)
            reflectance.set_legacy_mode(True)


try:
    bot = XRPBot(False, 288)
    drivetrain = bot.drivetrain
    reflectance = bot.reflectance
    sonar = bot.sonar
    led = bot.led
    servo = bot.servor
    buttons = bot.buttons

    def set_legacy_mode(is_legacy: bool = True):
        drivetrain.set_legacy_mode(is_legacy)
        sonar.set_legacy_mode(is_legacy)
        reflectance.set_legacy_mode(is_legacy)
except:
    print("WARNING: Legacy API not setup")
