import random
response = "y"
while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]") 
        print("[     ]")
        print("[-----]")
        response = input("Enter Y to Roll, Enter N to exit: ")
    elif no ==2:
          print("[-----]")
          print("[0    ]")
          print("[     ]") 
          print("[    0]")
          print("[-----]")
          response = input("Enter Y to Roll, Enter N to exit: ")   
    elif no ==3:
          print("[-----]")
          print("[    0]")
          print("[  0  ]") 
          print("[0    ]")
          print("[-----]")
          response = input("Enter Y to Roll, Enter N to exit: ") 
    elif no ==4:
          print("[-----]")
          print("[0   0]")
          print("[     ]") 
          print("[0   0]")
          print("[-----]")
          response = input("Enter Y to Roll, Enter N to exit: ") 
    elif no ==5:
          print("[-----]")
          print("[0   0]")
          print("[  0  ]") 
          print("[0   0]")
          print("[-----]")
          response = input("Enter Y to Roll, Enter N to exit: ")      
    else:
          print("[-----]")
          print("[0   0]")
          print("[0   0]") 
          print("[0   0]")
          print("[-----]")
          response = input("Enter Y to Roll, Enter N to exit: ")      
