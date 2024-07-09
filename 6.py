def num_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six","seven","eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]
    if 1 <= n <=9:
        return ones[n]
    elif 10 <= n <19:
        return teens[n - 10]
    elif 20 <= n <=99:
        return tens[n // 10] + ones[n % 10]
    elif 100 <=  n <= 999:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + num_to_words(n % 100)
            
    elif n == 1000:
        return "onethousand"

def count_letters():
    tot_letters = 0
    for num in range(1,1001):
        word = num_to_words(num)
        tot_letters += len(word)
    return tot_letters
        
tot_letters_used = count_letters
print("Total lettes used: ", tot_letters_used)
