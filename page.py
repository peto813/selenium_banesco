import settings, decimal, datetime, requests, shutil, csv, os
from datetime import timedelta, datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

from element import *
from locators import *




class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, browser, base_url='http://www.app.com/', timeout = 30, locator_class = None):
        self.base_url = base_url
        self.browser = browser
        self.timeout = timeout
        self.driver = browser.driver
        #self.locator_class = locator_class


    def find(self, *locator):
        return self.driver.find_element(*locator)
 
    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()



class ValidationPage(BasePage):
    def get_answer(self, text):
        answer = None

        if text =='¿Cuál es mi postre favorito?':
            answer = 'brownie'

        elif text== 'SSN':
            answer = '444087063'

        elif text== 'ciudad nacimiento mama':
            answer = 'barcelona'

        elif text== '¿Cuál es su película favorita?':
            answer = 'braveheart'

        elif text== '¿Cuál es su pasatiempo favorito?':
            answer = 'gym'

        elif text== '¿Qué país siempre has querido conocer?':
            answer = None

        elif text== '¿Cuál es mi carro preferido?':
            answer = None

        elif text== '¿Cuál es el nombre de mi profesor preferido?':
            answer = None


        elif text== '¿Cuál fue el nombre de mi primer colegio?':
            answer = 'chiquitines'

        elif text== '¿Dónde fue su luna de miel?':
            answer = None

        elif text== '¿Cuál fue el nombre de mi primer novio(a)?':
            answer = 'erika'

        elif text== '¿Cuál es la fecha aniversario de matrimonio (DD/MM/AAAA)?':
            answer = None

        elif text== '¿Dónde conoció a su pareja?':
            answer = None

        elif text== '¿Cuál es el nombre de mi mascota?':
            answer = None
        elif text== '¿Cuál es el segundo apellido de su padre o madre?':
            answer = 'arcia'

        elif text== '¿Quién fue el héroe de su infancia?':
            answer = None

        elif text== '¿Cuál fue su primer vehículo (marca)?':
            answer = 'toyota'




        return answer

    def fill_form(self):
        self.browser.switch_to_frame(self.browser.find(ValidationPageLocators.IFRAME))#go to iframe otherwise element wont be found
        
        #GET QUESTIONS

        question1 = self.browser.find(ValidationPageLocators.QUESTION1_FIELD).text#.send_keys(settings.BANESCO_PASSWORD)#feed params from locators, use second parameter to indicate element is within iframe
        question2 = self.browser.find(ValidationPageLocators.QUESTION2_FIELD).text

        answer1 = self.get_answer(question1)
        answer2 = self.get_answer(question2)

        self.browser.find(ValidationPageLocators.ANSWER1_FIELD).send_keys(answer1)
        self.browser.find(ValidationPageLocators.ANSWER2_FIELD).send_keys(answer2)
        self.browser.switch_to_default_content()
        return self

    def click_accept_button(self):
        self.browser.switch_to_frame(self.browser.find(ValidationPageLocators.IFRAME))
        self.browser.find(ValidationPageLocators.ACCEPT_BUTTON).click()
        self.browser.switch_to_default_content()
        return self


class LoginUsuarioPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    #usernamefield = SearchTextElement()
    url = 'https://www.banesconline.com/mantis/Website/Login.aspx'
    def __init__(self, browser):
        self.browser = browser


    def fill_form(self):
        self.browser.switch_to_frame(self.browser.find(LoginUsuarioPageLocators.IFRAME))#go to iframe otherwise element wont be found
        self.browser.find(LoginUsuarioPageLocators.USERNAME_FIELD).send_keys(settings.BANESCO_USERNAME)#feed params from locators, use second parameter to indicate element is within iframe
        self.browser.switch_to_default_content()
        return self

    def click_accept_button(self):
        self.browser.switch_to_frame(self.browser.find(LoginUsuarioPageLocators.IFRAME))
        self.browser.find(LoginUsuarioPageLocators.ACCEPT_BUTTON).click()
        self.browser.switch_to_default_content()
        return self

