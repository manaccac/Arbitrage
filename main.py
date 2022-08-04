from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


print("HELLO\n")

option = webdriver.ChromeOptions()
option.add_argument("enable-automation")
option.add_argument("disable-infobars")
driver = webdriver.Chrome("/Users/manaccac/.brew/bin/chromedriver", options=option)


gamdom_cs = 'https://gamdom.io/esports'
driver.get(gamdom_cs)

sleep(3)
#  ON PEUT VOIR QUE C L'AVENT DERNIERE DIV QUI NOUS permet de changer de match en match
#											     |||||
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1] 
# DANS LA div il y a le nom de l'equipe 1
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]/div[1]/div[1]/div

# et la de l'equipe 2
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]/div[1]/div[3]/div

# cote win equipe 1
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[1]/span[2]

#  cote win equipe 2
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[2]/span[2]

# si il y a cote draw
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[3]/span[2]

driver.get('https://hub88b-ytuoyswg.betsy.gg/csgo')

sleep(2)


# name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div[1]/div[2]/a[1]/div[1]/div[1]/div').text
# #									   //*[@id="app"]/div/div[3]/div/div[3]/div[2]/div[1]/div[2]/a[1]/div[1]/div[1]/div
# name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div[1]/div[2]/a[1]/div[1]/div[3]/div').text

# cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/button[1]/span[2]').text
# cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/button[2]/span[2]').text
# # draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[3]/span[2]').text


# print("------------------------------------DEBUT------------------------------------\n\n")
# print(name1)
# print(name2)

# print(cote1)
# print(cote2)

# print("\n\n-------------------------------------FIN-------------------------------------")


# while

count = len(driver.find_elements(By.CLASS_NAME, "grid-line"))
print("ALL = ", count);
count_Live = len(driver.find_elements(By.CSS_SELECTOR, "div.grid-event._live"))
print("Live = ", count_Live);
if count_Live == 0 :
	count_Live = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div[3]/div/div[4]/div[2]/div"))
	print("Aujourd'hui = ", count_Live);
	count_Today = 0
else :
	count_Today = len(driver.find_elements(By.XPATH, "//*[@id='app']/div/div[4]/div/div[4]/div[2]/div"))
	print("Aujourd'hui = ", count_Today);


# name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]/div[1]/div[1]/div').text
# name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]/div[1]/div[3]/div').text

# cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[1]/span[2]').text
# cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[2]/span[2]').text
# draw = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/button[3]/span[2]').text


print("------------------------------------Today------------------------------------\n\n")
i = 1;

while(i != count_Live + 1) : 
	name1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[1]/div').text
	name2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/a[1]/div[1]/div[3]/div').text

	cote1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[1]/span[2]').text
	cote2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div['+ str(i) +']/div[2]/div/div[1]/button[2]/span[2]').text
	print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\n")
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
	print(name1, " = " , cote1, "\n", name2 , " = " , cote2, "\n")
	i = i + 1

print("\n\n------------------------------------FIN------------------------------------")

# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div[2]/a[1]
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div[2]/div[4]/div[2]/a[1]

# driver.quit()
# 
# 
# # element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/a')
# element.click();