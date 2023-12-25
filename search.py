import re
s="Hello dev 104"
def contains_digits(s):
    return bool(re.search(r'\d', s))
print(contains_digits(s))
