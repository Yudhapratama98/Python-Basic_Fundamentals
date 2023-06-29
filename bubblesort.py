def bubblesort (theList):
    panjangList = len(theList)

    #Transverse seluruh elemen array
    for i in range(panjangList):
        swapped = False

        #Elementerakhir yang telah ada di tempatnya
        for j in range (0,panjangList-i-1):

            #Arraynya di transverse dari 0 ke panjangList-i-1.
            #Swap element jika elemen tersebut lebih besar dari elemen berikutnuya
            if(theList[j]>theList[j+1]):
                theList[j], theList[j+1] = theList[j+1],theList[j]
                swapped = True
            #Kalau kedua elemet swap by inner loop, then break
            if swapped == False:
                break
listTest = [19, 41, 24, 50, 41, 50]
bubblesort(listTest)

print(listTest) #[12, 19,24, 41, 50]