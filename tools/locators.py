sticky_bar_logo= "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']"     #Логотип в стики-баре
sticky_bar_constructor="//p[contains(text(),'Конструктор')]"    #Кнопка "Конструктор" в стики-баре
sticky_bar_open_profile_button= "//p[contains(text(),'Личный Кабинет')]"    #Кнопка "Личный Кабинет" в стики-баре

main_header="//h1[contains(text(),'Соберите бургер')]"      #Заголовок главной страницы
main_enter_to_account_button="//button[contains(text(),'Войти в аккаунт')]"     #Кнопка "Войти в аккаунт" на главной странице

registration_header="//h2[contains(text(),'Регистрация')]"      #Заголовок страницы регистрации
registration_name_input="(//input[@name='name'])[1]"        #Поле для ввода имени на странице регистрации
registration_email_input="(//input[@name='name'])[2]"       #Поле для ввода логина/email на странице регистрации
registration_password_input="//input[@name='Пароль']"       #Поле для ввода пароля на странице регистрации
registration_register_button="//button[contains(text(),'Зарегистрироваться')]"      #Кнопка "Зарегестрироваться" на странице регистрации
registration_invalid_password_error="//p[@class='input__error text_type_main-default']"     #Сообщение об ошибке при вводе пароля на странице регистрации
registration_login_button="//a[contains(text(),'Войти')]"       #Кнопка "Войти" на странице регистрации

authorization_header="//h2[contains(text(),'Вход')]"        #Заголовок страницы авторизации
authorization_email_input="//input[@name='name']"       #Поле для ввода логина/email на странице авторизации
authorization_password_input="//input[@name='Пароль']"      #Поле для ввода пароля на странице авторизации
authorization_login_button="//button[contains(text(),'Войти')]"     #Кнопка "Войти" на странице авторизации

recovery_header="//h2[contains(text(),'Восстановление пароля')]"      #Заголовок страницы восстановления пароля
recovery_email_input="//input[@name='name']"        #Поле для ввода email на странице восстановления пароля
recovery_recover_button="//button[contains(text(),'Восстановить')]"     #Кнопка "Восстановить" на странице восстановления пароля
recovery_login_button="//a[contains(text(),'Войти')]"       #Кнопка "Войти" на странице восстановления пароля

profile_header="//a[contains(text(),'Профиль')]"        #Заголовок страницы личного кабинета
profile_name_input= "//label[contains(text(),'Имя')]/following-sibling::input"      #Поле для ввода имени на странице личного кабинета
profile_login_input= "//label[contains(text(),'Логин')]/following-sibling::input"       #Поле для ввода логина/email на странице личного кабинета
profile_password_input= "//label[contains(text(),'Пароль')]/following-sibling::input"       #Поле для ввода пароля на странице личного кабинета
profile_exit_button="//button[contains(text(),'Выход')]"        # #Кнопка "Выход" на странице личного кабинета

constructor_bread=".//span[text()='Булки']/parent::*"     #Вкладка "Булки" на главной странице
constructor_sauces=".//span[text()='Соусы']/parent::*"        #Вкладка "Соусы" главной странице
constructor_fillings=".//span[text()='Начинки']/parent::*"        #Вкладка "Начинки" главной странице
