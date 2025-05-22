from mnemonic import Mnemonic
from bip44 import Wallet

# Masukkan mnemonic-mu di sini
mnemonic_phrase = "legal winner thank year wave sausage worth useful legal winner thank yellow"

# Gunakan English wordlist
mnemo = Mnemonic("english")

if not mnemo.check(mnemonic_phrase):
    print("Mnemonic tidak valid!")
else:
    # Generate seed dari mnemonic
    seed = mnemo.to_seed(mnemonic_phrase)

    # Buat wallet dari seed
    wallet = Wallet(seed)

    # Dapatkan private key Ethereum dari path m/44'/60'/0'/0/0
    private_key = wallet.get_private_key(account=0)
    address = wallet.get_address(account=0)

    print("Private Key:", private_key)
    print("Address    :", address)
