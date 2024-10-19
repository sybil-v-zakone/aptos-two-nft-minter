from aptos_sdk.account_address import AccountAddress

PRIVATE_KEYS_FILE_PATH: str = "data/private_keys.txt"
TRANSACTION_MODULE: str = "0x96c192a4e3c529f0f6b3567f1281676012ce65ba4bb0a9b20b46dec4e371cccd::unmanaged_launchpad"
COLLECTION_ID: AccountAddress = AccountAddress.from_str(
    "0xd42cd397c41a62eaf03e83ad0324ff6822178a3e40aa596c4b9930561d4753e5"
)
APTOS_EXPLORER_URL: str = "https://explorer.aptoslabs.com/txn/"
