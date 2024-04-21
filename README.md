# SSL Wireless SMS Python Integration

This repository contains a Python script for integrating with the SSL Wireless SMS API. It allows you to send single SMS, bulk SMS, and dynamic SMS messages using SSL Wireless API.

### Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/ssl-wireless-sms-python.git
    cd ssl-wireless-sms-python
    ```

2. Install the required dependencies (make sure you have Python and pip installed):

    ```bash
    pip install requests
    ```

3. Replace `YOUR_API_TOKEN` and `YOUR_SID_KEY` with your actual API token and SID in the `ssl_wireless_sms.py` file.

4. Run the Python script:

    ```bash
    python ssl_wireless_sms.py
    ```

### Example

Here's how to use the SSLWirelessSMS class in your Python code:

```python
from ssl_wireless_sms import SSLWirelessSMS

# Provide your API credentials and domain
api_token = "YOUR_API_TOKEN"
sid = "YOUR_SID_KEY"
domain = "https://smsplus.sslwireless.com"

# Initialize SSLWirelessSMS instance
ssl_wireless_sms = SSLWirelessSMS(api_token, sid, domain)

# Example usage:
phone_number = "88017XXXXXX"
message_body = "Test"
transaction_no = "GENERATE_UNIQUE_TRASACTION_ID"
response_single_sms = ssl_wireless_sms.send_single_sms(phone_number, message_body, transaction_no)
print("Response Single SMS:", response_single_sms)
