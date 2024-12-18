import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set constants
TABS_BEFORE_RESTART = 30  # Number of tabs to open before restarting the browser
DURATION = 5             # Duration to keep each tab open in seconds
WAIT_BEFORE_CLOSE = 50    # Wait time (in seconds) before closing the browser
RUN_TIME = 36000           # Total run time (1 hour) in seconds

# Hardcoded array of links
LINKS = [
    "https://youtu.be/E-Hs3VjvQaM?si=adSK0dOynKKlKRKe",
    "https://youtu.be/9AMtw_4Alfc?si=Gj7e7MDG8uW48jw1",
    "https://youtu.be/zGvxXBKbiFk?si=d-bov72cZXMZJy92",
    "https://youtu.be/LwBNHdcK0Ns?si=GyeTnnEWNzZiHwsS",
    "https://youtu.be/y2k3VudShic?si=hLA-hxdxP4_n9S2j",
    "https://youtu.be/7_QSNs5VZyU?si=100tQ8iy2SgxTz1j",
    "https://youtu.be/UKJNnRBs8H0?si=amM9fQzD-gRYfakv",
    "https://youtu.be/1Z30j6H-1qQ?si=pTKnKXs_bOXp4pKS",
    "https://youtu.be/fVNq_zBjqlU?si=zZmFKRBEAatNRY2h",
    "https://youtu.be/-YedESf5TwE?si=_Gfr2ePMRxt0nfcT"
]

def initialize_browser():
    """Initialize and return a new incognito Chrome browser."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Open Chrome in incognito mode
    options.add_experimental_option("detach", True)  # Keeps browser open
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def open_tabs(driver, links, num_tabs):
    """
    Open tabs in the browser, mute them, and keep them open for the specified duration.
    :param driver: Selenium WebDriver instance
    :param links: List of website URLs to open
    :param num_tabs: Number of tabs to open before closing the browser
    """
    num_links = len(links)  # Get the total number of links
    current_index = 0       # Track the current link index

    for i in range(num_tabs):
        # Get the next link in the array
        website = links[current_index]

        # Open a new tab with the current website
        driver.execute_script(f"window.open('{website}', '_blank');")
        print(f"Opened tab {i+1}: {website}")

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])

        # Mute the tab by executing JavaScript
        driver.execute_script("""
            var media = document.querySelector('video, audio');
            if (media) { media.muted = true; }
        """)
        print(f"Muted tab {i+1}")

        # Keep the tab open for the specified duration
        time.sleep(DURATION)

        # Move to the next link, looping back to the start if at the end
        current_index = (current_index + 1) % num_links

def main():
    start_time = time.time()  # Record the start time
    elapsed_time = 0          # Track elapsed time

    while elapsed_time < RUN_TIME:  # Run for 1 hour
        # Initialize the browser
        print("Starting a new browser session...")
        driver = initialize_browser()

        try:
            # Open the specified number of tabs
            open_tabs(driver, LINKS, TABS_BEFORE_RESTART)

            # Wait before closing the browser
            print(f"Waiting for {WAIT_BEFORE_CLOSE} seconds before closing the browser...")
            time.sleep(WAIT_BEFORE_CLOSE)

        finally:
            # Close the browser to reduce CPU load
            driver.quit()
            print("Closed browser to reduce CPU load.\n")

        # Update elapsed time
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {int(elapsed_time)} seconds\n")

    print("1 hour elapsed. Script completed successfully.")

if __name__ == "__main__":
    main()
