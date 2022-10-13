def is_leap(year):
    leap = False
    if year >= 1900 and year <= 10**5:
        if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap = True
    return leap
year = int(input())
print(is_leap(year))

if __name__ == '__main__':
    is_leap()