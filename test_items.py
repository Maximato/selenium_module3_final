import time


def test_existence_of_button(browser):
    # get link
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # visual test
    time.sleep(10)

    # find button 'add to basket'
    btn = browser.find_element_by_css_selector("button.btn-add-to-basket")

    assert btn.get_attribute("value") is not None, "Error, empty button value"
