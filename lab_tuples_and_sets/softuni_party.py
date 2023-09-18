number_of_reservation_codes = int(input())
codes_set = set()

for codes in range(number_of_reservation_codes):
    current_code = input()
    codes_set.add(current_code)

income_codes = input()
while income_codes != "END":
    if income_codes in codes_set:
        codes_set.remove(income_codes)
    income_codes = input()

print(len(codes_set))
for code in sorted(codes_set):
    print(code)
