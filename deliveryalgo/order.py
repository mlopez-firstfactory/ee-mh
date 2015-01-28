import random
from google.distance_matrix import DistanceMatrix

api_key = "AIzaSyAYeZZFs_LKiJ_pm-hsw5pD56XhxkFq2cY"
distance_matrix = DistanceMatrix(api_key)

"""
    This is dummy object model simulating app/models/order.py
    Order objects are held in a list in DeliverySlot
"""

class Order(object):
    def __init__(self, address):
        self.address = address
        self.dummyDistance = random.uniform(0, 8)

    def getDistance(self, order):
        """
            Implement Google Maps API here
        """
        distance = distance_matrix.distance(order.address, self.address)
        return distance

