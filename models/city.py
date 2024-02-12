#!/usr/bin/python3
"""shows the class the identifies the city from which the BnB"""

from models.base_model import BaseModel

class City(BaseModel):
    """Represent a city."""
    state_id = ""
    name = ""
