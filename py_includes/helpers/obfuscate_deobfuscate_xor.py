def obfuscate_xor(text, key=0x5A):
    return ''.join(chr(ord(char) ^ key) for char in text)

def deobfuscate_xor(obfuscated_text, key=0x5A):
    return ''.join(chr(ord(char) ^ key) for char in obfuscated_text)
