# import libraries
# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import csv
#from datetime import datetime

# specify the url
quote_page = ["https://www.dior.com/en_int/fragrance/mens_fragrance/all-products", "https://www.dior.com/en_int/fragrance/womens-fragrance/all-products" ]

for pg in quote_page:
	perfumes_array = []
	# query the website and return the html to the variable ‘page’
	page = urllib2.urlopen(pg)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, "html.parser")

	products = soup.find_all("div", class_="product-legend")

	
	
	for tag in products:
		
		perfumeBrand=tag.find("span",class_="title-with-level product-title font-century-std size-s bold").text
		perfumeName=tag.find("p",class_="multiline-text product-subtitle").text
		if tag.find("span",class_="sr-only"):
			perfumeIntensity=tag.find("span",class_="sr-only").text

		print perfumeBrand+" "+ perfumeName+ " "+perfumeIntensity
	
		perfumes_array.append((perfumeBrand.strip(), perfumeName.strip(), perfumeIntensity.strip()))

	#open a csv file with append, so old data will not be erased
	with open("index.csv", mode='a') as csv_file:
	 writer = csv.writer(csv_file)
	 writer.writerow(["*********".encode('utf-8').strip(),"*********".encode('utf-8').strip(),"*********".encode('utf-8').strip() ])
	 writer.writerow(["BRAND".encode('utf-8').strip(),"NAME".encode('utf-8').strip(),"INTENSITY".encode('utf-8').strip() ])
	 # The for loop
	 for perfumeBrand, perfumeName, perfumeIntensity  in perfumes_array:
	 	writer.writerow([perfumeBrand.encode('utf-8').strip(), perfumeName.encode('utf-8').strip(), perfumeIntensity.encode('utf-8').strip()])

print("Done")