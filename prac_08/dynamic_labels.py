from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabels(App):
    """Main program - Kivy app to demo dynamic labels creation."""
    start_text = StringProperty()
    def __init__(self, **kwargs):
        """Build the main application"""
        super(DynamicLabels, self).__init__(**kwargs)
        self.names = ["Tow", "Jack", "Jimbo", "Guido", "Jerry"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_names()
        return self.root

    def create_names(self):
        """Print the name in kivy"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()