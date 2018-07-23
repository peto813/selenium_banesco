from selenium.webdriver.common.by import By



class ValidationPageLocators(object):
	IFRAME= (By.CSS_SELECTOR, '#ctl00_cp_frmAplicacion')

	#within IFRAME
	QUESTION1_FIELD= (By.CSS_SELECTOR, '#lblPrimeraP')
	QUESTION2_FIELD= (By.CSS_SELECTOR, '#lblSegundaP')
	ANSWER1_FIELD= (By.CSS_SELECTOR, '#txtPrimeraR')
	ANSWER2_FIELD= (By.CSS_SELECTOR, '#txtSegundaR')
	ACCEPT_BUTTON= (By.CSS_SELECTOR, '#bAceptar')
	REGRESAR_BUTTON =  (By.CSS_SELECTOR, '#bRegresar2')




class LoginUsuarioPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    HIDDEN_DIV =  (By.CSS_SELECTOR, '#__VIEWSTATEGENERATOR')
    IFRAME = (By.CSS_SELECTOR, '#ctl00_cp_frmAplicacion')
    FORM = (By.CSS_SELECTOR, '#aspnetForm')

    #elements within iframe
    IFRAME_LOGIN_DIV = (By.CSS_SELECTOR, 'CamposLogin')
    IFRAME_HEAD_ELEM = (By.CSS_SELECTOR, 'head')
    IFRAME_INICIO_FORM = (By.CSS_SELECTOR, 'Inicio')
    USERNAME_FIELD = (By.CSS_SELECTOR, '#txtUsuario')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#txtClave')
    ACCEPT_BUTTON = (By.CSS_SELECTOR, '#bAceptar')
    REMEMBER_ME_BUTTON = (By.CSS_SELECTOR, '#CBMachine')
    FORGOT_PWD_LINK =(By.CSS_SELECTOR, '#lnkOlvidoClave')

class AnotherConnectionOpenPageLocators(object):
    
    
	IFRAME= (By.CSS_SELECTOR, '#ctl00_cp_frmAplicacion')
	FORM = (By.CSS_SELECTOR, '#aspnetForm')
	# #elements within iframe
	MESSAGE_ELEM =  (By.CSS_SELECTOR, '#lblMensaje')
	ACCEPT_BUTTON =  (By.CSS_SELECTOR, '#bAceptar')
	MESSAGE_TEXT= 'Hemos detectado que exíste otra conexión activa en este momento y por su seguridad\
	no podemos permitir el ingreso.Le recordamos que solo puede mantener una sesión activa con su usuario y contraseña\
	de BanescOnline'

class DashboardPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    BALANCE_ELEMENT =  (By.CSS_SELECTOR, '#content-right > table.GridViewHm > tbody > tr > td:nth-child(3)')
    EXIT_BUTTON= (By.CSS_SELECTOR, '#ctl00_btnSalir_lkButton')

    # #elements within iframe
    # IFRAME_LOGIN_DIV=(By.CSS_SELECTOR, 'CamposLogin')
    # IFRAME_HEAD_ELEM =(By.CSS_SELECTOR, 'head')
    # IFRAME_INICIO_FORM = (By.CSS_SELECTOR, 'Inicio')
    # USERNAME_FIELD = (By.CSS_SELECTOR, '#txtUsuario')
    # PASSWORD_FIELD = (By.CSS_SELECTOR, '#txtClave')
    # ACCEPT_BUTTON =(By.CSS_SELECTOR, '#bAceptar')



class VerificarUsuarioPageLocators(object):
    """wHEN PC NOT RECOGNIZED BANK REQUIRES USER VERIFICATION"""
    pass

class BanescoLocations(object):
	USER_LOGIN="https://www.banesconline.com/mantis/Website/Login.aspx"



class TransferPage1Locator(object):
	TRANSFER_DIV =  (By.CSS_SELECTOR, '#ctl00_cp_wz_StartNavigationTemplateContainerID_btnNext')
	ACCOUNT_NUMBER = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtCuentaTransferir')
	ACCOUNT_NAME = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtBen')
	NATIONALITY = (By.CSS_SELECTOR, '#ctl00_cp_wz_ddlNac')
	ID_NUMBER = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtCedula')
	AMOUNT = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtMonto')
	DESCRIPTION = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtConcepto')

	ACCOUNT_SELECTOR = (By.CSS_SELECTOR, '#ctl00_cp_wz_ddlCuentaDebitar')
	DESCRIPTION = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtConcepto')

	ACCEPT_BUTTON = (By.CSS_SELECTOR, '#ctl00_cp_wz_StartNavigationTemplateContainerID_btnNext')
	DESCRIPTION = (By.CSS_SELECTOR, '#ctl00_cp_wz_txtConcepto')
	
class TransferPage2Locator(object):
	ACCEPT_BUTTON = (By.CSS_SELECTOR, '#ctl00_cp_wz_StepNavigationTemplateContainerID_btnNext')


class TransferPage3Locator(object):
	ACCEPT_BUTTON = (By.CSS_SELECTOR, '#ctl00_cp_wz_CRbo_btnReg')
	RECEIPT_ELEM =(By.CSS_SELECTOR, '#ctl00_cp_wz')
	PRINT_BTN = (By.CSS_SELECTOR, '#ctl00_cp_wz_CRbo_btnImpRbo')


class DirectoryPageLocators(object):
	TABLE_ELEM = (By.CSS_SELECTOR, '#ctl00_cp_wz')

class DirectoryDetailPageLocators(object):
	ALIAS_ELEM = (By.CSS_SELECTOR, '#ctl00_cp_wz_DirData_txtAlias')
	CEDULA_ELEM = (By.CSS_SELECTOR, '#ctl00_cp_wz_DirData_txtIdent')
	NATIONALIDAD_ELEM = (By.CSS_SELECTOR, '#ctl00_cp_wz_DirData_ddlNac')
	BANCO_ELEM = (By.CSS_SELECTOR, '#ctl00_cp_wz_DirData_ddlNac')
