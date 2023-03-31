class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:       
    def create_link_list(self):
        inp_string = str(input("Enter nodes as eg 1 2 3 seprated with spaces"))
        list_of_inputs = inp_string.strip().split(" ")

        try:
            list_of_inputs = list(map(int, list_of_inputs))
        except Exception as e:
            raise ValueError("Type mismatch required int ", e)
        
        head = Node(list_of_inputs[0])
        current = head
        for i in range(1, len(list_of_inputs)):
            temp = Node(list_of_inputs[i])
            current.next = temp
            current = temp
        self.print_list(head)


    def add_node_at_index(self):
        pass


    def del_node_at_index(self):
        pass


    def print_list(self, head):
        temp = head
        while temp!=None:
            print(f"[{temp.data}]", end=" --> ")
            temp = temp.next
        print("None")


    def main(self):
        print("Enter the choice")

        choices = [
            'Create Link List',
            'Enter at index',
            'Delete at index',
            'Exit',
        ]
        
        methods = [
            self.create_link_list,
            self.add_head,
            self.del_head,
        ]
        
        for i, choice in enumerate(choices):
            print(f"Enter {i} for {choice}")
            
        while True:
            choice_entered = int(input("Enter choice"))
            if choice_entered == len(choices)-1:
                break
            else:
                methods[choice_entered]()

            



if __name__=="__main__":
    obj = LinkList()
    # obj.create_link_list()    
    obj.main()