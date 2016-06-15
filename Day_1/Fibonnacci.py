def fibonnacci_iteration(terms):
    if terms<0:
        terms=abs(terms)
    first_term=0
    second_term=1
    next_term=first_term+second_term
    fibonnacci_list=[first_term,second_term,next_term]
    for i in range(3,terms):
        second_term,next_term =next_term, second_term
        next_term+=second_term
        fibonnacci_list.append(next_term)
    return fibonnacci_list
#implementation of the fibonnacci series using recursion
def fibonnacci_recursion(terms):
    if terms <0:
        terms=abs(terms)
    if terms <=1:
        return terms
    else:
        return (fibonnacci_recursion(terms-1)+fibonnacci_recursion(terms-2))
terms=int(input("Enter the number of fibonacci terms"))
print("Fibonnacci terms using iteration")
print(fibonnacci_iteration(terms))
print("Fibonnacci terms using recursion")
recur_list=[]
for term in range(terms):
    recur_list.append(fibonnacci_recursion(term))
print(recur_list)