from selenium import webdriver
import pyautogui
import pandas as pd

#Extracting data using Pandas
df = pd.read_csv("C:\\path.csv) # For .xlsx use read_excel() instead
#Filtering dataframe
df = df[(df['Column_name']==value)]
#Slicing data frame in list
ids = df["Column_name_u_want_to_slice"][:len].values

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
