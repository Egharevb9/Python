name =input("please enter name ").split(",") 
names = set(name)
finding_len = {name: len(name) for name in name  }
print(finding_len)