import asyncio
import nodriver as uc

async def main():
    browser = await uc.start()
    page = await browser.get('https://www.google.com')

    search_input = await page.select('textarea[name="q"]')
    
    # Type 'multion' into the search field
    await search_input.send_keys("multion")
    
    # Optional: Press Enter to perform the search
    
    search = await page.find('Google Search', best_match=False)
    await search.click()

    content = await page.get_content()
    print(content)



if __name__ == '__main__':
    uc.loop().run_until_complete(main())

