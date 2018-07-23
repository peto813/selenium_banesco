
from browsers import *
from locators import *
import settings, time
from page import *
from selenium.common.exceptions import TimeoutException, WebDriverException



class BanescoAppCrawler():
	browser = BanescoBrowser(**settings.BROWSER_ARGUMENTS['CHROME'])
	#url = BanescoLocations.USER_LOGIN # ths is start url
	start_page = LoginUsuarioPage
	password_page = LoginPasswordPage
	# another_connection_page = AnotherConnectionOpenPage
	# validation_page = ValidationPage
	# dashboard_page = DashboardPage

	def __init__(self):
		self.browser.visit(self.start_page)
		self.start_page = self.start_page(self.browser)

	# def try_pwd_page(self):
	# 	# TRY PASSWORD PAGE
	# 	self.password_page = LoginPasswordPage(self.browser)
	# 	self.password_page.fill_form().click_accept_button()
	# 	#page = self.password_page

	# def try_alrdy_connected_pg(self):
	# 	self.another_connection_page = AnotherConnectionOpenPage(self.browser)
	# 	self.another_connection_page.click_accept_button()#.add_to_cue()# these do not yet exist
	# 	#page = self.another_connection_page

	def get_current_page(self):

		page = None

		#VALIDATION PAGE

		try:
			iframe =self.browser.driver.find_element_by_css_selector(ValidationPageLocators.IFRAME[1])
			self.browser.switch_to_frame(iframe)
			regresar_button =self.browser.driver.find_element_by_css_selector(ValidationPageLocators.REGRESAR_BUTTON[1])
			accept_button =self.browser.driver.find_element_by_css_selector(ValidationPageLocators.ACCEPT_BUTTON[1])
			question1 = self.browser.driver.find_element_by_css_selector(ValidationPageLocators.QUESTION1_FIELD[1]).text#.send_keys(settings.BANESCO_PASSWORD)#feed params from locators, use second parameter to indicate element is within iframe
			question2 = self.browser.driver.find_element_by_css_selector(ValidationPageLocators.QUESTION2_FIELD[1]).text			

			self.browser.switch_to_default_content()
			return 'validation_page'
		except:
			regresar_button = None
			page=None
			self.browser.switch_to_default_content()



		#ENTER PASSWORD PAGE
		try:
			iframe =self.browser.driver.find_element_by_css_selector(LoginUsuarioPageLocators.IFRAME[1])
			self.browser.switch_to_frame(iframe)
			forgot_password_link = self.browser.driver.find_element_by_css_selector(LoginUsuarioPageLocators.FORGOT_PWD_LINK[1])
			remember_me_button =self.browser.driver.find_element_by_css_selector(LoginUsuarioPageLocators.REMEMBER_ME_BUTTON[1])
			accept_button =self.browser.driver.find_element_by_css_selector(LoginUsuarioPageLocators.ACCEPT_BUTTON[1])
			pwd_input = self.browser.driver.find_element_by_css_selector(LoginUsuarioPageLocators.PASSWORD_FIELD[1])#.send_keys(settings.BANESCO_PASSWORD)#feed params from locators, use second parameter to indicate element is within iframe
		
			self.browser.switch_to_default_content()
			return 'password_page'

		except:
			regresar_button = None
			page=None
			self.browser.switch_to_default_content()


		#ANOTHER CONNECTIONPAGE
		try:
			iframe =self.browser.driver.find_element_by_css_selector(AnotherConnectionOpenPageLocators.IFRAME[1])
			self.browser.switch_to_frame(iframe)
			message_elem = self.browser.driver.find_element_by_css_selector(AnotherConnectionOpenPageLocators.MESSAGE_ELEM[1])
			accept_button =self.browser.driver.find_element_by_css_selector(AnotherConnectionOpenPageLocators.ACCEPT_BUTTON[1])
			self.browser.switch_to_default_content()
			return 'another_connection_page'

		except:
			regresar_button = None
			page=None
			self.browser.switch_to_default_content()

		#DASHBOARD PAGE
		try:
			balance_elem = self.browser.driver.find_element_by_css_selector(DashboardPageLocators.BALANCE_ELEMENT[1])
			exit_button = self.browser.driver.find_element_by_css_selector(DashboardPageLocators.EXIT_BUTTON[1])
			url = 'https://www.banesconline.com/mantis/WebSite/Default.aspx'
			if url ==self.browser.driver.current_url:
				return 'dashboard_page'
			return None

		except:
			regresar_button = None
			page=None
			self.browser.switch_to_default_content()
		return page



	def login(self):
		#input username
		balance = None
		end_loop = False
		self.start_page.fill_form().click_accept_button()

		i = 5
		while not end_loop and i <10: # max of ten iterations to avoid infinite loop
			page= self.get_current_page()

			if page or not page:
				if page =='validation_page':
					self.validation_page = ValidationPage(self.browser)
					self.validation_page.fill_form().click_accept_button()

				elif page=='another_connection_page':
					AnotherConnectionOpenPage(self.browser).click_accept_button()
					'''
					add current pending transaction to queue
					'''
					end_loop = True

				elif page=='password_page':
					LoginPasswordPage(self.browser).fill_form().click_accept_button()
					
				elif page =='dashboard_page':
					end_loop = True
			i+=1
		self.current_page = page
		return self


