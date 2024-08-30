# <span style="color:#007BFF;">Time Block</span>

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