class LoginPasswordPage(LoginUsuarioPage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    #usernamefield = SearchTextElement()
    def __init__(self, browser):
        self.browser = browser

    def fill_form(self):
        self.browser.switch_to_frame(self.browser.find(LoginUsuarioPageLocators.IFRAME))#go to iframe otherwise element wont be found
        self.browser.find(LoginUsuarioPageLocators.PASSWORD_FIELD).send_keys(settings.BANESCO_PASSWORD)#feed params from locators, use second parameter to indicate element is within iframe
        self.browser.switch_to_default_content()
        return self

    def click_accept_button(self):
        self.browser.switch_to_frame(self.browser.find(LoginUsuarioPageLocators.IFRAME))
        self.browser.find(LoginUsuarioPageLocators.ACCEPT_BUTTON).click()
        self.browser.switch_to_default_content()
        return self




class TransferPage1( BasePage ):
    url ='https://www.banesconline.com/mantis/WebSite/transferencias/tercerosbanesco.aspx'
    
    def click_accept_button(self):
        self.browser.find(TransferPage1Locator.ACCEPT_BUTTON).click()

    def get_payee_data(self, cedula =None, account_number = None, email = None):
        #print(locals())
        data= {}
        return data

    def fill_form(self, data):
        self.get_payee_data(id=19077308)
        ACCOUNT_SELECTOR= self.browser.find(TransferPage1.ACCOUNT_SELECTOR).send_keys()
        ACCOUNT_NUMBER= self.browser.find(TransferPage1.ACCOUNT_NUMBER).send_keys()
        ACCOUNT_NAME= self.browser.find(TransferPage1.ACCOUNT_NAME).send_keys()
        NATIONALITY= self.browser.find(TransferPage1.NATIONALITY).send_keys()
        ID_NUMBER= self.browser.find(TransferPage1.ID_NUMBER).send_keys()
        AMOUNT= self.browser.find(TransferPage1.AMOUNT).send_keys()
        DESCRIPTION= self.browser.find(TransferPage1.DESCRIPTION).send_keys()

        ACCEPT_BUTTON= self.browser.find(TransferPage1.ACCEPT_BUTTON).click()


class TransferPage2(BasePage):
    def click_accept_button(self):
        self.browser.find(TransferPage2Locator.ACCEPT_BUTTON).click()


class TransferPage3(BasePage):
    # def screenshot(self, path = None, filename= None):
    #     now = datetime.now()
    #     filename= filename  if filename else 'ss_%s_%s_%s.png' %(str(now.year), str(now.month), str(now.day))
    #     save_path= os.path.join(save_path, filename) if save_path else filename
    #     #self.screenshot = self.browser.find(TransferPage3Locator.RECEIPT_ELEM).driver.screenshot(save_path)
    #     return self

    def click_accept_button(self):
        self.browser.find(TransferPage3Locator.ACCEPT_BUTTON).click()


class LoggedInPage(BasePage):

    def __init__(self, browser):
        self.browser = browser

    def open_transfer_banesco_screen(self):
        #self.browser.driver.get('https://www.banesconline.com/mantis/WebSite/transferencias/tercerosbanesco.aspx')
        self.browser.visit('https://www.banesconline.com/mantis/WebSite/transferencias/tercerosbanesco.aspx')
        try:
            #myElem = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_cp_wz_StartNavigationTemplateContainerID_btnNext')))
            myElem= self.browser.find(TransferPage1.TRANSFER_DIV)
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        return self

    def logout(self):
        '''
        MODIFY THIS CODE TO CUSTOMIZE LOGIN EXPERIENCE
        '''
        try:
            exit_button = self.browser.driver.find_element_by_id('ctl00_btnSalir_lkButton').click()# path = //*[@id="ctl00_btnSalir_lkButton"]
            #browser.switch_to_default_content()
            print('loggging out of banesco')
        except:
            print('error occurred during logout')
            self.browser = None
        return self.browser


class AnotherConnectionOpenPage(BasePage):
    def __init__(self, browser):
        self.browser = browser

    def click_accept_button(self):
        self.browser.switch_to_frame(self.browser.find(AnotherConnectionOpenPageLocators.IFRAME))
        self.browser.find(AnotherConnectionOpenPageLocators.ACCEPT_BUTTON).click()
        self.browser.switch_to_default_content()
        return self

class DashboardPage(LoggedInPage):
    url = 'https://www.banesconline.com/mantis/WebSite/Default.aspx'
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    #usernamefield = SearchTextElement()

    def get_balance(self):
        balance = None
        current_url = self.browser.driver.current_url

        self.browser.visit(self.url)
        if current_url == self.url:
            balance = self.browser.find(DashboardPageLocators.BALANCE_ELEMENT).text.strip().replace('.', '').replace(',' , '.')
        balance = decimal.Decimal(balance) if balance else None
        return balance


class dlTransactionsPage1(LoggedInPage):
    url = 'https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx'
    def download_last_x_days(self , x=None):#date range to get transactions in CSV format.  x is number of days to subtract

        # wait for load code ctl00_cp_btnMostrar
        try:
            myElem = WebDriverWait(self.browser.driver, self.timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_cp_rdbRango')))
        except TimeoutException:
            print("Loading took too much time!")

        radio_button = self.browser.driver.find_element_by_id('ctl00_cp_rdbRango').click()
        #fill elements
        account_selector= Select(self.browser.driver.find_element_by_id('ctl00_cp_ddlCuenta')).select_by_index(1)

        desde = self.browser.driver.find_element_by_id("ctl00_cp_dtFechaDesde").clear()

        hasta = self.browser.driver.find_element_by_id("ctl00_cp_dtFechaHasta")

        now = datetime.now()
        desde_date = now if x==None else (now - timedelta(days=x))

        desde_date=desde_date.replace(hour= 0, minute = 0, second=0,microsecond=0).strftime('%d/%m/%Y')
        hasta_date = now.replace(hour= 23, minute = 59, second=59, microsecond=999999).strftime('%d/%m/%Y')
        
        desde = self.browser.driver.find_element_by_id("ctl00_cp_dtFechaDesde")
        desde.send_keys(desde_date)
        hasta.send_keys(hasta_date)
        exportar_button = self.browser.driver.find_element_by_name('ctl00$cp$ctl25').click()


        #next screen wait elemen ==ctl00_cp_optPredeterminada
        #radio_button = self.browser.find_element_by_id("ctl00_cp_optPredeterminada").click()
        #aceptar_button = self.browser.find_element_by_id("ctl00_cp_btnOk").click()


        # # To prevent download dialog
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('browser.download.folderList', 2) # custom location
        # profile.set_preference('browser.download.manager.showWhenStarting', False)
        # profile.set_preference('browser.download.dir', '/tmp')
        # profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        return self




class dlTransactionsPage2(LoggedInPage):
    url = 'https://www.banesconline.com/mantis/WebSite/ConsultaMovimientosCuenta/Exportar.aspx'
    def download_transactions(self):
        session = requests.Session()
        cookies = self.browser.driver.get_cookies()
        cookie_string  =''
        for cookie in cookies: 
            cookie_string+= '%s=%s; ' %(str(cookie['name']), str(cookie['value']))
            #session.cookies.set(cookie['name'], cookie['value'])

        #SETTING HEADERS FOR REQUEST
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'en-US,en;q=0.9,es;q=0.8',
            'Cache-Control' : 'max-age=0',
            'Connection' : 'keep-alive',
            'Content-Length' : '1240',
            'Host' : 'www.banesconline.com',
            'Origin': 'https://www.banesconline.com',
            'Referer': 'https://www.banesconline.com/mantis/WebSite/ConsultaMovimientosCuenta/Exportar.aspx',
            'Upgrade-Insecure-Requests': '1'  ,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
            'Cookie':cookie_string#__utmz=4340768.1524422462.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=4340768; ___tk56138=0.058324477621694015; ASPSESSIONIDSGQASSRQ=DGOPGEFBIEMPMOJEGIAOIDDJ; ASPSESSIONIDSERDQSQQ=OIOBHEFBLFKCAAOIPCPPDDMB; ASP.NET_SessionId=1sezrj45f2izlw55ya5yo1zi; __utma=4340768.1801574764.1524422462.1529008444.1529019141.47; __utmt=1; __utmb=4340768.2.10.1529019141; BanescoMenu_ctl00_FastMenu=1000000000000000000000
        }

        #SETTING FORM DATA INTO SOMETHING SERVER WILL UNDERSTAND
        data ={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': self.browser.driver.find_element_by_id("__VIEWSTATE").text,
            '__VIEWSTATEGENERATOR': self.browser.driver.find_element_by_id("__VIEWSTATEGENERATOR").text,
            '__EVENTVALIDATION': self.browser.driver.find_element_by_id("__EVENTVALIDATION").text,
            'TitleFormat':'BanescOnline dddd, dd de MMMM de yyyy HH:mm:ss f t',
            'ctl00$cp$Formato' : 'optParametros',
            'ctl00$cp$Encabezado': 'optEncabezadoSi',
            'ctl00$cp$Mov': 'optMovNo',
            'ctl00$cp$Delimitador': 'optDelimitador',
            'ctl00$cp$ddlDelimitadores': '2',
            'ctl00$cp$btnOk': 'Aceptar'
        }



        url ="https://www.banesconline.com/mantis/WebSite/ConsultaMovimientosCuenta/Exportar.aspx"

        #SENDING REQUEST
        local_filename = 'arberto.txt'
        
        with session as s:
            download = session.post(url, data, headers= headers)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=';')
            csv_data = list(cr)

            #csv_data    = [row for row in csv_data]
            json_data= []

            for row in csv_data:
                new_row=  [column.strip().replace('.','').replace(',','.') for column in row if column.strip() !='']
                new_row ={ 
                    'fecha' : datetime.strptime(new_row[0], '%d/%m/%Y'), #parsing string as date
                    'referencia' :new_row[1],
                    'decripcion' :new_row[2],
                    'monto': decimal.Decimal(new_row[3]), #parse string as type decimal
                    'saldo' : decimal.Decimal(new_row[4])
                } 
                json_data.append(new_row)

        print(json_data)
        return self

