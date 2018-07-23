

def iframe_present(original_method):
	'''
	decorator that enters and exits iframe
	'''
	def wrapper(self, locator ,iframe_locator=None):
		# try:
		# 	self.iframe  = WebDriverWait(self.browser, self.timeout).until(
		# 		EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
		# 	)
		# except:
		# 	self.iframe =None

		# if self.iframe:
		# 	self.browser.switch_to.frame(self.iframe)
			#self.iframe= iframe
		original_method(self, locator, iframe_locator=None)
		
		#if self.iframe:
		self.browser.switch_to_default_content()

	return wrapper