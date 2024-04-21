import requests
import json

class SSLWirelessSMS:
    def __init__(self, api_token, sid, domain):
        self.api_token = api_token
        self.sid = sid
        self.domain = domain

    def send_single_sms(self, phone_number, message_body, transaction_no):
        url = f"{self.domain}/api/v3/send-sms"
        payload = {
            "api_token": self.api_token,
            "sid": self.sid,
            "sms": message_body,
            "msisdn": phone_number,
            "csms_id": transaction_no
        }
        response = requests.post(url, json=payload)
        return response.json()

    def send_bulk_sms(self, phone_numbers, message_body, transaction_no):
        url = f"{self.domain}/api/v3/send-sms/bulk"
        payload = {
            "api_token": self.api_token,
            "sid": self.sid,
            "sms": message_body,
            "msisdn": phone_numbers,
            "batch_csms_id": transaction_no
        }
        response = requests.post(url, json=payload)
        return response.json()

    def send_dynamic_sms(self, message_data):
        url = f"{self.domain}/api/v3/send-sms/dynamic"
        payload = {
            "api_token": self.api_token,
            "sid": self.sid,
            "sms": message_data
        }
        response = requests.post(url, json=payload)
        return response.json()

# Provide your API credentials and domain
api_token = "YOUR_API_TOKEN"
sid = "YOUR_SID_KEY"
domain = "https://smsplus.sslwireless.com"

# Initialize SSLWirelessSMS instance
ssl_wireless_sms = SSLWirelessSMS(api_token, sid, domain)

# Example usage:
# Send single SMS
phone_number = "88017XXXXXX"
message_body = "Test"
transaction_no = "GENERATE_UNIQUE_TRASACTION_ID"
response_single_sms = ssl_wireless_sms.send_single_sms(phone_number, message_body, transaction_no)
print("Response Single SMS:", response_single_sms)

# # Send bulk SMS
# phone_numbers = ["019XXXXXXXX", "018xxxxxxxx"]
# message_body = "Test Message"
# transaction_no = "unique_batch_transaction_id"
# response_bulk_sms = ssl_wireless_sms.send_bulk_sms(phone_numbers, message_body, transaction_no)
# print("Response Bulk SMS:", response_bulk_sms)

# # Send dynamic SMS
# message_data = [
#     {"phone_number": "015XXXXXXXX", "message": "Test Message 1", "sms_id": "unique_sms_id_1"},
#     {"phone_number": "017xxxxxxxx", "message": "Test Message 2", "sms_id": "unique_sms_id_2"}
# ]
# response_dynamic_sms = ssl_wireless_sms.send_dynamic_sms(message_data)
# print("Response Dynamic SMS:", response_dynamic_sms)
