import hashlib

with open('top-10000-passwords.txt', 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

with open('known-salts.txt', 'r', encoding='utf-8') as file:
    salts = [line.strip() for line in file]

hashed_words = {
    word: [hashlib.sha1(word.encode()).hexdigest()] for word in words
}

hashed_salted_words = {}
for word in words:
    salted_hashes = []
    for salt in salts:
        salted_words = [salt + word, salt + word + salt, word + salt]
        for salted_word in salted_words:
            hashed_word = hashlib.sha1(salted_word.encode()).hexdigest()
            salted_hashes.append(hashed_word)
    hashed_salted_words[word] = salted_hashes

def crack_sha1_hash(hash, use_salts = False):
    if use_salts:
        for key, hashes in hashed_salted_words.items():
            for h in hashes:
                if h == hash:
                    return key
    else:
        for key, hashes in hashed_words.items():
            for h in hashes:
                if h == hash:
                    return key

    return 'PASSWORD NOT IN DATABASE'
