teen_code = {
    "hc" : "học tập",
    "ng" : "người",
    "ny" : "gấu",
    "lm" : "làm việc, kiếm tiền",
    "r" : "rồi",
    "k" : "okay"
}
using = True
while using:
    for key in teen_code.keys():
        print (key,end = "\t")
    print ()
    code = input ("Enter your code:")
    key = code
    if key in teen_code:
        print ("* "*9)
        print (teen_code[key])
        print ("* "*9)
    else:
        print ("* "*9)
        que=input ("Not found.Do you wish to add it to the dictionary(Y/N)?").upper()
        if que == "Y":
            ans = input("Enter your translation:")
            teen_code[code]= ans
            print ("Updated")
            print ("* "*9)
        else:
            using = False
    

