import nodriver as uc
import time

async def main():
    start_time = time.time()

    browser = await uc.start(sandbox=False, headless=True)
    page = await browser.get('https://www.google.com')

    search_input = await page.select('textarea[name="q"]')
    await search_input.send_keys("multion")

    search = await page.find('Google Search', best_match=False)
    await search.click()

    content = await page.get_content()
    print(content)

    if 'We are a technology and design group' in content:
        print("success")
    else:
        print("blocked")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    uc.loop().run_until_complete(main())

