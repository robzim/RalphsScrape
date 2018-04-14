from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.ralphsices.com/flavors-products/")
assert "Flavors" in driver.title
#elem = driver.find_element_by_xpath("//h2 [contains(text(),'Ices')]")
#print elem.text

# elems = driver.find_elements_by_xpath("//ul//li")
# elems = driver.find_elements_by_xpath("//div [@id='content']")
elems = driver.find_elements_by_xpath("//div [@class='text']")

#print "There are " + elems.count + " elements"

#print dir(elems)


for i in elems:
    # if "Store Locator" in  i.text : continue
    # if "Any flavor" in  i.text : continue
    # if "Ice Cream Flavors" in  i.text : continue
    # if "," in  i.text : continue
    print i.text, i.location['x'], i.location['y'], i.parent, i.size, i.tag_name, format(i.id)
