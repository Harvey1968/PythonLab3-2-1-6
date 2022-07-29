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

# range(1, 6) ;; deference is 5 (6-1=5), therefore it will increment by 1 (default) proceeding: 1,2,3,4,5,end
# range(1, 6, 1) ;; no need for 3rd value (default increment is 1 anyways), it would still proceed: 1,2,3,4,5,end
# range(2, 10, 2) ;; deference is 8 (10-2=8), and 3rd value means it will increment by 2 therefore it will proceed: 2,4,6,8,end
# range(5, 1, -1) ;; countdown timer ;; deference is -4 (1-5=-4), therefore it will increment by -1 proceeding: -5,-4,-3,-2,end ;; to do -5,-4,-3,-2,-1,end write: range(5, 0, -1)
