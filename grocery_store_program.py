import datetime, os

date = datetime.date.today()
now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")

with open("bill.txt", 'w') as f:
    f.write(f"""    ALL IN ONE GENERAL STORE
Date: {date}
Time: {time}

ITEM - PRICE(Rs.)
""")
i=0
entries = {}
total = 0
print("ENTER PRODUCT NAME AND PRICE SEPARATED BY ': ' (eg- pen: 20)\nPRESS 'q' TO QUIT")
f = open('bill.txt','a')
while True:
    article = input()
    if(article=='q' or article=='Q'):
        break
    colon = article.find(": ")
    product = article[0:colon]
    cp = article[colon+2:len(article)]
    f.write(f"{product} - {cp}\n")
    total = total+ int(cp)
    entries.update({product: cp})

f.write(f"\nTOTAL: {total}")
f.write(f"\nPLESE PAY: Rs. {round(total*1.08, 1)}(8% GST)")
f.close()

os.startfile('bill.txt')
