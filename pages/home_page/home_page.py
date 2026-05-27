from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import locators


class HomePage(BasePage):

    def new_item_click(self):
        self._element_is_clickable((By.XPATH, "//a[@href='/view/all/newJob']")).click()

    def get_project_names_list(self):
        project_elements = self.driver.find_elements(
            By.CLASS_NAME, "jenkins-table__link"
        )
        project_names = [element.text for element in project_elements]

        return project_names

    def schedule_build_click(self, job_name: str):
        self.driver.find_element(
            By.XPATH, f"//tr/td[7]//a[@tooltip='Schedule a Build for {job_name}']"
        ).click()

        return self

    def get_names_jobs_list_build_queue(self) -> list:
        list_elements = self.driver.find_elements(
            By.XPATH,
            f" //div[@class='pane-content']//tr/td/a[@class='model-link inside tl-tr']",
        )
        return [name_job.text for name_job in list_elements]

    def get_item_page_by_name(self, name: str):
        self.go_home_page()
        self._element_is_visible(locators.name_item_in_table(name=name)).click()

    def check_invisible_item_in_table(self, name):
        self.go_home_page()
        return self._element_is_not_visible(locators.name_item_in_table(name=name))
