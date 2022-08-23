from pickle import TRUE
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Gamdom_cs_paris :
	class_name1 = None
	class_name2 = None
	class_cote1 = None
	class_cote2 = None
	class_draw = None

class empire_cs_paris :
	class_name1 = None
	class_name2 = None
	class_cote1 = None
	class_cote2 = None
	class_draw = None

class vulkan_paris :
	class_name1 = None
	class_name2 = None
	class_cote1 = None
	class_cote2 = None
	class_draw = None



print("HELLO\n")

option = webdriver.ChromeOptions()
option.add_argument("enable-automation")
option.add_argument("disable-infobars")
driver = webdriver.Chrome("/Users/manaccac/.brew/bin/chromedriver", options=option)


while 1 :
	z = 0
	while z != 3 :
		if (z == 1):
			print("CSGO")
			gamdom_cs = 'https://gamdom.io/esports'
			in_gamdom = 'https://hub88b-ytuoyswg.betsy.gg/csgo'
			empire = 'https://csgoempire.com/match-betting'
			in_empire = '2'
			truc_de_merde = 4
			vulkan = 'https://thunderpick.com/en/esports/csgo'
		if (z == 0):
			print("DOTA2")
			gamdom_cs = 'https://gamdom.io/esports'
			in_gamdom = 'https://hub88b-ytuoyswg.betsy.gg/dota2'
			empire = 'https://csgoempire.com/match-betting'
			in_empire = '3'
			truc_de_merde = 4
			vulkan = 'https://thunderpick.com/en/esports/dota-2'
		if (z == 2):
			print("LOL")
			gamdom_cs = 'https://gamdom.io/esports'
			in_gamdom = 'https://hub88b-ytuoyswg.betsy.gg/lol'
			empire = 'https://csgoempire.com/match-betting'
			in_empire = '4'
			truc_de_merde = 4
			vulkan = 'https://thunderpick.com/en/esports/league-of-legends'
		if (z == 3):
			print("OWER")
			gamdom_cs = 'https://gamdom.io/esports'
			in_gamdom = 'https://hub88b-ytuoyswg.betsy.gg/ow'
			empire = 'https://csgoempire.com/match-betting'
			in_empire = '5'
			truc_de_merde = 4
			vulkan = 'https://thunderpick.com/en/esports/overwatch'

		# # # # # # # # # # # # # # # # # # # # # # # # # # # 

		print("####################################### GAMDOM #######################################")
		driver.get(gamdom_cs)

		sleep(7)
		# 											 dota2 / csgo / lol
		driver.get(in_gamdom)

		# sleep(10)
		sleep(3)

		count = len(driver.find_elements(By.CLASS_NAME, "grid-line"))
		print("ALL = ", count);
		count_Live = len(driver.find_elements(By.CSS_SELECTOR, "div.grid-event._live"))
		print("Live = ", count_Live);


		sleep(1)
		if count_Live == 0 :
			count_Live = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[3]/div[2]/div"))
			print("Aujourd'hui = ", count_Live);
			count_Today = 0
		else :
			count_Today = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[4]/div[2]/div"))
			print("Aujourd'hui = ", count_Today);
			if (count_Today == 0) :
				break
		if (count_Live == 0 and count_Today == 0) :
			break


		# print("------------------------------------Today------------------------------------\n\n")
		i = 1;

		class_gamdom = Gamdom_cs_paris()
		class_gamdom.class_name1 = []
		class_gamdom.class_name2 = []
		class_gamdom.class_cote1 = []
		class_gamdom.class_cote2 = []
		class_gamdom.class_draw = []

		while(i != count_Live + 1) : 
			try :
				scroll = driver.find_element(By.XPATH,"//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[3]/div[2]/div["+ str(i) +"]/div[2]/a[1]/div[1]/div[1]/div")
				driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
				sleep(0.005)
			except :
				print("")
			try :
				nb_paris = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[3]/div[2]/div["+ str(i) +"]/div[2]/div/div[1]/button"))
				# print(nb_paris)
				
				name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[1]/div').text
				name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[3]/div').text

				cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[1]/span[2]').text
				cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[2]/span[2]').text
				draw = "0"
				if (nb_paris == 3) :
					draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text
				else :
					draw = 0
				class_gamdom.class_name1.append(name1)
				class_gamdom.class_name2.append(name2)
				class_gamdom.class_cote1.append(cote1)
				class_gamdom.class_cote2.append(cote2)
				class_gamdom.class_draw.append(draw)


				# print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")
			except :
				print("")
			i = i + 1

		# print("\n\n------------------------------------FIN------------------------------------\n\n")

		# print("------------------------------------Tomorrow------------------------------------\n\n")
		i = 1;

		while(i != count_Today + 1) : 
			try :
				nb_paris = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[4]/div[2]/div["+ str(i) +"]/div[2]/div/div[1]/button"))
				# print(nb_paris)
				scroll = driver.find_element(By.XPATH,"//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[4]/div[2]/div["+ str(i) +"]/div[2]/a[1]/div[1]/div[1]/div")
				driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
				sleep(0.005)

				name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[4]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[1]/div').text
				name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[4]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[3]/div').text

				cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[4]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[1]/span[2]').text
				cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[4]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[2]/span[2]').text
				draw = "0"
				if (nb_paris == 3) :
					draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[4]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text
				else :
					draw = 0
				class_gamdom.class_name1.append(name1)
				class_gamdom.class_name2.append(name2)
				class_gamdom.class_cote1.append(cote1)
				class_gamdom.class_cote2.append(cote2)
				class_gamdom.class_draw.append(draw)
				# print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")s
			except :
				print("")
			i = i + 1

		print("####################################### FIN GAMDOM #######################################")

		sleep(2)

		print("####################################### EMPIRE #######################################")
		driver.get(empire)

		sleep(4)
		# 																									/// 2 pour cs 3 pour dota 4 lol ...
		driver.find_element(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div["+in_empire+"]/div").click()

		sleep(4)
		driver.find_element(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[2]/div[2]/button[5]/span").click()

		sleep(4)
		count = len(driver.find_elements(By.CLASS_NAME, "mb-lg"))
		print("ALL = ", count);

		class_empire = empire_cs_paris()
		class_empire.class_name1 = []
		class_empire.class_name2 = []
		class_empire.class_cote1 = []
		class_empire.class_cote2 = []
		class_empire.class_draw = []

		i = 1

		while i != count + 1:
			j = 2
			count_Today = len(driver.find_elements(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[3]/div/div/div["+ str(i) +"]/div/div"))
			while j != count_Today + 1 :
				nb_paris = len(driver.find_elements(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[3]/div/div/div["+ str(i) +"]/div/div["+ str(j) +"]/div/div[4]/button"))
				# print(nb_paris)



				if (driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/	div/div['+ str(j) +']/div/div[4]/button[1]').is_enabled() == True ) :
					name1 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[1]/p[1]').text
					name2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[2]/p[1]').text

					cote1 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[1]/span/div/span').text
					cote2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[2]/span/div/span').text

					draw = "0"
					if (nb_paris == 3) :
						draw = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[2]/span/div/span').text
						cote2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[3]/span/div/span').text
					else :
						draw = 0

					# print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")

					class_empire.class_name1.append(name1)
					class_empire.class_name2.append(name2)
					class_empire.class_cote1.append(cote1)
					class_empire.class_cote2.append(cote2)
					class_empire.class_draw.append(draw)
				j = j + 1

			i = i + 1

		print("####################################### FIN EMPIRE #######################################")

		#######################################


		# print("####################################### VULKAN #######################################")

		# div de match 1 soit live soit today
		# //*[@id="match-list-header"]/div[2]
		driver.get(vulkan)

		class_vulkan = vulkan_paris()
		class_vulkan.class_name1 = []
		class_vulkan.class_name2 = []
		class_vulkan.class_cote1 = []
		class_vulkan.class_cote2 = []
		class_vulkan.class_draw = []

		sleep(3)

		# print("count 1 =" , len(driver.find_elements(By.XPATH, "//*[@id='match-list-header']/div[2]/div[2]/div/div")))
		# print("count 2 =" , len(driver.find_elements(By.XPATH, "//*[@id='match-list-header']/div[3]/div[2]/div/div")))
		i = 0
		while i != 4 :
			driver.execute_script("window.scrollBy(0,200);")
			sleep(0.1)
			i = i + 1


		count_1 = len(driver.find_elements(By.XPATH, "//*[@id='match-list-header']/div[2]/div[2]/div/div"))
		count_2 = len(driver.find_elements(By.XPATH, "//*[@id='match-list-header']/div[3]/div[2]/div/div"))

		while i != 4 :
			driver.execute_script("window.scrollBy(0,-200);")
			sleep(0.1)
			i = i + 1

		i = 1
		while(i != count_1 + 1) : 
																									# // team 1 puis 2 ...
			try :

				scroll = driver.find_element(By.XPATH,"//*[@id='match-list-header']/div[2]/div[2]/div/div["+str(i)+"]/div[1]")
				driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
				sleep(0.5)
				name1 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[2]/div[2]/div/div['+str(i)+']/div[1]').text
				name2 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[2]/div[2]/div/div['+str(i)+']/div[4]').text

				cote1 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[2]/div[2]/div/div['+str(i)+']/div[3]/button/span').text
				cote2 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[2]/div[2]/div/div['+str(i)+']/div[6]/button/span').text
				try :
					draw = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[2]/div[2]/div/div['+str(i)+']/div[7]/button/span').text
				except :
					draw = 0
				class_vulkan.class_name1.append(name1)
				class_vulkan.class_name2.append(name2)
				class_vulkan.class_cote1.append(cote1)
				class_vulkan.class_cote2.append(cote2)
				class_vulkan.class_draw.append(draw)
			except :
				print("erreur 1")

			# print(name1, " = " , cote1, "\n", name2 , " = " , cote2)
			# print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")
			i = i + 1
		i = 1
		while(i != count_2 + 1) : 
																									# // team 1 puis 2 ...
			try :
				scroll = driver.find_element(By.XPATH,"//*[@id='match-list-header']/div[3]/div[2]/div/div["+str(i)+"]/div[1]")
				driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
				sleep(0.5)
				name1 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[3]/div[2]/div/div['+str(i)+']/div[1]').text
				name2 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[3]/div[2]/div/div['+str(i)+']/div[4]').text

				cote1 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[3]/div[2]/div/div['+str(i)+']/div[3]/button/span').text
				cote2 = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[3]/div[2]/div/div['+str(i)+']/div[6]/button/span').text
				try :
					draw = driver.find_element(By.XPATH, '//*[@id="match-list-header"]/div[3]/div[2]/div/div['+str(i)+']/div[7]/button/span').text
				except :
					draw = 0
				# //*[@id="match-list-header"]/div[3]/div[2]/div[1]/div[1]/div[7]/button/span

				class_vulkan.class_name1.append(name1)
				class_vulkan.class_name2.append(name2)
				class_vulkan.class_cote1.append(cote1)
				class_vulkan.class_cote2.append(cote2)
				class_vulkan.class_draw.append(draw)
			except :
				print("erreur 2")
			# print(name1, " = " , cote1, "\n", name2 , " = " , cote2)
			# print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")
			i = i + 1



		# print("####################################### FIN VULKAN #######################################")
		# sleep(1)
		#######################################



		for i in range(len(class_empire.class_name1)):
			class_empire.class_name1[i] = class_empire.class_name1[i].lower()

		for i in range(len(class_gamdom.class_name1)):
			class_gamdom.class_name1[i] = class_gamdom.class_name1[i].lower()

		for i in range(len(class_empire.class_name2)):
			class_empire.class_name2[i] = class_empire.class_name2[i].lower()

		for i in range(len(class_gamdom.class_name2)):
			class_gamdom.class_name2[i] = class_gamdom.class_name2[i].lower()

		match_name1 = set(class_empire.class_name1) & set(class_gamdom.class_name1)
		match_name2 = set(class_empire.class_name2) & set(class_gamdom.class_name2)

		index_name1 = []
		index_name2 = []
		match_name1_list = list(match_name1)
		match_name2_list = list(match_name2)

		for i in range(len(match_name1_list)):
			index_name1.append(class_empire.class_name1.index(match_name1_list[i]))

		for i in range(len(match_name2_list)):
			index_name2.append(class_empire.class_name2.index(match_name2_list[i]))

		for i in range(len(index_name2)):
			index_name1.append(index_name2[i])

		
		result = [] 
		[result.append(x) for x in index_name1 if x not in result] 

		result.sort()

		##################################################

		match_name1_list = list(match_name1)
		match_name2_list = list(match_name2)
		index_name1 = []
		index_name2 = []


		for i in range(len(match_name1_list)):
			index_name1.append(class_gamdom.class_name1.index(match_name1_list[i]))

		for i in range(len(match_name2_list)):
			index_name2.append(class_gamdom.class_name2.index(match_name2_list[i]))

		for i in range(len(index_name2)):
			index_name1.append(index_name2[i])

		result = [] 
		[result.append(x) for x in index_name1 if x not in result] 

		result.sort()
		print ("The list after removing duplicates: " + str(result)) 


		i = 0
		matches_name1 = []
		matches_name2 = []
		index_gamdom_name1 = []
		index_gamdom_name2 = []

		while i != len(result) :
			if class_gamdom.class_name1[result[i]] in class_empire.class_name1:
				index_gamdom_name1.append(result[i])
				matches_name1.append(class_gamdom.class_name1[result[i]] )
			i = i + 1
		i = 0
		print(index_gamdom_name1)

		while i != len(result):
			if result[i] not in index_gamdom_name1 :
				index_gamdom_name2.append(result[i])
			i = i + 1

		print(index_gamdom_name2)


		i = 0
		print(matches_name1)
		while i != len(index_gamdom_name2) :
			if class_gamdom.class_name2[index_gamdom_name2[i]] in class_empire.class_name2:
				matches_name2.append(class_gamdom.class_name2[index_gamdom_name2[i]])
			i = i + 1
		i = 0

		print(matches_name2)

		index_empire_name1 = []
		index_empire_name2 = []
		# # # # # # # # 
		while i != len(matches_name1) :
			index_empire_name1.append(class_empire.class_name1.index(class_gamdom.class_name1[index_gamdom_name1[i]]))
			i = i + 1
		j = 0
		while j != len(matches_name2) :
			index_empire_name2.append(class_empire.class_name2.index(class_gamdom.class_name2[index_gamdom_name2[j]]))
			j = j + 1

		print(index_empire_name1)
		print(index_empire_name2)

		i = 0
		while i != len(index_empire_name1) :
			if (class_empire.class_draw[index_empire_name1[i]] == 0) :
				bet_1 = 1 / float(class_empire.class_cote1[index_empire_name1[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name1[i]])
				bet_2 = 1 / float(class_empire.class_cote2[index_empire_name1[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name1[i]])
				if (bet_1 < bet_2 and bet_1 < 1) :
					print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
					, class_empire.class_cote1[index_empire_name1[i]], "			" , class_empire.class_cote2[index_empire_name1[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name1[i]], "	" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")
					print(bet_1)
				if (bet_1 > bet_2 and bet_2 < 1) :
					print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
					, class_empire.class_cote1[index_empire_name1[i]], "			" , class_empire.class_cote2[index_empire_name1[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name1[i]], "	" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")
					print(bet_2)
			else :
				if (float(class_empire.class_cote1[index_empire_name1[i]]) >  float(class_gamdom.class_cote1[index_gamdom_name1[i]]))  :
					cote1_max = float(class_empire.class_cote1[index_empire_name1[i]])
				else :
					cote1_max = float(class_gamdom.class_cote1[index_gamdom_name1[i]])
				if (float(class_empire.class_cote2[index_empire_name1[i]]) >  float(class_gamdom.class_cote2[index_gamdom_name1[i]]))  :
					cote2_max = float(class_empire.class_cote2[index_empire_name1[i]])
				else :
					cote2_max = float(class_gamdom.class_cote2[index_empire_name1[i]])
				if (float(class_empire.class_draw[index_empire_name1[i]]) >  float(class_gamdom.class_draw[index_gamdom_name1[i]]))  :
					draw_max = float(class_empire.class_draw[index_empire_name1[i]])
				else :
					draw_max = float(class_gamdom.class_draw[index_gamdom_name1[i]])
				if (1/ cote1_max + 1/ cote2_max + 1/ draw_max < 1) :
					print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
					, class_empire.class_cote1[index_empire_name1[i]], "	" , class_empire.class_draw[index_empire_name1[i]] ,"	" ,class_empire.class_cote2[index_empire_name1[i]],  " \n")
					print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name1[i]], "	", class_gamdom.class_draw[index_gamdom_name1[i]]  ,"	" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")
					print(1/ cote1_max + 1/ cote2_max + 1/ draw_max)
			i = i + 1

		i = 0
		while i != len(index_empire_name2) :
			if (class_empire.class_draw[index_empire_name2[i]] == 0) :
				bet_1 = 1 / float(class_empire.class_cote1[index_empire_name2[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name2[i]])
				bet_2 = 1 / float(class_empire.class_cote2[index_empire_name2[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name2[i]])
				if (bet_1 < bet_2 and bet_1 < 1) :
					print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
					, class_empire.class_cote1[index_empire_name2[i]], "			" , class_empire.class_cote2[index_empire_name2[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name2[i]], "			" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
					print(bet_1)
				if (bet_1 > bet_2 and bet_2 < 1) :
					print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
					, class_empire.class_cote1[index_empire_name2[i]], "			" , class_empire.class_cote2[index_empire_name2[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name2[i]], "			" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
					print(bet_2)
			else :
				if (float(class_empire.class_cote1[index_empire_name2[i]]) >  float(class_gamdom.class_cote1[index_gamdom_name2[i]]))  :
					cote1_max = float(class_empire.class_cote1[index_empire_name2[i]])
				else :
					cote1_max = float(class_gamdom.class_cote1[index_gamdom_name2[i]])
				if (float(class_empire.class_cote2[index_empire_name2[i]]) >  float(class_gamdom.class_cote2[index_gamdom_name2[i]]))  :
					cote2_max = float(class_empire.class_cote2[index_empire_name2[i]])
				else :
					cote2_max = float(class_gamdom.class_cote2[index_empire_name2[i]])
				if (float(class_empire.class_draw[index_empire_name2[i]]) >  float(class_gamdom.class_draw[index_gamdom_name2[i]]))  :
					draw_max = float(class_empire.class_draw[index_empire_name2[i]])
				else :
					draw_max = float(class_gamdom.class_draw[index_gamdom_name2[i]])
				if (1/ cote1_max + 1/ cote2_max + 1/ draw_max < 1) :
					print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
					, class_empire.class_cote1[index_empire_name2[i]], "	" , class_empire.class_draw[index_empire_name2[i]] ,"	" ,class_empire.class_cote2[index_empire_name2[i]],  " \n")
					print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name2[i]], "	", class_gamdom.class_draw[index_gamdom_name2[i]]  ,"	" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
					print(1/ cote1_max + 1/ cote2_max + 1/ draw_max)
			
			i = i + 1

		z = z + 1

		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # VULKAAAAAAA
		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # VULKAAAAAAA
		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # VULKAAAAAAA
		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # VULKAAAAAAA

		index_empire_name1 = []
		index_empire_name2 = []

		for i in range(len(class_vulkan.class_name1)):
			class_vulkan.class_name1[i] = class_vulkan.class_name1[i].lower()

		for i in range(len(class_vulkan.class_name2)):
			class_vulkan.class_name2[i] = class_vulkan.class_name2[i].lower()

		match_name_vulkan_gamdom1 = set(class_vulkan.class_name1) & set(class_gamdom.class_name1)
		match_name_vulkan_gamdom2 = set(class_vulkan.class_name2) & set(class_gamdom.class_name2)

		match_name_vulkan_empire1 = set(class_vulkan.class_name1) & set(class_empire.class_name1)
		match_name_vulkan_empire2 = set(class_vulkan.class_name2) & set(class_empire.class_name2)

		match_vulkan_gamdom_name1_list = list(match_name_vulkan_gamdom1)
		match_vulkan_gamdom_name2_list = list(match_name_vulkan_gamdom2)

		index_vulkan_gamdom_name1 = []
		index_vulkan_gamdom_name2 = []


		for i in range(len(match_vulkan_gamdom_name1_list)):
			index_vulkan_gamdom_name1.append(class_vulkan.class_name1.index(match_vulkan_gamdom_name1_list[i]))

		for i in range(len(match_vulkan_gamdom_name2_list)):
			index_vulkan_gamdom_name2.append(class_vulkan.class_name2.index(match_vulkan_gamdom_name2_list[i]))

		for i in range(len(index_vulkan_gamdom_name2)):
			index_vulkan_gamdom_name1.append(index_vulkan_gamdom_name2[i])

		result = [] 
		[result.append(x) for x in index_vulkan_gamdom_name1 if x not in result] 

		result.sort()
		# print ("The list after removing duplicates vulkan_gamdom: " + str(result)) 


		i = 0
		matches_vulk_gam_name1 = []
		matches_vulk_gam_name2 = []
		index_vulk_gam_name1 = []
		index_vulk_gam_name2 = []


		while i != len(result) :
			if class_vulkan.class_name1[result[i]] in class_gamdom.class_name1:
				index_vulk_gam_name1.append(result[i])
				matches_vulk_gam_name1.append(class_vulkan.class_name1[result[i]] )
			i = i + 1
		i = 0
		# print("vulkan_gam")
		# print(index_vulk_gam_name1)

		while i != len(result):
			if result[i] not in index_vulk_gam_name1 :
				index_vulk_gam_name2.append(result[i])
			i = i + 1

		# print("vulkan_gam")
		# print(index_vulk_gam_name2)

		i = 0
		while i != len(index_vulk_gam_name2) :
			if class_vulkan.class_name2[index_vulk_gam_name2[i]] in class_gamdom.class_name2:
				matches_vulk_gam_name2.append(class_vulkan.class_name2[index_vulk_gam_name2[i]])
			i = i + 1
		# print("vulkan_gam match")
		# print(matches_vulk_gam_name1)
		# print("vulkan_gam match")
		# print(matches_vulk_gam_name2)

		# # # # # # # # 

		i = 0

		matches_vulk_emp_name1 = []
		matches_vulk_emp_name2 = []
		index_vulk_emp_name1 = []
		index_vulk_emp_name2 = []
		match_vulkan_empire_name1_list = list(match_name_vulkan_empire1)
		match_vulkan_empire_name2_list = list(match_name_vulkan_empire2)

		index_empire_gamdom_name1 = []
		index_empire_gamdom_name2 = []

		for i in range(len(match_vulkan_empire_name1_list)):
			index_empire_gamdom_name1.append(class_vulkan.class_name1.index(match_vulkan_empire_name1_list[i]))

		for i in range(len(match_vulkan_empire_name2_list)):
			index_empire_gamdom_name2.append(class_vulkan.class_name2.index(match_vulkan_empire_name2_list[i]))

		for i in range(len(index_empire_gamdom_name2)):
			index_empire_gamdom_name1.append(index_empire_gamdom_name2[i])

		result = [] 
		[result.append(x) for x in index_empire_gamdom_name1 if x not in result] 

		result.sort()
		# print ("The list after removing duplicates vulkan_empire: " + str(result)) 

		i = 0
		while i != len(result) :
			# print("name 1 ======= ")
			# print(class_vulkan.class_name1[result[i]])
			if class_vulkan.class_name1[result[i]] in class_empire.class_name1:
				index_vulk_emp_name1.append(result[i])
				matches_vulk_emp_name1.append(class_vulkan.class_name1[result[i]] )
			i = i + 1
		i = 0
		# print(index_vulk_emp_name1)

		while i != len(result):
			if result[i] not in index_vulk_emp_name1 :
				index_vulk_emp_name2.append(result[i])
			i = i + 1

		# print(index_vulk_emp_name2)

		i = 0
		while i != len(index_vulk_emp_name2) :
			if class_vulkan.class_name2[index_vulk_emp_name2[i]] in class_empire.class_name2:
				matches_vulk_emp_name2.append(class_vulkan.class_name2[index_vulk_emp_name2[i]])
			i = i + 1

		# print(matches_vulk_emp_name1)
		# print(matches_vulk_emp_name2)

		# # # # # # # # 

		index_gamdom_name1 = []
		index_gamdom_name2 = []
		i = 0
		while i != len(matches_vulk_gam_name1) :
			index_gamdom_name1.append(class_gamdom.class_name1.index(class_vulkan.class_name1[index_vulk_gam_name1[i]]))
			i = i + 1
		j = 0
		while j != len(matches_vulk_gam_name2) :
			index_gamdom_name2.append(class_gamdom.class_name2.index(class_vulkan.class_name2[index_vulk_gam_name2[j]]))
			j = j + 1

		# print("index gamdom from vulkan match")
		# print(index_gamdom_name1)
		# print(index_gamdom_name2)

		# # # # # # # # 

		index_empire_name1 = []
		index_empire_name2 = []
		i = 0
		while i != len(matches_vulk_emp_name1) :
			index_empire_name1.append(class_empire.class_name1.index(class_vulkan.class_name1[index_vulk_emp_name1[i]]))
			i = i + 1
		j = 0
		while j != len(matches_vulk_emp_name2) :
			index_empire_name2.append(class_empire.class_name2.index(class_vulkan.class_name2[index_vulk_emp_name2[j]]))
			j = j + 1

		# print("index empire from vulkan match")
		# print(index_empire_name1)
		# print(index_empire_name2)

		## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  


		i = 0
		print("\n\n\nempire")
		print("thunderpick")
		while i != len(index_vulk_emp_name1) :
			if (class_empire.class_draw[index_empire_name1[i]] == 0) :
				bet_1 = 1 / float(class_empire.class_cote1[index_empire_name1[i]]) +  1 / float(class_vulkan.class_cote2[index_vulk_emp_name1[i]])
				bet_2 = 1 / float(class_empire.class_cote2[index_empire_name1[i]]) +  1 / float(class_vulkan.class_cote1[index_vulk_emp_name1[i]])
				if (bet_1 < bet_2 and bet_1 < 1) :
					print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
						, class_empire.class_cote1[index_empire_name1[i]], "			" , class_empire.class_cote2[index_empire_name1[i]], " \n")
					print(class_vulkan.class_name1[index_vulk_emp_name1[i]], " " , class_vulkan.class_name2[index_vulk_emp_name1[i]], "\n"
						, class_vulkan.class_cote1[index_vulk_emp_name1[i]], "	" , class_vulkan.class_cote2[index_vulk_emp_name1[i]], " \n")
					print(bet_1)

				if (bet_1 > bet_2 and bet_2 < 1 ):
					print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
						, class_empire.class_cote1[index_empire_name1[i]], "			" , class_empire.class_cote2[index_empire_name1[i]], " \n")
					print(class_vulkan.class_name1[index_vulk_emp_name1[i]], " " , class_vulkan.class_name2[index_vulk_emp_name1[i]], "\n"
						, class_vulkan.class_cote1[index_vulk_emp_name1[i]], "	" , class_vulkan.class_cote2[index_vulk_emp_name1[i]], " \n")
					print(bet_2)
			else :
				if (float(class_empire.class_cote1[index_empire_name1[i]]) >  float(class_vulkan.class_cote1[index_vulk_emp_name1[i]]))  :
					cote1_max = float(class_empire.class_cote1[index_empire_name1[i]])
				else :
					cote1_max = float(class_vulkan.class_cote1[index_vulk_emp_name1[i]])
				if (float(class_empire.class_cote2[index_empire_name1[i]]) >  float(class_vulkan.class_cote2[index_vulk_emp_name1[i]]))  :
					cote2_max = float(class_empire.class_cote2[index_empire_name1[i]])
				else :
					cote2_max = float(class_vulkan.class_cote2[index_empire_name1[i]])
				if (float(class_empire.class_draw[index_empire_name1[i]]) >  float(class_vulkan.class_draw[index_vulk_emp_name1[i]]))  :
					draw_max = float(class_empire.class_draw[index_empire_name1[i]])
				else :
					draw_max = float(class_vulkan.class_draw[index_vulk_emp_name1[i]])
				if (1/ cote1_max + 1/ cote2_max + 1/ draw_max < 1) :
					print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
					, class_empire.class_cote1[index_empire_name1[i]], "	" , class_empire.class_draw[index_empire_name1[i]] ,"	" ,class_empire.class_cote2[index_empire_name1[i]],  " \n")
					print(class_vulkan.class_name1[index_vulk_emp_name1[i]], " " , class_vulkan.class_name2[index_vulk_emp_name1[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_emp_name1[i]], "	", class_vulkan.class_draw[index_vulk_emp_name1[i]]  ,"	" , class_vulkan.class_cote2[index_vulk_emp_name1[i]], " \n")
					print(1/ cote1_max + 1/ cote2_max + 1/ draw_max)
			
			i = i + 1

		i = 0
		while i != len(index_vulk_emp_name2) :

			if (class_empire.class_draw[index_empire_name2[i]] == 0) :
				bet_1 = 1 / float(class_empire.class_cote1[index_empire_name2[i]]) +  1 / float(class_vulkan.class_cote2[index_vulk_emp_name2[i]])
				bet_1 = 1 / float(class_empire.class_cote2[index_empire_name2[i]]) +  1 / float(class_vulkan.class_cote1[index_vulk_emp_name2[i]])
				if (bet_1 < bet_2 and bet_1 < 1) :
					print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
					, class_empire.class_cote1[index_empire_name2[i]], "			" , class_empire.class_cote2[index_empire_name2[i]], " \n")
					print(class_vulkan.class_name1[index_vulk_emp_name2[i]], " " , class_vulkan.class_name2[index_vulk_emp_name2[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_emp_name2[i]], "	" , class_vulkan.class_cote2[index_vulk_emp_name2[i]], " \n")
					print(bet_1)

				if (bet_1 > bet_2 and bet_2 < 1 ):
					print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
					, class_empire.class_cote1[index_empire_name2[i]], "			" , class_empire.class_cote2[index_empire_name2[i]], " \n")
					print(class_vulkan.class_name1[index_vulk_emp_name2[i]], " " , class_vulkan.class_name2[index_vulk_emp_name2[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_emp_name2[i]], "	" , class_vulkan.class_cote2[index_vulk_emp_name2[i]], " \n")
					print(bet_2)

			else :
				if (float(class_empire.class_cote1[index_empire_name2[i]]) >  float(class_vulkan.class_cote1[index_vulk_emp_name2[i]]))  :
					cote1_max = float(class_empire.class_cote1[index_empire_name2[i]])
				else :
					cote1_max = float(class_vulkan.class_cote1[index_vulk_emp_name2[i]])
				if (float(class_empire.class_cote2[index_empire_name2[i]]) >  float(class_vulkan.class_cote2[index_vulk_emp_name2[i]]))  :
					cote2_max = float(class_empire.class_cote2[index_empire_name2[i]])
				else :
					cote2_max = float(class_vulkan.class_cote2[index_empire_name2[i]])
				if (float(class_empire.class_draw[index_empire_name2[i]]) >  float(class_vulkan.class_draw[index_vulk_emp_name2[i]]))  :
					draw_max = float(class_empire.class_draw[index_empire_name2[i]])
				else :
					draw_max = float(class_vulkan.class_draw[index_vulk_emp_name2[i]])
				if (1/ cote1_max + 1/ cote2_max + 1/ draw_max < 1) :
					print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
					, class_empire.class_cote1[index_empire_name2[i]], "	" , class_empire.class_draw[index_empire_name2[i]] ,"	" ,class_empire.class_cote2[index_empire_name2[i]],  " \n")
					print(class_vulkan.class_name1[index_vulk_emp_name2[i]], " " , class_vulkan.class_name2[index_vulk_emp_name2[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_emp_name2[i]], "	", class_vulkan.class_draw[index_vulk_emp_name2[i]]  ,"	" , class_vulkan.class_cote2[index_vulk_emp_name2[i]], " \n")
					print(1/ cote1_max + 1/ cote2_max + 1/ draw_max)
			
			i = i + 1

		i = 0
		print("\n\n\thunderpick")
		print("gamdom")
		while i != len(index_vulk_gam_name1) :
			if (class_vulkan.class_draw[index_vulk_gam_name1[i]] == 0) :
				bet_1 = 1 / float(class_vulkan.class_cote1[index_vulk_gam_name1[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name1[i]])
				bet_2 = 1 / float(class_vulkan.class_cote2[index_vulk_gam_name1[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name1[i]])

				if (bet_1 < bet_2 and bet_1 < 1) :
					print(class_vulkan.class_name1[index_vulk_gam_name1[i]], " " , class_vulkan.class_name2[index_vulk_gam_name1[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_gam_name1[i]], "			" , class_vulkan.class_cote2[index_vulk_gam_name1[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name1[i]], "			" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")
					print(bet_1)
				if (bet_1 > bet_2 and bet_2 < 1 ):
					print(class_vulkan.class_name1[index_vulk_gam_name1[i]], " " , class_vulkan.class_name2[index_vulk_gam_name1[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_gam_name1[i]], "			" , class_vulkan.class_cote2[index_vulk_gam_name1[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name1[i]], "			" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")
					print(bet_2)
			else :
				if (float(class_gamdom.class_cote1[index_gamdom_name1[i]]) >  float(class_vulkan.class_cote1[index_vulk_gam_name1[i]]))  :
					cote1_max = float(class_gamdom.class_cote1[index_gamdom_name1[i]])
				else :
					cote1_max = float(class_vulkan.class_cote1[index_vulk_gam_name1[i]])
				if (float(class_gamdom.class_cote2[index_gamdom_name1[i]]) >  float(class_vulkan.class_cote2[index_vulk_gam_name1[i]]))  :
					cote2_max = float(class_gamdom.class_cote2[index_gamdom_name1[i]])
				else :
					cote2_max = float(class_vulkan.class_cote2[index_gamdom_name1[i]])
				if (float(class_gamdom.class_draw[index_gamdom_name1[i]]) >  float(class_vulkan.class_draw[index_vulk_gam_name1[i]]))  :
					draw_max = float(class_gamdom.class_draw[index_gamdom_name1[i]])
				else :
					draw_max = float(class_vulkan.class_draw[index_vulk_gam_name1[i]])
				if (1/ cote1_max + 1/ cote2_max + 1/ draw_max < 1) :
					print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name1[i]], "	" , class_gamdom.class_draw[index_gamdom_name1[i]] ,"	" ,class_gamdom.class_cote2[index_gamdom_name1[i]],  " \n")
					print(class_vulkan.class_name1[index_vulk_gam_name1[i]], " " , class_vulkan.class_name2[index_vulk_gam_name1[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_gam_name1[i]], "	", class_vulkan.class_draw[index_vulk_gam_name1[i]]  ,"	" , class_vulkan.class_cote2[index_vulk_gam_name1[i]], " \n")
					print(1/ cote1_max + 1/ cote2_max + 1/ draw_max)
			
			i = i + 1

		i = 0
		while i != len(index_vulk_gam_name2) :
			if (class_vulkan.class_draw[index_vulk_gam_name2[i]] == 0) :
				bet_1 = 1 / float(class_vulkan.class_cote1[index_vulk_gam_name2[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name2[i]])
				bet_2 = 1 / float(class_vulkan.class_cote2[index_vulk_gam_name2[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name2[i]])
				if (bet_1 < bet_2 and bet_1 < 1) :
					print(class_vulkan.class_name1[index_vulk_gam_name2[i]], " " , class_vulkan.class_name2[index_vulk_gam_name2[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_gam_name2[i]], "			" , class_vulkan.class_cote2[index_vulk_gam_name2[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name2[i]], "			" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
					print(bet_1)
				if (bet_1 > bet_2 and bet_2 < 1 ):
					print(class_vulkan.class_name1[index_vulk_gam_name2[i]], " " , class_vulkan.class_name2[index_vulk_gam_name2[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_gam_name2[i]], "			" , class_vulkan.class_cote2[index_vulk_gam_name2[i]], " \n")
					print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name2[i]], "			" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
					print(bet_2)
			else :
				if (float(class_gamdom.class_cote1[index_gamdom_name2[i]]) >  float(class_vulkan.class_cote1[index_vulk_gam_name2[i]]))  :
					cote1_max = float(class_gamdom.class_cote1[index_gamdom_name2[i]])
				else :
					cote1_max = float(class_vulkan.class_cote1[index_vulk_gam_name2[i]])
				if (float(class_gamdom.class_cote2[index_gamdom_name2[i]]) >  float(class_vulkan.class_cote2[index_vulk_gam_name2[i]]))  :
					cote2_max = float(class_gamdom.class_cote2[index_gamdom_name2[i]])
				else :
					cote2_max = float(class_vulkan.class_cote2[index_gamdom_name2[i]])
				if (float(class_gamdom.class_draw[index_gamdom_name2[i]]) >  float(class_vulkan.class_draw[index_vulk_gam_name2[i]]))  :
					draw_max = float(class_gamdom.class_draw[index_gamdom_name2[i]])
				else :
					draw_max = float(class_vulkan.class_draw[index_vulk_gam_name2[i]])
				if (1/ cote1_max + 1/ cote2_max + 1/ draw_max < 1) :
					print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
					, class_gamdom.class_cote1[index_gamdom_name2[i]], "	" , class_gamdom.class_draw[index_gamdom_name2[i]] ,"	" ,class_gamdom.class_cote2[index_gamdom_name2[i]],  " \n")
					print(class_vulkan.class_name1[index_vulk_gam_name2[i]], " " , class_vulkan.class_name2[index_vulk_gam_name2[i]], "\n"
					, class_vulkan.class_cote1[index_vulk_gam_name2[i]], "	", class_vulkan.class_draw[index_vulk_gam_name2[i]]  ,"	" , class_vulkan.class_cote2[index_vulk_gam_name2[i]], " \n")
					print(1/ cote1_max + 1/ cote2_max + 1/ draw_max)
			
			i = i + 1

		## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
	sleep(10)

sleep(1)
driver.quit()