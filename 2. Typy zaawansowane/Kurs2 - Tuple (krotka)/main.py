#1
marketing=['loyalty program','client promotion','market research']
print(marketing)
#2
marketing.append('public relations')
print(marketing)
#3
print(marketing[3])
print(marketing)
#4
marketing.insert(2,'investor relations')
print(marketing)
#5
emailMarketing=marketing.copy()
print(emailMarketing)
#6
emailMarketing.sort()
print(emailMarketing)
#7
internalEmails=['internal communication']
print(internalEmails)
#8
emailMarketing.extend(internalEmails)
print(emailMarketing)
#9
tax=tuple(emailMarketing)
print(tax)