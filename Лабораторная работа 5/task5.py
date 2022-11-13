from random import sample
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
def generate_password(n)-> str:
    password = sample(symbols, n)
    password_str = "".join(password)
    return password_str
print(generate_password(8))

