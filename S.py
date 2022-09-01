N=input().split(",")
dict_N={"count":count_N,"list":list_N}
user_input=input()
count=0
def choosefunction(user_input()):
    if user_input=="count":
        print(dict_N[user_input])
    elif user_input=="list":
        print(dict_N[user_input])
def count_N(N):
     for i in N:
         count+=1
         print("count" ,count)
         exit()
def sort_n(count):
    for i in range(count):
        for l in range(i, count):
            if N[i] > N[l]:
                N[i],N[l] = N[l], N[i]
                print(N)
                exit()
def guessfunction():
    while choosefunction(user_input):


