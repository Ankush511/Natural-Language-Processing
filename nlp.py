def capitalize(text):
    if len(text) != 0:
        return text[0].upper() + text[1:].lower()
    else:
        return None

def uppercase(text):
    txt = ""
    for i in text:
        if (ord(i)>=97 and ord(i)<=122):
            txt += chr(ord(i) - 32)
        else:
            txt += i
    return txt

def lowercase(text):
    txt = ""
    for i in text:
        if (ord(i)>=65 and ord(i)<=90):
            txt += chr(ord(i) + 32)
        else:
            txt += i
    return txt

def isalpha(text):
    c = 0
    for i in text:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            c += 1
    if len(text) == c:
        return True
    else:
        return False

def isdigit(num):
    c = 0
    for i in num:
        if (ord(i)>=48 and ord(i)<=57):
            c += 1
    if len(num) == c:
        return True
    else:
        return False

def isalnum(text):
    c = 0
    for i in text:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
            c += 1
    if len(text) == c:
        return True
    else:
        return False

def title(text):
    str = []
    for word in text.split(' '):
        str.append(word[0].upper() + word[1:].lower())

    str = ' '.join(str)
    return str