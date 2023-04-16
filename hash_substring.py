# python3

def read_input():
   filek = input()
   pattern = ''
   text = ''
   if filek == "I":
        pattern = input().rstrip()
        text = input().rstrip()
   elif filek == "F":
        with open ("tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
   return (pattern, text)
  

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
      result = []
      if len(pattern) > len(text):
         return result
      patternhash = hash(pattern)
      texthash = [hash(text[i:i+len(pattern)]) for i in range(len(text) = len(pattern)+1)]
      for i in range (len(texthash)):
         if patternhash == texthash[i] and text[i:i+len(pattern)] == pattern:
            result.append(i)
      return result
         
         

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

