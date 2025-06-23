# **🚦Enhance main window - Card Stages**

> **Note:** This document is available in both English and Portuguese. The English version is presented first, followed by the Portuguese version.
>
> **Nota:** Este documento está disponível em inglês e português. A versão em inglês é apresentada primeiro, seguida pela versão em português.

---

<b>#### New Change:</b>
<b>2025-06-23 - Fix deprecated API usage</b>

<p align="center">
  *Anki interface before installing the add-on:*/<br>
  *Interface do Anki antes da instalação do add-on:*
  <br>
  <img src="https://i.ibb.co/mrjXT9J7/image.png" alt="Screenshot of Anki before addon">
</p>

<p align="center">
  *Anki interface with the "Enhance main window - Card Stages" add-on installed:*/<br>
  *Interface do Anki com o add-on "Enhance main window - Card Stages" instalado:*
  <br>
  <img src="https://i.ibb.co/xSwsgDfc/image.png" alt="Screenshot of Enhance main window - Card Stages">
</p>

## **English**

This add-on offers a streamlined and intuitive fork of the well-regarded "Enhance main window" functionality. It simplifies the Anki deck browser by presenting a clean and efficient column layout, focusing on an optimized order to help you quickly understand where your cards are across their various learning stages.

This version is inspired by the original "Enhance main window" by Arthur Milchior and its subsequent update "Enhance main window - add many columns to home decks (Customized by Shigeඞ)" by Shigeඞ. It aims to provide a more focused experience by concentrating on core information.

### **Core Idea**

The main goal is to offer a clear view by focusing on a set of simple columns. These columns are specifically chosen to transparently show the current stage of each card within Anki's learning lifecycle. The sum of card counts across these stage-representative columns should logically correspond to the total number of cards, accounting for all their diverse states. This addon refines the experience for users who prefer a straightforward overview of where their cards stand.

### **Features**

- **Intuitive Column Layout:** Presents a curated set of columns in a predefined order. This sequence is designed to logically display where your cards are located based on their current learning stage (e.g., New, Learning, Review, Due, Unseen, Suspended, Buried, Total), making it easier to assess your study progress at a glance.

- **Simplicity:** Works out-of-the-box with its streamlined view. No complex configuration is needed.
- **Focus on Essentials:** Provides key card count information without overwhelming the user with too many options or data points.
- **Multi-language Support:** Headers and tooltips for columns are now translatable, with initial support for English and Portuguese (Brazil). Users can define translations in `config.json`.
- **Based on Proven Code:** Built upon the solid foundation of the original "Enhance main window" addons, ensuring stability and compatibility.

### **Why "Enhance main window - Card Stages"?**

While the original "Enhance main window" and Shigeඞ's customized version offer a wealth of information and extensive customization, this version focuses on providing essential information in a highly intuitive and straightforward manner. If you appreciate a clean overview that helps you quickly locate cards within their study lifecycle, this addon is for you.

It retains the core benefit of detailed card counts in the deck browser but with an emphasis on an uncluttered presentation and ease of understanding the card pipeline.

### **Technical Details**

- Modifies the column rendering to display a specific, thoughtfully ordered set of columns.
- All additional configuration options have been removed.
- Includes a translation system allowing users to define custom text for column headers and tooltips in different languages via `config.json`.
- The codebase has been entirely rewritten to simplify future maintenance and ensure compatibility with upcoming Anki versions (developed targeting Anki 2.1.1-25.05+).
- Minimal overhead, designed for performance and simplicity.

### **Original Add-ons & Credits**

This add-on is a streamlined fork of:

