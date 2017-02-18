#Author: Billy Brickner
#Date:   02/18/2017
#
#
#Takes a set of discretized tones and converts them to





from abjad import *
import time
import os
from collections import Counter
from math import sqrt

class bot_Toven:
    def __init__(self,
        rawDataIn = [1,1,1,1,1,
                    1,1,5,1,1,
                    1,1,1,1,1,
                    2,1,2,2,2,
                    2,2,2,2,2,
                    2,2,2,2,2,
                    2,1,2,2,2,
                    2,2,2,2,2,
                    2,2,2,2,2,
                    2,2,2,2,2,
                    2,2,2,2,2,
                    2,2,2,7,2,
                    2,2,2,2,2,
                    2,2,2,2,2,2,2,
                    2,8,2,2,2,
                    1,1,1,1,1,
                    1,1,1,1,1,
                    3,3,3,3,3,
                    3,3,3,3,3]):
        #print("Test")
        self.rawData = rawDataIn
        self.scrub()
        #print(self.rawData)
        self.convert()
        #print(notes)
        #notate([[1,.13],[2,.26],[1,.14]])
        self.notate()




    #Determines the mode of a set of values
    def mode(self,notes):
        data = Counter(notes)
        data.most_common()   # Returns all unique items and their counts
        return data.most_common(1)[0][0]  # Returns the highest occurring item





    #Determines the std devation of a set of values
    def sdev(self,notes):
        #Error catch
        if len(notes) <= 1:
            return 0;

        #initialize values
        total = sum(notes)
        avg = total / len(notes)
        variance = 0

        #Calculate Variance
        for note in notes:
            variance = variance + (note-avg)*(note-avg)

        #Provide the determined value
        return sqrt(variance)/(len(notes)-1)





    #Fills in a set of th eraw input with the smoothed value
    def fill(self,value1, bound1, value2, bound2):
        for i in range(bound1,bound2+1):

            #fill with lower bound value
            if i < (bound1 + bound2)/2:
                self.rawData[i] = value1

            #fill with upper bound value
            else:
                self.rawData[i] = value2




    #Scrubs the input for values which are undesired
    def scrub(self):
        #initalize variables
        expected = self.rawData[0]
        catch = -1

        #main loop
        for i in range(1,len(self.rawData)):
            #An error has been found
            if catch != -1:
                if self.rawData[i] == expected:
                    if catch[2] < 2:
                        catch[2] = catch[2] + 1
                    else:
                        self.fill(catch[0],catch[1], expected, i)
                        catch = -1

                else:
                    if self.rawData[i] == catch[0]:
                        self.fill(catch[0],catch[1], catch[0], i)
                        expected = self.rawData[i]
                        catch = -1
                    else:
                        expected = self.rawData[i]
                        catch[2] = 0


            #No error found
            else:
                #Error found
                if self.rawData[i] != expected:
                    catch = [expected,i-1, 0]
                    expected = self.rawData[i]



    #Takes smoothed raw input and converts it to notes
    def convert(self, period = .01):
        #initialize Variables
        self.notes = []
        note = self.rawData[0]
        counter = 1

        #main loop
        for i in range(1,len(self.rawData)):
            #keep growing note
            if note == self.rawData[i]:
                counter += 1
            #length of note has been reached
            else:
                counter += 1
                self.notes.append([note,counter*period])
                note = self.rawData[i]
                counter = 0
        #end loop
        counter += 1
        self.notes.append([note,counter*period])





    def determineQ(self):
        #Determine the quarter note
        margin = .25
        #print(self.notes)

        #used to determine the average minimum
        minsum = self.notes[0][1]
        mincount = 1

        #loop for calculating the minimum average
        for note in self.notes:
            expected = minsum/mincount #minimum average
            #print(expected,note[1])
            #This is a smaller value
            if (note[1]-expected)/expected < -margin:
                minsum = note[1]
                mincount = 1

            #This is a similarly small value
            elif abs((note[1]-expected)/expected) <= margin:
                minsum += note[1]
                mincount += 1


        #print(minsum/mincount)
        return minsum/mincount






    def notate(self):
        #Initialize Varables
        timeSig = 4
        minimum = self.determineQ()
        self.song = []
        tie = Tie()
        tieList = []


        #main loop
        counter = 0
        for note in self.notes:
            #duration of note
            length = int(note[1]/minimum+.5)
            #print(length)

            #Tie over bar lines
            if counter + length > timeSig:
                duration = Duration(timeSig - counter,4)
                #print("Debug 2:", counter,length, note)
                self.song.append(Note(note[0],duration))

                tieList.append([self.song[-1]])
                #print(notes)
                #print(length, counter)
                length = length - counter + timeSig
                #print(length)
                counter = 0

                #really long note
                while length > timeSig:
                    #print("Debug 3", length, note[0])
                    length = length - timeSig
                    duration = Duration(timeSig,4)
                    self.song.append(Note(note[0],duration))
                    tieList[-1].append(self.song[-1])
                    ##print(notes)

                #print("Debug 4",length)

                counter = length%timeSig
                duration = Duration(length,4)
                self.song.append(Note(note[0],duration))
                tieList[-1].append(self.song[-1])

            #regular note
            else:
                duration = Duration(length,4)
                self.song.append(Note(note[0],duration))
                counter = (counter + length)%timeSig

        staff = Staff(self.song)
        tempList = []
        #print(tieList)
        for bigTie in tieList:
            for littleTie in bigTie:
                tempList.append(littleTie)
            attach(tie, tempList)
        show(staff)










def main():
    bot_Toven()
    time.sleep(1)
    os.system("sudo rm 00*")
    os.system("mv ~/.abjad/output/0* ~/projects/fsuhacks")


if __name__ == "__main__":
    main()
