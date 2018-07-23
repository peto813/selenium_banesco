import decimal, datetime, csv
from datetime import datetime, timedelta
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.utils import return_value_if_exists
from . import settings
	#decorator for escaping iframes
def iframe_present(original_method):
	'''
	decorator that enters and exits iframe
	'''
	def wrapper(self):
		try:
			self.iframe  = WebDriverWait(self.browser, self.timeout).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
			)
		except:
			self.iframe =None

		if self.iframe:
			self.browser.switch_to.frame(self.iframe)
			#self.iframe= iframe
		self.browser = original_method(self)
		self.browser.switch_to_default_content()
		return self.browser
	return wrapper


class banescoDataMiner():
	'''
	this class interacts with the banesco webpage via selenium data mining
	'''
	"""docstring for banescoMiner"""
	# def __init__(self, arg):
	# 	super(banescoMiner, self).__init__()
	# 	self.arg = arg
	timeout = settings.TIMEOUT
	usuario_banesco = settings.BANESCO_USERNAME
	clave_banesco = settings.BANESCO_PASSWORD
	initial_url=settings.BANESCO_STARTING_URL

	#helper handles
	def get_answer(title):
		text = title.text
		answer = None
		if text =='¿Cuál es mi postre favorito?':
			answer = 'brownie'
		elif text== 'SSN':
			answer = '444087063'
		elif text== 'ciudad nacimiento mama':
			answer = 'barcelona'
		elif text== '¿Cuál es su película favorita?':
			answer = 'braheveart'
		return answer

	def login(self, page=1):#page is optional, lets the method knwow if starting template is differente than 1

		self.browser = self.get_browser(self.get_options())
		login_method_dict={'1': self.process_page1(),'2':self.process_page2(),'3':self.process_page3(),'4':self.process_home()}
		finished= False
		try:
			while finished==False :
				self.browser = login_method_dict[str(page)] #calls corresponing method and returns refreshed browser
				self.browser, self.page = self.get_page() # get page number
				#print(page, 'pageee')
				finished= True if self.is_authenticated() else False #continue until an exit button is present in page (you are logged in)
		except TimeoutException:
			print('Timed out waiting for page to load')
			self.browser.quit()
		# finally:
		# 	pass
		return self

	def is_authenticated(self):
		'''
		get urls. if url is https://www.banesconline.com/mantis/WebSite/Default.aspx
		 and the exit button is presend then you are authenticated and are home screen
		print browser.current_url	
		'''

		try:
			exit_button = self.browser.find_element_by_id('ctl00_btnSalir_lkButton')
			authenticated = True if exit_button else False
		except:
			exit_button = None
			authenticated = False
		return authenticated



	def get_page(self):
		'''
		gets the current page number, returns browser also
		'''
		page = None
		self.iframe = self.get_current_frame()
		if self.iframe:
			self.browser.switch_to.frame(self.iframe)

		try:
			usuarioInput =self.browser.find_element_by_id('txtUsuario')
			if usuarioInput:
				page = 1
		except:
			pass

		#check for page 2
		try:
			usuario = self.browser.find_elements_by_class_name('titulo2')[0]
			if usuario:
				page = 2
		except:
			pass

		#check for page 3
		try:
			clave_input_elemet = browser.find_element_by_id('txtClave')
			if clave_input_elemet:
				page = 3
		except:
			pass

		#check for page 4
		try:
			clave_input_elemet = self.browser.find_element_by_id('txtClave')
			if clave_input_elemet:
				page = 4
		except:
			pass

		return (self.browser, page)

	def get_options(self):
		'''
		defines the options to be appended to the browser object upon initialization
		'''
		options = webdriver.ChromeOptions()
		options.add_argument("--incognito")
		return options

	def get_browser(self, options= None):
		if options:
			self.browser = webdriver.Chrome(executable_path='C:/Users/alberto.DESKTOP-3L8MSUI/Desktop/chromedriver', chrome_options=options)
		else:
			self.browser = webdriver.Chrome(executable_path='C:/Users/alberto.DESKTOP-3L8MSUI/Desktop/chromedriver')

		self.browser.get(self.initial_url)
		return self.browser

	def logout(self):
		'''
		MODIFY THIS CODE TO CUSTOMIZE LOGIN EXPERIENCE
		'''
		try:
			exit_button = self.browser.find_element_by_id('ctl00_btnSalir_lkButton').click()# path = //*[@id="ctl00_btnSalir_lkButton"]
			#browser.switch_to_default_content()
			print('loggging out of banesco')
		except:
			print('error occurred during logout')
			self.browser = None
		return self.browser






	def get_current_frame(self):
		'''
		finds an iframe in the current page (waits for load if necessary)
		'''
		try:
			self.iframe  = WebDriverWait(self.browser, self.timeout).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
			)
		except:
			self.iframe =None
		return self.iframe


	@iframe_present
	def process_page1(self):
		self.browser.find_element_by_id('txtUsuario').send_keys(self.usuario_banesco)
		self.browser.find_element_by_id('bAceptar').click()
		return self.browser

	@iframe_present
	def process_page2(self):
		print('starting process 2')
		'''
		this page processes the banesco validation page
		'''
		# iframe = self.get_current_frame()
		# if iframe:
		# 	self.browser.switch_to.frame(iframe)

		try:
			validation_text_element = self.browser.find_elements_by_class_name('titulo2')[0]
		except IndexError:
			validation_text_element=None

		if validation_text_element:
			print('VALIDACIÓN DE PREGUNTAS DE SEGURIDAD')
			if  validation_text_element.text=='VALIDACIÓN DE PREGUNTAS DE SEGURIDAD':
				#input security questions, (total of two)
				question1= self.browser.find_element_by_id('lblPrimeraP')#¿Cuál es mi postre favorito?
				question2= self.browser.find_element_by_id('lblSegundaP')#SSN
				answer_title1= get_answer(question1)
				answer_title2= get_answer(question2)
				self.browser.find_element_by_id('txtPrimeraR').send_keys(answer_title1)
				self.browser.find_element_by_id('txtSegundaR').send_keys(answer_title2)
				self.browser.find_element_by_id('bAceptar').click()
	
			#self.browser.switch_to_default_content()

		return self.browser

	@iframe_present
	def process_page3(self):
		'''
		inputs the password and logs in
		checks the rememeber me button
		'''
		#iframe = self.get_current_frame()
		if self.iframe:#iframe was found on page
			#self.browser.switch_to.frame(self.iframe)
			rememberBtn= self.get_remember_me_button()
			if rememberBtn:
				rememberBtn.click()

			clave_input_elemet = self.browser.find_element_by_id('txtClave').send_keys(self.clave_banesco)
			self.browser.find_element_by_id('bAceptar').click()
			#self.browser.switch_to_default_content()
		return self.browser


	def get_remember_me_button(self):
		try:
			remember_me_button =self.browser.find_element_by_id('CBMachine')
		except:
			remember_me_button = None
		return remember_me_button

	def get_home_button(self):
		try:
			home_button =self.browser.find_element_by_id('ctl00_btnTopHome_lkButton')
		except:
			home_button = None
		return home_button

	def get_exit_button(self):
		try:
			exit_button =self.browser.find_element_by_id('ctl00_btnSalir_lkButton')
		except:
			exit_button = None
		return exit_button

	def get_balance(self):
		self.balance = None
		current_url = self.browser.current_url
		if current_url == 'https://www.banesconline.com/mantis/WebSite/Default.aspx' and self.is_authenticated()==True:
			try:
				balance = self.browser.find_element_by_xpath('//*[@id="content-right"]/table[3]/tbody/tr/td[3]').text.strip().replace('.', '').replace(',' , '.')
				self.balance= decimal.Decimal(balance)
			except:
				pass
		return self

	def process_home(self):
		try:
			myElem = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_btnSalir_lkButton')))
			print("BanescoDashboard is ready!")
		except TimeoutException:
			print("Loading took too much time!")
		return self
		return self.browser

	def open_transfer_banesco_screen(self):
		self.browser.get('https://www.banesconline.com/mantis/WebSite/transferencias/tercerosbanesco.aspx')
		try:
			myElem = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_cp_wz_StartNavigationTemplateContainerID_btnNext')))
			print("Page is ready!")
		except TimeoutException:
			print("Loading took too much time!")
		return self

	def fill_transfer_banesco_form(self):
		account_selector_elem = Select(self.browser.find_element_by_id('ctl00_cp_wz_ddlCuentaDebitar')).select_by_index(1)
		#account_selector_elem
		account_number_input_elem = self.browser.find_element_by_id('ctl00_cp_wz_txtCuentaTransferir')


		beneficiario_input_elem = self.browser.find_element_by_id('ctl00_cp_wz_txtBen')

		nacionalidad_input_elem =Select(self.browser.find_element_by_id('ctl00_cp_wz_ddlNac')).select_by_value('V')#V value
		cedula_input_elem = self.browser.find_element_by_id('ctl00_cp_wz_txtCedula')
		monto_input_elem = self.browser.find_element_by_id('ctl00_cp_wz_txtMonto')
		concepto_input_elem = self.browser.find_element_by_id('ctl00_cp_wz_txtConcepto')
		aceptar_button_id ='ctl00_cp_wz_StartNavigationTemplateContainerID_btnNext'
		# other accept button id ctl00_cp_wz_StepNavigationTemplateContainerID_btnNext
		# nro_recibo_id
		# get screenshot
		#aceptar on receipt button id ctl00_cp_wz_CRbo_btnReg
		return self



	def wait(self, seconds=None):
		self.browser.implicitly_wait(seconds or self.timeout)
		return self

	def go_to_directorio_screen(self):
		self.browser.get('https://www.banesconline.com/mantis/WebSite/administraciondirectorios/individual.aspx')
		try:
			myElem = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_cp_wz')))
		except TimeoutException:
			pass
		return self


	def save_screenshot(self, save_path=None, filename=None):
		now = datetime.now()
		filename= filename	if filename	else 'ss_%s_%s_%s.png' %(str(now.year), str(now.month), str(now.day))
		save_path= os.path.join(save_path, filename) if save_path else filename
		self.browser.save_screenshot(save_path)
		return self


	def get_directory_list(self):
		i = 0
		self.directory = []
		table = self.browser.find_element_by_id('ctl00_cp_wz')
		rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table

		if len(rows >0):
			for row in rows:
				col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
				if len(col)==4 and i > 0: #skip title row
					alias=col[0].text
					descripcion=col[1].text
					beneficiario=col[2].text
					codigo_cuenta=col[3].text
					if descripcion.lower() =='cuenta':
						self.directory.append({
							'alias': alias,
							'descripcion': descripcion,
							'beneficiario': beneficiario,
							'codigo_cuenta': codigo_cuenta
						})
				i+=1

		#print(self.directory)
		#IndexError
		return self

	def download_last_x_days(self , x=None):#date range to get transactions in CSV format.  x is number of days to subtract
		self.browser.get('https://www.banesconline.com/mantis/WebSite/consultamovimientoscuenta/movimientoscuenta.aspx')

		# wait for load code ctl00_cp_btnMostrar
		try:
			myElem = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_cp_rdbRango')))
			print("Page is ready!")
		except TimeoutException:
			print("Loading took too much time!")

		radio_button = self.browser.find_element_by_id('ctl00_cp_rdbRango').click()
		#fill elements
		account_selector= Select(self.browser.find_element_by_id('ctl00_cp_ddlCuenta')).select_by_index(1)
		#all_options = account_selector.find_elements_by_tag_name("option")
		# for option in all_options:
		# 	if option.get_attribute("value")=='0134-0262-14-2623025724|mmk':
		# 		print("Value is: %s" % option.get_attribute("value"))
		# 		option.click()

		desde = self.browser.find_element_by_id("ctl00_cp_dtFechaDesde").clear()

		hasta = self.browser.find_element_by_id("ctl00_cp_dtFechaHasta")

		now = datetime.now()
		desde_date = now if x==None else (now - timedelta(days=x))

		desde_date=desde_date.replace(hour= 0, minute = 0, second=0,microsecond=0).strftime('%d/%m/%Y')
		hasta_date = now.replace(hour= 23, minute = 59, second=59, microsecond=999999).strftime('%d/%m/%Y')
		
		print (desde_date, hasta_date)
		desde = self.browser.find_element_by_id("ctl00_cp_dtFechaDesde")
		desde.send_keys(desde_date)
		hasta.send_keys(hasta_date)
		exportar_button = self.browser.find_element_by_name('ctl00$cp$ctl25').click()
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


miner_instance = banescoDataMiner()
miner_instance.login().download_last_x_days(2)

#print(miner_instance.balance)