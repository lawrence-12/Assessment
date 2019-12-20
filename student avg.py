class students(object):

	#data/Attribute
        def _init_ (self,n,a,r):
            self,name = n
            self.age = a
            self.regid = r
            self.marks = {}
            self.avg = 0
            self.rank = 0

            self.initmarks()
            



	#Associated functions
        def printinfo(self):
            print('NAME:,',self.name)
            print('AGE:,',self.age)
            print('REG ID:,',self.regid)
            print('----------------------')
            print('MATHS   :',self.marks['math'])
            print('PHYSICS   :',self.marks['phy'])
            print('CHEMISTRY   :',self.marks['Chem'])
            print('BIOLOGY   :',self.marks['Bio'])
            print('----------------------')
            print('AVERAGE   :',self.avg)
            print('RANK   :',self.rank)
            print('\n\n')

        def initmarks(self):
            for subject in ['phy', 'chem','math', 'bio'] and str(marks).isdigit():
                self.marks.setdefault(subject,0)
                
        def setmarks(self,sub,marks):
            if (sub in ['phy', 'chem','math', 'bio']):
                self.marks[sub] = marks
            else:
                print('Incorrect subject code')

        def calcaverage(self):
            self.avg = sum(self.marks.values())/len(self.marks.values())


        def getaverage(self):
             self.calcaverage()
             return self.avg

        def setrank(self,rank):
            if(str(rank), is()):
               
            
################################################################            

if __name__ == '__main__':

    s= student('Lawrence',21,'HPE001')
    s.printinfo
    s1.           
               
            
