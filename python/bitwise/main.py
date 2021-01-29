
def main():
    num = 256 * 256
    for i in range(49):
        num = num ^ 55 
    return f'{num:016b}'

print(main())
