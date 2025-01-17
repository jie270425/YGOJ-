
linked_list_input = input().strip()
head_index = int(input().strip())


linked_list = eval(linked_list_input)


index_to_node = {}
for idx, (value, next_index) in enumerate(linked_list):
    index_to_node[idx] = next_index


slow = head_index
fast = head_index

while fast != -1 and index_to_node[fast] != -1:
    slow = index_to_node[slow]  
    fast = index_to_node[index_to_node[fast]]  

    if slow == fast:
        print("有环")
        break
else:
    print("无环")
