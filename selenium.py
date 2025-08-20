#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open target site
driver.get("https://demo.testfire.net/")
print("Opened:", driver.title)
time.sleep(2)

# Step 1 - Click "Sign In"
driver.find_element(By.LINK_TEXT, "Sign In").click()
print("Clicked Sign In")
time.sleep(2)

# Step 2 - Enter login credentials
driver.find_element(By.NAME, "uid").send_keys("admin")   # demo username
driver.find_element(By.NAME, "passw").send_keys("admin") # demo password
driver.find_element(By.NAME, "btnSubmit").click()
print("Logged in as admin")
time.sleep(2)

# Step 3 - Navigate to "View Account Summary"
driver.find_element(By.LINK_TEXT, "View Account Summary").click()
print("Opened Account Summary")
time.sleep(2)

# Step 4 - Click on "Transfer Funds"
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
print("Opened Transfer Funds")
time.sleep(2)

# Step 5 - Click on "View Recent Transactions"
driver.find_element(By.LINK_TEXT, "SMALL BUSINESS").click()
print("SMALL BUSINESSs")
time.sleep(2)

# Step 6 - Click on "Online Banking"
driver.find_element(By.LINK_TEXT, "Retirement").click()
print("Opened Retirement")
time.sleep(2)

# Step 7 - Click on "Online Banking"
driver.find_element(By.LINK_TEXT, "MY ACCOUNT").click()
print("Opened MY ACCOUNT")
time.sleep(2)

# Step 8 - Log out
driver.find_element(By.LINK_TEXT, "Sign Off").click()
print("Logged out")

# Close browser
driver.quit()


# In[9]:


get_ipython().system('git init')


# In[4]:


git add selenium.ipynb   # Or .ipynb or any filename
git commit -m "Initial commit of selenium script"


# In[5]:


git remote add origin https://github.com/xshannu4-stack/selenium-demo.git


# In[6]:


git branch -M main
git push -u origin main


# In[7]:


git add selenium.ipynb 
git commit -m "Describe what changed"
git push


# In[8]:


pip install git


# In[ ]:




