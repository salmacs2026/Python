class multipleFunctions():
    def subfields():
        print("Sub-fields in AI are:")
        subfieldslist = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"] 
        for field in subfieldslist:
                print(field)
    def OddEven():
            num=int(input("Enter the Number:"))
            if((num%2)==0):
                print(num, "is Even Number")
            else:
                print(num, "is odd Number")
            
    def ElegibilityForMarriage():
            gender=(input("Your Gender:").lower())
            age=int(input("Your Age:"))
            if(gender=="male" and age>=21):
                return "Eligible"
            elif(gender=="female" and age>=18):
                return "Eligible"
            else:
                return "Not Eligible"
    def Percentage():
                Subject1=int(input("Subject1="))
                Subject2=int(input("Subject2="))
                Subject3=int(input("Subject3="))
                Subject4=int(input("Subject4="))
                Subject5=int(input("Subject5="))
                Full_Marks=int(500)
                total=Subject1+Subject2+Subject3+Subject4+Subject5
                percent=(total/Full_Marks*100)
                print("Total     :",total)
                print("Percentage:",percent)

    def triangle():
            length=int(input("Length:"))
            breadth=int(input("Breadth:"))
            area=length*breadth/2
            print("Area Formula :  (length*breadth)/2")
            print("Area of a traiangle:",area) 
            length1=int(input("Length1:"))
            length2=int(input("Length2:"))
            breadth=int(input("Breadth:"))
            perimeter=length1+length2+breadth
            print("Perimeter formula: length1+length2+breadth")
            print("Perimeter of Triangle:",perimeter)         