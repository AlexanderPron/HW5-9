import time
def time_this(num_runs):
    def my_decor(func):
        def wrapper(num):
            avg_time = 0
            for i in range(num_runs):
                t1= time.time()
                func(num)
                t2= time.time()
                delta = t2 - t1
                avg_time += delta
                print('{} проход: {}'.format(i+1,delta -1))
            avg_time /= num_runs    
            return avg_time -1
        return wrapper
    return my_decor
@time_this(num_runs=10)
def fibo(num):
    rez = [1,2,]
    fibo_num = 2 
    while fibo_num < num:
        fibo_num = rez[len(rez)-1]+ rez[len(rez)-2]
        if fibo_num < num:
            rez.append(fibo_num)
    time.sleep(1)
    return rez

def main():
    print(fibo(10**164))

if __name__ == "__main__":
    main()