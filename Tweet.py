class Tweet:
    """
    Base class for Tweet instance
    """
    def __init__(self, userId, message, time):
        self.userId = userId # - nodeId
        self.message = str(message)
        self.time = time # - local time