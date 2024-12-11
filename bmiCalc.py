kila = float(input("enter weight: "))
ucos = float(input("enter height: "))
dms = kila /( ucos * ucos)
if dms < 18.5:
    print("underweight")
elif dms >= 18.5 and dms < 24.9:
    print("healthy")
elif dms >= 24.9 and dms < 30:
    print("overweight")
else:
    print("obesity")
