def replace_name_function(name_func, *args):
    full_name = name_func.__name__.title().replace("_", " ")
    #print(full_name, *args, sep=' - ')

    print('\n------------------')
    print(f"Name of function: {full_name.replace('_', ' ')} ")
    print('Args:', *args)
    print('------------------')


def process(my_func, *args):

    #Iterate over all args, convert them to str, and join them
    args_str = ', '.join(map(str, args))

    #Form the final representation by adding func name
    print("Name of function: {}; Args: {}".format(my_func.__name__.title().replace("_", " "), ','.join([args_str])))


def open_browser(browser_name):
    process(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    process(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    process(find_registration_button_on_login_page, page_url, button_text)


def check_replace_name_function():
    browser_name = "Chrome"
    page_url = "https://github.com/"
    button_text = "login"

    open_browser(browser_name)
    go_to_companyname_homepage(page_url)
    find_registration_button_on_login_page(page_url, button_text)

check_replace_name_function()