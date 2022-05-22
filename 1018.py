# https://www.beecrowd.com.br/judge/en/problems/view/1018
 
n = int(input())

print(f'{n//100} nota(s) de R$ 100,00')
print(f'{(n%100) // 50} nota(s) de R$ 50,00')
print(f'{(n%50) // 20} nota(s) de R$ 20,00')
print(f'{((n%50)%20) // 10} nota(s) de R$ 10,00')
print(f'{(n%10) // 5} nota(s) de R$ 5,00')
print(f'{(n%5) // 2} nota(s) de R$ 2,00')
print(f'{(n%5)%2} nota(s) de R$ 1,00')