from selenium import webdriver 
import settings, datetime
from datetime import timedelta, datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.webdriver.support.ui import WebDriverWait 
from decorators import *

class Browser(object):

    #base_url = 'http://localhost:8000'
    #options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(10)
    def logout(self):
        '''
        MODIFY THIS CODE TO CUSTOMIZE LOGIN EXPERIENCE
        '''
        try:
            exit_button = self.driver.find_element_by_id('ctl00_btnSalir_lkButton').click()# path = //*[@id="ctl00_btnSalir_lkButton"]
            #browser.switch_to_default_content()
            print('loggging out of banesco')
        except:
            print('error occurred during logout')

        return self

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, pageClass):
        """
        navigate webdriver to different pages
        """
        self.driver.get(pageClass(self).url)
        self.current_page = pageClass(self)
        return self

    def switch_to_default_content(self):
        self.driver.switch_to_default_content()

    def switch_to_frame(self, frame):
        """
        navigate webdriver to different pages
        """
        #url = location
        self.driver.switch_to.frame(frame)


    def save_screenshot(self, save_path=None, filename=None):
        now = datetime.now()
        filename= filename  if filename else 'ss_%s_%s_%s.png' %(str(now.year), str(now.month), str(now.day))
        save_path= os.path.join(save_path, filename) if save_path else filename
        self.driver.save_screenshot(save_path)
        return self

    #@iframe_present
    def find(self, locator):
        # if iframe_locator:
        #     self.iframe=WebDriverWait(self.browser, settings.TIMEOUT).until(EC.presence_of_element_located(iframe_locator))
        #     self.browser.switch_to.frame(self.iframe)
            #DO WHAT YOU NEED TO DO
            #element =WebDriverWait(self.browser, settings.TIMEOUT).until(EC.presence_of_element_located(locator))
            #self.browser.switch_to_default_content()

        #element =WebDriverWait(self.browser, settings.TIMEOUT).until(EC.presence_of_element_located(locator))
        return  WebDriverWait(self.driver, settings.TIMEOUT).until(EC.presence_of_element_located(locator))




    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)


class ChromeBrowser(Browser):
    
    #driver = webdriver.Chrome(executable_path=setings.CHROME_DRIVER_EXECUTABLE_PATH, chrome_options=options)
    #takes same arguments as top class?
    chrome_options = webdriver.ChromeOptions()
    def __init__(self, *args,**kwargs):
        #self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        # for item in chrome_optionsList:
        #     try:
        #         self.options.add_argument("--%s" %(str('item')))
        #     except:
        #         print('%s is not a chrome driver option' %(str(item)))
        self.driver= webdriver.Chrome(**kwargs)



class FireFoxBrowser(Browser):
    #driver = webdriver.Firefox()
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        options = Options()
        #options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options, executable_path="C:/Utility/BrowserDrivers/geckodriver.exe")
        #print("Firefox Headless Browser Invoked")
        #driver.get('http://google.com/')


class PhantomJSBrowser(Browser):
    #driver = webdriver.PhantomJS()
    pass


class BanescoBrowser(ChromeBrowser):
    pass


'''
GENERAL
Request URL: https://www.banesconline.com/mantis/WebSite/ConsultaMovimientosCuenta/Exportar.aspx
Request Method: POST
Status Code: 200 OK
Remote Address: 200.6.27.17:443
Referrer Policy: no-referrer-when-downgrade
'''

'''
DOWNLOAD FILE REQUEST HEADERS
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,es;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 1114
Content-Type: application/x-www-form-urlencoded
Cookie: __utmz=4340768.1524422462.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=4340768; ___tk56138=0.058324477621694015; ASPSESSIONIDSGQASSRQ=DGOPGEFBIEMPMOJEGIAOIDDJ; ASPSESSIONIDSERDQSQQ=OIOBHEFBLFKCAAOIPCPPDDMB; ASP.NET_SessionId=1sezrj45f2izlw55ya5yo1zi; __utma=4340768.1801574764.1524422462.1529008444.1529019141.47; __utmt=1; __utmb=4340768.2.10.1529019141; BanescoMenu_ctl00_FastMenu=1000000000000000000000
Host: www.banesconline.com
Origin: https://www.banesconline.com
Referer: https://www.banesconline.com/mantis/WebSite/ConsultaMovimientosCuenta/Exportar.aspx
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36

'''


'''
DOWNLOAD FILE RESPONSE HEADERS
Cache-Control: private
content-disposition: attachment;filename=V006750435.txt
Content-Type: application/vnd.text
Date: Thu, 14 Jun 2018 23:44:17 GMT
Expires: Thu, 14 Jun 2018 23:43:17 GMT
Server: Microsoft-IIS/7.0
Transfer-Encoding: chunked
X-AspNet-Version: 2.0.50727
X-Powered-By: ASP.NET
'''


'''
FORM DATA
__EVENTTARGET: 
__EVENTARGUMENT: 
__VIEWSTATE: /wEPDwUJNDMzMjIzMTAyZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WFAUaY3RsMDAkY3Akb3B0UHJlZGV0ZXJtaW5hZGEFGmN0bDAwJGNwJG9wdFByZWRldGVybWluYWRhBRZjdGwwMCRjcCRvcHRQYXJhbWV0cm9zBRZjdGwwMCRjcCRvcHRQYXJhbWV0cm9zBRhjdGwwMCRjcCRvcHRFbmNhYmV6YWRvU2kFGGN0bDAwJGNwJG9wdEVuY2FiZXphZG9TaQUYY3RsMDAkY3Akb3B0RW5jYWJlemFkb05vBRhjdGwwMCRjcCRvcHRFbmNhYmV6YWRvTm8FEWN0bDAwJGNwJG9wdE1vdlNpBRFjdGwwMCRjcCRvcHRNb3ZTaQURY3RsMDAkY3Akb3B0TW92Tm8FEWN0bDAwJGNwJG9wdE1vdk5vBRdjdGwwMCRjcCRvcHREZWxpbWl0YWRvcgUXY3RsMDAkY3Akb3B0RGVsaW1pdGFkb3IFGGN0bDAwJGNwJG9wdExvbmdpdHVkRmlqYQUYY3RsMDAkY3Akb3B0TG9uZ2l0dWRGaWphBRhjdGwwMCRjcCRvcHRRdWlrZW5PTW9uZXkFGGN0bDAwJGNwJG9wdFF1aWtlbk9Nb25leQURY3RsMDAkY3Akb3B0RXhjZWwFEWN0bDAwJGNwJG9wdEV4Y2Vs3PG6URYPTHS/KG71JmmcYRjYOCs=
__VIEWSTATEGENERATOR: A5EC16FD
__EVENTVALIDATION: /wEWDQK/1ZjjCALXl925CQLhgsX4CgLM65X8BALi5PbyCQKv7I2QDgKonduuAQL2jNmUDwLNjs8TAvPiyNYBAr3t+v4KAsu8pKsMAsK8iPYKMw53uqFtne+yVShGJhB+dhDc5Xs=
TitleFormat: BanescOnline dddd, dd de MMMM de yyyy HH:mm:ss f t
ctl00$cp$Formato: optPredeterminada
ctl00$cp$btnOk: Aceptar

'''