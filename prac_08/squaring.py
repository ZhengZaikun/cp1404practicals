from kivy.app import App
from kivy.lang import Builder


class SquareNumber(App):
    """SquareNumber is a Kivy application for calculating the square of numbers."""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Squaring"
        self.root = Builder.load_file("squaring.kv")
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            input_text = self.root.ids.input_number.text
            number = float(input_text)
            square_number = number ** 2
            self.root.ids.output_label_result.text = str(square_number)
        except ValueError:
            self.root.ids.output_label_result.text = "Error: Invalid number"

SquareNumber().run()