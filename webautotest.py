import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests


class kmitlScienceTest(unittest.TestCase):
    delay = 3000

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

    def testSearch(self):
        print("----------------Search Test---------------")
        driver = self.driver
        driver.get("http://sci-en.kmitl.ac.th/index.php/component/search")
        searchEditText = driver.find_element(by=By.ID, value="search-searchword")
        text = "test"
        searchEditText.send_keys(text)
        searchButtom = driver.find_element_by_tag_name("button")
        searchButtom.click()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'search-results'))
            WebDriverWait(driver, self.delay).until(element_present)
            print("Page is ready!")
        except:
            print("Loading took too much time!")

        results = driver.find_element_by_class_name("search-results")
        for r in range(len(results.find_elements_by_class_name("result-title"))):
            print(results.find_elements_by_class_name("result-title")[r].text)
            print(results.find_elements_by_class_name("result-text")[r].text)
            assert text in results.find_elements_by_class_name("result-title")[r].text or \
                    text in results.find_elements_by_class_name("result-text")[r].text, "Search text doesn't in result"



    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()
