from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    """Base page class that is initialized on every page object class."""
    # def __init__(self, iframe_id= None):
    #     self.iframe_id  = iframe_id

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        if self.iframe_locator:
            #iframe= driver.find_element(self.iframe_locator)
            iframe=WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.iframe_locator))
            driver.switch_to.frame(iframe)
            #DO WHAT YOU NEED TO DO
            driver.find_element_by_name(self.locator).clear()
            driver.find_element_by_name(self.locator).send_keys(value)
            driver.switch_to_default_content()

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        if self.iframe_locator:
            #iframe= driver.find_element(self.iframe_locator)
            iframe=WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.iframe_locator))
            driver.switch_to.frame(iframe)
            #DO WHAT YOU NEED TO DO
            element=WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.locator))
            driver.switch_to_default_content()
        return element.get_attribute("value")