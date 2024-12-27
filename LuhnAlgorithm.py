#1. From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
#2. Take the sum of all the digits.
#3. If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    # print(card_number_reversed)
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        print(odd_digits)
        (sum_of_odd_digits) += int(digit)
    print(sum_of_odd_digits)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        print(digit)
        number = int(digit) *2
        if number >= 10:
            number = number // 10 + number % 10
            print(number)
        sum_of_even_digits += number
    total = sum_of_even_digits + sum_of_odd_digits
    print(total)
    return 0 == total % 10
    
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    # print(translated_card_number)

    verify_card_number(translated_card_number)

main()