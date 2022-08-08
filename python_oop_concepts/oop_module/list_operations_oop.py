class list_operations:
    def __init__(self, mylist=[]) :
        self.my_list = mylist
        
          
    #Average finder function
    def average_finder_of_list(self,merged_list):
        sum = 0
        for number in range(len(merged_list)):
             print(merged_list[number])
             sum = sum + merged_list[number]
        
        print ("Sum of merged list is:", sum)
        print ("Average of merged list is:", sum/len(merged_list))
        
    #End of definiton of average_finder_function


    #function to find largest number from a list
    def largest_number_finder(self, numbers_list):
        largest_number = numbers_list[0]
        for number in range(len(numbers_list)):
            if numbers_list[number] > largest_number:
                largest_number = numbers_list[number]
        print("Largest number is:", largest_number)
    #End of definiton of largest_number_finder
        
    #function to find smallest number from a list
    def smallest_number_finder(self, numbers_list):
        smallest_number = numbers_list[0]
        for number in range(len(numbers_list)):
            if numbers_list[number] < smallest_number:
                smallest_number = numbers_list[number]
        print("Smallest number is:", smallest_number)
    #End of definition of smallest_number_finder
    
    #Average finder function using contructor
    def average_finder_testing(self):
        
        sum = 0
        for number in range(len(self.my_list)):
             print(self.my_list[number])
             sum = sum + self.my_list[number]
        
        print ("Sum of merged list is:", sum)
        print ("Average of merged list is:", sum/len(self.my_list))
    #End of definition of average_finder_testing function done using constructor
    
    #Largest number finder using constructor    
    def largest_number_testing(self):
        largest_number = self.my_list[0]
        for number in range(len(self.my_list)):
            if self.my_list[number] > largest_number:
                largest_number = self.my_list[number]
        print("Largest number is:", largest_number)
    #End of defintion of largest_number_testing function done using constructor
        


