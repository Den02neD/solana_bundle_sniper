import requests, time

def bundle_sniper():
    print("Solana Jito bundle sniper - catching new tokens before confirm")
    seen = set()
    while True:
        r = requests.get("https://bundles-api-rest.jito.wtf/bundle/new_bundles")
        for bundle in r.json().get("bundles", []):
            for tx in bundle.get("transactions", []):
                mint = tx.get("mint")
                if not mint or mint in seen: continue
                seen.add(mint)
                print(f"BUNDLE SNIPE!\n"
                      f"New mint: {mint}\n"
                      f"Bundle ID: {bundle['bundle_id']}\n"
                      f"Tip: {bundle['tip']} Jito\n"
                      f"https://solscan.io/token/{mint}\n"
                      f"{'-'*50}")
        time.sleep(1.5)

if __name__ == "__main__":
    bundle_sniper()
