import matplotlib.pyplot as plt
import matplotlib
matplotlib.interactive(True)


def printNewpos():
    new = []
    for i in an:
        new+= [ (i.get_text(), i.get_position()) ]
    import pprint
    pp= pprint.PrettyPrinter(indent=4)
    pp.pprint(new)


xlim={'xmin':2, 'xmax':10}
ylim={'ymin':0, 'ymax':0.45}

text_labels = [     #SW
                    [8.91, 0.157, 'p=0.2'] ,
                    [7.582, 0.177, 'p=0.3'] ,
                    [6.754, 0.217, 'p=0.4'] ,
                    [6.375, 0.285, 'p=0.5'] ,
                    [6.056, 0.325, 'p=0.6'] ,
                    [5.813, 0.365, 'p=0.7'] ,
                    [5.68, 0.395, 'p=0.8'] ,
                    [4.72, 0.375, 'p=0.9'] ,

                    #RSF k=1
                    [ 4.15 , 0.028, 'N=100' ],
                    [ 5.20 , 0.028, 'N=200' ],
                    [ 6.02 , 0.015, 'N=400' ],

                    #RSF k=2
                    [ 2.56 , 0.375, 'N=100' ],
                    [ 2.72 , 0.425, 'N=200' ],
                    [ 3.70 , 0.40, 'N=400' ],

                    #DSF
                    [ 2.85 , 0.26, 'N=27' ],
                    [ 3.68 , 0.2, 'N=81' ],
                    [ 4.55 , 0.16, 'N=243' ],
                ]
plt.xlim(**xlim)
plt.ylim(**ylim)

an = []
for x,y, label in text_labels:
    an+= [plt.annotate(label, (x,y))]
    an[-1].draggable()

plt.show()
