print("Enter a Year to check if it is a Leap Year or not: ")

year = int(input())

if(int(year)%100 == 0):
    print(year, "is not a Leap and Century Year ")

elif (int(year)%400 == 0):
    print(year, "is a century year and the leap year both")

elif (int(year)%4 == 0):
    print(year, "is a leap year and not the century year")

else:
    print(year, "is not a Leap Year and not century year")