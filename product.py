import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Product:
    def __init__(self, title, url, date, model=None, specifications=None, guarantee=None,
                 accessories=None, price=None, payment_methods=None, contact=None, note=None):
        self.title = title
        self.url = url
        self.data = date
        self.model = model
        self.specifications = specifications
        self.guarantee = guarantee
        self.accessories = accessories
        self.price = price
        self.payment_methods = payment_methods
        self.contact = contact
        self.note = note

