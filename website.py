from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  # print(response.status_code)
  if response.status_code == 200:
    results[website] = "OK"
    
  else:
    results[website] = "FAILED"

print(results)