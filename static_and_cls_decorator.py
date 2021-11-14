class House:
    def __init__(self, size, num_bedrooms, num_restrooms):
        self.size = size
        self.beds = num_bedrooms
        self.rest_rooms = num_bedrooms

    @classmethod
    def create(cls, description):
        """ Test"""
        size, beds, baths = description.split(' ')
        return cls(float(size), int(beds), int(baths))

    @staticmethod
    class build_doors(width, height):
        return (width, height)
