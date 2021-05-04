import urllib
import requests

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    words = bookascii.split()
    #test = sorted([str(word, 'utf-8') for word in words])
    maxlength = len(max(words, key = lambda x: len(x)))
    for i in range(len(words)):
        words[i] += bytes(maxlength - len(words[i]))
    def radix_sort(arr, index):
        length = len(arr)
        positions = [0] * 128
        ans = [0] * length
        for i in range(length):
            ascii_decimal = arr[i][-1 * index]
            positions[ascii_decimal] += 1
        for i in range(1, len(positions)):
            positions[i] += positions[i - 1]
        for i in range(length-1,-1,-1):
            ascii_decimal = arr[i][-1 * index]
            ans[positions[ascii_decimal] - 1] = arr[i]
            positions[ascii_decimal] -= 1
        return ans
    for i in range(1,maxlength + 1):
        words = radix_sort(words,i)
    words = [str(word, 'utf-8').rstrip('\x00') for word in words]
    return words
radix_a_book()