# Portal Interativo de História — projeto acadêmico

Projeto acadêmico desenvolvido por **Gabriel Silveira Lima** e **Jordana França Soares** como protótipo de portal educacional inclusivo.

## Objetivo

Explorar uma interface web com conteúdos de História e recursos de interação, incluindo navegação temática, quiz, linha do tempo, jogo de memória, leitura por síntese de voz e elementos voltados à acessibilidade.

## Implementação atual

O repositório contém uma aplicação HTML/CSS/JavaScript concentrada em `index.html`.

## Mídia da demonstração

A versão original referenciava imagens, vídeos e áudios que não estavam no repositório. Para evitar links quebrados e requisições 404, a versão atual usa placeholders explícitos para imagens e informa quando áudio/vídeo não está incluído.

Os arquivos multimídia só devem ser adicionados futuramente quando houver autoria/licença e origem documentadas.

## Executar localmente

```bash
python -m http.server 8000
```

Depois abra:

```text
http://localhost:8000
```

## Melhorias recomendadas

- [x] eliminar referências quebradas de mídia e usar placeholders explícitos;
- [ ] separar CSS e JavaScript do arquivo HTML principal;
- [ ] revisar todas as fontes históricas e referências;
- [ ] testar acessibilidade com teclado e leitor de tela;
- [ ] validar contraste e semântica HTML;
- [ ] adicionar testes básicos;
- [ ] documentar quais recursos são protótipos e quais foram efetivamente validados.

## Observação sobre acessibilidade

O projeto contém funcionalidades pensadas para inclusão, mas isso não equivale a conformidade formal com WCAG ou outras normas. Uma alegação de conformidade exige avaliação específica.
