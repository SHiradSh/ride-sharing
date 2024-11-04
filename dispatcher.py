from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
        """
        self.identifier = identifier
        self.location = location
        self.speed = speed

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str
        """
        return "(ID:{}, Location:{}, Speed:{}"\
            .format(self.identifier, self.location, self.speed)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @type other: Driver | other
        @rtype: bool
        """
        return (self.identifier == other.identifier)\
               and (self.location == other.location)\
               and (self.speed == other.speed)

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int
        """
        return int(((destination.row - self.location.row) +\
                (destination.column - self.location.column)) / self.speed)

    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int
        """
        return int(((location.row - self.location.row) +\
                (location.column - self.location.column)) / self.speed)

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        # TODO
        pass

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int
        """
        # TODO
        pass

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        # TODO
        pass
