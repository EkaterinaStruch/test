from string import ascii_uppercase, ascii_lowercase, digits
from random import sample
def get_random_password(length_=8) -> str:
    chars_ = ascii_uppercase + ascii_lowercase + digits
    password = "".join(sample(chars_, length_))
    return password
print(get_random_password())
