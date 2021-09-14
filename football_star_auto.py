import pyautogui
import time


if __name__ == "__main__":
    #screenWidth, screenHeight = pyautogui.size() 
    #print("scrwidth:{}-scrheight:{}".format(screenWidth, screenHeight))

    ############################### way 1 to move and click ################
    pyautogui.moveTo(280, 750) 
    pyautogui.click() 
    time.sleep(2)


    #######################   2  ####################################
    def ball_check():
        im = pyautogui.screenshot()
        #for i in range(320, 600, 5):
            #r, g, b = im.getpixel((425, i))
            #if r == g == b == 255:
                #return True
            #r, g, b = im.getpixel((430, i+10))
            #r2, g2, b2 = im.getpixel((425, i))
            #if (r2 > 250) & (g2 > 250) & (b2 > 250) & (b > 100)
                #return True
        #return False
        for i in range(420, 435):
        	if (im.getpixel((i, 609)) == (114, 136, 5)):
        		return True
        return False

############3
    while(1):
        if(ball_check()):
            pyautogui.press('space')
            time.sleep(.05)
  
        


        