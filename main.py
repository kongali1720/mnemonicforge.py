#!/usr/bin/env python3

from eth_account import Account

# Aktifkan fitur Mnemonic HD Wallet yang belum stabil
Account.enable_unaudited_hdwallet_features()

def main():
    print("=== Mnemonic to Private Key Converter ===\n")
    words = input("Enter your mnemonic: ").strip()
    try:
        acct = Account.from_mnemonic(words)
    except Exception as e:
        print(f"Error: {e}")
        return

    print("\nOutput:")
    print(f"Private Key: {acct.key.hex()}")
    print(f"Address    : {acct.address}")

if __name__ == "__main__":
    main()
