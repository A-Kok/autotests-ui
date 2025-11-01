import allure


@allure.step("Opening the browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Start browser"):
        ...



@allure.step("Creating a new course with title '{title}'")
def create_new_course(title: str): ...


@allure.step("Closing the browser")
def close_browser(): ...


def test_feature():
    open_browser()
    create_new_course("Playwright")
    create_new_course("Selenium")
    create_new_course("Appium")
    create_new_course("Cypress")
    close_browser()
