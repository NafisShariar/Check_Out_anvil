from ._anvil_designer import AllTaskTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...TaskEdit import TaskEdit
from datetime import datetime

class AllTaskTemplate(AllTaskTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(TaskEdit(item=self.item),title="edit task details", large=True)
    self.refresh_data_bindings()

    #delete button
  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.item.delete() #deletes an item
    self.remove_from_parent() #visually Removes
#     self.refresh_data_bindings() # refreshes everything from database
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    description = str(self.item['description'])
    
   
    
    if self.item['completed_on']:
      current_time= self.item['completed_on'].strftime('%b %d %Y at %I:%M%p')
      alert(description + " -Task completed on: " + current_time)
    else:
      alert(description)
    

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.item["done"] == True:
      self.item['completed_on']= datetime.now()
      n = Notification(" Description: " + str(self.item['description']),title=" Completed Task: " + str(self.item['task']),style="success")
      
      n.show()
      




