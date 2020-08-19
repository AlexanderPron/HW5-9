import time
from functools import wraps
class Timer():
    def __init__(self, num_runs):
        self.num_runs = num_runs

    def __enter__(self):
        self.t0= time.time()

    def __call__(self, func):
        @wraps(func) # Нужно для корректного отображения названий декорируемых функций (если не использовать wraps, то func.__name__ всегда будет wrapper)
        def wrapper(*args, **kwargs):
            avg_time = 0
            for i in range(self.num_runs):
                t1= time.time()
                func(*args, **kwargs)
                t2= time.time()
                delta1 = t2 - t1
                avg_time += delta1
                print('{} проход: {}'.format(i+1, delta1))
            avg_time /= self.num_runs    
            return avg_time
        return wrapper

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t4= time.time()
        delta2 = self.t4 - self.t0
        print('{} проходов выполнено за {} секунд'.format(self.num_runs, delta2))


num_runs1 = 10
num_runs2 = 20

@Timer(num_runs1)
def fibo(num):
    rez = [1,2,]
    fibo_num = 2 
    while fibo_num < num:
        fibo_num = rez[len(rez)-1]+ rez[len(rez)-2]
        if fibo_num < num:
            rez.append(fibo_num)
    return rez
@Timer(num_runs2)
def f():
    for _ in range(1000000):
        pass

def main():
    with Timer(num_runs1):
        print('Среднее время выполнения функции {} : {}'.format(fibo.__name__, fibo(10**164)))
    with Timer(num_runs2):
        print('Среднее время выполнения функции {} : {}'.format(f.__name__, f()))

    # print('Среднее время выполнения функции {} : {}'.format(fibo.__name__, fibo(10**164)))
    # print('Среднее время выполнения функции {} : {}'.format(f.__name__, f()))

if __name__ == "__main__":
    main()