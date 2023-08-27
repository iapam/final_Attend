import psycopg2
from collections import Counter
conn = psycopg2.connect(host="localhost", dbname="apam", port="5432", user="postgres", password="Zingaro1")
cur = conn.cursor()
cur.execute("""SELECT * FROM students where month='08/2023'""")
r = cur.fetchall()

id=[]
st=[]
for i in r:
    id.append(i[0])

element_counts = Counter(id)
elment=[]
for element, count in element_counts.items():
    elment.append(element)
print(elment)

for t in elment:
    cur.execute("""SELECT * FROM students where id="""+ "\'" + t + "\'")
    y= cur.fetchall()
    countab = 0
    countp=0
    for o in y:
        if o[2]=='absent':
            countab+=1
        if o[2]=='present':
            countp+=1

    print(o[0])
print(len("1234567"))


