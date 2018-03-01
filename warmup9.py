#julia golder
#3/1/18
#warmup.py

text = input('Enter text: ')
for ch in text:
    if ch in 'aeiou':
        print(ch.upper())
    else:
        print(ch)