class DirectoryPage(LoggedInPage):

    url = 'https://www.banesconline.com/mantis/WebSite/administraciondirectorios/individual.aspx'
    locator_class= DirectoryPageLocators
    def click_link_by_alias(self, alias):
        print(alias)

    def get_directory_list(self):
        i = 0
        self.directory = []
        table = self.browser.find(DirectoryPageLocators.TABLE_ELEM)
        
        rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table

        if len(rows) >0:
            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
                if len(col)==4 and i > 0: #skip title row
                    print(col[0])
                    alias=col[0].text
                    descripcion=col[1].text
                    beneficiario=col[2].text
                    codigo_cuenta=col[3].text
                    anchor_elem= col[1]
                    #.find_elements_by_tag_name('a')[0].click()
                    if descripcion.lower() =='cuenta':
                        self.directory.append({
                            'alias': alias,
                            'descripcion': descripcion,
                            'beneficiario': beneficiario,
                            'codigo_cuenta': codigo_cuenta
                        })
                i+=1
            rows[0].find_elements(By.TAG_NAME, "a")[0].click()

        print(self.directory)
        return self.directory

class DirectoryDetailPage(LoggedInPage):

    url = 'https://www.banesconline.com/mantis/WebSite/administraciondirectorios/individual.aspx'
    locator_class= DirectoryDetailPageLocators
    def get_form_data(self):
        data = {
            'alias': self
        }
    # def click_link_by_alias(self, alias):
    #     print(alias)

    # def get_directory_list(self):
    #     i = 0
    #     self.directory = []
    #     table = self.browser.find(DirectoryPageLocators.TABLE_ELEM)
        
    #     rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table

    #     if len(rows) >0:
    #         for row in rows:
    #             col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
    #             if len(col)==4 and i > 0: #skip title row
    #                 alias=col[0].text
    #                 descripcion=col[1].text
    #                 beneficiario=col[2].text
    #                 codigo_cuenta=col[3].text
    #                 if descripcion.lower() =='cuenta':
    #                     self.directory.append({
    #                         'alias': alias,
    #                         'descripcion': descripcion,
    #                         'beneficiario': beneficiario,
    #                         'codigo_cuenta': codigo_cuenta
    #                     })
    #             i+=1
    #     print(self.directory)
    #     return self
