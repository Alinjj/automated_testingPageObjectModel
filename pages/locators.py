from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.XPATH,"//a[@class='btn btn-default']")
    USER_ICON = (By.CLASS_NAME,'icon-user')

class BasketPageLocators():
    BASKET_EMPTY = (By.XPATH,'//p')
    BASKET_ITEMS = (By.CLASS_NAME,'basket-items')

class ProductPageLocators():
    ADD_IN_CART = (By.CLASS_NAME,'btn-add-to-basket')
    ADD_MESSAGE = (By.CLASS_NAME, "alert-success")
    NAME_OF_BOOK = (By.XPATH, '//h1')
    PRICE_OF_BOOK = (By.XPATH, "//p[@class='price_color']")
    TOTAL_OF_CART = (By.XPATH, "//div[@class='alertinner ']/p[1]")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')

class LoginPageLocators():
    LOGIN_LOG_IN = (By.ID,'id_login-username')
    LOGIN_LOG_IN_PSWRD = (By.ID,'id_login-password')
    LOGIN_LOG_IN_SUBMIT = (By.NAME,'login_submit')
    LOGIN_FORM = (By.ID,'login_form')
    CHECK_IN_FORM = (By.ID,'register_form')

class CheckInPageLocators():
    LOGIN_CHECK_IN = (By.ID,'id_registration-email')
    LOGIN_CHECK_IN_PSWRD = (By.ID,'id_registration-password1')
    LOGIN_CHECK_IN_PSWRD_CONFIRM = (By.ID,'id_registration-password2')
    LOGIN_CHECK_IN_SUBMIT = (By.NAME,'registration_submit')



