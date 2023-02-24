 #STRING PERMUTATION
def permutation(string,i=0):
    if i==len(string):
        print("".join(string))
    for j in range(i,len(string)):
        words = [a for a in string]
        print(words[i])
        print(words[j])
        words[i],words[j] = words[j],words[i]
        permutation(words,i+1)
permutation("vim")