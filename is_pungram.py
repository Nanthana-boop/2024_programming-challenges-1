import string
import sys
sys.stdout.reconfigure(encoding='utf-8')

input_pang = "Jinxed wizards pluck ivy from the big quilt"
x = "Hello"
def is_pg(input_pang):
    return set(string.ascii_lowercase) <= set(input_pang.lower())

def longest_word(input_pang):
    if is_pg(input_pang):
        return max(input_pang.split(), key=len)
    else:
        return "Not a Pangram"

res = longest_word(input_pang)
print(f'Output : "{res}"')