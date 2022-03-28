#1040

n1,n2,n3,n4=map(float, input().split())
media=((n1*2)+(n2*3)+(n3*4)+n4)/10

print(f"Media: {media:.1f}")

if media >= 7:
    situacao = "Aluno aprovado."
    print(situacao)
elif 6.9 >= media >= 5:
    situacao = "Aluno em exame."
    print(situacao)
    n5=float(input())
    print(f"Nota do exame: {n5:.1f}")
    final=(media+n5)/2
    if final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {final:.1f}")
elif media < 5:
    situacao = "Aluno reprovado."
    print(situacao)