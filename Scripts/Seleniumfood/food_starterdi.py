from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time


csv_file = open('reviewsi.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# available.versions<-binman::list_versions("chromedriver") latest.version = available.versions$win32[length(available.versions)]
# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome()
# Go to the page that we want to scrape
# https://www.foodnetwork.com/recipes/food-network-kitchen/a
driver.get("https://www.foodnetwork.com/recipes/food-network-kitchen/i")
# button = driver.find_element_by_xpath('//div[@class="o-AssetNavigation__m-Body prev-next-wrapper"]/div/a[2]')
# button.click()
foods = driver.find_elements_by_xpath('//div[@class="l-Columns l-Columns--2up"]/ul/li/a')

# trial = foods[0]
# trial.click()
# time.sleep(8)
# driver.get("https://www.foodnetwork.com/recipes/food-network-kitchen/a-birthday-cake-recipe-2047270")
index= 0
abc = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','xyz']
while True:
    try:
    # for food in foods[:10]:

        
        driver.get("https://www.foodnetwork.com/recipes/food-network-kitchen/i")
        foods = driver.find_elements_by_xpath('//div[@class="l-Columns l-Columns--2up"]/ul/li/a')
        food = foods[index]
        index = index+1
        time.sleep(5)
        print(food)
        food.click()
        time.sleep(5)

        try:
            wait_rc = WebDriverWait(driver, 10)
            wait_rc.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="o-ReviewSummary"]')))
            revcount = driver.find_elements_by_xpath('//div[@class="o-ReviewSummary"]')
            # tit  = driver.find_elements_by_xpath('//section[@]class="o-AssetTitle"]')
            # titl = driver.find_elements_by_xpath('.//span/[@class="o-AssetTitle__a-HeadlineText]')


        except:
            continue
        # for rev in revcount:
        #   r=rev.find_element_by_xpath('.//div/a/span[2]').text
        #   revcounti = re.findall('\d+',r)[0]
        #   print(revcounti,type(revcounti))
        # if (int(revcounti) == 0 or (not r)): dontwait = True
        # print(dontwait)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
        # name    = driver.find_elements_by_xpath ('//span[@class="o-AssetTitle__a-HeadlineText"]')[0].text
        # print(name)
        try:
            reviews = driver.find_elements_by_xpath ('//div[@class="gig-comment"]')
            # titl= driver.find_element_by_class_name("o-AssetTitle__a-HeadlineText").text
            titl = driver.find_elements_by_xpath('//*[@id="mod-recipe-summary-1"]/div[5]/section/h1/span')[0].text
          
            #class="o-AssetTitle__a-Headline" //*[@id="mod-recipe-summary-1"]/div[5]/section/h1/span
            # rating1  = driver.find_elements_by_xpath('//a[@class="m-Rating__a-StarsLink"]/span').get_attribute("title")
            rating2 = driver.find_elements_by_xpath('//span[@class="o-Capsule__m-Rating m-Rating"]/a/span[@class="gig-rating-stars "]')[0].get_attribute('title')
            
            # rating2 = driver.find_elements_by_xpath('//span[@class="o-Capsule__m-Rating m-Rating"]/a/span[@class="gig-rating-stars "]').get_attribute("title")
            print('\n*****************n\n',rating2)
            print(titl)
            print('======================',titl)
            # print(name, rating2)
        except:
            pass


        # print(rating1)
        # if dontwait != True:
            # wait_review = WebDriverWait(driver, 10)
            # reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="gig-comment"]')))
            # print(reviews)
        for review in reviews:
                review_dict = {}
                try:
                    text = review.find_element_by_xpath('.//div[@class="gig-comment-body"]').text


                    # rating= review.find_element_by_xpath('.//div[@class="gig-comment-rating-star gig-comment-rating-star-full"]')
                    # rating = review.find_element_by_xpath('//a[@class="m-Rating__a-StarsLink"]/span').get_attribute('title')
                except:
                    continue

                print('Text  = {}'.format(text))
                print('Name  = {}'.format(titl))

                review_dict['title'] = titl
                review_dict['text']  = text
                # review_dict['username'] = username
                # review_dict['date_published'] = date_published
                review_dict['rating'] = rating2

                writer.writerow(review_dict.values())
    except Exception as e:
            print(e)
            csv_file.close()
            driver.close()
            break
        # driver.execute_script("arguments[0].scrollIntoView();", reviews[0])
        # print(reviews[0])

        # button = driver.find_element_by_xpath('//div[@class="o-AssetNavigation__m-Body prev-next-wrapper"]/div/a[2]')
        # button.click()
        # time.sleep(2)
        # driver.get("https://www.foodnetwork.com/recipes/food-network-kitchen/b")
        # foods = driver.find_elements_by_xpath('//div[@class="l-Columns l-Columns--2up"]/ul/li/a')
        # food.click()


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# reviews = driver.find_elements_by_xpath('//div[@class="gig-comment"]')
# print(reviews)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# Click review button to go to the review section
# review_button = driver.find_element_by_xpath('//span[@class="padLeft6 cursorPointer"]')
# review_button = driver.find_element_by_xpath('//li[@class="o-IndexPagination__a-Button "]')
# review_button.click()

# food_button = driver.find_element_by_xpath('//li[@class="m-PromoList__a-ListItem"]')

# reviews = driver.find_elements_by_xpath('//div[@class="gig-comment-content"]')



# Page index used to keep track of where we are.
index = 1
# We want to start the first two pages.
# If everything works, we will change it to while True
# while index <=3:
#   try:
#       print("Scraping Page number " + str(index))
#       index = index + 1
#       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#               # Find all the reviews on the page
#       # wait_review = WebDriverWait(driver, 10)
#       # time.sleep(2)
#       # Find all the reviews. The find_elements function will return a list of selenium select elements.
#       # Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
#       reviews = driver.find_elements_by_xpath('//div[@class="gig-comment"]')
#       print(reviews)
#       # Iterate through the list and find the details of each review.
#       for review in reviews:
#           # Initialize an empty dictionary for each review
#           review_dict = {}
#           # Use try and except to skip the review elements that are empty. 
#           # Use relative xpath to locate the title.
#           # Once you locate the element, you can use 'element.text' to return its string.
#           # To get the attribute instead of the text of each element, use 'element.get_attribute()'
#           try:
#               title = review.find_element_by_xpath('.//div[@class="gig-comment-body"]').text
#           except:
#               continue

#           print('Title = {}'.format(title))

#           # OPTIONAL: How can we deal with the "read more" button?
            
#           # Use relative xpath to locate text, username, date_published, rating.
#           # Your code here

#           # Uncomment the following lines once you verified the xpath of different fields
            
#           # review_dict['title'] = title
#           # review_dict['text'] = text
#           # review_dict['username'] = username
#           # review_dict['date_published'] = date_published
#           # review_dict['rating'] = rating

#       # We need to scroll to the bottom of the page because the button is not in the current view yet.
#       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#       # Locate the next button element on the page and then call `button.click()` to click it.
#       button = driver.find_element_by_xpath('//div[@class="o-AssetNavigation__m-Body prev-next-wrapper"]/div/a[2]')
#       button.click()
#       time.sleep(2)

#   except Exception as e:
#       print(e)
#       driver.close()
#       break