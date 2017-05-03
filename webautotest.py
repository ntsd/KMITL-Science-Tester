import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

class PythonOrgSearch():

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

class kmitlScienceTest(unittest.TestCase):
    delay = 30

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors = []

    def testIndex(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, self.delay)

        driver.get("http://www.science.kmitl.ac.th")
        assert "" == driver.title
        homePic = driver.find_element_by_tag_name("img")
        assert "http://www.science.kmitl.ac.th/images/r10p.jpg" == homePic.get_property("src")
        homePic.click()


    def testMain(self):
        print("----------------Thai Web Test---------------")
        driver = self.driver
        driver.get("http://www.science.kmitl.ac.th/main.php")
        assert "คณะวิทยาศาสตร์ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง" in driver.title, "Title is "+driver.title
        links = {}
        allTagA = driver.find_elements_by_tag_name("a")
        for a in allTagA:
            link = a.get_property("href")
            links[link] = a

        deadLinks = []

        for l in links:
            print(l)
            try:
                if "pdf" not in l.lower():
                    r = requests.get(l)
                    print(r.headers['content-type'])
                    if r.status_code != 200:
                        deadLinks.append((l, links[l]))
            except Exception:
                print(Exception.__name__)

        self.assertEqual([], deadLinks)

        print("----------------Image Test---------------")

        allTagImg = driver.find_elements_by_tag_name("img")
        images = {}
        deadPics =[]

        for a in allTagImg:
            img = a.get_property("src")
            images[img] = a

        for i in images:
            print(i)
            try:
                r = requests.get(i)
                print(r.headers['content-type'])
                if r.status_code != 200:
                    deadPics.append((i, images[i]))

            except Exception:
                print(Exception.__name__)

        self.assertEqual([], deadPics)


    def testMainEng(self):
        print("----------------Eng Web Test---------------")
        driver = self.driver
        driver.get("http://www.science.kmitl.ac.th/SC-Eng/index.php")
        assert "Faculty of Science" in driver.title, "Title is "+driver.title
        links = {}
        allTagA = driver.find_elements_by_tag_name("a")
        for a in allTagA:
            link = a.get_property("href")
            links[link] = a

        deadLinks = []

        for l in links:
            print(l)
            try:
                if "pdf" not in l.lower():
                    r = requests.get(l)
                    print(r.headers['content-type'])
                    if r.status_code != 200:
                        deadLinks.append((l, links[l]))
            except Exception:
                print(Exception.__name__)

        self.assertEqual([], deadLinks)

        print("----------------Image Test---------------")

        allTagImg = driver.find_elements_by_tag_name("img")
        images = {}
        deadPics =[]

        for a in allTagImg:
            img = a.get_property("src")
            images[img] = a

        for i in images:
            print(i)
            try:
                r = requests.get(i)
                print(r.headers['content-type'])
                if r.status_code != 200:
                    deadPics.append((i, images[i]))

            except Exception:
                print(Exception.__name__)

        self.assertEqual([], deadPics)

    def tearDown(self):
        self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()
