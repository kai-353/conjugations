from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def conjugation_error(werkwoord):
    print(f"Sorry, er zijn geen (Spaanse) vervoegingen gevonden van '{werkwoord}'")


class Vervoeger:

    def __init__(self, path):
        self.PATH = path

    def get_conjugation(self, werkwoord, optie):
        driver = webdriver.Chrome(self.PATH)
        try:
            driver.get(f"https://www.vertalen.nu/vervoeging?vervoeg={werkwoord}&taal=es")
            header = driver.find_element_by_xpath(f"//*[contains(text(), '{optie}')]")
            parent = header.find_element_by_xpath("./..")
            # conjugation_list = parent.find_element_by_tag_name("ul")
            print(parent.text)
            driver.close()
        except NoSuchElementException:
            driver.close()
            conjugation_error(werkwoord)

    def get_conjugations(self, werkwoord):
        driver = webdriver.Chrome(self.PATH)
        try:
            driver.get(f"https://www.vertalen.nu/vervoeging?vervoeg={werkwoord}&taal=es")
            ul = driver.find_element_by_class_name("conjugation-container")
            print(ul.text)
            driver.close()
        except NoSuchElementException:
            driver.close()
            conjugation_error(werkwoord)
