def word_to_binary_advanced():
    print("=== ADVANCED BINARY CONVERTER ===")
    print("Converts text to multiple binary formats\n")
    
    # Get input
    text = input("Enter text to convert: ")
    
    print(f"\nOriginal Text: '{text}'")
    print("=" * 50)
    
    # Method 1: 8-bit binary with spaces
    print("\n1. 8-bit Binary (with spaces):")
    binary_spaces = ' '.join(format(ord(char), '08b') for char in text)
    print(binary_spaces)
    
    # Method 2: Continuous binary (no spaces)
    print("\n2. Continuous Binary:")
    binary_continuous = ''.join(format(ord(char), '08b') for char in text)
    print(binary_continuous)
    
    # Method 3: 7-bit binary (standard ASCII)
    print("\n3. 7-bit Binary:")
    binary_7bit = ' '.join(format(ord(char), '07b') for char in text)
    print(binary_7bit)
    
    # Method 4: Hexadecimal representation
    print("\n4. Hexadecimal:")
    hex_representation = ' '.join(format(ord(char), '02X') for char in text)
    print(hex_representation)
    
    # Method 5: Detailed character breakdown
    print("\n5. Character Breakdown:")
    print("-" * 40)
    print("Char | Decimal | Binary     | Hex")
    print("-" * 40)
    
    for char in text:
        decimal = ord(char)
        binary = format(decimal, '08b')
        hex_val = format(decimal, '02X')
        print(f" {char:^3} | {decimal:^7} | {binary} | {hex_val:^3}")

# Run the program
word_to_binary_advanced()
