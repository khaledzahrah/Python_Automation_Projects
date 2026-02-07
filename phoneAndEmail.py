import pyperclip, re
phoneRegex=re.compile(r'''(\d{3}|\(\d{3}\))? #رمز المنطقة
(-|\s|\.)? #فاصل 
(\d{3}) #أول ثلاث أرقام
(-|\s|\.)?  #فاصل 
(\d{4})   #اخر أربع أرقام
(\s*(ext|x|ext.)\s(\d{2,5}))? #اللاحقة
''' , re.VERBOSE)
EmailRegex=re.compile('''[a-zA-Z0-9.%+-]+  # اسم المستخدم
@ #allahike
[a-zA-Z0-9.-]+ #alnatek
(\.[a-zA-Z]{2,4}) #allahike''' , re.VERBOSE)
text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum +='x'+groups[8]
    matches.append(phoneNum)
for groups in EmailRegex.findall(text):
    matches.append(groups[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
