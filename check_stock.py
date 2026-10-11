"""Check a Shopify product's stock and push a notification via ntfy when it's available."""
import json
import os
import sys
import urllib.request

PRODUCT_URL = "https://kimostore.net/products/onikuma-b2-bluetooth-wireless-wired-gaming-headset-black"
NTFY_TOPIC = os.environ["NTFY_TOPIC"]


def fetch_product():
    req = urllib.request.Request(PRODUCT_URL + ".js", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def notify(title, message, priority="urgent"):
    req = urllib.request.Request(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=message.encode(),
        headers={"Title": title, "Priority": priority, "Tags": "headphones", "Click": PRODUCT_URL},
    )
    urllib.request.urlopen(req, timeout=30)


def main():
    if "--test" in sys.argv:
        notify("Test notification", "Stock notifier is set up correctly.", priority="default")
        print("Test notification sent")
        return

    product = fetch_product()
    available = product["available"]
    print(f"{product['title']}: available={available}")

    if available:
        price = product["price"] / 100
        notify("Back in stock!", f"{product['title']} is available for {price:.2f} EGP. Tap to open.")
        print("Notification sent")

    with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"available={str(available).lower()}\n")


if __name__ == "__main__":
    main()
