import os
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoAlertPresentException

def before_scenario(context, scenario):
    """
    Esta función se ejecuta antes de cada escenario de prueba.
    Inicializa el WebDriver y lo almacena en el contexto.
    """
    options = Options()

    # Configuración para evitar popups y advertencias de seguridad
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--password-store=basic")
    options.add_argument("--headless")  # Modo sin interfaz gráfica (importante en GitHub Actions)
    options.add_argument("--no-sandbox")  # Necesario en contenedores como GitHub Actions
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas en entornos virtualizados
    options.add_argument("--disable-gpu")  # Solo en caso de necesitar compatibilidad con GPU

    options.add_argument("--disable-features=PasswordProtectionService")
    options.add_argument("--disable-features=PasswordLeakDetection")
    
    user_data_dir = os.path.join(tempfile.gettempdir(), 'chrome_profile')
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Preferencias experimentales para desactivar advertencias
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
        "credentials_enable_autosignin": False
    })

    # Descargar el driver automáticamente con `webdriver-manager`
    service = Service(ChromeDriverManager().install())  
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(15)
    context.driver.maximize_window()

    # Intentar cerrar cualquier popup o alerta inesperada
    try:
        context.driver.switch_to.alert.dismiss()
    except NoAlertPresentException:
        pass 

def after_step(context, step):
    time.sleep(0.5)

def after_scenario(context, scenario):
    """
    Esta función se ejecuta después de cada escenario de prueba.
    Cierra el navegador para limpiar después de cada prueba.
    """
    context.driver.quit()