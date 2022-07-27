import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = [str.upper(i) for i in lowercase_letters]
numbers = [i for i in range(10)]

n_low_letters = input('How many lowercase letters do you want to use?: ')
n_low_letters = int(n_low_letters)
n_up_letters = input('How many uppercase letters do you want to use?: ')
n_up_letters = int(n_up_letters)
n_numbers = input('How many numeric characters do you want to use?: ')
n_numbers = int(n_numbers)

char_bool = input('Do you want to use other characters besides letters and numbers? (1: Yes | 2: No): ')
if char_bool == '1':
    user_str = input('What other characters do you want to use? (write them without spaces): ')
    user_chars = [i for i in user_str]
    n_user_chars = input('How many of these characters do you want to include?: ')
    n_user_chars = int(n_user_chars)

rand_up_letters =  random.choices(uppercase_letters, k=n_up_letters)
rand_low_letters =  random.choices(lowercase_letters, k=n_low_letters)
rand_nums = random.choices(numbers, k=n_numbers)
rand_other_chars = random.choices(user_chars, k=n_user_chars)
rand_chars = rand_up_letters + rand_low_letters + rand_nums + rand_other_chars
rand_chars = random.sample(rand_chars, k=len(rand_chars))

password = ''
for i in rand_chars:
    i = str(i)
    password = password + i

print(password)