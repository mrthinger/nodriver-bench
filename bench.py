import nodriver as uc
import time


async def main():
    start_time = time.time()

    browser = await uc.start(sandbox=False, headless=True)
    async def googleSearch():
        search_start = time.time()
        page = await browser.get("https://www.google.com")

        search_input = await page.select('textarea[name="q"]')
        await search_input.send_keys("multion")

        search = await page.find("Google Search", best_match=False)
        await search.click()

        await page.get_content()
        search_end = time.time()
        search_time = search_end - search_start
        print(f"Search execution time: {search_time:.2f} seconds")
        return search_time

    total_search_time = 0
    for i in range(100):
        search_time = await googleSearch()
        total_search_time += search_time

    end_time = time.time()
    total_elapsed_time = end_time - start_time
    print(f"Total execution time for 100 searches: {total_elapsed_time:.2f} seconds")
    print(f"Average search time: {total_search_time / 100:.2f} seconds")


if __name__ == "__main__":
    uc.loop().run_until_complete(main())
