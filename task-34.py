for i in range(1,11):
    print(*[f"{j:^3}* {i:^3}= {j*i:^3}" for j in range(1,11)])
