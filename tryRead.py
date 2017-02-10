f=open('HW1_data.txt', 'r')
s=f.readline().strip().split(",")[0] #takes out everything after authors

s= s.split("&") #takes out all subsequent authors; first entry is year up to first author

print s


initial = s[0]
initial = initial.split(" ") #split the first entry into years, etc.
n = len(initial)
s[0] = initial[n-1]

year = int(initial[0])

print s
print year
