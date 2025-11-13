from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ultils.logger import log


class BasePage:
    def __init__(self, mobile_driver):
        self.driver = mobile_driver
        self.wait = WebDriverWait(mobile_driver, 10)
        log.info(f"BasePage inicializada com o driver: {mobile_driver.session_id}")

    def find_element(self, by, locator):
        """
        Espera pela presença de um elemento e o retorna.
        """
        log.info(f"Procurando elemento (pela presença): {locator}")
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            log.info(f"Elemento encontrado: {locator}")
            return element
        except (TimeoutException, NoSuchElementException) as e:
            log.error(f"Elemento NÃO encontrado (Timeout): {locator}", exc_info=True)
            raise e

    def click_element(self, by, locator):
        """
        Espera um elemento ficar clicável e clica nele.
        """
        log.info(f"Tentando clicar no elemento: {locator}")
        try:
            element = self.wait_for_element_to_be_clickable(by, locator)
            element.click()
            log.info(f"Elemento clicado com sucesso: {locator}")
        except Exception as e:
            log.error(f"Falha ao CLICAR no elemento: {locator}", exc_info=True)
            raise

    def send_keys_to_element(self, by, locator, text):
        """
        Encontra um elemento e digita um texto nele.
        """
        log_text = text
        if "password" in str(locator).lower() or "senha" in str(locator).lower():
            log_text = "***"
            
        log.info(f"Enviando texto '{log_text}' para o elemento: {locator}")
        try:
            element = self.find_element(by, locator)
            element.send_keys(text)
            log.info(f"Texto enviado com sucesso para: {locator}")
        except Exception as e:
            log.error(f"Falha ao ENVIAR TEXTO para o elemento: {locator}", exc_info=True)
            raise

    def get_element_text(self, by, locator):
        """
        Encontra um elemento e retorna seu atributo 'text'.
        """
        log.info(f"Tentando pegar o atributo 'text' do elemento: {locator}")
        try:
            text = self.find_element(by, locator).text
            log.info(f"Texto recuperado: '{text}' do elemento: {locator}")
            return text
        except Exception as e:
            log.error(f"Falha ao pegar o 'text' do elemento: {locator}", exc_info=True)
            raise

    def is_element_displayed(self, by, locator):
        """
        Verifica se um elemento está visível. Não falha o teste.
        """
        log.info(f"Verificando se o elemento está visível: {locator}")
        try:
            self.wait_for_visibility_of_element(by, locator)
            log.info(f"Elemento está visível: {locator}")
            return True
        except (TimeoutException, NoSuchElementException):
            log.info(f"Elemento NÃO está visível: {locator}")
            return False
        
    def is_element_enabled(self, by, locator):
        """
        Verifica se um elemento está habilitado.
        """
        log.info(f"Verificando se o elemento está habilitado: {locator}")
        try:
            enabled = self.find_element(by, locator).is_enabled()
            log.info(f"Status de 'enabled' do elemento: {enabled} para: {locator}")
            return enabled
        except Exception as e:
            log.error(f"Falha ao verificar 'enabled' do elemento: {locator}", exc_info=True)
            raise    
    
    def wait_for_visibility_of_element(self, by, locator):
        """
        Espera explicitamente pela visibilidade de um elemento.
        """
        log.info(f"Esperando VISIBILIDADE do elemento: {locator}")
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, locator)))
            log.info(f"Elemento está visível: {locator}")
            return element
        except (TimeoutException, NoSuchElementException) as e:
            log.error(f"Elemento NÃO ficou visível (Timeout): {locator}", exc_info=True)
            raise e

    def wait_for_element_to_be_clickable(self, by, locator):
        """
        Espera explicitamente que um elemento seja clicável.
        """
        log.info(f"Esperando elemento ser CLICÁVEL: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            log.info(f"Elemento está clicável: {locator}")
            return element
        except (TimeoutException, NoSuchElementException) as e:
            log.error(f"Elemento NÃO ficou clicável (Timeout): {locator}", exc_info=True)
            raise e

    def get_element_content_desc(self, by, locator):
        """
        Método robusto para pegar o 'content-desc' no Appium.
        """
        log.info(f"Tentando pegar o 'content-desc' do elemento: {locator}")
        try:
            name = self.find_element(by, locator).get_attribute("content-desc")
            log.info(f"'content-desc' recuperado: '{name}' do elemento: {locator}")
            return name
        except Exception as e:
            log.error(f"Falha ao pegar o 'content-desc' do elemento: {locator}", exc_info=True)
            raise