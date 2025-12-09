"""
Created on Sun Dec  07 20:30:33 (GMT: +00:00 ) 2025

@author: ram86
"""
import hashlib
def main():
    inp = 'abcdefg'
    ans = 1
    to_md5 = inp + str(ans)
    md5 = hashlib.md5(to_md5.encode('utf-8')).hexdigest()
    print(f"The hash is {md5}")
    while md5[:6] != "000000":
        ans += 1
        to_md5 = inp + str(ans)
        md5 = hashlib.md5(to_md5.encode('utf-8')).hexdigest()
    
    print(f"The answer is {ans}")

main()
