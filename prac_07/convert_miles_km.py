"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Joseph Hallows
Started 26/09/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Joseph Hallows'

MILES_TO_KM = 1.61


class ConvertMtoKM(App):
    km_result = StringProperty()
    """ Convert M to KM is a kivy app to convert miles to kilometres"""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ Handle calculation to convert the miles input number to kilometres"""
        km = self.convert_to_number(text) * MILES_TO_KM
        self.root.ids.output_label.text = str(km)
        self.update_result(km)

    def update_result(self, km):
        self.km_result = str(km)

    def handle_increment(self, text):
        pass

    def convert_to_number(self, text):
        """Convert text to float, or to 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

ConvertMtoKM().run()
