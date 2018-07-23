#settings for selenium bank browser app
#BANESCO_STARTING_URL ="https://www.banesconline.com/mantis/Website/Login.aspx"
BANESCO_USERNAME= "fractalsw"
BANESCO_PASSWORD= "amillan813!"
#BANESCO_PASSWORD= "ou63ut14!#"
TIMEOUT=10

#CHROME
CHROME_INCOGNITO = True
CHROME_EXECUTABLE_PATH = 'C:/Users/alberto.DESKTOP-3L8MSUI/Desktop/chromedriver'
CHROME_DRIVER_OPTIONS = ["incognito"] ## double dash is added by application automatically

BROWSER_ARGUMENTS ={
	'FIREFOX': {
        #'firefox_options': CHROME_EXECUTABLE_PATH or None, 
        'executable_path': "C:/Utility/BrowserDrivers/geckodriver.exe"
        # 'options': None,
        # 'service_args': None,
        # 'desired_capabilities': None,
        # 'service_log_path': None,
        # 'chrome_options': None
	},
	'CHROME': {
        'executable_path': CHROME_EXECUTABLE_PATH or None, 
        'port': 0,
        'options': None,
        'service_args': None,
        'desired_capabilities': None,
        'service_log_path': None,
        'chrome_options': None
        #'chrome_optionsList': CHROME_DRIVER_OPTIONS
	},
	'PHANTOMJS': {},
}