import random

# Get the users input and validate to ensure all the algorithm conditions are met
def getUserInput():
    p = g = 0

    checkPrime = False
    while checkPrime == False:
        try:
            # Get P from the users keyboard
            p = int(raw_input("\nPlease enter p: "))

            if p < 0:
                print "p must be greater than or equal to 0"
            else:
                # Check to see if the number provided is a prime number
                if isPrime(p) == False:
                    print p, "is not a prime number. Please try again."
                else:
                    checkPrimitiveRoot = False
                    while checkPrimitiveRoot == False:
                        try:
                            # Get G from the users keyboard
                            g = int(raw_input("\nPlease enter g: "))

                            if g < 0:
                                print "g must be greater than or equal to 0"
                            else:
                                # Check to see if the numbers provided are a primitive root
                                if isPrimitieRoot(g, p) == False:
                                    print g, "is not a primitive root of", p, ". Please try again."
                                else:
                                    checkPrimitiveRoot = True
                                    break
                        except ValueError:
                            print "value entered into g is not valid. Please try again."
                    break
        except:
            print "value entered into p is not valid. Please try again."

    # Get Xa from the users keyboard and validate
    while True:
        try:
            xa = int(raw_input("\nPlease enter Xa: "))

            if xa < 0:
                print "Xa must be greater than or equal to 0"
            elif xa > p:
                print "Xa must be less than p"
            else:
                break
        except ValueError:
            print "value entered into Xa is not valid. Please try again."
    
    # Get Xb from the users keyboard and validate
    while True:
        try:   
            xb = int(raw_input("\nPlease enter Xb: "))

            if xb < 0:
                print "Xb must be greater than or equal to 0"
            elif xb > p:
                print "Xa must be less than b"
            else:
                break
        except ValueError:
            print "value entered into Xb is not valid. Please try again."

    return p, g, xa, xb

# Calculate random numbers for P, G, XA and XB to autorun the algorithm
def calculateRand(min, max):
    isSatisifed = False

    while isSatisifed == False:
        # Generate a random number for P
        p = random.randint(min, max)

        if isPrime(p):
            # Generate a random number for G
            g = random.randint(min, p)
            if isPrimitieRoot(g, p):
                print "p:", p
                print "g: ", g
                isSatisifed = True

    # Generate random numbers for XA and XB
    xa = random.randint(min, p)
    xb = random.randint(min, p)
    return p, g, xa, xb

# Check if number is prime
def isPrime (n):
    # Loop from 2 to input
    for x in range(2, n):
        if (n % x == 0):
            return False
    return True

#Check to see if number is a primitive root
def isPrimitieRoot(g, p):
    # Create a list of numbers from 1 to p
    numbers = list(range(1, p))

    for n in range(1, p):
        # Calculate g^n % p
        val = (g ** n) % p
        
        # Loop to see if every number 1 to p is in the list
        for x in range(0, len(numbers)):
            if val == numbers[x]:
                numbers.remove(val)
                break

    # If no numbers remain then the number is a primitive root
    if len(numbers) > 0:
        return False
    
    return True

# Get the bit representation from a whole number input
def getBit (b, bit):
    return (b & (1 << bit)) >> bit

# Calculate a^b mod n using the Square and Multiply algorithm
def squareMulti ( a, b, n ):
    d = 1
    bits = 64 # Support for upto 64bit calculation
    # Loop in reverse order to calculate the bits
    for bit in range (bits, -1, -1):
        # Check to see if the bit is 1 or 0
        if(getBit(b, bit) == 1):
            d = (d * d * a) % n
        else:
            d = (d * d) % n
    return d

while True:
    # Declare and initialise the variables need for the algorithm
    p = g = xa = xb = 0

    try:
        # Get the users selection from the users keyboard
        input_mode = int(raw_input(">> Enter '1' for Manual Input\n>> Enter '2' for Random Numbers\n>> Enter '3' to Exit\n\nPlease enter your choice: "))
        if input_mode == 1 :
            # Store the users inputed numbers into their appropriate variables
            p, g, xa, xb = getUserInput()
        elif input_mode == 2:
            # Store the random calculated values into their appropriate variables
            p, g, xa, xb = calculateRand(1, 100)
        elif input_mode == 3:
            # Exit the application
            break
        else:
            print "\n--- Selected choice is invalid. Please try again.\n"

        # Check to see if we are running the program
        if input_mode == 1 or input_mode == 2:
            # Alice sends Ya to Bob
            ya = squareMulti(g, xa, p)

            # Bob sends Yb to Alice
            yb = squareMulti(g, xb, p)

            # Alice computes the shared secret key
            ka = squareMulti(yb, xa, p)

            # Bob computes the shared secret key
            kb = squareMulti(ya, xb, p)

            # Print results
            print "\nA picks", xa, "but does not tell B"
            print "B picks", xb, "but does not tell A"
            print "\nA sends B a computed number", ya
            print "B sends A a computed number", yb
            print "\nA and B compute the shared keys", ka, "AND", kb, "... These should be identical."
            print "\nThe secret key is", ka, "\n"
    except ValueError:
        print "\n--- Selected choice is invalid. Please try again.\n"