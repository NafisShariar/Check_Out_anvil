from ._anvil_designer import AllTasksTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AllTasks(AllTasksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items=app_tables.todos.search(done=False)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.todos.add_row(task=self.new_reminder_box.text, done=False)
    self.repeating_panel_1.items=app_tables.todos.search(done=False)
    self.new_reminder_box.text=""
    

  def new_reminder_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AllTasks')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AllCompletedTasks')





