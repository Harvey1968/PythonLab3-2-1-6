#3.2.1.6 LAB: Essentials of the for loop - counting mississippily

# To get 'time', the 'import' function is used with the in-built 'time' module.
import time

# The 'for' loop is required to count to five ;; If you put 5 = 0,1,2,3,4 ;; Therefore the 'range' must begin at 1 and end at 6 to return 5x "Mississippi's".
for seconds in range(1, 6):
    # Prints the loop iteration number and the word "Mississippi".
    print(seconds, "Mississippi")
    # The 'sleep(n)' function delays output ;; where n = number of seconds.
    # Can use an 'int' or 'float' variable.
    time.sleep(0.9) 
	
# Print function with the final message.
print('\n"Ready or not, here I come!"')
print("""
     ,-''''-.
   ,'       _`.
  /        )_) \\
 :              :
 \              /
  \            /
   `.        ,'
     `.    ,'
       `.,'
        /\`.   ,-._
            `-'     
""", '              "Remember they all float down here! Ha Ha!"\n') #credit art - www.ascii-art.de/
