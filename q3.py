my_file=open("person3.txt","w")
file_data= my_file.write("life is very beautifull and life is very small so all time happy and accept your challenge")
my_file.close()
a_name=open("person3.txt","r")
name_data=a_name.read()
print(name_data)
a_name.close()