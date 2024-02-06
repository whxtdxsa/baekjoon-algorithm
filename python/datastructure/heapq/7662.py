import heapq
import sys

def dual_priority_queue(operations):
    min_heap = []
    max_heap = []
    entry_finder = {}  # 추적용 딕셔너리: 값의 존재 여부를 기록
    counter = 0  # 유효한 요소의 수

    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            num = int(num)
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_finder[num] = entry_finder.get(num, 0) + 1
            counter += 1
        elif op == 'D' and counter > 0:
            if num == '1':
                # 최댓값 삭제
                while max_heap and entry_finder[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder[max_val] -= 1
                    counter -= 1
            elif num == '-1':
                # 최솟값 삭제
                while min_heap and entry_finder[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder[min_val] -= 1
                    counter -= 1

    while min_heap and entry_finder[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_finder[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if counter > 0:
        return f"{-max_heap[0]} {min_heap[0]}\n"
    else:
        return "EMPTY\n"

def main():
    input = sys.stdin.readline
    print = sys.stdout.write

    T = int(input().rstrip())
    operations_list = [[] for _ in range(T)]

    for i in range(T):
        for _ in range(int(input().rstrip())):
            operations_list[i].append(input().rstrip())

    for operations in operations_list:
        print(dual_priority_queue(operations))

if __name__ == "__main__":
    main()