
#Requirements
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#URL to be scraped
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#Opens up connection, and grabs html from page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parser
page_soup = soup(page_html, "html.parser")


#Grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})
                                      
#Makes a CSV file with the name of products    
filename = "products.csv"
f = open(filename, "w")

#Writes the headers into the products.csv file
headers = "brand, product_name, shipping\n"
f.write(headers)
        
#Loops through each product        
for container in containers:
    
    #Locates and grabs image title and uses it for brand name
    brand = container.div.div.a.img["title"] 
                                      
    #Locates and grabs all containers with the class "item-title" inside an <a> tag and extracts text from those for product name    
    title_container = container.findAll("a", {"class":"item-title"})    
    product_name = title_container[0].text
                                      
    #Locates and grabs all <li> tags with the class "price-ship" and extracts text for shipping data   
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    #Prints items to the console
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    
    #Writes items to the products.csv file and closes it    
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
    f.close
    
    
    
                                      
                                      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        