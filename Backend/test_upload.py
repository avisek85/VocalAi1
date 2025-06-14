import requests

url = "http://127.0.0.1:8000/generate-voice/"

# Prepare file and text form data
files = {
    "file": open("test_audio.mp3", "rb")
}
data = {
    "text": "नमस्ते! मेरा नाम अभिषेक है, और मैं आपका नया वॉइस असिस्टेंट हूँ। आप मुझे कभी भी बुला सकते हैं—चाहे मौसम की जानकारी चाहिए हो, रिमाइंडर सेट करना हो, या बस थोड़ा समय बिताना हो। मैं हमेशा आपकी मदद के लिए तैयार हूँ। आपको बस कहना है, 'हे असिस्टेंट!' और मैं तुरंत काम शुरू कर दूंगा। वैसे, आज का दिन काफ़ी अच्छा लग रहा है, तो आइए मिलकर इसे उत्पादक और सकारात्मक बनाते हैं!"
}

# Make POST request
response = requests.post(url, files=files, data=data)

# Output response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
