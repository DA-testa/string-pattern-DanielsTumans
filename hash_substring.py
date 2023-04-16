# python3

def read_input():
   filek = input()
   if filek == "I":
        pattern = input().rstrip()
        text = input().rstrip()
   elif filek == "F":
      bebrik = "./tests/" + "06"
      with open (bebrik, "r") as f:
         pattern = f.readline().rstrip()
         text = f.readline().rstrip()
    
    
   return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    result = []
    p = 10**9+7
    x=263
    patternlength = len(pattern)
    textlength = len(text)
    pattern_hash = 0
    for i in range(patternlength):
       pattern_hash = (pattern_hash * x * ord(pattern[i])) % p
    text_hash = 0
    for i in range(patternlength):
        text_hash = (text_hash * x * ord(text[i])) % p
    if pattern_hash == text_hash and pattern == text[:patternlength]:
        result.append(0)
    x_pow = pow(x, patternlength -1, p)
    for i in range(patternlength, textlength):
        text_hash = (text_hash - ord(text[i-patternlength]) * x_pow) % p
        text_hash = (text_hash * x + ord(text[i])) % p
        if pattern_hash == text_hash and pattern == text[i - p_len + 1:i + 1]:
            result.append(i - p_len + 1)
    
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

