def stringtointegerarray(stringnumbers):
    numberarray = stringnumbers.split("'");
    print(numberarray)
    sum = 0
    for i in numberarray:
        print(i)
        sum = sum + int(i)
        print(sum)
    print(sum)
    return(sum)

stringtointegerarray("1,2,3,4,5,8,10")
