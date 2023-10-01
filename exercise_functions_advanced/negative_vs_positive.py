def total_sum(*args):
    negative_sum = sum([x for x in args if x < 0])
    positive_sum = sum([x for x in args if x >= 0])
    return negative_sum, positive_sum


numbers = [int(num) for num in input().split()]
negative_numbers, positive_numbers = total_sum(*numbers)
print(f"{negative_numbers}\n{positive_numbers}")
print(f"The negatives are stronger than the positives" if abs(negative_numbers) > abs(positive_numbers)
      else "The positives are stronger than the negatives")
