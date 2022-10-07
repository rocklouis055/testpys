
from datetime import datetime as dt
# from utils import add_class, remove_class
import os
import pandas as pd
name=Element('name')
email=Element('email')
password=Element('password')
opt=Element('inandop')
# define the task template that will be use to render new templates to the page
# task_template = Element("task-template").select(".task", from_content=True)
# task_list = Element("list-tasks-container")
# new_task_content = Element("new-task-content")
# new_new_task_content = Element("newnew-task-content")
# new_pass_task_content = Element("newpass-task-content")
# newhello=Element("hello")
# mai file name kaise du?wahi soach rahi div mei daal de ok abhi ke liye,div id? filename? inandop
def getdata():
  console.log("hello")
  print(" world")
  print(os.listdir())
  l={}
  l['Name']=name.element.value
  l['Email']=email.element.value
  l['PassWord']=password.element.value
  print(l)
  print(os.getcwd())
  # os.chdir(r'home\pyodide\louise')
  print(os.listdir())
  if "data.xlsx" in os.listdir():
    d=pd.read_excel("data.xlsx")
    d=d.append(l, ignore_index=True)
  else:
    d=pd.DataFrame(l,index=[0])
  d.to_excel("data.xlsx",index=False)
  password.clear()
  name.clear()
  email.clear()
def readdata():
  print(os.listdir())
  if 'data.xlsx' in os.listdir():
    d=pd.read_excel('data.xlsx',)
    print(d)

  
def getfilename():
  for x in os.listdir():
    if x.endswith('.xlsx'):
      opt.element.innerText='../home/pyodide/data.xlsx'
      return

# def add_task(*ags, **kws):
#     # ignore empty task
#     if not new_task_content.element.value:
#         return None

#     # create task
#     task_id = f"task-{len(tasks)}"
#     task = {
#         "id": task_id,
#         "content": new_task_content.element.value,
#         "done": False,
#         "created_at": dt.now(),
#     }

#     tasks.append(task)
#     l=[]
#     # console.log(new_new_task_content.element.value,new_pass_task_content.element.value)
#     l.append(new_new_task_content.element.value)
#     l.append(new_pass_task_content.element.value)
#     console.log(l[0],l[1])
#     newhello.element.innerText=3

#     # add the task element to the page as new node in the list by cloning from a
#     # template
#     task_html = task_template.clone(task_id)
#     task_html_content = task_html.select("p")
#     task_html_content.element.innerText = task["content"]
#     task_html_check = task_html.select("input")
#     task_list.element.appendChild(task_html.element)

    
#     def new():
#         return "louise"

#     def check_task(evt=None):
#         task["done"] = not task["done"]
#         if task["done"]:
#             add_class(task_html_content, "line-through")
#         else:
#             remove_class(task_html_content, "line-through")

#     # new_task_content.clear()
#     task_html_check.element.onclick = check_task




# def add_task_event(e):
#     if e.key == "Enter":
#         add_task()


# new_task_content.element.onkeypress = add_task_event