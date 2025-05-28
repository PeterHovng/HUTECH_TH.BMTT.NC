from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(self.alphabet)

    def encrypt_text(self, text: str, key: int) -> str:
        encrypted_text = []
        try:
            key = int(key)  # Đảm bảo key là số nguyên
            for letter in text:
                if letter.upper() in self.alphabet:  # Kiểm tra chữ hoa trong bảng chữ cái
                    letter_index = self.alphabet.index(letter.upper())
                    output_index = (letter_index + key) % self.alphabet_len
                    output_letter = self.alphabet[output_index]
                    encrypted_text.append(output_letter if letter.isupper() else output_letter.lower())
                else:
                    encrypted_text.append(letter)  # Giữ nguyên dấu câu và khoảng trắng
        except ValueError as e:
            return f"Lỗi: {e}"
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        decrypted_text = []
        try:
            key = int(key)  # Đảm bảo key là số nguyên
            for letter in text:
                if letter.upper() in self.alphabet:
                    letter_index = self.alphabet.index(letter.upper())
                    output_index = (letter_index - key) % self.alphabet_len
                    output_letter = self.alphabet[output_index]
                    decrypted_text.append(output_letter if letter.isupper() else output_letter.lower())
                else:
                    decrypted_text.append(letter)
        except ValueError as e:
            return f"Lỗi: {e}"
        return "".join(decrypted_text)
