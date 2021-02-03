from ._anvil_designer import AllCompletedTasksTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AllCompletedTasks(AllCompletedTasksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = app_tables.todos.search(done=True)
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AllTasks')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AllCompletedTasks')


