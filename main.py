import os, time
todoList = []

print("To Do List Manager: ")

def printList():
  print() 
  for item in todoList:
    print(item)
  print() 

while True:
  menu = input("Do you want to view, add or edit your to do list?: ")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What should I add to the list?: ")
    todoList.append(item)
  elif menu == "edit":
    item = input("What should I remove from the list?: ")
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()