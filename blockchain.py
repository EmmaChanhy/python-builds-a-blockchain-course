blockchain = []


def get_last_blockchain_value():
    # len = length
    if len(blockchain) < 1:
    # None tells your program, there's nothing
        return None
    # else is not needed here, 'cause if None is fulfilled, below line skips
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')


print('Done!')