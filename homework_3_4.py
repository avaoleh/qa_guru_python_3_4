def replace_name_function(name_func, *args):
    full_name = name_func.__name__.title().replace("_", " ")
    print(full_name, *args)


def open_browser(browser_name):
    replace_name_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    replace_name_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    replace_name_function(find_registration_button_on_login_page, page_url, button_text)


def check_replace_name_function():
    browser_name = 'Chrome'
    page_url = 'https://github.com/'
    button_text = 'Sign up'

    open_browser(browser_name)
    go_to_companyname_homepage(page_url)
    find_registration_button_on_login_page(page_url, button_text)

check_replace_name_function()