# kimostore-stock-notifier

Checks every ~10 minutes whether the [Onikuma B2 headset](https://kimostore.net/products/onikuma-b2-bluetooth-wireless-wired-gaming-headset-black) is in stock on kimostore.net and sends a push notification via [ntfy](https://ntfy.sh) when it is.

- The ntfy topic is stored in the `NTFY_TOPIC` repo secret.
- After sending the notification, the workflow disables itself. Re-enable it from the Actions tab to keep watching.
- GitHub pauses scheduled workflows after 60 days of repo inactivity; re-enable from the Actions tab if that happens.
