def percent(m):
    p = sum(m)/4
    # sum = m[0] + m[1] + m[2] + m[3]
    return p

marks1=[86,99,94,99]
percentage1=percent(marks1)

marks2=[97,99,98,100]
percentage2=percent(marks2)

print(percentage1,percentage2)