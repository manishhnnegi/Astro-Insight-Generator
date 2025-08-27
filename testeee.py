import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "name": "Geeta",
    "birth_date": "1995-08-20",
    "birth_time": "03:30",
    "birth_place": "Jaipur, India",
    "language": "Hindi",
}


# data = {
#     "name": "Shureshkumar",
#     "birth_date": "1995-08-20",
#     "birth_time": "14:30",
#     "birth_place": "Jaipur, India",
#     "language": "Hindi",
# }

# data = {
#     "name": "satish",
#     "birth_date": "1995-08-20",
#     "birth_time": "14:30",
#     "birth_place": "Jaipur, India",
#     "language": "Hindi",
# }

response = requests.post(url, json=data)
print(response.json())


# import requests

# url = "http://127.0.0.1:8000/predict"  # Flask default port is 5000, FastAPI default is 8000

# # Test cases
# test_cases = [
#     {
#         "name": "Ritika",
#         "birth_date": "1995-08-20",
#         "birth_time": "14:30",
#         "birth_place": "Jaipur, India",
#         "language": "en",
#     },
#     {
#         "name": "Ritika",
#         "birth_date": "1995-08-20",
#         "birth_time": "14:30",
#         "birth_place": "Jaipur, India",
#         "language": "hi",
#     },
#     {
#         "name": "Ritika",
#         "birth_date": "20-08-1995",  # invalid date
#         "birth_time": "14:30",
#         "birth_place": "Jaipur, India",
#         "language": "en",
#     },
#     {
#         "name": "",  # missing name
#         "birth_date": "1995-08-20",
#         "birth_time": "14:30",
#         "birth_place": "Jaipur, India",
#         "language": "en",
#     },
# ]

# for idx, data in enumerate(test_cases, start=1):
#     response = requests.post(url, json=data)
#     print(f"Test case {idx}:")
#     try:
#         print(response.json())
#     except Exception:
#         print("Error:", response.text)
#     print("-" * 50)
