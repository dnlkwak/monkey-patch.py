
import hashlib

h = hashlib.shake_256(b'Nobody inspects the spammish repetition')
hash = h.hexdigest(8)
print(len(hash))
print(hash)