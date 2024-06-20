n = int(input('Quantos nuemros você que ver da fibo? '))

sequencia_fibo = [0, 1]

while len(sequencia_fibo) < n:
    sequencia_fibo.append(sequencia_fibo[-1] + sequencia_fibo[-2])
    
    
print(sequencia_fibo)
