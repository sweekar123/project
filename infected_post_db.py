# [{"id":22,"province":1,"district":14,"municipality":14007,"createdOn":"2020-04-17T19:54:32.704295+05:45","modifiedOn":"2020-05-06T20:10:59.216325+05:45","label":"COV-NPL-22","gender":"male","age":28,"point":{"type":"Point","coordinates":[86.683718071875,26.813987534074418]},"occupation":null,"reportedOn":"2020-04-17","recoveredOn":"2020-05-06","deathOn":null,"currentState":"recovered","isReinfected":false,"source":"https://www.mohp.gov.np/eng/","comment":"","type":"local_transmission","nationality":3,"ward":2781,"relatedTo":[]},
# {"id":19,"province":1,"district":14,"municipality":14007,"createdOn":"2020-04-17T19:51:20.285022+05:45","modifiedOn":"2020-05-06T20:11:39.089068+05:45","label":"COV-NPL-19","gender":"male","age":34,"point":{"type":"Point","coordinates":[86.69333110898438,26.83175775966178]},"occupation":null,"reportedOn":"2020-04-17","recoveredOn":"2020-05-06","deathOn":null,"currentState":"recovered","isReinfected":false,"source":"https://www.mohp.gov.np/eng/","comment":"","type":"local_transmission","nationality":null,"ward":2776,"relatedTo":[]},
# {"id":21,"province":1,"district":14,"municipality":14007,"createdOn":"2020-04-17T19:53:40.612661+05:45","modifiedOn":"2020-05-06T20:12:22.521170+05:45","label":"COV-NPL-21","gender":"male","age":26,"point":{"type":"Point","coordinates":[86.69298778623047,26.818583549224297]},"occupation":null,"reportedOn":"2020-04-17","recoveredOn":"2020-05-06","deathOn":null,"currentState":"recovered","isReinfected":false,"source":"https://www.mohp.gov.np/eng/","comment":"","type":"local_transmission","nationality":3,"ward":2781,"relatedTo":[]},

import json
import mysql.connector as connector
import requests

class Infected:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
        print(self.con)
        query = "create table if not exists infected(infected_Id INT NOT NULL AUTO_INCREMENT,provinceId int,districtID int NOT NULL,municipalId int NOT NULL,gender varchar(10),ward int,PRIMARY KEY(infected_Id),CONSTRAINT fk_infected_provinceId FOREIGN KEY(provinceId) REFERENCES province(provinceId),CONSTRAINT fk_infected_districtId FOREIGN KEY(districtId) REFERENCES district(districtId),CONSTRAINT fk_municipal_municipalId FOREIGN KEY(municipalId) REFERENCES municipality(municipalId))"
        cur = self.con.cursor()
        print(cur)
        cur.execute(query)
        self.con.commit()
        print("Created")

    def insert_infected(self,province,district,municipal,gender,ward):
        query = "insert into infected(provinceId,districtId,municipalId,gender,ward) values({},{},{},'{}',{})".format(province,district,municipal,gender,ward)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Municipality Created")


infected = Infected()
json_data = json.loads(requests.get("https://data.askbhunte.com/api/v1/covid").text)
for data in json_data:
    infected.insert_infected(data.get('province'),data.get('district'),data.get('municipality'),data.get('gender'),data.get('ward'))
    print("infected added in database")

