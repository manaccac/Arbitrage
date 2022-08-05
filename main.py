from heapq import nlargest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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



print("HELLO\n")

option = webdriver.ChromeOptions()
option.add_argument("enable-automation")
option.add_argument("disable-infobars")
driver = webdriver.Chrome("/Users/manaccac/.brew/bin/chromedriver", options=option)


gamdom_cs = 'https://gamdom.io/esports'
empire = 'https://csgoempire.com/match-betting'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 


driver.get(gamdom_cs)

sleep(3)

driver.get('https://hub88b-ytuoyswg.betsy.gg/csgo')

sleep(1)

# driver.find_element(By.XPATH, "//*[@id='app']/div/div[4]/div/div[2]/div/a[3]").click()

# sleep(2)
# driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div[1]").click()

# sleep(1.2)
# driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div[2]/div[1]").click()

sleep(2)
count = len(driver.find_elements(By.CLASS_NAME, "grid-line"))
print("ALL = ", count);
count_Live = len(driver.find_elements(By.CSS_SELECTOR, "div.grid-event._live"))
print("Live = ", count_Live);
if count_Live == 0 :
	count_Live = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div[4]/div/div[3]/div[2]/div"))
	print("Aujourd'hui = ", count_Live);
	count_Today = 0
else :
	count_Today = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div[4]/div/div[4]/div[2]/div"))
	print("Aujourd'hui = ", count_Today);


# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[3]/span[2]').text


print("------------------------------------Today------------------------------------\n\n")
i = 1;

class_gamdom = Gamdom_cs_paris()
class_gamdom.class_name1 = []
class_gamdom.class_name2 = []
class_gamdom.class_cote1 = []
class_gamdom.class_cote2 = []

while(i != count_Live + 1) : 

	scroll = driver.find_element(By.XPATH,"//*[@id='app']/div/div[4]/div/div[3]/div[2]/div["+ str(i) +"]/div[2]/a[1]/div[1]/div[1]/div")
	driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
	sleep(0.005)

	name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[1]/div').text
	name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[3]/div').text

	cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[1]/span[2]').text
	cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[2]/span[2]').text

	class_gamdom.class_name1.append(name1)
	class_gamdom.class_name2.append(name2)
	class_gamdom.class_cote1.append(cote1)
	class_gamdom.class_cote2.append(cote2)


	# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text
	#  "\nDRAW = ", draw
	print(name1, " = " , cote1, "\n", name2 , " = " , cote2,"\n")
	i = i + 1

print("\n\n------------------------------------FIN------------------------------------\n\n")

print("------------------------------------Tomorrow------------------------------------\n\n")
i = 1;
while(i != count_Today + 1) : 
# 																		    |||
	name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[4]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[1]/div').text
	name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[4]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[3]/div').text

	cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[4]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[1]/span[2]').text
	cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[4]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[2]/span[2]').text

	class_gamdom.class_name1.append(name1)
	class_gamdom.class_name2.append(name2)
	class_gamdom.class_cote1.append(cote1)
	class_gamdom.class_cote2.append(cote2)

	# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[3]/span[2]').text
	#  "\nDRAW = ", draw
	print(name1, " = " , cote1, "\n", name2 , " = " , cote2,"\n")
	i = i + 1

print("\n\n------------------------------------FIN------------------------------------")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
sleep(1)
driver.get(empire)

sleep(2)
driver.find_element(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div").click()

sleep(1)
driver.find_element(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[2]/div[2]/button[5]/span").click()

sleep(3)
count = len(driver.find_elements(By.CLASS_NAME, "mb-lg"))
print("ALL = ", count);

class_empire = empire_cs_paris()
class_empire.class_name1 = []
class_empire.class_name2 = []
class_empire.class_cote1 = []
class_empire.class_cote2 = []

i = 1

# //*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div
while i != count + 1:
	j = 2
	count_Today = len(driver.find_elements(By.XPATH, "//*[@id='page-scroll']/div[1]/div[2]/div/div[1]/div[3]/div/div/div["+ str(i) +"]/div/div"))
	while j != count_Today + 1 :
		name1 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[1]/p[1]').text
		name2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[2]/p[1]').text

		cote1 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[1]/span/div/span').text
		cote2 = driver.find_element(By.XPATH, '//*[@id="page-scroll"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div['+ str(i) +']/div/div['+ str(j) +']/div/div[4]/button[2]/span/div/span').text
		print(name1, " = " , cote1, "          ", name2 , " = " , cote2,"\n")

		class_empire.class_name1.append(name1)
		class_empire.class_name2.append(name2)
		class_empire.class_cote1.append(cote1)
		class_empire.class_cote2.append(cote2)
		j = j + 1

	i = i + 1

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

# index_name1.sort()
# index_name2.sort()

# print(index_name1)
# print(index_name2)

for i in range(len(index_name2)):
	index_name1.append(index_name2[i])

 
# to remove duplicated from list 
result = [] 
[result.append(x) for x in index_name1 if x not in result] 

# printing list after removal 
result.sort()
# print ("The list after removing duplicates: " + str(result)) 

##################################################

index_name1 = []
index_name2 = []
match_name1_list = list(match_name1)
match_name2_list = list(match_name2)

for i in range(len(match_name1_list)):
	index_name1.append(class_gamdom.class_name1.index(match_name1_list[i]))

for i in range(len(match_name2_list)):
	index_name2.append(class_gamdom.class_name2.index(match_name2_list[i]))

# index_name1.sort()
# index_name2.sort()

# print(index_name1)
# print(index_name2)

for i in range(len(index_name2)):
	index_name1.append(index_name2[i])

 
# to remove duplicated from list 
result = [] 
[result.append(x) for x in index_name1 if x not in result] 

# printing list after removal 
result.sort()
print ("The list after removing duplicates: " + str(result)) 


i = 0
matches_name1 = []
matches_name2 = []
index_gamdom_name1 = []
while i != len(result) :
	if class_gamdom.class_name1[result[i]] in class_empire.class_name1:
		index_gamdom_name1.append(result[i])
		matches_name1.append(class_gamdom.class_name1[result[i]] )
	i = i + 1
i = 0
index_gamdom_name2 = []
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

index_empire_name1 = []
index_empire_name2 = []
print(matches_name2)
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



driver.quit()