# Atividade 02 - Teste de Software
## José Fagner Silva Junqueira

## #1
Para elaboração e execução desse trabalho foi seguido o como base o vídeo [Introdução ao teste de mutação em Python com a ferramenta mutmut] do Stevao Andrade, todos os passos foram executados em máquina local utilizando um repositório do GitHub e respeitando os requisitos minimos para execução dos teste que são:
- [Python 3.7+]

- [python3-venv]

- [pytest]

- [pytest-cov]

- [mutmut : python mutation tester]

## #2
Abaixo estão descritas as etapas executas seguindo o tutorial do vídeo supracitado do Stevao Andrade.

### Etapa 1
Na primeira etapa para a realização dos testes foi necessário a escolha de um repositório no GitHub que atendesse aos requisistos minimos anteriormente expressos, para que então o mesmo pudesse ser clonado localmente. Foi escolhido o [py_calculator] e então executado o comando `git clone https://github.com/JanTeffo442/simple_calculator.git` para poder possuir o arquivo localmente e executar os testes necessários.

### Etapa 2
Com o repositório localmente partimos para a segunda etapa que consiste na preparação de um ambiente virtual para poder instalar todas as depêndecias do software a ser testado sem que ele sofra interferências de outros ambientes, assim, conseguimos ter um maior controle real do cenário existente.

Foram executados os seguintes comandos na ordem expressa:

- `cd .\python-oauth2\` para adentrar a pasta com o repositório recem clonado do GitHub

- `python -m venv .venv` para criar o ambiente virtual

- `.\.venv\Scripts\Activate` para iniciar o ambiente virtual

### Etapa 3

Agora dentro da pasta com o projeto clonado e com o ambiente virtual em execução podemos prosseguir com a configuração da aplicação, para isso se faz necessário a instalação das depêndecias do software em suas respectivas versões através do comando `pip install -r .\requirements.txt` que instalará todas as dependências necessárias através do PIP.

### Etapa 4

Com tudo configurado e instalado começamos a execução dos testes com o comando `pytest -vv`, o mesmo pode receber mais parametros, inclusive qual o diretório ou arquivo executará os testes, mas no caso desse repositório não se faz necessário mais parametro, uma vez que o mesmo já está configurado.

Veja abaixo a saída do comando.

```
(.venv) PS C:\Users\fagne\Documents\py_calculator> pytest -vv
========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.11.1, pytest-8.3.2, pluggy-1.5.0 -- C:\Users\fagne\Documents\py_calculator\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\fagne\Documents\py_calculator
plugins: cov-5.0.0
collected 23 items

test/test_calculator.py::test_sum_returns_number PASSED                                                                                                                                            [  4%]
test/test_calculator.py::test_sum_3_and_8_equals_11 PASSED                                                                                                                                         [  8%] 
test/test_calculator.py::test_sum_0_and_0_equals_0 PASSED                                                                                                                                          [ 13%] 
test/test_calculator.py::test_sum_4_and_minus_10_equals_minus_6 PASSED                                                                                                                             [ 17%] 
test/test_calculator.py::test_sum_minus_1_and_minus_10_equals_minus_11 PASSED                                                                                                                      [ 21%] 
test/test_calculator.py::test_sum_3_4_and_4_5_equals_7_9 PASSED                                                                                                                                    [ 26%] 
test/test_calculator.py::test_sum_3_46_and_4_57_equals_8_08 PASSED                                                                                                                                 [ 30%] 
test/test_calculator.py::test_subtract_7_from_12_equals_5 PASSED                                                                                                                                   [ 34%]
test/test_calculator.py::test_subtract_7_from_7_equals_minus_0 PASSED                                                                                                                              [ 39%] 
test/test_calculator.py::test_subtract_7_from_5_equals_minus_2 PASSED                                                                                                                              [ 43%] 
test/test_calculator.py::test_multiply_6_by_3_returns_18 PASSED                                                                                                                                    [ 47%] 
test/test_calculator.py::test_multiply_6_by_minus_3_returns_minus_18 PASSED                                                                                                                        [ 52%] 
test/test_calculator.py::test_multiply_minus_6_by_3_returns_minus_18 PASSED                                                                                                                        [ 56%] 
test/test_calculator.py::test_multiply_0_by_3_returns_0 PASSED                                                                                                                                     [ 60%] 
test/test_calculator.py::test_multiply_6_by_0_returns_0 PASSED                                                                                                                                     [ 65%] 
test/test_calculator.py::test_multiply_6_4_by_4_3_returns_27_52 PASSED                                                                                                                             [ 69%]
test/test_calculator.py::test_multiply_6_48_by_4_35_returns_28_188 PASSED                                                                                                                          [ 73%] 
test/test_calculator.py::test_multiply_6_481_by_4_357_returns_28_237717 PASSED                                                                                                                     [ 78%] 
test/test_calculator.py::test_divide_8_by_4_equals_2 PASSED                                                                                                                                        [ 82%] 
test/test_calculator.py::test_divide_7_by_2_equals_3_5 PASSED                                                                                                                                      [ 86%] 
test/test_calculator.py::test_divide_7_by_4_equals_1_75 PASSED                                                                                                                                     [ 91%] 
test/test_calculator.py::test_divide_7_by_3_equals_2_33 PASSED                                                                                                                                     [ 95%] 
test/test_calculator.py::test_division_by_zero_raises_exception PASSED                                                                                                                             [100%] 

