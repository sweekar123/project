
# {'id': 22,
#  'province': 1,
#   'district': 14,
#    'municipality': 14007,
#     'createdOn': '2020-04-17T19:54:32.704295+05:45',
#      'modifiedOn': '2020-05-06T20:10:59.216325+05:45',
#       'label': 'COV-NPL-22',
#        'gender': 'male',
#         'age': 28,
#          'point': {'type': 'Point', 'coordinates': [86.683718071875, 26.813987534074418]},
#           'occupation': None,
#            'reportedOn': '2020-04-17',
#             'recoveredOn': '2020-05-06',
#              'deathOn': None,
#               'currentState': 'recovered',
#                'isReinfected': False,
#                 'source': 'https://www.mohp.gov.np/eng/',
#                  'comment': '',
#                   'type': 'local_transmission',
#                    'nationality': 3,
#                     'ward': 2781,
#                      'relatedTo': []
#                      }
#[{"_id":"5e8c4ea53e4d8a5ecdb0b3d0","id":2,"bbox":[87.4925678500812,26.8598967052017,88.0802293074398,27.4383535384553],"centroid":{"type":"Point","coordinates":[87.77579807095165,27.114999613984395]},"title":"Panchthar","title_en":"Panchthar","title_ne":"पाँचथर","code":"panchthar","province":1}]



import json
import requests
import mysql.connector as connector


class District:
	def __init__(self):
		self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		query = 'create table if not exists district(districtId int unique,DistrictName varchar(100),provinceId int,CONSTRAINT fk_provinceId FOREIGN KEY(provinceId) REFERENCES province(provinceId))'
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("Created")

	def insert_district(self,id,district,province):
		query = "insert into district(districtId,DistrictName,provinceId) values({},'{}',{})".format(
			id,district,province)
		print(query)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("district saved to db")		

#main Program
district = District()
response = requests.get("https://data.askbhunte.com/api/v1/districts")
print(response.text)
json_data = json.loads(response.text)
for data in json_data: 
	district.insert_district(data.get('id'),data.get('code'),data.get('province'))
	print("District with id : ",str(data.get('id')))




# json_data = json.load([{"id":22,"province":1,"district":14,"municipality":14007,"createdOn":"2020-04-17T19:54:32.704295+05:45","modifiedOn":"2020-05-06T20:10:59.216325+05:45","label":"COV-NPL-22","gender":"male","age":28,"point":{"type":"Point","coordinates":[86.683718071875,26.813987534074418]},"occupation":null,"reportedOn":"2020-04-17","recoveredOn":"2020-05-06","deathOn":null,"currentState":"recovered","isReinfected":false,"source":"https://www.mohp.gov.np/eng/","comment":"","type":"local_transmission","nationality":3,"ward":2781,"relatedTo":[]},
# 	{"id":19,"province":1,"district":14,"municipality":14007,"createdOn":"2020-04-17T19:51:20.285022+05:45","modifiedOn":"2020-05-06T20:11:39.089068+05:45","label":"COV-NPL-19","gender":"male","age":34,"point":{"type":"Point","coordinates":[86.69333110898438,26.83175775966178]},"occupation":null,"reportedOn":"2020-04-17","recoveredOn":"2020-05-06","deathOn":null,"currentState":"recovered","isReinfected":false,"source":"https://www.mohp.gov.np/eng/","comment":"","type":"local_transmission","nationality":null,"ward":2776,"relatedTo":[]},
# 	{"id":21,"province":1,"district":14,"municipality":14007,"createdOn":"2020-04-17T19:53:40.612661+05:45","modifiedOn":"2020-05-06T20:12:22.521170+05:45","label":"COV-NPL-21","gender":"male","age":26,"point":{"type":"Point","coordinates":[86.69298778623047,26.818583549224297]},"occupation":null,"reportedOn":"2020-04-17","recoveredOn":"2020-05-06","deathOn":null,"currentState":"recovered","isReinfected":false,"source":"https://www.mohp.gov.np/eng/","comment":"","type":"local_transmission","nationality":3,"ward":2781,"relatedTo":[]}])
# print(json_data)



