import pyshorteners
url = input("Enter thr URL: ")
shortener= pyshorteners.Shortener()
shortener_url=shortener.tinyurl.short(url)

print("shortened URL: ",shortener_url)