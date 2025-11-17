from kivy.app import App
from kivy.lang import Builder


class ConvertUnit(App):
    """ConvertUnit is a Kivy App for converting miles to kilometres"""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert miles to km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert_unit(self):
        """Convert miles to kilometres """
        try:
            mile = self.root.ids.input_number.text
            number = float(mile)
            kilometre = number * 1.60934
            self.root.ids.output_label.text = str(kilometre)
        except ValueError:
            self.root.ids.output_label.text = "0"

    def handle_increment(self, number):
        """Increase number or reduce number"""
        try:
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + number)
        except ValueError:
            self.root.ids.input_number.text = "0"

ConvertUnit().run()