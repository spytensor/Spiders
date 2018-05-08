a = ["\nBy Ray Downs  |  May 7, 2018 at 8:09 PM"]
b = ["\nBy ", "\t\t\t\t", "\n\t\t\t\t", "\n\t\t\t\t  |  May 1, 2018 at 10:03 AM", "\t\t"]
c = ["\nBy ", "\n\t\t\t\t","\t\t\t\t","  |  May 7, 2018 at 12:57 PM", "\t\t"]
remove_ = ["\n\t\t\t\t","\t\t\t\t",]

tim = []
for i in c:
    if i == "\n\t\t\t\t" or i == "\t\t\t\t":
        pass
    else:
        tim.append(i)
print(b)
print(tim)
