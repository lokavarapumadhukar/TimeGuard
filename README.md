# <span style="color:#007BFF;">TimeGuard</span>

This tool is designed to help manage social media addiction or limit access to any website that you find yourself visiting more frequently than desired. Inspired by the [SelfControl](https://selfcontrolapp.com) project, which blocks a URL for a certain period, this script takes a reverse approach: instead of blocking URLs, it temporarily allows access to certain websites for a predetermined amount of time.

## <span style="color:#007BFF;">How It Works</span>

The script leverages the hosts file—a system file that maps URLs to their associated IP addresses—to control access. While "SelfControl" adds entries to the hosts file to block access to specific websites, this tool does the opposite.

- **Blocked URLs List:** The script maintains a list of blocked URLs.
- **Time-Limited Access:** To access a blocked site, you must specify the amount of time you want to spend on it.
- **Automated Browser Control:** Using Selenium, the script will unblock the site, launch a browser instance, and allow access for the specified time. After this time expires, the browser will automatically close, preventing further access.

This helps users avoid getting caught in endless loops of consuming content by setting a predetermined usage time.

## <span style="color:#007BFF;">Features</span>

- **Streamlit Integration:** The tool uses Streamlit for its user interface, providing a simple and interactive Python-based GUI.
- **Python GUI:** Leveraging Python's simplicity, the GUI allows users to input their desired time on a specific website and manage their online time effectively.

## <span style="color:#007BFF;">Setup</span>

To get started with the script, follow these steps:

1. **Install Required Packages:**

   Ensure all necessary Python packages are installed by running:

   ```bash
   pip install -r requirements.txt

To get started with the script, follow these steps:

2. **Set Up Selenium WebDriver:**

   Make sure you have the Selenium WebDriver set up on your system. You need to fill in two specific lines in your code with the correct paths:

   ```python
   chrome_options.binary_location = os.getenv('CHROME_BINARY', '/default/path/to/chrome')
   service_path = os.getenv('CHROMEDRIVER_PATH', '/default/path/to/chromedriver')

3. **Run the Application**

   Navigate into the TimeBlock directory (the name of the project) and run the following command:

   ```bash
   sudo streamlit run main.py

   Note: The sudo command may be required for permissions to modify the hosts file, which is essential for the tool's functionality.

4. **Potential Customizations**
- You can add this script into the sudoers file so you do not need to type in your password every time.
- You can add a functionality with a website's cookies so when you access sites it has recommendations for you and you do not need to login.
- You can add a max amount of time to unblock if you would like. 
-  Hope this is useful!



https://github.com/user-attachments/assets/ecc6e4c7-38a5-4c16-9ba5-05992c691141

5. **Common Errors**
- The version of the driver is wrong, you can get the correct driver here: https://googlechromelabs.github.io/chrome-for-testing/ ( make sure you select driver )
- sudo xattr -rd com.apple.quarantine ( this is in case that you have a mac and that it doesn't trust the chrome driver)
