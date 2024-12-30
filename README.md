# Mima

Tem problema em dar/receber presentes? Convide todo mundo pra cá!

A funcionalidade principal é poder escolher um item da lista de um amigo sem ele saber, mas os outros amigos dele sabendo que o item já será dado por alguém.

## Objetivos

- [ ] Cadastro/Login
- [ ] Adição de sugestões
...

```mermaid
classDiagram

Amigo "1"--"*" SugestaoDePresente
Amigo "1"--"*" Amizade : remetente
Amigo "1"--"*" Amizade : destinatario


class Amigo {
    username
    bio
    data_de_nascimento
    foto
}

class Amizade {
    data
}

class SugestaoDePresente {
    nome
    link
    descricao
}
```