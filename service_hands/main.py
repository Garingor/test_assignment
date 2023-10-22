import re
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_telephones(url):
    telephones = []
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    driver.implicitly_wait(10)

    try:
        for i in driver.find_elements(By.XPATH, "//button[contains(@class, 'button')]"):
            i.click()
    except:
        pass

    matches = list(
        re.finditer('[>]((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,9}[<]', driver.page_source))  # сотовый номер
    matches.append(
        re.finditer('[>]((8|\+7)[\- ]?)?(\(?\d{5}\)?[\- ]?)?[\d\- ]{5,9}[<]', driver.page_source))  # городской номер

    if len(matches) == 0:
        driver.close()
        driver.quit()
        return matches

    for match in matches:
        try:
            telephones.append(match.group())
        except AttributeError:
            continue

    telephones = list(set(telephones))

    char_remove = [" ", ">", "<", "(", ")", "-"]
    for i in range(len(telephones)):
        for char in char_remove:
            telephones[i] = telephones[i].replace(char, "")
        telephones[i] = telephones[i].replace("+7", "8")

        if len(telephones[i]) == 7:  # Если для номера не указан код города — номер московский
            telephones[i] = "8495" + telephones[i]

    driver.close()
    driver.quit()

    return telephones
