import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

websites=["https://nrega.nic.in/netnrega/home.aspx","https://www.usa.gov/","https://www.bits-pilani.ac.in/","https://www.isro.gov.in/","https://medium.com/"]

for website in websites:
   print("\n"+website+"\n")
   driver = webdriver.Chrome()
   driver.maximize_window() 
   driver.get(website) 
   elements=driver.find_elements_by_tag_name("a")
   links=[]
   for element in elements:
      # print(element.get_attribute("href"))
      links.append(element.get_attribute("href"))
      #links=[link.get_attribute("href") for link in list]
   for link in links:
   #print(link)
      time=0
      for x in range(5):
   # try:
         driver.get(link)
         load = driver.execute_script("return window.performance.timing.domComplete")
         loadnav = driver.execute_script("return window.performance.timing.navigationStart")
         loadres = driver.execute_script("return window.performance.timing.responseStart")
         time_backend=loadres-loadnav
         time_frontend=load-loadres
         time+=time_backend+time_frontend
         # print(link,time_backend+time_frontend)
      print(link,time/5)
   # except:
      # print(link," YES")
self.driver.close()

# search_bar = driver.find_element_by_name("q") 
# search_bar.send_keys("bits hyderabad") 
# search_bar.send_keys(Keys.RETURN) 
#link = driver.find_element_by_link_text("BITS Campuses")
#link.click() 
#driver.execute_script("window.scrollTo(0, 850)") 
