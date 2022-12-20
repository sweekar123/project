import mysql.connector as connector
from collections import defaultdict


con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
cur = con.cursor()
province_list = {1:'Province 1',2:'Madesh',3:'Bagmati',4:'Gandaki',5:'Lumbini',6:'Karnali',7:'Sudhur Paschim'}


	# def district_total_details(self,province_no):
	# 	province_query = "select count(*) from covid.data where ProvinceName = '{}'; ".format(province_list[province_no])
	# 	province_total_data = self.connect_db(province_query)
	# 	print(province_total_data)

	# def district_male_details(self,province_no):
	# 	query = "select count(*) from covid.data where ProvinceName = '{}' and gender = '{}' ".format(province_list[province_no],'male')
	# 	province_male_data = self.connect_db(query)
	# 	print(province_male_data)

	# def district_female_details(self,province_no):
	# 	query = "select count(*) from covid.data where ProvinceName = '{}' and gender = '{}' ".format(province_list[province_no],'female')
	# 	province_female_data = self.connect_db(query)
	# 	print(province_female_data)



class Province:
	con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
	#cur = con.cursor()
	def __init__(self):
		self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		cur = self.con.cursor()

	
	def connect_db(self,query):
		data = []
		cur.execute(query)
		for item in cur:
			data.append(item[0])
		return data

	def get_districts(self,province_no):
		district_query = "select DistrictName from covid.district where provinceId = {} ;".format(province_no)
		district_list = self.connect_db(district_query)
		return district_list

	def get_municipality(self,district_list):
		provincial_municipality_list = defaultdict(list)
		for districts in district_list:
			municipality_query = "select MunicipalName from covid.municipalities where DistrictName='{}';".format(districts)
			municipality_list = self.connect_db(municipality_query)
			provincial_municipality_list[districts].append(municipality_list)
		return provincial_municipality_list


	def province_total_details(self,province_no):
		province_query = "select count(*) from covid.data where ProvinceName = '{}'; ".format(province_list[province_no])
		province_total_data = self.connect_db(province_query)
		print(province_total_data)

	def province_male_details(self,province_no):
		query = "select count(*) from covid.data where ProvinceName = '{}' and gender = '{}' ".format(province_list[province_no],'male')
		province_male_data = self.connect_db(query)
		print(province_male_data)

	def province_female_details(self,province_no):
		query = "select count(*) from covid.data where ProvinceName = '{}' and gender = '{}' ".format(province_list[province_no],'female')
		province_female_data = self.connect_db(query)
		print(province_female_data)

# class District(Province):

# 	def district_total_list(self,district_list):





p1 = Province()
province_num = int(input("Enter province no"))
# p1.province_female_details(num)
# p1.province_male_details(num)
print(p1.get_municipality(p1.get_districts(province_num)))





