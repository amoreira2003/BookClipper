import pyautogui
import time
from PIL import Image

bookName= "Teste"
imageList = []
pages=248

cover = Image.open(r'./cape.png')
imgsaver = cover.convert("RGB")

def Clip(x):
    pageScreenShot=pyautogui.screenshot(region=(874,203, 873, 1167))
    pageScreenShot.save(r'./cache/'+str(x+1)+'.png')
    print("Clipping Page "+str(x+1))
    pyautogui.click()
    pyautogui.press("down")
    print("Going Down to page "+str(x+2))
    print("Sleeping zzzZzzz")
    time.sleep(0.6)
    print("Back to work")
    
def TransformImageGroupToPDF():
    print("Initiating transformation")
    for x in range(pages+1):
     if x < pages: 
      image = Image.open(r'./cache/'+str(x+1)+'.png')
      timg= image.convert('RGB')
      imageList.append(timg)
     else:
      print("Capturing and Converting Images Finished")
      print("Starting Saving Progress")
      imgsaver.save(r'./export/'+str(bookName)+'.pdf',save_all=True, 
      append_images=imageList)
      print("Book Clipped Successfully")
      break


time.sleep(2)
for x in range(pages+1):
    if x < pages: Clip(x)
    else:
        print("Clipping Finished")
        TransformImageGroupToPDF()
        break
          
        
  



