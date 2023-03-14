# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import os
from datetime import datetime, timezone
from pytz import timezone
from selenium.common.exceptions import TimeoutException


now=datetime.now()
x=datetime.now()
x=str(x.strftime("%Y%m%d:%H:%M:%S"))

###############################################################

try:

    opts = Options()
    opts.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
    options = webdriver.ChromeOptions() 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service('driver/chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://www.playbycourt.com/users/sign_in')
    user = "ricardomen7@gmail.com"
    password = "Ric21ric"



    input_user = WebDriverWait(driver, 5).until( 
        EC.presence_of_element_located((By.XPATH, '//input[@name="user[email]"]'))
    )
    input_pass = driver.find_element(By.XPATH, '//input[@name="user[password]"]')

    input_user.send_keys(user)
    input_pass.send_keys(password)



    login_button = driver.find_element(
        By.XPATH, '//div[@class="form-actions"]//input[@class="ui button green gradient ui button fluid"]')
    login_button.click()

    inicio = time.time()

    calendar_button = WebDriverWait(driver, 0.5).until(  
        EC.presence_of_element_located((By.XPATH, "//div/a[@class='ui button large fluid white']"))
    )   

    calendar_button.click()

    driver.refresh()

    time.sleep(0.2)  #se puede quitar

    padel_button = WebDriverWait(driver, 0.9).until(  
     EC.presence_of_element_located((By.XPATH,"//div[@class='flex_mobile_button_container']/button[text()='Padel']"))
    )   
    padel_button.click()

    time.sleep(0.4)


    ayer = WebDriverWait(driver, 0.9).until(  
        EC.presence_of_element_located((By.XPATH, "//button/div[text()='26']"))
    )   
    ayer.click()

    time.sleep(0.4)

    dia = WebDriverWait(driver, 0.9).until(  
        EC.presence_of_element_located((By.XPATH, "//button/div[text()='23']"))
    )   
    dia.click()

    time.sleep(0.4)

    hoy = WebDriverWait(driver, 0.9).until(  
        EC.presence_of_element_located((By.XPATH, "//button/div[text()='26']"))
    )   
    hoy.click()


    driver.execute_script("window.scrollTo(0, 350);")

    time.sleep(0.4)

    inicio_calendario = time.time()

    h1 = WebDriverWait(driver, 45).until(  #60
        EC.presence_of_element_located((By.XPATH, "//button[text()='7:30-9pm']"))
    )                        
    driver.execute_script("arguments[0].click();", h1) 


    time.sleep(0.5)

    


    driver.execute_script("window.scrollTo(0, 750);")
    time.sleep(0.4)

    next1 = WebDriverWait(driver, 0.5).until(  
        EC.presence_of_element_located((By.XPATH,'//div[@class="ui buttons fluid"]/button[@class="ui icon small button primary "]'))
    )   
    next1.click()

    time.sleep(0.5) #de aqui en adelante


    player1 = WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH,"//button[text()='Add Players']"))
    )   
    player1.click()

    time.sleep(0.45)

    add1 = WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH,"//button[text()='Add']"))
    )   
    add1.click()

    time.sleep(0.5)

    player2 =WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH, "//button[text()='Add Players']"))
    )   
    player2.click()

    time.sleep(0.5)

    add2 = WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH,"//button[text()='Add']"))
    )
    add2  = driver.find_elements(By.XPATH, "//button[text()='Add']")   
    add2[1].click()

    time.sleep(0.1)

    player3 = WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH, "//button[text()='Add Players']"))
    )   
                              
    player3.click()

    time.sleep(0.5)

    add3 = WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH,"//button[text()='Add']"))
    )   
    add3  = driver.find_elements(By.XPATH, "//button[text()='Add']")
    add3[2].click()


    time.sleep(0.5)  

    next2 = WebDriverWait(driver, 8).until(  
        EC.presence_of_element_located((By.XPATH,"//h2[text()='Checkout']"))
    )  
    next2.click()

    driver.execute_script("window.scrollTo(0, 990);")

    time.sleep(0.10) 

    book = WebDriverWait(driver,8).until(  
        EC.presence_of_element_located((By.XPATH,"//div//button[text()='Book']"))
    ) 
    driver.execute_script("arguments[0].click();", book)


    time.sleep(0.3)#0.3
    driver.close()

except TimeoutException:

    #Hora
    fecha_y_hora_actuales = datetime.now()
    zona_horaria = timezone('America/New_York')
    fecha_y_hora_miami = fecha_y_hora_actuales.astimezone(zona_horaria)
    hora_miami = fecha_y_hora_miami.strftime('%H:%M:%S')

    fin1 = time.time()
    fin2 = time.time()
    resumen1=fin1-inicio_calendario
    resumen2=fin2-inicio
    print("Tiempo a partir de que abren las canchas:",resumen1, "\n Tiempo desde el Login:",resumen2)
    now=str(now.strftime("%Y%m%d_%H_%M_%S"))

    #C:/consolas/padel/logs/
    #C:/Users/eduardo/OneDrive/Documentos/padel/logs/padel_am_
    file = open("C:/consolas/padel/logs/padel_pm_"+now+".txt", "w")
    file.write("-------------Inicio el flujo: "+x+"-------------")
    file.write("\n-------------")
    file.write("Tiempo a partir de que abren las canchas:"+str(resumen1))
    file.write("-------------")
    file.write("\n-------------")
    file.write("Tiempo desde el Login:"+str(resumen2))
    file.write("-------------")
    file.write("\n-------------")
    file.write("Finalizo:"+str(hora_miami))
    file.write("-------------")
    file.close()
