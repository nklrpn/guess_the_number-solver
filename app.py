import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def make_answer(left, right):
    return left + (right - left) // 2

def get_boundaries(left, right, y_val, response):
    if response == 'The required number is greater':
        left = y_val
    elif response == 'The required number is less':
        right = y_val
    return left, right

if __name__ == '__main__':
    url = 'http://guess-the-number.nklrpn.ru/'
    MIN_VALUE, MAX_VALUE = 0, 100

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    y_elem = browser.find_element_by_id('num')
    response = browser.find_element_by_id('output')

    left, right = MIN_VALUE, MAX_VALUE
    y_val, res = None, None
    iter_count = round(math.log2(right)) + 1

    for iter in range(1, iter_count):
        left, right = get_boundaries(left, right, y_val, res)

        y_val = make_answer(left, right)
        y_elem.send_keys(str(y_val) + Keys.RETURN)

        res = response.text
        print(f'{iter}) {y_val} -> {res}')
        if res == 'Congratulations! You got it!':
            break

    browser.quit()
