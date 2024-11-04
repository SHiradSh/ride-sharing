"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    def __init__(self, identifier, origin, destination, status, patience):
        """Initialize an rider.

        @type self: Rider
        @type identifier: int
        @type origin: str
        @type destination: str
        @type status: str
        @type patience: int
        @rtype: None
        """
        self.identifier = identifier
        self.origin = origin
        self.destination = destination
        self.status = status
        self.patience = patience

    def __str__(self):
        """Return a string representation.

        @type self: Rider
        @rtype: str
        """
        return "(ID:{}, Origin:{}, Destination:{}, Status:{}, Patience:{})"\
            .format(self.identifier, self.origin, self.destination,\
                    self.status, self.patience)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Rider
        @type other: Rider | other
        @rtype: bool
        """
        return (self.identifier == other.identifier)\
               and (self.origin == other.origin)\
               and (self.destination == other.destination)\
               and (self.status == other.status)\
               and (self.patience == other.patience)
