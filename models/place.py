#!/usr/bin/python3
""" module stores place info for hbnb """
from models.base_model import BaseModel

class Place(BaseModel):
    """ place class for airbnb clone """

    def __init__(self, *args, **kwargs):
        """initializes place for airbnb clone"""
        if len(kwargs) == 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest  = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
        super().__init__(*args, **kwargs)
