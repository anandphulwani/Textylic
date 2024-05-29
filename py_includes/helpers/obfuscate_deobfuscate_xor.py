def obfuscate_xor(text, key=0x5A):
    return ''.join(format(ord(char) ^ key, '02x') for char in text)

def deobfuscate_xor(obfuscated_text, key=0x5A):
    # Split the hex string into pairs of characters
    chars = [obfuscated_text[i:i+2] for i in range(0, len(obfuscated_text), 2)]
    return ''.join(chr(int(char, 16) ^ key) for char in chars)

def obfuscate_text_by_lines(text, key=0x5A):
    lines = text.split('\n')
    obfuscated_lines = [obfuscate_xor(line, key) for line in lines]
    return '\n'.join(obfuscated_lines)

def deobfuscate_text_by_lines(obfuscated_text, key=0x5A):
    lines = obfuscated_text.split('\n')
    deobfuscated_lines = [deobfuscate_xor(line, key) for line in lines]
    return '\n'.join(deobfuscated_lines)
