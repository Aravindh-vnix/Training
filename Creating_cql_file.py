import csv
import datetime

csvfile1 = open("Comments.csv", 'rb')
comments = csv.reader(csvfile1)
csvfile2 = open("AMER Scheduling.csv","rb")
Amer_scheduling = csv.reader(csvfile2)
rows = [r for r in Amer_scheduling]

for row in comments:
    val = [int(s) for s in row[0].split() if s.isdigit()]
    for s in val:
        print s
        a=rows[s][12]
        print a
        insert=open("insert_comments.cql","a")
        insert.writelines("insert into user_comments(tenant_id,comment_id,parent_id,parent_category,comment,created_by,created_ts,updated_by,updated_ts) values('DSX',%s,'dse','dse','dse','dse',%s,'dse',%s)"%(a,datetime.datetime.now(),datetime.datetime.now())+'\n')