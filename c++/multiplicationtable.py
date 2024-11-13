print("Multiplication Table")

n_table = int(input("Enter the table for"))
q_upto = int(input("length of table"))

for i in range(1,q_upto+1):
    print(f"{i} X {n_table} = {i*n_table}")