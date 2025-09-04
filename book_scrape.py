from bs4 import BeautifulSoup as scraper
from urllib.request import urlopen, Request
import csv
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin



'''
Things to extract:
Title
Price(without the currency sign)
Availability
Star rating
Category it belongs to
'''


#Website to be scraped
try:
    url= 'https://books.toscrape.com/'
    html=urlopen(url)
except HTTPError as e:
    print('Connection Error')
except URLError as e:
    print(f'Error opening the link, Error: {e}') 


bs= scraper(html.read(), 'lxml')

#we want to scrape the data using the category so we can get the name and links to other categories
try:
    categories = bs.find("div", class_="side_categories").find_all("a")[1:]
except AttributeError as e:
    print('Tag Wasnt found')

x=0
#Csv File so we can save all the data weve scrapped
try:
    with open('books_data.csv', 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['Title', 'Price', 'Available?', 'Rating', 'Category']) 

        #Looping through all the categories name & link
        for cat in  categories:
            #getting the name of each category
            category_name=cat.get_text(strip=True)
            
            #the link when we go to a category is the combination of our url and the href tag in the category we scraped
            category_link=url + cat['href']
            
            # PAGINATION LOOP STARTS HERE
            while category_link:
                try:
                    html= urlopen(category_link)#openig the link
                except URLError as e:
                    print(f'Error opening category link {e}')
                    break

                bs= scraper(html.read(), 'lxml')
                
                #getting all the books in each link we scrape data from
                try:
                    books=bs.find_all('article', class_='product_pod')
                except AttributeError:
                    print('Error Finding tag')
                    break

                #getting all the information of our books and is displayed on our terminal so we know our program is running smoothly
                for info in books:
                    book_title=info.h3.a.get('title')
                    book_prices= info.find('p', class_='price_color')
                    prices=book_prices.text[1:]
                    in_stock= info.find('i', class_='icon-ok')
                    
                    print(f'Title: {book_title}')
                    print(f'Price: {prices}')
                    print(f'Category: {category_name}')
                    
                    #checking if the book is availale
                    if in_stock and book_title:
                        available='True'
                        print(f'In Stock?: True')
                    else:
                        available=False
                        print('In stock?: False')
                    
                    #checking for the ratings
                    if 'One' in info.p['class']:
                        rating= 'Ratings: 1 star'
                        print(f'Ratings: 1 stars\n')
                        
                    if 'Two' in info.p['class']:
                        rating= 'Ratings: 2 stars'
                        print(f'Ratings: 2 stars\n')
                        
                    if 'Three' in info.p['class']:
                        rating= 'Ratings: 3 stars'
                        print(f'Ratings: 3 stars\n')
                        
                    if 'Four' in info.p['class']:
                        rating= 'Ratings: 4 stars'
                        print(f'Ratings: 4 stars\n')
                        
                    if 'Five' in info.p['class']:
                        rating= 'Ratings: 5 stars'
                        print(f'Ratings: 5 stars\n')
                    x+=1
                    #writing each of the data in our csv file
                    writer.writerow([book_title, prices, available, rating, category_name])
                    

                # FIND NEXT PAGE (pagination)
                next_page = bs.find("li", class_="next")
                if next_page:
                    # build full link for next page
                    next_link = next_page.a["href"]
                    # handle relative paths like "page-2.html"
                    category_link = urljoin(category_link, next_link)

                    
                else:
                    category_link = None  # stop the loop if no next page
                
except Exception as e:
    print(f'Error opening the file {e}')
print('File saved to working directory')
print(f'A total of {x} boks was found')
