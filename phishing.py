from __future__ import division
import os,time,sys,traceback
from math import *
from time import sleep

try:
        import curses,requests
except :
        os.system('pip install curses-menu')
        os.system('pip install requests')

#
screen = curses.initscr()
screen.erase()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad( 1 )
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_GREEN)
highlightText = curses.color_pair( 1 )
normalText = curses.A_NORMAL
curses.curs_set( 0 )
h,w=screen.getmaxyx()
strings = [
'WEEMAN','SOCIALFISH',
'BLACKEYE','SHELLPISH','PISH','HIDDENEYE','EVILURL','EXIT']
m = len(strings)

max_row = 10
box = curses.newwin(m+2, 40, h//2-max_row+3,w//2-20) #utama
box1 = curses.newwin(m+4, 44,h//2-max_row+2,w//2-22)
box2= curses.newwin( 4,w,h-4,0) #bawah
box3= curses.newwin(7,w,0,0) #atas

box.box()
box1.box()
box2.box()
box3.box()
title ='[| INSTALLER v.2 |]'
box3.addstr(1,0,' ' *(w),curses.color_pair(2))
box3.addstr(1,(w//2)-(len(title)//2),title)
attributes = {}
attributes['normal'] = curses.color_pair(1)
attributes['highlighted'] = curses.color_pair(2)


def main(screen):
  row_num = len( strings )
  pages = int( ceil( row_num / max_row ) )
  position = 1
  page = 1
  last = row_num + 1

  for i in range( 1, max_row + h//2 ):
    if row_num == 0:
        box.addstr( 1, 1, "Tidak ada menu", highlightText )
    else:
        if (i == position):
            box.addstr( i,20-len(strings[i-1])//2,strings[ i - 1 ], highlightText )
        else:
            box.addstr( i,20-len(strings[i-1])//2,strings[i-1], normalText )
        if i == row_num:
            break
  screen.clear()
  screen.refresh()
  box3.refresh()
  box2.refresh()
  box1.refresh()
  box.refresh()
  x = screen.getch()
  while x != 27:
    if x == curses.KEY_DOWN:
        if page == 1:
            if position < i:
                position = position + 1
            else:
                if pages > 1:
                    page = page + 1
                    position = 1 + ( max_row * ( page - 1 ) )
        elif page == pages:
            if position < row_num:
                position = position + 1
        else:
            if position < max_row + ( max_row * ( page - 1 ) ):
                position = position + 1
            else:
                page = page + 1
                position = 1 + ( max_row * ( page - 1 ) )
    if x == curses.KEY_UP:
        if page == 1:
            if position > 1:
                position = position - 1
        else:
            if position > ( 1 + ( max_row * ( page - 1 ) ) ):
                position = position - 1
            else:
                page = page - 1
                position = max_row + ( max_row * ( page - 1 ) )
    if x == curses.KEY_LEFT:
        if page > 1:
            page = page - 1
            position = 1 + ( max_row * ( page - 1 ) )

    if x == curses.KEY_RIGHT:
        if page < pages:
            page = page + 1
            position = ( 1 + ( max_row * ( page - 1 ) ) )
    if x == ord( "\n" ) and row_num != 0:
        box2.erase()
	box2.border(0)


#  Menu pertama
        if position==1:
	   load()
	   os.system("cd /$HOME && git clone https://github.com/samyoyo/weeman")
   	   screen.clear()
# menu kedua
        if position==2:
           load()
	   os.system("cd /$HOME && git clone https://github.com/UndeadSec/SocialFish.git")
	   screen.clear()
#menu ketiga
        if position==3:
           load()
	   os.system("cd /$HOME && git clone https://github.com/thelinuxchoice/blackeye")
	   screen.clear()
# menu keempat
	if position==4:
           load()
	   os.system("cd /$HOME && git clone https://github.com/thelinuxchoice/shellphish")
	   screen.clear()
# menu kelima
	if position==5:
           load()
	   os.system("cd /$HOME && git clone https://github.com/Cabdulahi/pish")
	   screen.clear()
# menu keenam
	if position==6:
           load()
	   os.system("cd /$HOME && git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git")
	   screen.clear()
# 7
	if position==7:
	   load()
	   os.system("cd /$HOME && git clone https://github.com/UndeadSec/EvilURL.git")
  	   screen.clear()
# menu keluar
	if position==8:
	   break
	   curses.endwin()







#
    box.erase()
    box1.border(0)
    box.border(0)
    box2.border(0)
    box3.border(0)
    screen.refresh()
    last=row_num+1
    for i in range(1 + ( max_row * ( page - 1 ) ), max_row + 1 + ( max_row * ( page - 1 ) ) ):
        if row_num == 0:
            box.addstr( 1, 1, "Tidak ada menu",  highlightText )
        else:
            if ( i + ( max_row * ( page - 1 ) ) == position + ( max_row * ( page - 1 ) ) ):
                box.addstr( i - ( max_row * ( page - 1 ) ),20-len(strings[i-1])//2,strings[ i - 1 ], highlightText )
            else  :
                box.addstr( i - ( max_row * ( page - 1 ) ),20-len(strings[i-1])//2,strings[ i - 1 ], normalText )
            if i == row_num:
                break
    box1.refresh()
    box.refresh()
    box2.refresh()
    box3.refresh()
    screen.refresh()
    x = screen.getch()

  curses.endwin()

def load():
     box2.erase()



curses.wrapper(main)
