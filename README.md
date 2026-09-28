# Portal Interativo de História — projeto acadêmico

Projeto acadêmico desenvolvido por **Gabriel Silveira Lima** e **Jordana França Soares** como protótipo de portal educacional inclusivo.

## Objetivo

Explorar uma interface web com conteúdos de História e recursos de interação, incluindo navegação temática, quiz, linha do tempo, jogo de memória, leitura por síntese de voz e elementos voltados à acessibilidade.

## Implementação atual

O repositório contém uma aplicação HTML/CSS/JavaScript concentrada em `index.html`.

## Limitação importante

A versão atual referencia arquivos em `media/` — imagens, vídeos e áudios — que **não estão presentes no repositório**. Por isso, parte da experiência visual e multimídia não funciona quando o projeto é executado a partir do estado atual.

Esse ponto deve ser corrigido antes de usar o projeto como demonstração pública.

## Executar localmente

```bash
python -m http.server 8000
```

Depois abra:

```text
http://localhost:8000
```

## Melhorias recomendadas

- [ ] restaurar ou substituir os arquivos de mídia ausentes;
- [ ] separar CSS e JavaScript do arquivo HTML principal;
- [ ] revisar todas as fontes históricas e referências;
- [ ] testar acessibilidade com teclado e leitor de tela;
- [ ] validar contraste e semântica HTML;
- [ ] adicionar testes básicos;
- [ ] documentar quais recursos são protótipos e quais foram efetivamente validados.

## Observação sobre acessibilidade

O projeto contém funcionalidades pensadas para inclusão, mas isso não equivale a conformidade formal com WCAG ou outras normas. Uma alegação de conformidade exige avaliação específica.
