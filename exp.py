import asyncio
import nodriver as uc
import logging


logger = logging.getLogger(__name__)


async def main():
    browser = await uc.start(
        headless=False,
        # sandbox=False,
        browser_args=["--proxy-server=http://127.0.0.1:8080"],
    )

    tab = await browser.get("https://www.expedia.com/", new_tab=True)

    await tab.sleep(5000)

    browser.stop()


if __name__ == "__main__":
    tasks = [main() for _ in range(10)]
    uc.loop().run_until_complete(asyncio.gather(*tasks))
