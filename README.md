**Time Block **
This tool is designed to help manage social media addiction or limit access to any website that you find yourself visiting more frequently than desired. Inspired by the "SelfControl" project, which blocks a URL for a certain period, this script takes a reverse approach: instead of blocking URLs, it temporarily allows access to certain websites for a predetermined amount of time.

**How It Works**
The script leverages the hosts file—a system file that maps URLs to their associated IP addresses—to control access. While "SelfControl" adds entries to the hosts file to block access to specific websites, this tool does the opposite.

Blocked URLs List: The script maintains a list of blocked URLs.
Time-Limited Access: To access a blocked site, you must specify the amount of time you want to spend on it.
Automated Browser Control: Using Selenium, the script will unblock the site, launch a browser instance, and allow access for the specified time. After this time expires, the browser will automatically close, preventing further access.
This helps users avoid getting caught in endless loops of consuming content by setting a predetermined usage time.

Features
Streamlit Integration: The tool uses Streamlit for its user interface, providing a simple and interactive Python-based GUI.
Python GUI: Leveraging Python's simplicity, the GUI allows users to input their desired time on a specific website and manage their online time effectively.
Setup
To get started with the script, follow these steps:

Install Required Packages:

Ensure all necessary Python packages are installed by running:

pip install -r requirements.txt

Set Up Selenium WebDriver:

Make sure you have the Selenium WebDriver set up on your system. You need to fill in two specific lines in your code with the correct paths:


chrome_options.binary_location = os.getenv('CHROME_BINARY', '/default/path/to/chrome')
service_path = os.getenv('CHROMEDRIVER_PATH', '/default/path/to/chromedriver')
CHROME_BINARY: This should be set to the path where your Chrome browser is installed.
CHROMEDRIVER_PATH: This should point to where the chromedriver executable is located on your machine.

Run the Application:

Navigate into the TimeBlock directory (the name of the project) and run the following command:

sudo streamlit run main.py
Note: The sudo command may be required for permissions to modify the hosts file, which is essential for the tool's functionality.

Usage Example
Add URLs to Block:



Run the Application:

Launch the Streamlit interface by running the command above.

Configure and Start:

Add the URLs you wish to block to the list in the script's configuration.
Enter the URL you want to access.
Set the duration for how long you want to stay on the site.
Click the button to start the timer and open the site.
The tool will unblock the site, allow access for the specified time, and then automatically close the browser once the time is up.

Additional Notes
Permissions: Modifying the hosts file usually requires elevated privileges (root or administrator access). Ensure you run the script with the necessary permissions.
Cross-Platform Compatibility: The script is designed to work on Unix-based systems (Linux, macOS). For Windows users, please adjust the paths accordingly.
Disclaimer
Use this tool responsibly to manage your online time effectively. This script is provided "as-is" without warranty of any kind, and its usage is solely at your own risk.

