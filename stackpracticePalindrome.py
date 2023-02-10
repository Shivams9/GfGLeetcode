from stack import stack
word='RaJaR'.lower().strip()            #strip for removing the space
st=stack()
for ch in word:
    st.push(ch)
print(st)
result='Palindrome'
for ch in word:
    out =st.pop()
    if ch!=out:
        result='Not Palindrome'
        break
print(result)


