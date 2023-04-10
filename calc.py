# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def devide(x, y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit\n1: plus, 2: subtract, 3: multiply, 4: devide:  ")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))

        elif check == 2:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", subtract(x,y))  #"2" 입력 시 곱셈

        elif check == 3:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", multiply(x,y)) #"3" 입력 시 나눗셈
            
        elif check == 4:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            if y == 0:
                print(" 분모가 0이면 계산할 수 없습니다.") #분모 "0" 입력 차단
            else:
                print("answer : ", devide(x,y)) #"4" 입력 시 곱
        elif check > 4:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
