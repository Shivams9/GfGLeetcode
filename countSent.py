#takes sentence as input and count number of words in it.
n= input('Enter the Sentence')
count=0
for i in n:
    count+=1
print('Number of Sentence : ',count,end=' ')


#takes sentense as input and count number of words in it #Example = Jay Shree Ram (Count=3)

n=input("Enter Sentence :")

word_count=n.split()
number=len(word_count)
print("WordsCount in Sentence: ",number)
