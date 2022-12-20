# [{"_id":"5e8c4ea33e4d8a5ecdb0b0c3","id":1005,"bbox":[87.6501351349468,27.4059813235384,88.2016677742523,27.9529233658092],"centroid":{"type":"Point","coordinates":[87.89713038573582,27.703009327937185]},"title":"Phaktanglung","title_en":"Phaktanglung","title_ne":"फक्ताङलुङ","type":"Rural Municipality","code":"phaktanglungmun","district":1},
# {"_id":"5e8c4ea33e4d8a5ecdb0b0c4","id":1008,"bbox":[87.77471745301,27.2923328214121,88.1547806944035,27.7020365869892],"centroid":{"type":"Point","coordinates":[87.94650703496033,27.476015174396345]},"title":"Sirijangha","title_en":"Sirijangha","title_ne":"सिरीजङ्घा","type":"Rural Municipality","code":"sirijanghamun","district":1}]

import requests
import json
import mysql.connector as connector
class Municipal:
	def __init__(self):
		self.conn = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		query = "create table if not exists municipality(municipalId int unique,MunicipalName varchar(200),districtId int NOT NULL,CONSTRAINT fk_districtId FOREIGN KEY(districtId) REFERENCES district(districtId))"
		cur = self.conn.cursor()
		cur.execute(query)
		self.conn.commit()	
		print("Municipality Created")

	def insert_municipality(self,id,municipal,district):
		query = "insert into municipality(municipalId,MunicipalName,districtId) values({},'{}',{})".format(id,municipal,district)
		cur = self.conn.cursor()
		cur.execute(query)
		self.conn.commit()
		print("Municipality Created")

municipal = Municipal()
json_data = json.loads(requests.get("https://data.askbhunte.com/api/v1/municipals").text)
for data in json_data:
	municipal.insert_municipality(data.get('id'),data.get('title'),data.get('district'))
	print("Municipality added in database")




