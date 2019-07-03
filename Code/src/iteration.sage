m = [1, 2, 3, 4]

c = [ [1,3], [2,3], [1,2], [3,4] ]

for i in Subsets(m):
    print(i)
    alpha_ij=0

    for j in c:
        delta_ij=set(i).symmetric_difference(set(j))
        print(delta_ij)

        for k in delta_ij:
            alpha_ij=alpha_ij+2^k

    print(alpha_ij)