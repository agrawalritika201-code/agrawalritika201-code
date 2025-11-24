import matplotlib.pyplot as pl
x=['Maths','English','Cs','Science']
y1=[40,24,38,42]
y2=[19,17,27,32]
pl.title("Books in Library")
pl.xlabel('Subjects')
pl.ylabel('No. of Books in Libraries')
pl.bar(x,y1,color='c',label='Books in College Library',width=0.4)
pl.bar(x,y2,color='m',label='Books in School Library',width=0.4)
pl.legend()
pl.show()
