import sys

from client import client1
from librarian import librarian1
from book import book1
from borrowingOrder import borrowingOrder1

c1=client1()
l1=librarian1()
b1=book1()
bo=borrowingOrder1()
books=[]
clients=[]
librarians=[]
borrowed_orders=[]
page1=1
#*********************************************************page1***************
while page1==1:
 print("welcome")
 print("choose one of them")
 print("1- Enter as librarian")
 print("2- Enter as client")
 print("3- Exit")
 user_choice=int(input())
 if user_choice==1:
  #**********************************page2***********************
  page2=1
  while page2==1:
   print("**librarian page**")
   print("choose one of them.")
   print("1- Create a new client.")
   print("2- Create a new librarian.")
   print("3- Creat a new book.")
   print("4- Exit this page.")
   lib_choice=int(input())
   if lib_choice==1:
    print("enter id:")
    c1.id=int(input())
    print("Enter full name:")
    c1.full_name=input()
    print("Enter  age:")
    c1.age = int(input())
    print("Enter id_no:")
    c1.id_no = int(input())
    print("Enter phone number:")
    c1.phone_number = int(input())
    clients.append([c1.id,c1.full_name,c1.age,c1.id_no,c1.phone_number])
    page2=1
   elif lib_choice==2:
    print("Enter id")
    l1.id = int(input())
    print("Enter full name:")
    l1.full_name = input()
    print("Enter  age:")
    l1.age = int(input())
    print("Enter id_no:")
    l1.id_no = int(input())
    print("Enter employment_type (full/part")
    l1.employment_type=input()
    librarians.append([l1.id, l1.full_name, l1.age, l1.id_no, l1.employment_type])
    page2=1
   elif lib_choice==3:
    print("Enter id")
    b1.id = int(input())
    print("Enter book title:")
    b1.title=input()
    print("Enter description:")
    b1.description=input()
    print("Enter author:")
    b1.author = input()
    print("Enter status (Available/UnAvailable):")
    b1.status = input()
    books.append([b1.id, b1.title, b1.description, b1.author, b1.status])
    page2=1
   elif lib_choice==4:
    page2=0
    page1=1
   else:
    page2=1
  #*****************************************page2******************************
  #******************************************page3****************************
 elif user_choice==2:
  page3=1
  while page3==1:
   print("**client page**")
   print("choose one of them")
   print("1- show all book in system.")
   print("2- choose one of these book.")
   print("3- search for an order with order_id.")
   print("4- show all orders")
   print("5- Exit this page.")
   client_choice = int(input())
   if client_choice==1:
    for i in range(0,len(books)):
     print((i+1),"- id: ",books[i][0]," Title: ",books[i][1])
    page3=1
   elif client_choice==2:
    print("choose one of these book")
    book_choice=int(input())
    if books[book_choice-1][4]=="Available":
     print("this book is available , make order")
     print("Enter your id_no")
     id_no=int(input())
     for i in range(0,len(clients)):
      if clients[i][3]==id_no:
       print("Enter borrowing order id:")
       bo.id=int(input())
       bo.book_id=books[book_choice-1][0]
       bo.client_id=clients[i][0]
       bo.status="Active"
       print("Enter date in form (dd/mm/yyyy")
       bo.date=input()
       borrowed_orders.append([bo.id,bo.date,bo.client_id,bo.book_id,bo.status])
       books[book_choice - 1][4] = "UnAvailable"
       page3 = 1
       wrong=0
       break
      else :
       wrong=1
       page3=1
     if wrong==1:
      print("this id is not exist")
    else:
     print("this book is not available.")
     page3=1
   elif client_choice == 3:
    print("Enter order id")
    order_id=int(input())
    for i in range (0,len(borrowed_orders)):
     if borrowed_orders[i][0]==order_id:
      print("order_id: ",borrowed_orders[i][0]," date: ",borrowed_orders[i][1]," client_id: ",borrowed_orders[i][2]," book_id: ",borrowed_orders[i][3]," status: ",borrowed_orders[i][4])
      break
    page3=1
   elif client_choice == 4:
    for i in range(0, len(borrowed_orders)):
     print("order_id: ", borrowed_orders[i][0], " date: ", borrowed_orders[i][1], " client_id: ", borrowed_orders[i][2]," book_id: ", borrowed_orders[i][3], " status: ", borrowed_orders[i][4])
    page3=1
   elif client_choice == 5:
    page3=0
   else:
    page3=1
   page1=1
  #*************************************page3*************************
 elif user_choice==3:
  sys.exit()
 else:
  page1=1
 #******************************************page1****************************



