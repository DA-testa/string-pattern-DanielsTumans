# python3

def read_input():
    if "I" in input():
        pat=input().strip()
        txt=input().strip()
    else:
        with open("tests/06") as file:
            pat=file.readline().strip()
            txt=file.readline().strip()

    return (pat, txt)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pat, txt):
    ot=[]
    if len(pat) > len(txt):
        return ot

    pat_hash = hash(pat)

    text_hashes = [hash(txt[i:i+len(pat)]) for i in range(len(txt)-len(pat)+1)]

    for i in range(len(text_hashes)):
        if pat_hash == text_hashes[i] and txt[i:i+len(pat)] == pat:
            ot.append(i)

    return ot

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
