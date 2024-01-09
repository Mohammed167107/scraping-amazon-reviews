import requests
from bs4 import BeautifulSoup
import csv

link = input("Type the link of the Amazon product you want to get reviews for: ")
page = requests.get(link)

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    all_reviews = soup.find_all("div", {'class': 'a-section review aok-relative'})
    reviews = []

    def give_reviews(all_reviews):
        for review in all_reviews:
            rev = review.find("div", {'class': 'a-expander-content reviewText review-text-content a-expander-partial-collapse-content'})
            if rev:
                rev_text = rev.find("span").text.strip()
                reviews.append({'Review': rev_text})

    with open('scrap/reviews.csv', 'w', encoding="utf-8") as output_file:
        fieldnames = ['Review']
        dict_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        dict_writer.writeheader()
        give_reviews(all_reviews)
        dict_writer.writerows(reviews)

    print("File created")

main(page)
