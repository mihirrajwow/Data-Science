
for i in range():
    with open(f"tables/Multiplication_table_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")
            # if j!=10:
            #     f.write('\n')
    # break
