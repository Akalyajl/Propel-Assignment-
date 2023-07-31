#1.Write a function named sort_odd_even() that will  sort a list of
# numbers with the odd numbers coming first and the even numbers coming second.
# You can use the list.sort function.


def sort_odd_even(list):
    odd_list=[]
    even_list=[]
    for num in list:
        if num%2==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    odd_list.sort()
    even_list.sort()
    new_list=odd_list+even_list
    return new_list
list=[3,2,5,7,6,4,8,9,45,78,73]
sorted_list=sort_odd_even(list)
print(sorted_list)



#2.By using list comprehension, write a program to print the list after removing the
#value 24 in [12,24,35,24,88,120,155].By using list comprehension,
#write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

list = [12, 24, 35, 24, 88, 120, 155]
new_list = [num for num in list if num != 24]
print(new_list)



#3. Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Step 1: Get the input sequence from the user


input_sequence = input("Enter a sequence of comma-separated numbers: ")
numbers = input_sequence.split(',')
odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]
squared_odd_numbers = [num ** 2 for num in odd_numbers]
print("Squared odd numbers:", squared_odd_numbers)


#4.Using list comprehension, return the number of even integers in the given array.

input_sequence = input("Enter a sequence of comma-separated numbers: ")
numbers = input_sequence.split(',')
even_numbers =len([int(num) for num in numbers if int(num) % 2 == 0])
print("the number of even number is: ",even_numbers)

#5.Use filter() to eliminate all words that are shorter than 4 letters from a list of words

words = ["app", "banana", "grape", "kiwi", "orange", "pear"]
def filter_words(word):
    return len(word) >= 4
filtered_words = list(filter(filter_words, words))
print("Words with 4 or more letters:", filtered_words)

#6.Write a list comprehension statement to convert a list of Fahrenheit temperatures to Celsius

fahrenheit_temperatures = [32, 68, 86, 104, 122]
celsius_temperatures = [(temp - 32) * 5/9 for temp in fahrenheit_temperatures]
print("Celsius Temperatures:", celsius_temperatures)


#7.Use map and a lambda function to convert a list of Fahrenheit temperatures
# to a list of Celsius temperatures

fahrenheit_temperatures = [32, 68, 86, 104, 122]
celsius_temperatures = list(map(lambda temp: (temp - 32) * 5/9, fahrenheit_temperatures))
print("Celsius Temperatures:", celsius_temperatures)

#8. Input two lists and convert the two list to dictionary.


keys = ["name", "id", "city"]
values = ["Anc", 110, "tvm"]
my_dict = dict(zip(keys, values))
print("Dictionary:", my_dict)


#9.Make a two-player Rock-Paper-Scissors game. One of the players is the
#computer. 10 chances. Print out the winner and points earned by both players.
# Remember the rules:
#Rock beats scissors Scissors beats paper Paper beats rock

import random

def get_player_choice():
    player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")
        player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().lower()
    return player_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "Player"
    else:
        return "Computer"

def main():
    player_score = 0
    computer_score = 0

    for round in range(1, 11):
        print(f"\nRound {round}:")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chooses: {computer_choice.capitalize()}")
        winner = determine_winner(player_choice, computer_choice)

        if winner == "Player":
            player_score += 1
            print("You win this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    print("\nGame Over!")
    print(f"Player's Points: {player_score}")
    print(f"Computer's Points: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You win the game!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("It's a tie. No overall winner.")

if True:
    main()

#10.Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


input_sequence = input("Enter a sequence of comma-separated numbers: ")
numbers_list = input_sequence.split(',')
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)

#11. Write a program that accepts a comma separated sequence of
# words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
##bag,hello,without,world

input = input("Enter a sequence of words: ")
words_list = input.split(',')
sorted_words_list = so
sorted(words_list)
sorted_sequence = ",".join(sorted_words_list)
print(sorted_sequence)



#12. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010

def is_divisible_by_5(binary):
    decimal = int(binary, 2)
    return decimal % 5 == 0
input_sequence = input("Enter a sequence of  numbers: ")
output_sequence = ",".join(binary for binary in input_sequence.split(',') if is_divisible_by_5(binary))
print(output_sequence)
