from heapq import nlargest
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


gamdom_cs = 'https://gamdom.io/esports'
empire = 'https://csgoempire.com/match-betting'
vulkan = 'https://vulkan.bet/en/esports/counter-strike?dateTo=2022-08-18T08%3A50%3A55.419Z&time=24'
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

print("####################################### GAMDOM #######################################")
driver.get(gamdom_cs)

sleep(5)
# 											 dota2 / csgo / lol
driver.get('https://hub88b-ytuoyswg.betsy.gg/csgo')

sleep(10)

# driver.find_element(By.XPATH, "//*[@id='app']/div/div[4]/div/div[2]/div/a[3]").click()

# sleep(2)
# driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div[1]").click()

# sleep(1.2)
# driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div[2]/div[1]").click()

# sleep(5)
count = len(driver.find_elements(By.CLASS_NAME, "grid-line"))
print("ALL = ", count);
count_Live = len(driver.find_elements(By.CSS_SELECTOR, "div.grid-event._live"))
print("Live = ", count_Live);

truc_de_merde = 4


if count_Live == 0 :

	count_Live = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[3]/div[2]/div"))
	print("Aujourd'hui = ", count_Live);
	count_Today = 0
else :
	count_Today = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[4]/div[2]/div"))
	print("Aujourd'hui = ", count_Today);


# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[3]/span[2]').text


print("------------------------------------Today------------------------------------\n\n")
i = 1;

class_gamdom = Gamdom_cs_paris()
class_gamdom.class_name1 = []
class_gamdom.class_name2 = []
class_gamdom.class_cote1 = []
class_gamdom.class_cote2 = []
class_gamdom.class_draw = []
# grid-event__competitor-name

while(i != count_Live + 1) : 
	# try:
	# 	myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "//*[@id='app']/div/div[3]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]")))
	# 	print("Page is ready!")
	# except TimeoutException:
	# 	print("Loading took too much time!")
		
													                 #   ///         ///       ca depend
	nb_paris = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[3]/div[2]/div["+ str(i) +"]/div[2]/div/div[1]/button"))
	print(nb_paris)
	# //*[@id="app"]/div/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[1]

	scroll = driver.find_element(By.XPATH,"//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[3]/div[2]/div["+ str(i) +"]/div[2]/a[1]/div[1]/div[1]/div")
	driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
	sleep(0.005)

	name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[1]/div').text
	name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[3]/div').text

	cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[1]/span[2]').text
	cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[2]/span[2]').text
	draw = "0"
	if (nb_paris == 3) :
		draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div['+str(truc_de_merde)+']/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text

	class_gamdom.class_name1.append(name1)
	class_gamdom.class_name2.append(name2)
	class_gamdom.class_cote1.append(cote1)
	class_gamdom.class_cote2.append(cote2)
	class_gamdom.class_draw.append(draw)


	# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text
	#  "\nDRAW = ", draw
	print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")
	i = i + 1

print("\n\n------------------------------------FIN------------------------------------\n\n")

print("------------------------------------Tomorrow------------------------------------\n\n")
i = 1;

# try:
# 	myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "//*[@id='app']/div/div[3]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]")))
# 	print("Page is ready!")
# except TimeoutException:
# 	print("Loading took too much time!")
while(i != count_Today + 1) : 
	nb_paris = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div["+str(truc_de_merde)+"]/div/div[4]/div[2]/div["+ str(i) +"]/div[2]/div/div[1]/button"))
	print(nb_paris)
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

	class_gamdom.class_name1.append(name1)
	class_gamdom.class_name2.append(name2)
	class_gamdom.class_cote1.append(cote1)
	class_gamdom.class_cote2.append(cote2)
	class_gamdom.class_draw.append(draw)

	# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text
	#  "\nDRAW = ", draw
	print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")
	i = i + 1

print("####################################### FIN GAMDOM #######################################")