'''
{'domain': 'www.banesconline.com', 'httpOnly': False, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False, 'value': 'gkcw0ym1zl1n5m55xy1lsu55'}
{'domain': '.banesconline.com', 'expiry': 1592017618, 'httpOnly': False, 'name': '__utma', 'path': '/', 'secure': False, 'value': '4340768.1437087551.1528945617.1528945617.1528945617.1'}
{'domain': '.banesconline.com', 'httpOnly': False, 'name': '__utmc', 'path': '/', 'secure': False, 'value': '4340768'}
{'domain': '.banesconline.com', 'expiry': 1528947418, 'httpOnly': False, 'name': '__utmb', 'path': '/', 'secure': False, 'value': '4340768.2.10.1528945617'}
{'domain': '.banesconline.com', 'expiry': 1544713618, 'httpOnly': False, 'name': '__utmz', 'path': '/', 'secure': False, 'value': '4340768.1528945617.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
{'domain': '.banesconline.com', 'expiry': 1528946217, 'httpOnly': False, 'name': '__utmt', 'path': '/', 'secure': False, 'value': '1'}

'''

'''

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'en-US,en;q=0.9,es;q=0.8',
    'Cache-Control' : 'max-age=0',
    'Connection' : 'keep-alive',
    'Content-Length' : '1114',
    'Host' : 'www.banesconline.com',
    'Origin': 'https://www.banesconline.com',
    'Referer': 'https://www.banesconline.com/mantis/WebSite/ConsultaMovimientosCuenta/Exportar.aspx',
    'Upgrade-Insecure-Requests': '1'  ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

r = requests.post(url, data=json.dumps(payload), headers=headers)

'''