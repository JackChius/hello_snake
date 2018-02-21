import random
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def get(foos):
    if foos == 1:
        return '123'
    elif foos == 2:
        return '789'
    elif foos == 3:
        return '233'


r = random.randint(1, 3)
bars = get(r)
print('qqww'+bars)
spam = {12345: '111wrwrew', 'Cat': 'one_catsss', 'Haha': 'lookMyTrue'}
for v in spam.items():
    print(v)

birthdays = {12345: '111wrwrew', 'cat': 'one_catsss', 'haha': 'lookMyTrue'}
while True:
    print(birthdays)
    print('Enter-a-name:-(blank-to-quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print('OhWell {} \'s birthday is {}'.format(name, birthdays[name]))
    else:
        print('can not find this name')
        print('tell me what it is ?')
        newday = input()
        birthdays[name] = newday
        print('well the info is update!!')