sleep(2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

print("####################################### EMPIRE #######################################")
driver.get(empire)

sleep(4)
# 																									/// 2 pour cs 3 pour dota 4 lol ...
driver.find_element(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div").click()

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

# //*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div
while i != count + 1:
	j = 2
	count_Today = len(driver.find_elements(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[3]/div/div/div["+ str(i) +"]/div/div"))
	while j != count_Today + 1 :
		# 											   //*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div/div[2]/div/div[4]
		nb_paris = len(driver.find_elements(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[3]/div/div/div["+ str(i) +"]/div/div["+ str(j) +"]/div/div[4]/button"))
		print(nb_paris)



		name1 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[1]/p[1]').text
		name2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[2]/p[1]').text

		cote1 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[1]/span/div/span').text
		cote2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[2]/span/div/span').text

		draw = "0"
		if (nb_paris == 3) :
			draw = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[3]/span/div/span').text

		print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\ndraw = ", draw ,"\n")

		class_empire.class_name1.append(name1)
		class_empire.class_name2.append(name2)
		class_empire.class_cote1.append(cote1)
		class_empire.class_cote2.append(cote2)
		class_empire.class_draw.append(cote2)
		j = j + 1

	i = i + 1

print("####################################### FIN EMPIRE #######################################")

#######################################


print("####################################### VULKAN #######################################")

driver.get(vulkan)


sleep(3)
i = 0
while (i != 10) :
	sleep(0.5)
	driver.execute_script("window.scrollBy(0,275);")
	i = i + 1
sleep(1)
count = len(driver.find_elements(By.CLASS_NAME, "multimarketMatchRow__container___9A12O"))

class_vulkan = vulkan_paris()
class_vulkan.class_name1 = []
class_vulkan.class_name2 = []
class_vulkan.class_cote1 = []
class_vulkan.class_cote2 = []
class_vulkan.class_draw = []

i = 1
all_name = driver.find_elements(By.CLASS_NAME, "__match-list-Competitor-name")
j = 0
for value in all_name:
	if (j % 2) == 0:
		name1 = value.text
		class_vulkan.class_name1.append(name1)
	if (j % 2) != 0:
		name2 = value.text
		class_vulkan.class_name2.append(name2)

	j = j + 1

all_cote = driver.find_elements(By.CLASS_NAME, "__app-MarketDefault-odd-container")
j = 0
for value in all_cote:
	if (j % 2) == 0:
		cote1 = value.text
		class_vulkan.class_cote1.append(cote1)
	if (j % 2) != 0:
		cote2 = value.text
		class_vulkan.class_cote2.append(cote2)

	j = j + 1
i = 0
while i != count - 1 :
	print(class_vulkan.class_name1[i], " = " , class_vulkan.class_cote1[i], "\n", class_vulkan.class_name2[i] , " = " , class_vulkan.class_cote2[i])
	i = i + 1
print("####################################### FIN VULKAN #######################################")
sleep(1)
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
	print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
		, class_empire.class_cote1[index_empire_name1[i]], "			" , class_empire.class_cote2[index_empire_name1[i]], " \n")
	print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
		, class_gamdom.class_cote1[index_gamdom_name1[i]], "	" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")

	print(1 / float(class_empire.class_cote1[index_empire_name1[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name1[i]]))
	print(1 / float(class_empire.class_cote2[index_empire_name1[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name1[i]]))
	i = i + 1

i = 0
while i != len(index_empire_name2) :
	print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
		, class_empire.class_cote1[index_empire_name2[i]], "			" , class_empire.class_cote2[index_empire_name2[i]], " \n")
	print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
		, class_gamdom.class_cote1[index_gamdom_name2[i]], "			" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
	print(1 / float(class_empire.class_cote1[index_empire_name2[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name2[i]]))
	print(1 / float(class_empire.class_cote2[index_empire_name2[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name2[i]]))
	i = i + 1


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
print("vulkan")
while i != len(index_vulk_emp_name1) :
	print(class_empire.class_name1[index_empire_name1[i]], " " , class_empire.class_name2[index_empire_name1[i]], "\n"
		, class_empire.class_cote1[index_empire_name1[i]], "			" , class_empire.class_cote2[index_empire_name1[i]], " \n")
	print(class_vulkan.class_name1[index_vulk_emp_name1[i]], " " , class_vulkan.class_name2[index_vulk_emp_name1[i]], "\n"
		, class_vulkan.class_cote1[index_vulk_emp_name1[i]], "	" , class_vulkan.class_cote2[index_vulk_emp_name1[i]], " \n")

	print(1 / float(class_empire.class_cote1[index_empire_name1[i]]) +  1 / float(class_vulkan.class_cote2[index_vulk_emp_name1[i]]))
	print(1 / float(class_empire.class_cote2[index_empire_name1[i]]) +  1 / float(class_vulkan.class_cote1[index_vulk_emp_name1[i]]))
	i = i + 1

i = 0
while i != len(index_vulk_emp_name2) :
	print(class_empire.class_name1[index_empire_name2[i]], " " , class_empire.class_name2[index_empire_name2[i]], "\n"
		, class_empire.class_cote1[index_empire_name2[i]], "			" , class_empire.class_cote2[index_empire_name2[i]], " \n")
	print(class_vulkan.class_name1[index_vulk_emp_name2[i]], " " , class_vulkan.class_name2[index_vulk_emp_name2[i]], "\n"
		, class_vulkan.class_cote1[index_vulk_emp_name2[i]], "	" , class_vulkan.class_cote2[index_vulk_emp_name2[i]], " \n")

	print(1 / float(class_empire.class_cote1[index_empire_name2[i]]) +  1 / float(class_vulkan.class_cote2[index_vulk_emp_name2[i]]))
	print(1 / float(class_empire.class_cote2[index_empire_name2[i]]) +  1 / float(class_vulkan.class_cote1[index_vulk_emp_name2[i]]))
	i = i + 1

i = 0
print("\n\n\nvulkan")
print("gamdom")
while i != len(index_vulk_gam_name1) :
	print(class_vulkan.class_name1[index_vulk_gam_name1[i]], " " , class_vulkan.class_name2[index_vulk_gam_name1[i]], "\n"
		, class_vulkan.class_cote1[index_vulk_gam_name1[i]], "			" , class_vulkan.class_cote2[index_vulk_gam_name1[i]], " \n")
	print(class_gamdom.class_name1[index_gamdom_name1[i]], " " , class_gamdom.class_name2[index_gamdom_name1[i]], "\n"
		, class_gamdom.class_cote1[index_gamdom_name1[i]], "			" , class_gamdom.class_cote2[index_gamdom_name1[i]], " \n")
	print(1 / float(class_vulkan.class_cote1[index_vulk_gam_name1[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name1[i]]))
	print(1 / float(class_vulkan.class_cote2[index_vulk_gam_name1[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name1[i]]))
	i = i + 1

i = 0
while i != len(index_vulk_gam_name2) :
	print(class_vulkan.class_name1[index_vulk_gam_name2[i]], " " , class_vulkan.class_name2[index_vulk_gam_name2[i]], "\n"
		, class_vulkan.class_cote1[index_vulk_gam_name2[i]], "			" , class_vulkan.class_cote2[index_vulk_gam_name2[i]], " \n")
	print(class_gamdom.class_name1[index_gamdom_name2[i]], " " , class_gamdom.class_name2[index_gamdom_name2[i]], "\n"
		, class_gamdom.class_cote1[index_gamdom_name2[i]], "			" , class_gamdom.class_cote2[index_gamdom_name2[i]], " \n")
	print(1 / float(class_vulkan.class_cote1[index_vulk_gam_name2[i]]) +  1 / float(class_gamdom.class_cote2[index_gamdom_name2[i]]))
	print(1 / float(class_vulkan.class_cote2[index_vulk_gam_name2[i]]) +  1 / float(class_gamdom.class_cote1[index_gamdom_name2[i]]))
	i = i + 1

## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  

sleep(1)
driver.quit()