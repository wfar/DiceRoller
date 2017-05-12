from graphics import *


class Button:
    ''' A button is a labeled rectangle in a window.
       It is activated or deactivated with the activate()
       and deactivate() methods. The clicked(p) method
       retuerns True if the button is active and p is inside it.'''

    def __init__(self, win, center, width, height, label):
        ''' Creates a rectangular button, eg:
            qb = Button(myWin, centerPoint, width, height, 'Quit') '''

        w, h = width/2.0 , height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+w, y-w
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def getLabel(self):
        '''Returns the label string of this button.'''
        return self.label.getText()


    def activate(self):
        '''Sets this button to 'activate' '''
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        ''' Sets this button to 'inactive' '''
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, p):
        ''' Return true if button is active and p is inside'''
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
            

'''
pt = getMouse()
if button1.clicked(pt):
    #Do button1 stuff
elif button2.clicked(pt):
    #Do button 2 stuff
elif button3.clicked(py):
    # Do button 3 stuff

'''

    
    