========================================================================================== 23 passed in 0.08s ===========================================================================================
```

Podemos então concluir que foram executados 23 testes e todos passaram com êxito.

### Etapa 5

Agora vericamos a cobertura desses testes utilizando o `pytest -vv --cov=cal` que retorna essa saída:

```
========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.11.1, pytest-8.3.2, pluggy-1.5.0 -- C:\Users\fagne\Documents\py_calculator\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\fagne\Documents\py_calculator
plugins: cov-5.0.0
collected 23 items

test/test_calculator.py::test_sum_returns_number PASSED                                                                                                                                            [  4%] 
test/test_calculator.py::test_sum_3_and_8_equals_11 PASSED                                                                                                                                         [  8%] 
test/test_calculator.py::test_sum_0_and_0_equals_0 PASSED                                                                                                                                          [ 13%] 
test/test_calculator.py::test_sum_4_and_minus_10_equals_minus_6 PASSED                                                                                                                             [ 17%] 
test/test_calculator.py::test_sum_minus_1_and_minus_10_equals_minus_11 PASSED                                                                                                                      [ 21%] 
test/test_calculator.py::test_sum_3_4_and_4_5_equals_7_9 PASSED                                                                                                                                    [ 26%]
test/test_calculator.py::test_sum_3_46_and_4_57_equals_8_08 PASSED                                                                                                                                 [ 30%] 
test/test_calculator.py::test_subtract_7_from_12_equals_5 PASSED                                                                                                                                   [ 34%] 
test/test_calculator.py::test_subtract_7_from_7_equals_minus_0 PASSED                                                                                                                              [ 39%] 
test/test_calculator.py::test_subtract_7_from_5_equals_minus_2 PASSED                                                                                                                              [ 43%] 
test/test_calculator.py::test_multiply_6_by_3_returns_18 PASSED                                                                                                                                    [ 47%]
test/test_calculator.py::test_multiply_6_by_minus_3_returns_minus_18 PASSED                                                                                                                        [ 52%] 
test/test_calculator.py::test_multiply_minus_6_by_3_returns_minus_18 PASSED                                                                                                                        [ 56%] 
test/test_calculator.py::test_multiply_0_by_3_returns_0 PASSED                                                                                                                                     [ 60%] 
test/test_calculator.py::test_multiply_6_by_0_returns_0 PASSED                                                                                                                                     [ 65%] 
test/test_calculator.py::test_multiply_6_4_by_4_3_returns_27_52 PASSED                                                                                                                             [ 69%] 
test/test_calculator.py::test_multiply_6_48_by_4_35_returns_28_188 PASSED                                                                                                                          [ 73%] 
test/test_calculator.py::test_multiply_6_481_by_4_357_returns_28_237717 PASSED                                                                                                                     [ 78%] 
test/test_calculator.py::test_divide_8_by_4_equals_2 PASSED                                                                                                                                        [ 82%] 
test/test_calculator.py::test_divide_7_by_2_equals_3_5 PASSED                                                                                                                                      [ 86%] 
test/test_calculator.py::test_divide_7_by_4_equals_1_75 PASSED                                                                                                                                     [ 91%] 
test/test_calculator.py::test_divide_7_by_3_equals_2_33 PASSED                                                                                                                                     [ 95%]
test/test_calculator.py::test_division_by_zero_raises_exception PASSED                                                                                                                             [100%] 

---------- coverage: platform win32, python 3.11.1-final-0 -----------
Name                Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------
cal\__init__.py         0      0      0      0   100%
cal\calculator.py      10     10      2      0     0%
-----------------------------------------------------
TOTAL                  10     10      2      0     0%


