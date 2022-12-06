import string, random
def get_random_password() -> str:
    chars_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    length_ = 8
    password = "".join(random.sample(chars_, length_))
    return password
print(get_random_password())
