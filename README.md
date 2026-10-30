# PDV com Descontos (Nível 1)

## O que o código faz

Este programa simula um PDV (Ponto de Venda). Ele recebe o valor de uma compra e a idade do cliente, aplica descontos progressivos de acordo com regras de negócio e mostra o valor final em reais. O programa aceita várias compras seguidas e, ao ser encerrado, exibe um resumo do dia com quantidade de compras, total bruto, total de descontos e total final.

## Como ele faz

1. Pede o valor da compra. Se for `0`, o loop termina; se for negativo, mostra um aviso e pede de novo (`if` + `continue`).
2. Pede a idade do cliente. Se for negativa, mostra um aviso e volta ao início do loop.
3. Se a idade for maior ou igual a 65, aplica 20% de desconto (valor × 0.8).
4. Se o valor **já com o desconto de idade** for maior que 100, aplica mais 10% (valor × 0.9).
5. Arredonda para duas casas decimais e mostra o valor final, ex.: `R$ 144.00`.
6. Guarda a compra (valor original e valor final) numa lista com `.append()`.
7. Ao encerrar, um `for` percorre a lista somando os valores. O total de descontos é `total bruto - total final`.

## Como rodar

```
python pdv.py
```