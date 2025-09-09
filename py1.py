try :
     x= int("hello")
except ValueError as e:
     print("ValueError:", e)
finally:
     print("Execution completed.") 