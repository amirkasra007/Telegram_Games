import pyautogui
import time


if __name__ == "__main__":
    screenWidth, screenHeight = pyautogui.size() 
    print("scrwidth:{}-scrheight:{}".format(screenWidth, screenHeight))
    #time.sleep(3)
    #while(1):
    #    im = pyautogui.screenshot()
    #    print("mouse:{}, color:{}".format(pyautogui.position(), im.getpixel(pyautogui.position())))
    #    time.sleep(.1)

    ############################### way 1 to move and click ################
    pyautogui.moveTo(152, 750) 
    pyautogui.click() 
    time.sleep(2)


    #######################   1  ####################################
    #def tree_check(input, start, end):
    #    im = pyautogui.screenshot()
    #    for i in range(start, end, 9):
    #        if (im.getpixel((input, i)) == (161, 116, 56)):
    #            return False
    #    return True


    #def spaces(input):
    #    space = -1
    #    im = pyautogui.screenshot()
    #    for k in range(1, 7):
    #        for i in range(338 - 50*k, 338 - 50*(k-1), 10):
    #            if (im.getpixel((input, i)) == (161, 116, 56)):
    #                space = k - 1
    #                break
    #        if(space != -1):
    #            break
    #    if(space == -1):
    #        space = 6
    #    return space

    #######################   2  ####################################
    def tree_check(input, start, end):
        im = pyautogui.screenshot()
        for i in range(start, end, 10):
            if (im.getpixel((input, i)) == (161, 116, 56)):
                return False
        return True


    def spaces(input):
        space = -1
        im = pyautogui.screenshot()
        for k in range(1, 7):
            for i in range(338 - 50*k, 338 - 50*(k-1), 10):
                if (im.getpixel((input, i)) == (161, 116, 56)):
                    space = k - 1
                    break
            if(space != -1):
                break
        if(space == -1):
            space = 6
        return space


############################# way 1 (max 354) ##########################################3
    #while(1):
    #    if(tree_check(737, 300, 324)):
    #        pyautogui.moveTo(730, 610)
    #        while(1):

    #            for i in range(spaces(737)):
    #                pyautogui.click()

    #            if(tree_check(620, 280, 324)):
    #                pyautogui.moveTo(640, 610)
    #                while(1):
    #                    for i in range(spaces(620)):
    #                        pyautogui.click()

    #                    if((tree_check(737, 280 , 324))):
    #                        pyautogui.moveTo(730, 610)
    #                        break
    #    else:
    #        pyautogui.moveTo(640, 610)
    #        while(1):
    #            for i in range(spaces(737)):
    #                pyautogui.click()

    #            if((tree_check(737, 280 , 324))):
    #                pyautogui.moveTo(730, 610)
    #                while(1):
    #                    for i in range(spaces(620)):
    #                        pyautogui.click()

    #                    if(tree_check(620, 280, 324)):
    #                        pyautogui.moveTo(640, 610)
    #                        break

############################# way 2 (max 358) ##########################################3
    #pyautogui.moveTo(730, 610) ### starting with right area
    pyautogui.press('right')
    while(1):
        for i in range(spaces(737)):
        	pyautogui.press('right')
            #pyautogui.click()

        if(tree_check(620, 260, 324)):  #### to enter left area
            #pyautogui.moveTo(640, 610)
            while(1):
                for i in range(spaces(620)):
                	pyautogui.press('left')
                    #pyautogui.click()

                if(tree_check(737, 260 , 324)):
                    #pyautogui.moveTo(730, 610)
                    break



                
        


        