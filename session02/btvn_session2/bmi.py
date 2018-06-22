height_cm = float(input("Height(cm):"))
weight = float(input("Weight(kg):"))
height_m = height_cm/100
BMI = weight/(height_m*height_m)
if BMI<16:
    print("BMI(Body mass index)=",BMI,"(severely underweight)")
elif BMI<18.5:
    print("BMI(Body mass index)=",BMI,"(underweight)")
elif BMI<25:
    print("BMI(Body mass index)=",BMI,"(normal)")
elif BMI<30:
    print("BMI(Body mass index)=",BMI,"(overweight)")
else:
    print("BMI(Body mass index)=",BMI,"(obese)")
