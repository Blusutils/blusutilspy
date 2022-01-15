import selenium, os
from selenium import webdriver
#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#browser.get('https://vk.com/rouc.main')
#assert 'RouC ' in browser.title
#comment_btn = webdriver.common.by.By.CSS_SELECTOR = '.comment'
#webdriver.common.touch_actions.TouchActions(browser).tap(comment_btn[0])
#comment = browser.find_element(webdriver.common.by.By.CSS_SELECTOR, '.reply_field')
#comment.send_keys('Комментарий'+webdriver.common.keys.Keys.RETURN)
#browser.quit()
class Browser(webdriver.Chrome):
    def __init__(self, *, url: str = None) -> None:
        super.__init__(executable_path=f'chromedriver.exe')
        self.url = url

    def open(self, *, url: str = None) -> None:
        self.get(url if url else self.url if self.url else None)

    def close(self) -> None:
        self.quit()