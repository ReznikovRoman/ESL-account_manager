import app_account_manager.main_page.main_page_file
import app_account_manager.login_page.loginPage
import app_account_manager.email_handler
import app_account_manager.registration_page.signup_page


def setup_info():
    file_info = app_account_manager.email_handler.get_file_info()
    a_email_handler = app_account_manager.email_handler.EmailHandler(file_info)
    a_email = a_email_handler.get_address()
    a_remember_me = a_email_handler.get_remember_me_state()
    a_error = app_account_manager.email_handler.get_error(file_info)
    return a_email, a_remember_me, a_error


if __name__ == "__main__":
    email, remember_me, is_error = setup_info()

    if not is_error:
        if not remember_me:
            app_account_manager.login_page.loginPage.main()
        else:
            app_account_manager.main_page.main_page_file.main()
    else:
        if __name__ == '__main__':
            app_account_manager.registration_page.signup_page.main()
