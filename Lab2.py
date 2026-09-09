wieght = float(input("Enter your Wieght in Kg :"))
height = float(input("Enter your Height in Meters :"))

heightCalcu = height**2
BMI = wieght/heightCalcu

if BMI<18.5 :
    print("wieght Underweight")
elif BMI>=18.5 and BMI<=24.9 :
    print("wieght Fit & healthy")
elif BMI>25 :
    print("wieght Overweight")

