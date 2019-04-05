from stack import Stack

# Minimum Span problem
def find_span(array):
    span_array = []
    day_stack = Stack()
    for index,day_value in enumerate(array):
        if index ==0:
            day_stack.push(index)
            span_array.append(0)
            continue
        top = array[day_stack.get_top()]
        while day_value > top and not day_stack.is_empty():
            day_stack.pop()
            top = array[day_stack.get_top()]
           
        if not day_stack.is_empty():
            top = day_stack.get_top()
            span_array.append(index - top)
            day_stack.push(index)
            #print("day {} value {} top {}".format(index,day_value,array[top]))
            #print(day_stack)
        else:
            #print("In else for day {} value {}".format(index,day_value))
            span_array.append(0)
            span_array.append(index)
            
    return span_array
            
        


def main():
    print(find_span([100,80,60,70,60,75,85]))
main()
