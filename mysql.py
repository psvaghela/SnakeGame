import pymysql
mydb = pymysql.connect(host="localhost",user="root",passwd='Vps@8824',db='firstdb')

cur = mydb.cursor()
cur.execute('DROP TABLE firsttb')

mydb.close()