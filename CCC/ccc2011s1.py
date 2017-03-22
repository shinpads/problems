def main():
    n = int(input())
    text = ""
    for i in range(n):
        text += (input())
    
    if text.count('T') + text.count('t') <= text.count('s') + text.count('S'):
        print("French")
    else:
        print("English")
main()
