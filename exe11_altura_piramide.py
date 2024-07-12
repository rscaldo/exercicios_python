"""  
our task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

Test your code using the data we've provided.


"""

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("The number must be a positive integer.")
            else:
                return value
        except ValueError:
            print("That's not a valid number. Please enter an integer.")


blocks = get_int('Insira o número de blocos: ')


altura = 0
 
while altura < blocks:
    altura += 1
    blocks = blocks - altura
    print('#' * altura)

#

print("A altura da pirâmide:", altura)