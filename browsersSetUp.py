from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains




def setUpBrowser():
    try:
        Chrome_driver_path = ChromeDriverManager().install()
        print(Chrome_driver_path)
        print(
            "Try to get the path of the Chrome driver executable without downloading it again"
        )
    except:
        print(Chrome_driver_path)
        # If the driver is not already installed, download and install it
        Chrome_driver_path = ChromeDriverManager().install()
        print("If the driver is not already installed, download and install it")

    # Create a Service instance using the Firefox driver executable path
    s = Service(executable_path=Chrome_driver_path)
    print("Create a Service instance using the Chrome driver executable path")

    # Create a Firefox webdriver instance using the Service
    driver = webdriver.Chrome(service=s)
    
    
    

    driver.get("https://rpachallenge.com/")
    
    driver.maximize_window()

    waitDriver = WebDriverWait(driver, 5)
    actiondriver = ActionChains(driver)
    waitdriverForLogin = WebDriverWait(driver, 30)
    waitdriverForReport = WebDriverWait(driver, 60)

    

    return driver, waitDriver, actiondriver, waitdriverForLogin, waitdriverForReport