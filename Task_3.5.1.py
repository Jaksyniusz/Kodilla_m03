numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

# odpowiedź 1
for i,n in enumerate(numbers):
  tens = n//10
  remainder = 10 if n%10 >= 5 else 0
  numbers[i] = tens*10 + remainder

# odpowiedź 2
numbers.remove(min(numbers))
numbers.remove(max(numbers))

# odpowiedź 3
mean_number = sum(numbers) / len(numbers)
print(mean_number)