import time


def test_existence_of_button(browser):
    # get link
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # for visual test
    # time.sleep(10)

    # find button 'add to basket'
    buttons = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))

    assert buttons == 1, f"Error! Should be one button 'Add to basket'. {buttons} buttons were found"
