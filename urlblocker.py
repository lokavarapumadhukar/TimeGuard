import re
from selenium_browser import SeleniumController
import streamlit as st


class URLBlocker:
    """
    A class to manage URL blocking and unblocking by modifying the system hosts file.
    """

    def __init__(self):
        # Path to the hosts file
        self.hosts_path = "/etc/hosts"

    def validate_ip(self, ip):
        """
        Validate if the given IP address is in a correct format.
        """
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return pattern.match(ip) is not None

    def validate_hostname(self, hostname):
        """
        Validate if the given hostname is in a correct format.
        """
        pattern = re.compile(r"^[a-zA-Z0-9.-]+$")
        return pattern.match(hostname) is not None

    def add_host_entry(self, ip_address, hostname):
        """
        Add a hostname to the hosts file to block it, given an IP address.
        """
        # Validate the IP address and hostname
        if not self.validate_ip(ip_address):
            print("Invalid IP address format.")
            return
        if not self.validate_hostname(hostname):
            print("Invalid hostname format.")
            return

        # Create entry with the www prefix
        hostname_with_www = f"www.{hostname}"
        entry = f"{ip_address} {hostname_with_www}\n"

        # Attempt to add the entry to the hosts file
        try:
            with open(self.hosts_path, 'a') as file:
                file.write(entry)
            print(f"Added entry: {entry.strip()}")
            st.text(f"Added entry: {entry.strip()}")
        except PermissionError:
            print("Permission denied: Run the script with administrator/root privileges.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_host_entry(self, hostname):
        """
        Remove a hostname from the hosts file to unblock it.
        """
        try:
            # Read the current contents of the hosts file
            with open(self.hosts_path, 'r') as file:
                lines = file.readlines()

            # Rewrite the hosts file without the blocked hostname
            with open(self.hosts_path, 'w') as file:
                removed = False
                for line in lines:
                    if not line.strip().endswith(hostname):
                        file.write(line)
                    else:
                        removed = True

                if removed:
                    print(f"Removed entry for hostname: {hostname}")
                    st.text(f"Removed entry for hostname: {hostname}")
                else:
                    print(f"No entry found for hostname: {hostname}")

        except PermissionError:
            print("Permission denied: Run the script with administrator/root privileges.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def unblock_time(self, hostname, time_to_unblock):
        """
        Unblock a hostname for a specified amount of time before blocking it again.
        Launch a browser instance to navigate to the URL during the unblock period.
        """
        while True:
            # Remove the hostname from the hosts file
            self.remove_host_entry(hostname)

            # Create a new browser instance to navigate to the URL
            selenium_instance = SeleniumController()
            temp_hostname = hostname

            # Ensure the URL is properly formatted with HTTP
            if 'http://' not in hostname:
                hostname = 'http://' + hostname

            selenium_instance.createInstance(hostname, time_to_unblock)

            # Block the hostname again after the specified time
            self.add_host_entry('127.0.0.1', temp_hostname)
            break
