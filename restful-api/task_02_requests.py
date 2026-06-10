#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    j = r.json()
    for post in j:
        print(post['title'])

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code >= 200 and r.status_code < 300:
        j = r.json()
        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames, extrasaction='ignore')
            for post in j:
                writer.writerow(post)



if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
