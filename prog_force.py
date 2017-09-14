import re

regex_from= r"(?P<flag>From)\s+(?P<email>\S+[@]\S+[.][a-z]+)\s(?P<date>[A-Z][a-z]{2}\s[A-Z][a-z]{2}\s((\s\d)|(\d{2}))\s[\d]{2}[:][\d]{2}[:][\d]{2}\s[\d]{4})"
regex_subject = r"(?P<flag>Subject: )(?P<subject>.+)"

path = "mbox.txt"

def make_magic():
    
    check = {
        "from_date" : 0,
        "subject" : 0,
    }
    
    from_quantity = {}
    datas = ""
    
    f = open(path,'r')
    
    while True:
        
        text = f.readline()
        
        if not text:
            break  
    
        from_date = re.search(regex_from, text)
        subject = re.search(regex_subject, text)
    
        if from_date:
            email = from_date.group('email')
            date = from_date.group('date')
            datas = "{email} ({date}): ".format(email=email, date=date)
            check["from_date"] += 1
            
            try:
                from_quantity[email] += 1
            except KeyError:
                from_quantity[email] = 1
                        
        if subject:
            datas += "{s}\n".format(s=subject.group('subject'))
            check["subject"] += 1
            print(datas)
            datas = ""
    
    for data in from_quantity.items():
        print("{email}: {quantity}\n".format(email=data[0], quantity=data[1]))

    #print check

make_magic()