from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app to demo BoxLayout creation."""
    def build(self):
        """Build the Kivy GUI from the KV file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout_demo.kv")
        return self.root

    def handle_greet(self):
        """Handle greet: write name of user"""
        print(f'greet {self.root.ids.user_input.text}')
        self.root.ids.user_input.text = "Holle" + str(self.root.ids.user_input.text)

    def handle_clear(self):
        """Handle clear: clear user input"""
        print("Name has been Cleared")
        self.root.ids.user_input.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()