'''
name_list = ["Ali",  "Aysu", "Aysel", "Ada"]
age_list = [10, 25, 15]
for ad, yash in zip(name_list, age_list):
    print(f"ad: {ad}, yas-{yash}")
    '''

'''
score1 = [55, 67. 34, 88]
score2 = [50, 65, 99, 66]
for s1,s2 in zip(score1, score2):
    if s1>60 and s2>60:
        print(f"{s1} ve {s2}")
    elif s1>60:
        print(f"{s1}")
    elif s2>60:
        print(f"{s2}")
'''

'''
test_list = [66, 77, 88]
test_list2 = [22, 33, 44]

for tl1, tl2 in zip(test_list, test_list2):
    if tl1 > tl2:
        print(f" {tl1} daha böyükdür")
    else:
        print(f" {tl2} daha böyükdür")
'''


'''
test3 = [4, 6, 9. 5]
result = map(lambda x: x**2, test3)
print(list(result))
'''

'''
dynamic_list = input(map((("5-eded daxil edin")))).split()

for dl1 in zip(dynamic_list):
    dl1 + 5
    print(dl1)
    '''




deyer1 = input(int)

if deyer1 > 100:
    print("100-den boyük eded daxil edile bilmez")
elif deyer1 < 100:
    print(" " * deyer1) 
    deyer1 + 1
   




i = 1
while (i < 4):
    print(" " * i)
    i + 1    


#exact version of that task 
deyer1 = int(input("eded daxil edin"))
 
if deyer1 > 100 or deyer1 < 1:
    print("100-den boyük ve ya 1-den kicik eded daxil edile bilmez")
else:
    
  for i in range(1, deyer1):
      print(" " * i, i + 1)


cedvel = int(input())

for i in range(1, cedvel):
    print(f"{cedvel} x {i + 1} = {cedvel * i}")

array1 = [5, -2, 8, -10, 3, 0, 7]
musbet_ededler = 0

for i in array1:
    if i < 0:
        continue

musbet_ededler ++ i


numbers = [4, 8, 15, 16, 23, 42]
input_number = int(input("Bir eded daxil edin"))
tapildi = False
for i in numbers:
    if input_number == numbers:
        print("Bu eded massive daxildir")
        break

if input_number == True:
    print("eded tapilmadi")