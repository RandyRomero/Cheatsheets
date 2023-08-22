user = {"profile": {"address": {"city": "Moscow"}}}

user_city = user.get("profile", {}).get("address", {}).get("city", "")

print(user_city)
