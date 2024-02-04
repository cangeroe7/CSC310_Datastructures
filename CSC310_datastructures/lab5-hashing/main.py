from MD5 import test_md5
from hashing import hash1
from hashing import hash2

with open("passwords.txt", newline="\n") as file:
    passwords = file.read().split("\n")
    # using sets, since the only thing we're checking for is duplicates, and we don't have to handle these duplicates 
    md5_set, hash1_set, hash2_set = set(), set(), set()
    duplicates_md5 = 0
    duplicates_hash1 = 0
    duplicates_hash2 = 0
    for password in passwords:
        # finding the hash result for all functions
        result_md5 = test_md5(bytes(password, 'utf-8'))
        result_hash1 = hash1(password)
        result_hash2 = hash2(password)

        # check if hash result is a duplicate. If it is we add 1 to the duplicate counter,
        # otherwise we add the value to the set
        if result_md5 in md5_set:
            duplicates_md5 += 1
        else:
            md5_set.add(result_md5)

        if result_hash1 in hash1_set:
            duplicates_hash1 += 1
        else:
            hash1_set.add(result_hash1)

        if result_hash2 in hash2_set:
            duplicates_hash2 += 1
        else:
            hash2_set.add(result_hash2)
        
    print(f"""
Duplicates for MD5: {duplicates_md5}
Duplicates for hash1: {duplicates_hash1}
Duplicates for hash2: {duplicates_hash2}
          """)
    