========================================================================================== 23 passed in 0.14s =========================================================================================== 
```

Atentemos apenas ao final onde ele indica a porcentagem de cobertura, podemos notar que `cal\__init__.py` não possui nenhum teste, o que já era esperado e por isso tem um retorno de `100%` de cobertura, diferente de `cal\calculator.py` que acusa ter `0%` de cobertura.

### Etapa 6

Agora com testes unitários executados partiremos para o que propõe esta atividade, mutação de teste. Para isso usaremos o `mutmut` do python com o comando `mutmut run --paths-to-mutate=test`, o qual nos informa essa saída:

```
(.venv) PS C:\Users\fagne\Documents\py_calculator> mutmut run --paths-to-mutate=test

- Mutation testing starting -

These are the steps:
1. A full test suite run will be made to make sure we
   can run the tests successfully and we know how long
   it takes (to detect infinite loops for example)
2. Mutants will be generated and checked

Results are stored in .mutmut-cache.
Print found mutants with `mutmut results`.

Legend for output:
🎉 Killed mutants.   The goal is for everything to end up in this bucket.
⏰ Timeout.          Test suite took 10 times as long as the baseline so were killed.
🤔 Suspicious.       Tests took a long time, but not long enough to be fatal.
🙁 Survived.         This means your tests need to be expanded.
🔇 Skipped.          Skipped.

1. Using cached time for baseline tests, to run baseline again delete the cache file

2. Checking mutants
⠋ 101/101  🎉 93  ⏰ 0  🤔 0  🙁 8  🔇 0
```

Assim concluimos que foi realizado 101 testes de mutação, dos quais 93 passaram sem problemas e 8 sobreviveram as mutações, o que não indica um bom sinal, para termos uma melhor análise do problemas executamos o `mutmut results` que nos detalhará melhor essas mutações que sobreviveram e então obtivemos essa saída:

```
(.venv) PS C:\Users\fagne\Documents\py_calculator> mutmut results
To apply a mutant on disk:
    mutmut apply <id>

To show a mutant:
    mutmut show <id>


Survived 🙁 (8)

---- test\test_calculator.py (8) ----

1-2, 62, 65, 97-98, 100-101
```

Asssim os ids dos testes que devemos analisar são `1-2, 62, 65, 97-98, 100-101`, no propio comando acima ele nos retorna que podemos detalhar melhor os problemas ao utilizar o comando `mutmut show <id>`, fiz então uma execução para ver melhor o problema de id 65 e obtive a seguinte saída:

```
(.venv) PS C:\Users\fagne\Documents\py_calculator> mutmut show 65  
--- test\test_calculator.py
+++ test\test_calculator.py
@@ -63,7 +63,7 @@
     assert multiply(0, 3) == 0

 def test_multiply_6_by_0_returns_0():
-    assert multiply(6, 0) == 0
+    assert multiply(7, 0) == 0

 def test_multiply_6_4_by_4_3_returns_27_52():
     assert multiply(6.4, 4.3) == 27.52
```

Analisando o contexto podemos ver que ele fez uma mutação na função que realiza uma mutiplicação com zero e pelo principio matematico sabemos que qualquer valor multiplicado por zero sempre será zero, e é o nosso caso, a mutação troca o `6` por `7` e mantem o zero, assim, a saída ainda é a mesma e podemos descartar a sobrevida dessa mutação.

### Etapa 7

Para melhor analisar todos os testes vamos executar o comando `mutmut html` que nos retornará um arquivo html com todos os mutantes que sobreviveram e então saberemos melhor como agir mediante o problema.

Só foi necessário mudar uma função:

transformar 
``` py
def test_division_by_zero_raises_exception():
    with pytest.raises(ZeroDivisionError):
        assert divide(7, 0) == 0
```

em
``` py
def test_division_by_zero_raises_exception():
    with pytest.raises(ZeroDivisionError):
        divide(7, 0)
```

os outros testes estão corretos e não existem melhorias a serem feitas, uma vez que as operações estão corretas em todos os casos testados. Após a mudança o número de mutações que sobreviveram caiu de 8 para 6.

[Introdução ao teste de mutação em Python com a ferramenta mutmut]: https://www.youtube.com/watch?v=FbMpoVOorFI&t=1471s

[mutmut : python mutation tester]: https://github.com/boxed/mutmut

[pytest-cov]: https://pypi.org/project/pytest-cov/

[Python 3.7+]: https://www.python.org/

[python3-venv]: https://docs.python.org/3/library/venv.html

[pytest]: https://docs.pytest.org/en/stable/

[py_calculator]: https://github.com/JanTeffo442/simple_calculator.git


# Calculator

## Purpose
Basic example of different features of unit testing in Pytest.
The system under test is a basic calculator module that implements the functions `sum`, `subtract`, `multiply` and `divide`.

## Tools
Pytest / Python

## Author:
Arturo Mora-Rioja