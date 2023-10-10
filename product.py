import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Product:
    def __init__(self, title, url, date):
        self.title = title
        self.url = url
        self.date = date

    @property
    def model(self):
        return self.model

    @property
    def specifications(self):
        return self.specifications

    @property
    def guarantee(self):
        return self.guarantee

    @property
    def accessories(self):
        return self.accessories

    @property
    def price(self):
        return self.price

    @property
    def payment_methods(self):
        return self.payment_methods

    @property
    def contact(self):
        return self.contact

    @property
    def note(self):
        return self.contact