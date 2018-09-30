import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options

inputfile = sys.argv[1] # presumbaly you have a list of input data you want to enter into the website to generate data output
outputfile = "output_"+inputfile
datafile = open(inputfile)
outfile = open(outputfile,'w+')
eachline = datafile.readline()
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

while eachline != '':
    inputdata = eachline.rstrip()
    #print postalcode
    #options = Options()
    #options.add_argument("--headless")
    #driver = webdriver.Firefox(firefox_options=options)

# go to the google home page
    driver.get("website url you want to scrap")
    driver.find_element_by_id('txtSearch').send_keys("markup key to the data you want") # output data format
    driver.find_element_by_css_selector('input[type=\"button\"]').click() # virtually "clicking" button

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'tabResults')))
    except TimeoutException:
        print >> outfile, outdata+",",
        print >> outfile, "Timed out waiting for page to load"
        #driver.quit()

#driver.quit()
    table = driver.find_element_by_id('tabResults').text
    table_lines = table.splitlines()
#print table
#print table_lines[0]
    print >> outfile, outdata+",",
    n=0
    for s in table_lines:
        # do some data prepration output things here
        
    print >>outfile, n
       
       
    eachline = datafile.readline()

driver.quit()

