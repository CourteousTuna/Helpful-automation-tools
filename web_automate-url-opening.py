from selenium import webdriver
import pyautogui

'''
Opens multiples url at once given a list of ids. Useful when the url you want top open have a generic format, here it is url/document_id.pdf

To open multiple windows at once, add more drivers and iterate through the drivers as well
'''

driver = webdriver.Chrome()
url = "your_url"

# If you want to open the 100 url, 10 at once each time
for i in range(0, min(100,len(ids)),10):
    for x in range(10):
        print(f"Opening file {i + x + 1} ... ")
        driver.get(url + ids[i+x] +'.pdf')
        driver.execute_script("window.open()")  # opening blank tab
        driver.switch_to.window(driver.window_handles[-1]) # switching to last window
    
    print("Waiting ... ")
    pyautogui.alert('Continue ?') # alert box to stop the progam until you click the button

    # Close all tabs except the last one
    curr = driver.current_window_handle 
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if handle != curr:
            driver.close()
