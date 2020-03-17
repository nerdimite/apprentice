from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)


    def check_click(self, **event_args):
        result = anvil.server.call('check', self.answer.text, self.solution.text)
        self.result.text = result[2]



