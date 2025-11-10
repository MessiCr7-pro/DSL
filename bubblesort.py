def bubblesort (salaries):
    n= len(salaries)
    for i in range (n-1):
        for j in range (n-i-1):
            if (salaries[j] > salaries[j+1]):
                salaries[j],salaries[j+1] = salaries[j+1],salaries[j]

salaries = [40000,29000,38000,45790,23233,90000,23000,15000]

print("original salaries",salaries)
bubblesort(salaries)
print("sorted salaries:",salaries)


print("top 5 salaries: ")
for sal in salaries [-1:-6:-1]:
    print(sal)