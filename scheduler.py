import schedule
import time
import requests

SERVER_URL = "https://shivam-blog-superagent-7.onrender.com"


def wake_server():
    try:
        requests.get(SERVER_URL)
        print("Server wake check")
    except:
        print("Server wake failed")


def generate_blog():
    print("Generating scheduled blog")


schedule.every().day.at("07:50").do(wake_server)
schedule.every().day.at("08:00").do(generate_blog)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(30)