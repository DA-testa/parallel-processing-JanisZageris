# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    for i, t in enumerate(data):
        free_time, index = heapq.heappop(threads)
        output.append((index, free_time))
        heapq.heappush(threads, (free_time + t, index))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for index, start_time in result:
        print(index, start_time)
    
if __name__ == "__main__":
    main()
