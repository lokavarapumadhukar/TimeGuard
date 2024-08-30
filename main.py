import streamlit as st
from urlblocker import URLBlocker


def main():
    """
    Main function to run the Streamlit app for managing URL blocking and unblocking.
    """

    # Instantiate Clear object to manage host entries
    clear_instance = URLBlocker()

    # Path to the hosts file, this is for UNIX systems
    hosts_path = "/etc/hosts"

    # Read the current contents of the hosts file
    with open(hosts_path, 'r') as file:
        hosts_content = file.readlines()

    # Display the contents of the hosts file in the console
    for line in hosts_content:
        print(line.strip())

    # Print the path of the hosts file
    print(hosts_path)

    # Streamlit app title
    st.title("TimeGuard")

    # Input field for user to enter a URL to block
    user_input = st.text_input("Enter URL to block")
    ip_address = '127.0.0.1'  # Localhost IP address

    # Block URL when the 'block' button is clicked
    if st.button("Block"):
        clear_instance.add_host_entry(ip_address, user_input)

    # Input field for user to enter a URL to unblock
    user_host = st.text_input("Enter URL to unblock")

    # Input field for user to specify the duration to unblock the URL
    duration_minutes = st.number_input(
        "Enter duration to unblock URL in minutes",
        min_value=0,
        max_value=1200,
        value=0,
        step=1
    )

    # Convert duration from minutes to seconds
    duration_seconds = duration_minutes * 60

    # Unblock URL when the 'unblock' button is clicked
    if st.button("Unblock"):
        clear_instance.unblock_time(user_host, duration_seconds)


# Entry point to run the script
if __name__ == '__main__':
    main()
