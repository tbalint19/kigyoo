import curses
import time
import random

screen = curses.initscr()
screen.keypad(1)
hatar = screen.getmaxyx()
m=int(hatar[0]/2)
n=int(hatar[1]/2)

# romlott, tobb palya, rekordtarolas, ujraindul
def menu():

    screen.addstr(m, n, "choose a map")


def createmap() :

    screen.addch(m, n, 'o')
    for a in range(-(m-7), m-7) :
        screen.addch(m+a, n , 'o')
    for a in range(-(n-7), n-7) :
        screen.addch(m, n+a , 'o')
    screen.addch(5, 5, "1")
    screen.addch(2*m-5, 2*n-5, "2")
    screen.addch(5, 2*n-5, "3")
    screen.addch(2*m-5, 5, "4")

def game() :

    screen.nodelay(1)

    fej = [20, 20] # a kigyo a 20,20 pontnal jelenik meg (1,1 - bal felso sarok)
    test = [fej[:]]*5

    screen.border()

    direction = 8 # 6: right, 2: down, 4: left, 8: up - a kigyo felfele indul
    jatek = True
    jokaja = False
    rosszkaja = False
    romlottmegevett = 0
    vege = test[-1][:]

    while jatek :

        while not jokaja :
            q, w = random.randrange(1, hatar[0]-1), random.randrange(1, hatar[1]-1)
            y, x = random.randrange(1, hatar[0]-1), random.randrange(1, hatar[1]-1)
            if screen.inch(y, x) == ord(' '):
                jokaja = True
                screen.addch(y, x, ord('x'))
                screen.addch(q, w, ord('o'))

        if vege not in test :

            screen.addch(vege[0], vege[1], ' ')

        screen.addch(fej[0], fej[1], 'x')

        action = screen.getch()
        if action == curses.KEY_UP and direction != 2 :
            direction = 8
        if action == curses.KEY_DOWN and direction != 8 :
            direction = 2
        if action == curses.KEY_RIGHT and direction != 4 :
            direction = 6
        if action == curses.KEY_LEFT and direction != 6 :
            direction = 4
        if action == curses.KEY_HOME and direction != 3 :
            direction = 7
        if action == curses.KEY_END and direction != 9 :
            direction = 1
        if action == curses.KEY_PPAGE and direction != 1 :
            direction = 9
        if action == curses.KEY_NPAGE and direction != 7 :
            direction = 3



        if direction == 6 :
            fej[1] += 1
        elif direction == 4 :
            fej[1] -= 1
        elif direction == 2 :
            fej[0] += 1
        elif direction == 8 :
            fej[0] -= 1
        elif direction == 7 :
            fej[1] -= 1
            fej[0] -= 1
        elif direction == 1 :
            fej[1] -= 1
            fej[0] += 1
        elif direction == 9 :
            fej[1] += 1
            fej[0] -= 1
        elif direction == 3 :
            fej[1] += 1
            fej[0] += 1


        vege = test[-1]

        for z in range(len(test)-1, 0, -1) :
            test[z] = test[z-1][:]

        test[0] = fej[:]

        if screen.inch(fej[0], fej[1]) != ord(' ') :
            if screen.inch(fej[0], fej[1]) == ord('x') :
                jokaja = False
                test.append(test[-1])
            elif screen.inch(fej[0], fej[1]) == ord('o') :
                jatek = False
            else :
                jatek = False

        screen.move(hatar[0]-1, hatar[1]-1)
        screen.refresh()


        speed = 0.5/len(test)

        if direction == 8 or 2 :

            time.sleep(speed*2)

        else :

            time.sleep(speed)


menu()
createmap()
game()
#highscore()
#again()

curses.endwin()
