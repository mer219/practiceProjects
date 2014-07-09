"""This module provides functionality to evaluate the "Collatz conjecture"""


class Collatz:
    """This is the main class for the Collatz module"""

    def __init__(self):
        self.number_of_iterations = 0
        self.intermediary_results = []

    def evaluate_conjecture(self, number_to_evaluate):
        """This is the main logic function to process the collatz conjecture"""
        result = 0
        while int(number_to_evaluate) > 1:
            self.number_of_iterations += 1
            if self.number_is_odd(number_to_evaluate):
                result = self.perform_odd_processing(number_to_evaluate)
            else:
                result = self.perform_even_processing(number_to_evaluate)
            self.intermediary_results.append(result)
            number_to_evaluate = result

    @staticmethod
    def number_is_odd(input_number):
        """determine if a number is odd"""
        remainder = int(input_number) % 2
        return remainder

    @staticmethod
    def perform_odd_processing(input_number):
        """multiply the input by three and add one"""
        result = 3 * int(input_number) + 1
        return result

    @staticmethod
    def perform_even_processing(input_number):
        """divide by two"""
        result = int(input_number) // 2
        return result

    def get_number_of_iterations(self):
        """a getter for number_of_iterations"""
        return self.number_of_iterations

    def print_intermediary_results(self):
        """a printer for the steps to get to 1 from the original number"""
        output_string = ""
        string_counter = 0
        for i in range(0, (self.number_of_iterations)):
            output_string = output_string + str(self.intermediary_results[i])
            if i != (self.number_of_iterations - 1):
                output_string = output_string + ", "
            string_counter += 1
            if string_counter == 10:
                print(output_string)
                output_string = ""
                string_counter = 0
        if string_counter > 0:
            print(output_string)
