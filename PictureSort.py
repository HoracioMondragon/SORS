import os
import shutil

class PictureSort:
    '''These are "global" array that contain keywords tha will categorize
    the the picture into the correct folder'''
    person = ['man', 'women', 'child', 'teenager', 'boy',
              'girl', 'person', 'human', 'dad', 'mom',
              'father', 'mother', 'grandmother', 'face','facial expression',
              'nose', 'chin', 'emotion', 'music artist','photograph',
              'hairstyle', 'person', 'eyewear', 'human behavior','moustache',
              'facial hair', 'skin', 'hair', 'homosapien', 'politician'
              'business man']

    animal = ['pet', 'dog', 'cat', 'tiger', 'animal',
              'monkey', 'fish', 'cow', 'lion', 'wild animal',
              'bird','beak', 'livestock', 'grass', 'mammal',
              'snout', 'carnivore', 'wildlife']

    abstract = ['handwriting', 'text', 'writing', 'font', 'paper',
                'homework', 'graffiti', 'document', 'calligraphy', 'advertising',
                'banner', 'signage', 'billboard', 'line', 'logo',
                'brand', 'product', ]

    place = ['historic site', 'ancient history', 'tourist attraction', 'ruins',
             'history', 'statue', 'landmark', 'monument',
             'sculpture', 'tourism', 'hill',
             'mountain', 'building', 'sky', 'water']

    '''Array within the category arrays as elements to help with recursive method'''
    categories = [person, animal, abstract, place, 'person', 'animal', 'abstract', 'place']

    '''olddirectory'''
    old_directory = ''

    '''newdirectory'''
    new_directory = ''

    '''Constructor'''
    def __init__(self, old, new, array_labels):
        self.old_directory += old
        self.new_directory += new
        self.__isCategory(array_labels, 0)

    '''Recursive to find the category in which the picture belongs'''
    def __isCategory(self, labels, category):
        if (set(labels) & set(self.categories[category])):
            self.__createFolder(self.new_directory, self.categories[category + 4])
            #loops to the others in the categories to figure out which element
            #it belongs to
        elif (category < 4):
            return self.__isCategory(labels, category + 1)
        else:
            print(self.old_directory)
            print("error alot")

    '''Creates the folder in which the category and the directory are going to
    be placed'''
    def __createFolder(self, dirr, folderName):
        newDirr = dirr + "/" + folderName
        self.directory = newDirr
        try:
            if not os.path.exists(newDirr):
                os.makedirs(newDirr)
        except OSError:
            print ('test')

        self.__redirect( newDirr)

    '''Moves the original directory of the selected files and moves it to the new directory'''
    def __redirect(self, new):
        shutil.move(self.old_directory,new)