def BMI(h,w):
    print("height: "+str(h))
    print("weight: "+str(w))
    h,w = float(h),float(w)
    calc = w/(h**2)
    bmi = "under weight"if calc<18.5 else "normal weight" if calc<25 else"overweight"
    print(bmi)
