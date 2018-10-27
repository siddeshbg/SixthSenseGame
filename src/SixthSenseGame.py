import random

class Boxes:
    box = [0, 0, 0, 0, 0, 0]
    denominations = [10, 100, 1000, 10000, 100000, 1000000]

    def initialize(self):
        addressed_box_numbers = []

        for x in range(6):
            while True:
                num = self.get_random_number()
                if num not in addressed_box_numbers:
                    addressed_box_numbers.append(num)
                    self.box[x] = self.denominations[num]
                    num = self.get_random_number()
                    break

    def get_random_number(self):
        return random.randint(0, 5)


    def play(self):
        unlocked_boxes = []
        print("Box to unlock ???")

        while len(unlocked_boxes) < 6:
            print("Boxes to choose")
            if len(unlocked_boxes) == 0:
                print("*" * 40)
                for x in range(1, 7):
                    print("BOX-%s|" % x, end='')
                print()
                print("*" * 40)
            else:
                print("*" * 40)
                for x in range(1, 7):
                    if x not in unlocked_boxes:
                        print("BOX %s|" % x, end=' ')
                print()
                print("*" * 40)
            while True:
                your_choice = input("\nBOX? ")
                if int(your_choice) not in unlocked_boxes:
                    break
                else:
                    print("You have already unlocked this box. Choose again..")

            unlocked_boxes.append(int(your_choice))

            print("You lost : %d" % self.box[int(your_choice) - 1])

            if len(unlocked_boxes) == 5:
                for x in range(1, 7):
                    if x not in unlocked_boxes:
                        print("You won: %d" % self.box[x-1])
                break

