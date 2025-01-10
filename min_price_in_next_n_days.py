
# import heapq
# data = [1,5,3,2,8,5]
# heap = []
# for n in data:
#     heapq.heappush(heap, n)
# print(heap)


# while heap:
#     res = heapq.heappop(heap)
#     print("heap:", heap)
#     print("res:", res)


import heapq

def get_min_price(input_list, n):

    if input_list==[]:
        return []

    len_input_list = len(input_list)
    res_list = []
    heap = []
    for i in range(min(n+1, len(input_list))):
        cur = input_list[i]
        heapq.heappush(heap, cur)

    min_to_remove = {}
    cur_min = heapq.heappop(heap)
    res_list.append(cur_min)
    heapq.heappush(heap, cur_min)

    cur = input_list[0]
    if cur==cur_min:
        heapq.heappop(heap)
    else:
        min_to_remove[cur]=1


    for i in range(1, len_input_list):
        # print("i:", i)
        # print("min_to_remove:", min_to_remove)
        i_end = i+n
        if i_end<len_input_list:
            cur = input_list[i_end]
            heapq.heappush(heap, cur)

        cur_min = heapq.heappop(heap)
        
        while cur_min in min_to_remove:
            min_to_remove[cur_min]-=1
            if min_to_remove[cur_min]==0:
                del min_to_remove[cur_min]
            cur_min = heapq.heappop(heap)
            
        # print("cur_min:", cur_min)

        res_list.append(cur_min)
        heapq.heappush(heap, cur_min)

        cur = input_list[i]
        # print("cur:", cur)

        if cur_min==cur:
            heapq.heappop(heap)
            if cur in min_to_remove:
                min_to_remove[cur]-=1
                if min_to_remove[cur]==0:
                    del min_to_remove[cur]

        elif cur_min<cur:
            if cur in min_to_remove:
                min_to_remove[cur]+=1
            else:
                min_to_remove[cur]=1
        else:
            min_to_remove[cur]-=1
            if min_to_remove[cur]==0:
                del min_to_remove[cur]

        # print("min_to_remove:", min_to_remove)
        # print()



    return res_list


def main():
    input_list = [10,9,8,8,4,3,6,7,12,24]
              # "[8, 8,4,3,3,3,6,7,12,24]"
    n = 2
    res_list = get_min_price(input_list, n)
    print("input_list:", input_list)
    print("n:", n)
    print("res_list:", res_list)
    print()


    input_list = [10,9,8,8,4,3,6,7,12,24]
    n = 0
    res_list = get_min_price(input_list, n)
    print("input_list:", input_list)
    print("n:", n)
    print("res_list:", res_list)
    print()


    input_list = [10,9,8]
    n = 2
    res_list = get_min_price(input_list, n)
    print("input_list:", input_list)
    print("n:", n)
    print("res_list:", res_list)
    print()

    input_list = [10,9,8]
    n = 1
    res_list = get_min_price(input_list, n)
    print("input_list:", input_list)
    print("n:", n)
    print("res_list:", res_list)
    print()


if __name__=="__main__":
    main()
    print("\nDone!\n")