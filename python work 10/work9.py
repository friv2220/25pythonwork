def timeConversion(s):
    median = s[-2:]
    if merdian == 'PM' and s[:2]!='12':
        s = str(12 + int(s[:2])) + s[2:]
    if meridian == 'AM' and s[:2]=='12':
        s = '00' + s[2:]
        return s[:-2]
    
        