def testAnotherConnection():

	banesco_crawler = BanescoAppCrawler()

	a=banesco_crawler.login().browser.visit(DirectoryPage).current_page.get_directory_list()

	# peo=banesco_crawler.browser.find(DashboardPageLocators.BALANCE_ELEMENT)
	# peo.screenshot('peo.png')
	# banesco_crawler.browser.logout()
	# if banesco_crawler.current_page =='dashboard_page':
	# 	balance=DashboardPage(banesco_crawler.browser).get_balance()

	# #GET LAST 30 DAYS AND PRINT
	# banesco_crawler.browser.visit('https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx')
	# dl_transactions_page1= dlTransactionsPage1(banesco_crawler.browser)
	# dl_transactions_page1.download_last_x_days(30)
	# dl_transactions_page2= dlTransactionsPage2(banesco_crawler.browser)
	# dl_transactions_page2.download_transactions()

	# print(balance or 'nope no balance retreived')
	# dl_transactions_page2.logout()
def get_transactions(last_x_days=1):
	banesco_crawler = BanescoAppCrawler()

	transactions=banesco_crawler.login().browser.visit(dlTransactionsPage1).current_page.download_last_x_days(last_x_days)#.download_transactions()#.current_page.get_directory_list()


	#browser.visit('https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx')

	
	#PAGE X
	# dl_transactions_page1= dlTransactionsPage1(browser)
	# dl_transactions_page1.download_last_x_days(download_last_x_days)

	dl_transactions_page2= dlTransactionsPage2(banesco_crawler.browser)
	dl_transactions_page2.download_transactions()
	return transactions

def main():
	browser = BanescoBrowser(**settings.BROWSER_ARGUMENTS['CHROME'])
	browser.visit(location=BanescoLocations.USER_LOGIN)

	#PAGE 1
	page1 = LoginUsuarioPage(browser)#takes driver as instatntiation
	page1.fill_form().click_accept_button()

	#login password second screen (PAGE 2)
	try:
		page2 = LoginPasswordPage(browser)
		page2.fill_form().click_accept_button()

	except:
		'''
		exeception will be thrown if it sends you to validation page
		'''
		pass

	dashboard_page = DashboardPage(browser)
	balance = dashboard_page.get_balance()


	browser.visit('https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx')

	
	#PAGE X
	dl_transactions_page1= dlTransactionsPage1(browser)
	dl_transactions_page1.download_last_x_days(10)

	dl_transactions_page2= dlTransactionsPage2(browser)
	dl_transactions_page2.download_transactions()
	#current_pate =dl_transactions_page2


	#dashboard_page = DashboardPage(browser)
	#balance = dashboard_page.get_balance()


	# browser.visit('https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx')

	
	# #PAGE X
	# dl_transactions_page1= dlTransactionsPage1(browser)
	# dl_transactions_page1.download_last_x_days(2)

	# dl_transactions_page2= dlTransactionsPage2(browser)
	# dl_transactions_page2.download_transactions()
	# current_pate =dl_transactions_page2


	# try:
	# 	#PAGE 3 (DASHBOARD)
	# 	dashboard_page = DashboardPage(browser)
	# 	balance = dashboard_page.get_balance()


	# 	browser.visit('https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx')

		
	# 	#PAGE X
	# 	dl_transactions_page1= dlTransactionsPage1(browser)
	# 	dl_transactions_page1.download_last_x_days(2)

	# 	dl_transactions_page2= dlTransactionsPage2(browser)
	# 	dl_transactions_page2.download_transactions()
	# 	current_pate =dl_transactions_page2

	# except:
	# 	already_connected_page = AnotherConnectionOpenPage(browser)
	# 	print('b')
	# 	already_connected_page.back_to_pwd_page()
	# 	print('c')
	# 	current_page =already_connected_page

	#time.sleep(120)
	current_pate.logout()	
	
	#dl_transactions_page1.logout()
	browser.close()
	
	#browser
	#page = LoginUsuarioPage(browser, timeout = settings.TIMEOUT)
	#usuario_field= page.find_element()
if __name__ == '__main__':
    #print( "Hello World again from %s!" % __name__)
    #testAnotherConnection()
    a= get_transactions(30)
    print(a)