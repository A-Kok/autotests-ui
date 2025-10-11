from playwright.sync_api import sync_playwright, Request, Response

def log_request(req: Request):
    print(f'Request: {req.url}')

def log_response(res: Response):
    print(f'Response: {res.url}, {res.status_text}, {res.status}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()

    page.on('request', log_request)
    page.on('response', log_response)

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.remove_listener('request', log_request)

    # page.wait_for_timeout(5000)