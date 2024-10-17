sample = str(input())
number_b = sample.count('b')
number_k = sample.count('k')
if number_b == number_k and number_b != 0:
    print("boki")
elif number_b > number_k:
    print("boba")
elif number_k > number_b:
    print("kiki")
else:
    print("none")