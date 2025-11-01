import re
from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.text import Text
from elements.button import Button
import allure


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "courses-list-toolbar-title-text", "Title")
        self.create_courses_button = Button(page, "courses-list-toolbar-create-course-button", "Create Course")

    @allure.step("Check Courses List Toolbar View Component is visible")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Courses")

        self.create_courses_button.check_visible()

    def click_create_courses_button(self):
        self.create_courses_button.click()
        self.check_current_url(re.compile(r".*/#/courses/create"))
