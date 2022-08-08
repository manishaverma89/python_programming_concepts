from list_operations_oop import list_operations

numbers_list = [2,4,6,7]
numbers_list2 = [2,3,4]

list_operation_object = list_operations()
list_operation_object.average_finder_of_list(numbers_list)
list_operation_object.largest_number_finder(numbers_list)
list_operation_object.smallest_number_finder(numbers_list)

list_operation_object2 =list_operations(numbers_list2)
list_operation_object2.average_finder_testing()
list_operation_object2.largest_number_testing()

