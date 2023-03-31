import inspect

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

        if inspect.stack()[1].function == "main":
            self.print_list(head=head)
        else:
            return head, len(list_of_inputs)


    def add_node_at_index(self):
        input_link_list, size = self.create_link_list()
        positions = {'0' : 'Head', '-1': 'End','2': "Between"}
        for i in positions:
            print(f"The postions are as {i} for {positions[i]} ")

        choice = int(input("Enter choice"))
        
        if choice == 0:
            head = self._add_head(input_link_list)
            self.print_list(head)
        elif choice ==-1 or choice == size:
            head = self._add_end(input_link_list)
            self.print_list(head)
        else:
            head = self._add_between(input_link_list, size)
            self.print_list(head)


    def _add_head(self, head):
        data = int(input("Enter the head node data."))
        temp = Node(data)
        temp.next = head
        head = temp
        return head


    def _add_between(self, head, size):
        data = int(input("Enter the data"))
        index = int(input("Enter the index"))
        temp = head
        
        if index < 1 and index >size-1:
            raise ValueError(f"Input range not satisifed should be in range [1, {size-1}]")
        
        for i in range(index):
            previous = temp
            temp = temp.next

        new_node = Node(data)
        previous.next = new_node
        new_node.next = temp

        return head


    def _add_end(self, head):
        data = int(input("Enter the data"))
        new_node = Node(data)
        temp = head
        while not temp.next is None:
            temp=temp.next
    
        temp.next = new_node

        return head
        


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
            self.add_node_at_index,
            self.del_node_at_index,
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