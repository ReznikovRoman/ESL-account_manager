import main_page.main_page_file
import login_page.loginPage
import email_handler
import registration_page.signup_page
import settings_page.settings_page


# TODO: 1. - Add new form "Forgot Password" --> 1) send verification code by email -> 2) user enters code
#  and creates new password

# TODO: 2. - Use MySQL db to store users' passwords and emails

# TODO: 3. - Add button/slider in Settings: "Signal's volume --> "100%, 75%, 50%, 25%, 0%"


# TODO: (Optional) - Learn about Machine learning and AI in Python
# TODO: Create AI, which will recognize protests topics and main problems there (e.g. - "Opponents don't join us" -->
#                                                                                        --> "Wait for 10 minutes...")


def setup_info():
    file_info = email_handler.get_file_info()
    a_email_handler = email_handler.EmailHandler(file_info)
    a_email = a_email_handler.get_address()
    a_remember_me = a_email_handler.get_remember_me_state()
    a_error = email_handler.get_error(file_info)
    return a_email, a_remember_me, a_error


if __name__ == "__main__":
    email, remember_me, is_error = setup_info()

    if not is_error:
        if not remember_me:
            login_page.loginPage.main()
        else:
            main_page.main_page_file.main()
    else:
        if __name__ == '__main__':
            login_page.loginPage.main()
            # registration_page.signup_page.main()
            settings_ui = settings_page.settings_page.ui
            settings_ui.settings_email_input.setText(email)
