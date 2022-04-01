# https://www.beecrowd.com.br/judge/en/problems/view/1013

a, b, c = map(int, input().split())

maiorab = (a + b + abs(a-b)) / 2
maiorxc = (maiorab + c + abs(maiorab-c)) / 2

print(f'{int(maiorxc)} eh o maior')