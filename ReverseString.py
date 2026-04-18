
from typing import Reversible


originalStr = "MADAM";

print("Reverse String: ",originalStr[::-1]);


palindroneStr = originalStr[::-1];

if (originalStr == palindroneStr):
    print("Its a Palindrome.."+originalStr);
else:
    print("Its Not a Palindrome.."+originalStr);

