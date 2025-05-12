# PASS OR FAIL
m1=int(input("Enter your marks in 1st subject: "))
m2=int(input("Enter your marks in 2nd subject: "))
m3=int(input("Enter your marks in 3rd subject: "))

# Fast Method
# c1=(m1+m2+m3)/3
# if(c1>40 and m1,m2,m3>33):
#     print("PASSED!")
# else:
#     print("FAILED!")

if(m1<33 or m2<33 or m3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(m1+m2+m3)/3 < 40:
    print("You are fail due to total percentage is less tahn 40")
else:
    print("Congratulations! You are passed!")