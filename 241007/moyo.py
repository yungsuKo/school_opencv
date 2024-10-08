class String:
    data= ''
    def append(self):
        s=input("Type : ")
        self.data += "/"+s
    def show(self):
        print(self.data)

st = String()
st.append()
st.show()
st.append()
st.show()