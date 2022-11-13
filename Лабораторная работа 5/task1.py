from pprint import pprint
dicts= [{'bin': bin(i), 'dec': int(i), 'oct': oct(i), 'hex': hex(i)} for i in range (16)]
pprint(dicts)
