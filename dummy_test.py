import sys
import time
import os

dummy_boolean = False
dummy_string = "dummy test string for learning"

print(dummy_string)
print("dummy text")


while True:
    input_for_dummy = input(">>")
    try:
        if input_for_dummy == '1':
            dummy_boolean = True
        
        elif input_for_dummy == '2':
            dummy_boolean = False
        
        elif input_for_dummy == '3':
            print(dummy_string)
            print("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890")

        elif input_for_dummy == '4':
            current_time = time.ctime()
            print(f"time is {current_time}")

        elif input_for_dummy == '5':
            image_filename = "dummy_image.png"
            os.system(f"feh {image_filename} &")
        elif input_for_dummy == '3':
            sys.exit
        
        if dummy_boolean == True:
            print("dummy boolean is true")

        elif dummy_boolean == False:
            print("dummy boolean is false")
    
    except Exception as e:
        print(f"syntax error:  {e}")

