from playwright.sync_api import  sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

try:
    page.goto("https://www.saucedemo.com/", timeout=5000) #открыть браузер
    page.fill("#user-name", "Stepanova") #ввести логин
    page.fill("#password", "123") #ввести пароль
    #page.press("#user-name", "Enter")
    page.click("#login-button") #кликнуть по кнопке
    page.wait_for_timeout(5000) #таймаут 5 сек

    #проверка, если в тексте появится элемент "error"
    if page.wait_for_selector("#login_button_container > div > form > div.error-message-container.error > h3", timeout=2000):
        print("OK")
    else:
        print("NO")

except Exception as e:
    print(f"ошибка {e}")

finally:
    browser.close()
    playwright.stop()



