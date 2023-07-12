# import module
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# get https://www.geeksforgeeks.org/
driver.get("https://guarani.frba.utn.edu.ar/autogestion/grado/acceso")

# Maximize the window and let code stall
# for 5s to properly maximise the window.
driver.maximize_window()
time.sleep(5)

# autocomplete user field
input = driver.find_element_by_name('usuario')
input.send_keys("salvacastro")

# autocomplete password field
input = driver.find_element_by_name('password')
input.send_keys("S@lvatore95")

# Obtain button by link text and click to login.
button = driver.find_element_by_name('login')
button.click()

# goes to the teacher survey sector
driver.get("https://guarani.frba.utn.edu.ar/autogestion/grado/encuestas_kolla")
time.sleep(10)

# Go to the first poll. in this case, matematica superior
driver.get("https://guarani.frba.utn.edu.ar/autogestion/grado/encuestas_kolla/1a61d5bc78bf0c9311f26e434dc7236f992920fc")
time.sleep(20)

# Create a function in which it waits for the page https://guarani.frba.utn.edu.ar/autogestion/grado/encuestas_kolla/1a61d5bc78bf0c9311f26e434dc7236f992920fc to finish loading. Once the above is done, look for the radio button with the value id d8829_lk_10502 and click on it. Then use this function to click on all the radio buttons of the page.