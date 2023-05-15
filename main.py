# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]                   # Inicialize threads ka (brivais laiks, indeks) kortežos
    heapq.heapify(threads)                                 # Konverte listu uz heep

    for i, t in enumerate(data):
        free_time, index = heapq.heappop(threads)          # Atrod threadu ar visagrako brivo laiku
        output.append((index, free_time))
        heapq.heappush(threads, (free_time + t, index))    # Atjaunina threada brivo laiku ar jauno darbu ilgumu

    return output

def main():
    n, m = map(int, input().split())                       # Pirmie divi input
    data = list(map(int, input().split()))                 # Parejais inputs
    result = parallel_processing(n, m, data)
    for index, start_time in result:
        print(index, start_time)
    
if __name__ == "__main__":
    main()
