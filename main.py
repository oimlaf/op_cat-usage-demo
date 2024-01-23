import bitcoin


# Abstract functions
def OP_CAT(data1: bytes, data2: bytes) -> bytes:
    return data1+data2


def op_cat_example(data1: bytes, data2: bytes) -> bytes:
    return OP_CAT(data1, data2)


def no_op_cat_example(data1: bytes, data2: bytes) -> bytes:
    combined_data = b""
    for byte in data1:
        combined_data += byte
    for byte in data2:
        combined_data += byte
    return combined_data


# Suppose we have two public keys
pubkey1 = bytes.fromhex('pub_key_1_hex_format')
pubkey2 = bytes.fromhex('pub_key_2_hex_format')

op_cat_example(pubkey1, pubkey2)
no_op_cat_example(pubkey1, pubkey2)


# More examples

# Without OP_CAT: Use OP_SIZE, OP_SPLIT, OP_DROP and OP_CAT operations for key concatenation
multisig_script_1 = script.compile([
    pubkey1,
    pubkey2,
    bitcoin.OP_SIZE,
    33,  # Длина публичного ключа
    bitcoin.OP_SPLIT,
    bitcoin.OP_DROP,
    2,
    bitcoin.OP_CHECKMULTISIG
])

# Using OP_CAT: Concatenating keys with OP_CAT
multisig_script_2 = script.compile([
    pubkey1,
    pubkey2,
    bitcoin.OP_CAT,
    2,
    bitcoin.OP_CHECKMULTISIG
])
