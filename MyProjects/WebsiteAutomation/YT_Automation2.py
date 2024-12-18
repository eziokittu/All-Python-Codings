import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set constants
TABS_BEFORE_RESTART = 30  # Number of tabs to open before restarting the browser
DURATION = 5             # Duration to keep each tab open in seconds
RUN_TIME = 36000           # Total run time (1 hour) in seconds

def initialize_browser():
    """Initialize and return a new incognito Chrome browser."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Open Chrome in incognito mode
    options.add_experimental_option("detach", True)  # Keeps browser open
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def open_tabs(driver, website, num_tabs):
    """
    Open tabs in the browser, mute them, and keep them open for the specified duration.
    :param driver: Selenium WebDriver instance
    :param website: Website URL to open
    :param num_tabs: Number of tabs to open before closing the browser
    """
    for i in range(num_tabs):
        # Open a new tab with the given website
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

def main():
    # Get user input for website URL
    website = input("Enter the website URL to open in incognito tabs: ")

    start_time = time.time()  # Record the start time
    elapsed_time = 0          # Track elapsed time

    while elapsed_time < RUN_TIME:  # Run for 1 hour
        # Initialize the browser
        print("Starting a new browser session...")
        driver = initialize_browser()

        try:
            # Open the specified number of tabs
            open_tabs(driver, website, TABS_BEFORE_RESTART)
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
