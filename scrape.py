import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.amazon.in/Solimo-Plastic-Container-White-SOPLA186/product-reviews/B07P94VK1Q/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

reviewlist=[]
def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_reviews(soup): 
    reviews = soup.find_all('div',{'data-hook':'review'})
    try:
        for item in reviews:
            review = {
            'product':soup.title.text.replace('Amazon.in:Customer reviews:','').strip(),
            'title ':item.find('a',{'data-hook':'review-title'}).text.strip(),
            'rating':float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
            'body': item.find('span',{'data-hook':'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass
for x in range(1,10):
    soup = get_soup(f'https://www.amazon.in/Solimo-Plastic-Container-White-SOPLA186/product-reviews/B07P94VK1Q/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews={x}')
    print(f'Getting page:{x}')
    get_reviews(soup) 
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_csv('reviews.csv')
print('End')