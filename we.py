score = input("Enter Score:")
f = float(score)
try:
    if(f>0.0 and f<1.0):
        if(f >= 0.9):
            print('A')
        elif(f >= 0.8):
            print('B')
        elif(f >= 0.7):
            print('C')
        elif(f >= 0.6):
            print('D')
        else:
            print('F')
except:
    print("Error..enter a value in the range")

    

    

