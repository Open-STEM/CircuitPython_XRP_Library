
import rotaryio

class Encoder:

    def __init__(self, pinA, pinB, ticksPerRev, doFlip=False):
        self.ticksPerDeg = ticksPerRev/360
        self.reverse = doFlip
        self.encoder = rotaryio.IncrementalEncoder(pinA, pinB)

    def getPos(self) -> float:
        """
        Retrieves the position of the encoder in degrees

        :return: The position of the encoder in degrees
        :rtype: float
        """
        r = self.encoder.position / self.ticksPerDeg
        if self.reverse:
            return -r
        else:
            return r


    def setPos(self, pos: float = 0):
        """
        Recalibrates the encoder to the specified position
        :param pos: The number of rotations to set encoder to
        :type pos: float
        :return: void
        """
        self.encoder.position = round(pos * self.ticksPerDeg)