-   **Enhance main window** by Arthur Milchior ([Add-on page](https://ankiweb.net/shared/info/877182321))
-   **Enhance main window - add many columns to home decks (Customized by Shigeඞ)** by Shigeඞ ([Add-on page](https://ankiweb.net/shared/info/911023479))

Full credit for the original concept, the extensive feature set, and much of the underlying code goes to Arthur Milchior and Shigeඞ for their respective significant contributions. This version aims to offer a more focused and streamlined alternative, building upon their excellent work.

### **Report Bugs or Suggest Improvements**

If you encounter any issues or have ideas for simple enhancements that align with the addon's philosophy, please open an issue on the project's repository (if available) or contact the current maintainer.

### **License**

-   **Copyright(C)** | [Carlos Duarte]
-   This add-on is likely to inherit the license of the original works it is based on. Please refer to the original add-ons for specific license details (typically GNU AGPL, version 3 or later). It is recommended to include a copy of the relevant license if you distribute this addon.

    *   Original "Enhance main window" License: [GNU AGPL, version 3](http://www.gnu.org/licenses/agpl.html)

### **Changelog**

- **v1.6 - 2025-06-23 - Fix deprecated API usage**:
  - Replaced deprecated `deckDueTree()` with modern `sched.deck_due_tree()` API.
  - Added fallback compatibility for older Anki versions.
  - Eliminated deprecated API warning messages in Anki logs.
- **v1.5 - 2025-06-12 - Fix URL parsing error**:
  - Fixed ValueError when URLs contain multiple colons by limiting split to first occurrence only.
- **v1.4 - 2025-06-03 - Preset Column Header**:
  - Added a translatable header ("Preset") to the deck options/preset column.
- **v1.3 - 2025-05-27 - macOS Fix**:
  - Fixed `UnicodeDecodeError` on macOS by specifying UTF-8 encoding when reading `.js` and `.css` files.
- **v1.2 - 2025-05-25 - Feature Removal**: 
  - Removed the `vertical_line_after` functionality and associated CSS for drawing vertical lines between columns.
- **v1.1 - 2025-05-24 - Internationalization & Configurable Translations**:
  - Added multi-language support for column headers and tooltips.
  - Translations can now be configured in `config.json` via `header_key`, `overlay_key`, and the `translation_maps` section.
  - Updated `config.md` to reflect these changes.
- **v1.0 - 2025-05-23 - Initial Release**:
  - Streamlined column view for the Anki deck browser.
  - Focus on essential card stage information.
  - Rewritten codebase for simplicity and maintainability.
  - Removed all additional configuration options from previous versions.

---

## **Português**

Este add-on oferece um fork simplificado e intuitivo da bem conceituada funcionalidade "Enhance main window". Ele simplifica o navegador de baralhos do Anki ao apresentar um layout de colunas limpo e eficiente, focando em uma ordem otimizada para ajudar você a entender rapidamente onde seus cartões estão em seus diversos estágios de aprendizado.

Esta versão é inspirada no "Enhance main window" original de Arthur Milchior e sua subsequente atualização "Enhance main window - add many columns to home decks (Customized by Shigeඞ)" por Shigeඞ. O objetivo é fornecer uma experiência mais focada, concentrando-se nas informações principais.

### **Ideia Central**

O objetivo principal é oferecer uma visão clara, focando em um conjunto de colunas simples. Essas colunas são especificamente escolhidas para mostrar de forma transparente o estágio atual de cada cartão dentro do ciclo de aprendizado do Anki. A soma das contagens de cartões nessas colunas representativas de estágios deve corresponder logicamente ao número total de cartões, abrangendo todos os seus diversos estados. Este addon refina a experiência para usuários que preferem uma visão geral direta de onde seus cartões se encontram.

### **Funcionalidades**

- **Layout de Colunas Intuitivo:** Apresenta um conjunto curado de colunas em uma ordem predefinida. Esta sequência é projetada para exibir logicamente onde seus cartões estão localizados com base em seu estágio de aprendizado atual (ex: Novos, Aprendendo, Revisão, Devem, Não Vistos, Suspensos, Enterrados, Total), facilitando a avaliação do seu progresso de estudo rapidamente.

- **Simplicidade:** Funciona imediatamente com sua visualização simplificada. Nenhuma configuração complexa é necessária.
- **Foco no Essencial:** Fornece informações chave sobre a contagem de cartões sem sobrecarregar o usuário com muitas opções ou pontos de dados.
- **Suporte Multilíngue:** Cabeçalhos e dicas de ferramenta das colunas agora são traduzíveis, com suporte inicial para Inglês e Português (Brasil). Os usuários podem definir traduções no `config.json`.
- **Based on Proven Code:** Construído sobre a base sólida dos addons originais "Enhance main window", garantindo estabilidade e compatibilidade.

### **Por que "Enhance main window - Card Stages"?**

Enquanto o "Enhance main window" original e a versão personalizada de Shigeඞ oferecem uma vasta quantidade de informações e personalização extensiva, esta versão foca em fornecer informações essenciais de uma maneira highly intuitiva e direta. Se você aprecia uma visão geral limpa que ajuda a localizar rapidamente os cartões dentro do seu ciclo de estudo, este addon é para você.

Ele retém o benefício central das contagens detalhadas de cartões no navegador de baralhos, mas com ênfase em uma apresentação organizada e facilidade de compreensão do fluxo de cartões.

### **Detalhes Técnicos**

- Modifica a renderização das colunas para exibir um conjunto específico e cuidadosamente ordenado de colunas.
- Todas as opções de configuração adicionais foram removidas.
- Inclui um sistema de tradução que permite aos usuários definir textos personalizados para cabeçalhos de colunas e dicas de ferramenta em diferentes idiomas através do `config.json`.
- A base de código foi inteiramente reescrita para simplificar manutenções futuras e garantir compatibilidade com as próximas versões do Anki (desenvolvido visando as versões 2.1.1-25.05+ do Anki).
- Sobrecarga mínima, projetado para desempenho e simplicidade.

### **Add-ons Originais & Créditos**

Este add-on é um fork simplificado de:

-   **Enhance main window** por Arthur Milchior ([Página do Add-on](https://ankiweb.net/shared/info/877182321))
-   **Enhance main window - add many columns to home decks (Customized by Shigeඞ)** por Shigeඞ ([Página do Add-on](https://ankiweb.net/shared/info/911023479))

Todo o crédito pelo conceito original, o extenso conjunto de funcionalidades e grande parte do código subjacente vai para Arthur Milchior e Shigeඞ por suas respectivas e significativas contribuições. Esta versão visa oferecer uma alternativa mais focada e simplificada, construída sobre o excelente trabalho deles.

### **Reportar Bugs ou Sugerir Melhorias**

Se você encontrar quaisquer problemas ou tiver ideias para melhorias simples que se alinhem com a filosofia do addon, por favor, abra uma issue no repositório do projeto (se disponível) ou contate o mantenedor atual.

### **Licença**

-   **Copyright(C)** | [Carlos Duarte]
-   Este add-on provavelmente herdará a licença dos trabalhos originais em que se baseia. Por favor, consulte os add-ons originais para detalhes específicos da licença (tipicamente GNU AGPL, versão 3 ou posterior). Recomenda-se incluir uma cópia da licença relevante se você distribuir este addon.

    *   Licença Original "Enhance main window": [GNU AGPL, version 3](http://www.gnu.org/licenses/agpl.html)

### **Histórico de Alterações**

- **v1.6 - 2025-06-23 - Correção de API deprecated**:
  - Substituída a API deprecated `deckDueTree()` pela moderna `sched.deck_due_tree()`.
  - Adicionada compatibilidade com fallback para versões mais antigas do Anki.
  - Eliminadas as mensagens de aviso de API deprecated nos logs do Anki.
- **v1.5 - 2025-06-12 - Erro ao processar URLs**:
  - Corrigido ValueError quando URLs contêm múltiplos dois-pontos limitando o split apenas à primeira ocorrência.
- **v1.4 - 2025-06-03 - Cabeçalho da Coluna de Modelo**:
  - Adicionado um cabeçalho traduzível ("Modelo") para a coluna de opções/modelo do baralho.
- **v1.3 - 2025-05-27 - Correção para macOS**:
  - Corrigido `UnicodeDecodeError` no macOS ao especificar a codificação UTF-8 na leitura de arquivos `.js` e `.css`.
- **v1.2 - 2025-05-25 - Remoção de Funcionalidade**:
  - Removida a funcionalidade `vertical_line_after` e o CSS associado para desenhar linhas verticais entre colunas.
- **v1.1 - 2025-05-24 - Internacionalização & Traduções Configuráveis**:
  - Adicionado suporte multilíngue para cabeçalhos de colunas e dicas de ferramenta.
  - As traduções agora podem ser configuradas no `config.json` através de `header_key`, `overlay_key` e da seção `translation_maps`.
  - Atualizado o `config.md` para refletir essas mudanças.
- **v1.0 - 2025-05-23 - Lançamento Inicial**:
  - Visualização de colunas simplificada para o navegador de baralhos do Anki.
  - Foco nas informações essenciais sobre o estágio dos cartões.
  - Base de código reescrita para simplicidade e manutenibilidade.
  - Removidas todas as opções de configuração adicionais das versões anteriores.
