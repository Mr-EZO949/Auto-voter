from selenium import webdriver
import time

class VoteBot():
  def __init__(self):
    self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")

  def vote(self):
    self.driver.get('https://vote.kaztrk.kz/30bilim/')
    # time.sleep(0.5)
    self.driver.find_elements_by_tag_name("button")[4].click()
    print(len(self.driver.find_elements_by_tag_name("button")))
    self.driver.close()
    # w-full flex flex-col justify-center relative
    # w-full flex flex-col justify-center relative  

while True:
  bot = VoteBot()
  bot.vote()