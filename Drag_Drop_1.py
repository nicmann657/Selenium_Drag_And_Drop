import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_DragAndDrop():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    driver.get('https://qavbox.github.io/demo/')
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)
    driver.fullscreen_window()


    driver.find_element(By.XPATH,'//*[contains(text(),"DragnDrop")]').click()
    print("\n",f"Current Page URL: {driver.current_url}")
    drag = driver.find_element(By.ID,'draggable')
    drop = driver.find_element(By.ID, 'droppable')
    time.sleep(2)
    actions.drag_and_drop(drag,drop).perform()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'dropText')))
    driver.save_screenshot("/Users/nicolas/Desktop/Sauce_Lab_Selenium/screenshot.png")

    assert 'Dropped!' in drop.text


    driver.quit()

if __name__ == "__main__":
    test_DragAndDrop()