import os.path

def myfunction():
    #print os.path.abspath(os.path.join(yourpath, os.pardir))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    THIS_FILE = os.path.abspath(__file__)
    ANOTHER_FILE = os.path.dirname(os.path.abspath(__file__))
    SETTINGS_DIR = os.path.dirname(__file__)
    PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
    #PROJECT_PATH = os.path.abspath(PROJECT_PATH)
    TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

    print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print os.path.abspath(__file__)
    print os.path.dirname(os.path.abspath(__file__))
    print os.pardir
    #print os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    #print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print os.path.abspath(__file__)
    #print os.path.dirname(os.path.abspath(__file__))
    #print os.path.dirname(__file__)
    #print os.path.join(SETTINGS_DIR, os.pardir)
    #print os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    #print os.path.join(PROJECT_PATH, 'templates')

if __name__ == '__main__':
    print "Starting myfunction script..."
    myfunction()
