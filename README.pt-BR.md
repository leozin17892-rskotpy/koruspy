🇧🇷 Português | 🇺🇸[English](README.md)
# Koruspy 🦀

**v0.9.8** --- Abstrações funcionais para Python (inspiradas em Rust /
FP)

Koruspy fornece `Option`, `Result` e coleções funcionais com:

-   Contratos claros\
-   Comportamento previsível\
-   Sem "mágica" oculta\
-   Sem falhas silenciosas

A versão **0.9.8** consolida a API e fortalece estruturas imutáveis e
assíncronas, aproximando a biblioteca da **1.0.0**.

------------------------------------------------------------------------

# ✨ Recursos

## 🔹 Option

Representa um valor opcional que pode estar presente (`Some`) ou ausente
(`nothing`).

**Construtores** - `Some(valor)` - `nothing`

**Operações funcionais** - `map` - `and_then` - `filter` - `flatten`

**Extração segura** - `unwrap_or` - `unwrap_or_else` - `expect`

**Garantias** - Igualdade bem definida (`__eq__`) - Sem recursão
infinita - Propagação correta de `nothing`

------------------------------------------------------------------------

## 🔹 Result

Representa o resultado de uma operação que pode ter sucesso (`Okay`) ou
falhar (`Err`).

**Construtores** - `Okay(valor)` - `Err(erro)`

**Operações funcionais** - `map` - `and_then` - `flat_map` - `fold`

**Extração segura** - `unwrap` - `unwrap_or` - `unwrap_or_else` -
`unwrap_err`

**Utilidades** - `result_of(fn)` para captura automática de exceções

As exceções são sempre explícitas --- nunca ocultas.

------------------------------------------------------------------------

## 🔹 AsyncOption

Wrapper assíncrono para `Option`.

Totalmente compatível com `await`.

**Métodos assíncronos** - `map_async` - `and_then_async` -
`filter_async` - `unwrap_or_async` - `unwrap_or_else_async`

Sem auto-await implícito.\
Sem comportamento escondido.

------------------------------------------------------------------------

## 🔹 SomeList / FrozenSomeList

Coleções funcionais baseadas em `Option`.

### SomeList

Coleção funcional mutável.

### FrozenSomeList

-   Estrutura imutável\
-   Hashável (pode ser usada como chave de `dict` ou em `set`)\
-   Baseada em `collections.abc.Sequence`\
-   Contrato explícito de imutabilidade

------------------------------------------------------------------------

# 🧪 Qualidade e Testes

✅ 62 testes automatizados passando

Cobertura inclui:

-   Contratos de igualdade (`__eq__`)
-   Garantias de imutabilidade
-   Consistência de hashing
-   Propagação de `nothing` / `Err`
-   Encadeamento funcional
-   API preparada para refatorações seguras

------------------------------------------------------------------------

# 🎯 Filosofia de Design

Koruspy busca ser:

-   Pequena\
-   Explícita\
-   Previsível\
-   Segura por padrão

Evita intencionalmente:

-   Exceções silenciosas\
-   Efeitos colaterais escondidos\
-   Abstrações excessivamente complexas\
-   "Açúcar sintático" desnecessário

Clareza e correção vêm em primeiro lugar.

------------------------------------------------------------------------

# 🚧 Status

**Versão atual:** 0.9.8 (pré-1.0)

-   API majoritariamente estável\
-   Pequenos ajustes de naming ou contratos ainda podem ocorrer\
-   A versão 1.0.0 marcará o congelamento da API pública

------------------------------------------------------------------------

# 📦 Instalação

``` bash
pip install koruspy
```

------------------------------------------------------------------------

# 🚀 Exemplo de Uso

``` python
from koruspy import Some, nothing, Okay, Err, result_of

# Option
opt = Some(42)
resultado = opt.map(lambda x: x * 2).unwrap_or(0)
print(resultado)  # 84


# Result
def dividir(a: int, b: int):
    if b == 0:
        return Err("Divisão por zero")
    return Okay(a / b)

resultado = dividir(10, 2).map(lambda x: x + 1).unwrap()
print(resultado)  # 6.0


# Captura automática de exceções
def pode_falhar():
    return result_of(lambda: 1 / 0)

resultado = pode_falhar()
print(resultado)  # Err(ZeroDivisionError)
```

------------------------------------------------------------------------

# 📄 Licença

MIT License

------------------------------------------------------------------------

# 📞 Contato

leozin17892@gmail.com
