import allure
from allure_commons.types import AttachmentType
from selene import Browser


def add_screenshot(browser: Browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser: Browser):
    try:
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    except Exception as exc:
        print(exc)
        log = "Драйвер браузера не содержит метод получения логов"
    allure.attach(body=log, name='browser_log', attachment_type=AttachmentType.TEXT, extension='.log')


def add_html(browser: Browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=AttachmentType.HTML, extension='.html')


def add_video(browser: Browser):
    video_url = f"https://selenoid.autotests.cloud/video/{browser.driver.session_id}.mp4"
    html = f"<html><body><video width='100%' height='100%' controls autoplay><source src='{video_url}' type='video/mp4'></video></body></html>"
    allure.attach(body=html, name=f"video_{browser.driver.session_id}", attachment_type=AttachmentType.HTML, extension='.html')
