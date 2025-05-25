# **Configuration for "Enhance main window - 🚦Card Stages" Add-on**

> **Note:** This document is available in both English and Portuguese. The English version is presented first, followed by the Portuguese version.
>
> **Nota:** Este documento está disponível em inglês e português. A versão em inglês é apresentada primeiro, seguida pela versão em português.

---

## **English**

This document explains the configuration options available in the `config.json` file for the "Enhance main window - 🚦Card Stages" Anki add-on. This add-on aims for simplicity, so configuration is minimal compared to its predecessors.

### **1. General Options**

These options control the overall behavior and appearance of the add-on.

*   **`book symbol`**: (string)
    *   A symbol (e.g., "{") that, if present in a deck's name, can be used by custom logic (currently not implemented in this simplified version for special coloring/behavior).
    *   Default: `"{`

*   **`color empty`**: (string, CSS color)
    *   The color used for the names of decks that have no new cards (unseen).
    *   Default: `"red"`

*   **`color empty descendant`**: (string, CSS color)
    *   The color used for the names of decks that have a sub-deck موسمnew cards (unseen).
    *   Default: `"green"`

*   **`color zero`**: (boolean or string CSS color)
    *   Controls how zero values in columns are displayed.
    *   If `false` (default in this add-on): Zero values are not shown (cell appears empty).
    *   If a string (e.g., `"#e0e0e0"` or `"grey"`): Zero values are displayed in this color.
    *   If `null`: Uses the default column color.
    *   Default: `false`

*   **`default column color`**: (string, CSS color)
    *   The default color for text within the custom columns if no specific color is set for that column or for zero values.
    *   Default: `"grey"`

*   **`do color empty`**: (boolean)
    *   If `true`, enables the coloring of deck names based on `color empty` and `color empty descendant`.
    *   Default: `true`

*   **`end symbol`**: (string)
    *   A symbol (e.g., ";") that, if present in a deck's name, signifies the deck is considered "ended." This can affect coloring if `do color empty` is true (ended decks might not be colored as "empty").
    *   Default: `";"`

*   **`given up symbol`**: (string)
    *   Similar to `end symbol`, a symbol (e.g., "/") for decks considered "given up."
    *   Default: `"/"`

*   **`hide values of parent decks`**: (boolean)
    *   If `true`, numbers in a parent deck's row are hidden if it has children.
    *   Default: `false`

*   **`hide values of parent decks when subdecks are shown`**: (boolean)
    *   Similar to the above, but only hides parent deck numbers if its sub-decks are currently expanded (visible).
    *   Default: `false`

*   **`option`**: (boolean)
    *   If `true`, displays the deck's option group name at the end of its row.
    *   Default: `true`

*   **`pause symbol`**: (string)
    *   Similar to `end symbol`, a symbol (e.g., "=") for decks considered "paused."
    *   Default: `"="`

### **2. Column Configuration (`columns`)**

This is an array of objects, where each object defines a column to be displayed in the deck browser. The order in this array determines the display order of the columns.

Each column object has the following properties:

*   **`name`**: (string, internal)
    *   The internal identifier for the column's data type (e.g., `"new today"`, `"cards"`, `"bar"`).
    *   **Do NOT alter this value**, as it's used to fetch the correct data.

*   **`description`**: (string, English)
    *   A brief English description of what the column represents. This is primarily for reference when editing `config.json` and is **not displayed** in the Anki interface.

*   **`header_key`**: (string, translation key)
    *   A key used to look up the translated header text for this column from the `translation_maps` section.
    *   Example: `"col_new_today_header"`

*   **`overlay_key`**: (string, translation key)
    *   A key used to look up the translated tooltip text (shown on mouse hover) for this column from the `translation_maps` section.
    *   Example: `"col_new_today_overlay"`

*   **`present`**: (boolean)
    *   If `true`, the column is displayed. If `false`, it's hidden.
    *   Default (if omitted): `true`

*   **`color`**: (string, CSS color, or `null`)
    *   The color for the numbers/text in this column.
    *   `null` uses a default color scheme (often from Anki's built-in stats or `default column color`).
    *   Example: `"blue"`, `"#FF0000"`

*   **`absolute`**: (boolean)
    *   If `true`, displays absolute numbers.
    *   Default (if omitted and `percent` is `false`): `true`

*   **`percent`**: (boolean)
    *   If `true`, displays values as percentages (usually relative to the total number of cards in the deck/subdecks).
    *   Default (if omitted): `false`

*   **`subdeck`**: (boolean)
    *   If `true`, calculations for this column include cards from sub-decks.
    *   If `false`, calculations are only for the current deck.
    *   Default (if omitted): `true` is common for aggregated views.

*   **`names`**: (array of strings, for `bar` type columns only)
    *   If `name` is `"bar"`, this array lists the internal names of other columns whose values should be part of this progress bar.
    *   Example: `["mature", "young", "learning card", "unseen"]`

### **3. Translation Maps (`translation_maps`)**

This section holds the actual translated strings for headers and overlays.

*   **`translation_maps`**: (object)
    *   A top-level object.
    *   Inside, create sub-objects for each supported language code (e.g., `"en"`, `"pt_BR"`).
    *   Each language sub-object contains key-value pairs, where the key is a `header_key` or `overlay_key` (as defined in the `columns` section) and the value is the translated string for that language. HTML can be used in these strings (e.g., `<br/>` for line breaks).

    ```json
    "translation_maps": {
        "en": {
            "col_new_today_header": "NewToday",
            "col_new_today_overlay": "New cards for today",
            // ... other English translations
        },
        "pt_BR": {
            "col_new_today_header": "NovHoje",
            "col_new_today_overlay": "Cartões novos para hoje",
            // ... other Portuguese translations
        }
        // ... other languages if supported
    }
    ```

---

## **Português**

Este documento explica as opções de configuração disponíveis no arquivo `config.json` para o add-on Anki "Enhance main window - 🚦Card Stages". Este add-on visa a simplicidade, então a configuração é mínima em comparação com seus predecessores.

### **1. Opções Gerais**

Estas opções controlam o comportamento geral e a aparência do add-on.

*   **`book symbol`**: (string)
    *   Um símbolo (ex: "{") que, se presente no nome de um baralho, pode ser usado por lógica customizada (atualmente não implementado nesta versão simplificada para coloração/comportamento especial).
    *   Padrão: `"{`

*   **`color empty`**: (string, cor CSS)
    *   A cor usada para os nomes de baralhos que não possuem cartões novos (não vistos).
    *   Padrão: `"red"`

*   **`color empty descendant`**: (string, cor CSS)
    *   A cor usada para os nomes de baralhos que possuem um sub-baralho sem cartões novos (não vistos).
    *   Padrão: `"green"`

*   **`color zero`**: (booleano ou string de cor CSS)
    *   Controla como os valores zero nas colunas são exibidos.
    *   Se `false` (padrão neste add-on): Valores zero não são mostrados (célula aparece vazia).
    *   Se uma string (ex: `"#e0e0e0"` ou `"grey"`): Valores zero são exibidos nesta cor.
    *   Se `null`: Usa a cor padrão da coluna.
    *   Padrão: `false`

*   **`default column color`**: (string, cor CSS)
    *   A cor padrão para o texto dentro das colunas customizadas se nenhuma cor específica for definida para aquela coluna ou para valores zero.
    *   Padrão: `"grey"`

*   **`do color empty`**: (booleano)
    *   Se `true`, habilita a coloração dos nomes dos baralhos com base em `color empty` e `color empty descendant`.
    *   Padrão: `true`

*   **`end symbol`**: (string)
    *   Um símbolo (ex: ";") que, se presente no nome de um baralho, significa que o baralho é considerado "finalizado". Isso pode afetar a coloração se `do color empty` for verdadeiro (baralhos finalizados podem não ser coloridos como "vazios").
    *   Padrão: `";"`

*   **`given up symbol`**: (string)
    *   Similar ao `end symbol`, um símbolo (ex: "/") para baralhos considerados "desistidos".
    *   Padrão: `"/"`

*   **`hide values of parent decks`**: (booleano)
    *   Se `true`, os números na linha de um baralho pai são ocultados se ele tiver filhos.
    *   Padrão: `false`

*   **`hide values of parent decks when subdecks are shown`**: (booleano)
    *   Similar ao anterior, mas oculta os números do baralho pai apenas se seus sub-baralhos estiverem expandidos (visíveis).
    *   Padrão: `false`

*   **`option`**: (booleano)
    *   Se `true`, exibe o nome do grupo de opções do baralho no final de sua linha.
    *   Padrão: `true`

*   **`pause symbol`**: (string)
    *   Similar ao `end symbol`, um símbolo (ex: "=") para baralhos considerados "pausados".
    *   Padrão: `"="`

### **2. Configuração das Colunas (`columns`)**

Este é um array de objetos, onde cada objeto define uma coluna a ser exibida no navegador de baralhos. A ordem neste array determina a ordem de exibição das colunas.

Cada objeto de coluna possui as seguintes propriedades:

*   **`name`**: (string, interno)
    *   O identificador interno para o tipo de dado da coluna (ex: `"new today"`, `"cards"`, `"bar"`).
    *   **NÃO altere este valor**, pois é usado para buscar os dados corretos.

*   **`description`**: (string, Inglês)
    *   Uma breve descrição em inglês do que a coluna representa. Isto é primariamente para referência ao editar o `config.json` e **não é exibido** na interface do Anki.

*   **`header_key`**: (string, chave de tradução)
    *   Uma chave usada para buscar o texto traduzido do cabeçalho para esta coluna na seção `translation_maps`.
    *   Exemplo: `"col_new_today_header"`

*   **`overlay_key`**: (string, chave de tradução)
    *   Uma chave usada para buscar o texto traduzido da dica de ferramenta (mostrada ao passar o mouse) para esta coluna na seção `translation_maps`.
    *   Exemplo: `"col_new_today_overlay"`

*   **`present`**: (booleano)
    *   Se `true`, a coluna é exibida. Se `false`, é ocultada.
    *   Padrão (se omitido): `true`

*   **`color`**: (string, cor CSS, ou `null`)
    *   A cor para os números/texto nesta coluna.
    *   `null` usa um esquema de cores padrão (frequentemente das estatísticas embutidas do Anki ou `default column color`).
    *   Exemplo: `"blue"`, `"#FF0000"`

*   **`absolute`**: (booleano)
    *   Se `true`, exibe números absolutos.
    *   Padrão (se omitido e `percent` for `false`): `true`

*   **`percent`**: (booleano)
    *   Se `true`, exibe valores como porcentagens (geralmente relativo ao número total de cartões no baralho/sub-baralhos).
    *   Padrão (se omitido): `false`

*   **`subdeck`**: (booleano)
    *   Se `true`, os cálculos para esta coluna incluem cartões de sub-baralhos.
    *   Se `false`, os cálculos são apenas para o baralho atual.
    *   Padrão (se omitido): `true` é comum para visualizações agregadas.

*   **`names`**: (array de strings, apenas para colunas do tipo `bar`)
    *   Se `name` for `"bar"`, este array lista os nomes internos de outras colunas cujos valores devem fazer parte desta barra de progresso.
    *   Exemplo: `["mature", "young", "learning card", "unseen"]`

### **3. Mapas de Tradução (`translation_maps`)**

Esta seção contém as strings traduzidas para cabeçalhos e dicas de ferramenta.

*   **`translation_maps`**: (objeto)
    *   Um objeto de nível superior.
    *   Dentro dele, crie sub-objetos para cada código de idioma suportado (ex: `"en"`, `"pt_BR"`).
    *   Cada sub-objeto de idioma contém pares de chave-valor, onde a chave é uma `header_key` ou `overlay_key` (conforme definido na seção `columns`) e o valor é a string traduzida para aquele idioma. HTML pode ser usado nestas strings (ex: `<br/>` para quebras de linha).

    ```json
    "translation_maps": {
        "en": {
            "col_new_today_header": "NewToday",
            "col_new_today_overlay": "New cards for today",
            // ... outras traduções em inglês
        },
        "pt_BR": {
            "col_new_today_header": "NovHoje",
            "col_new_today_overlay": "Cartões novos para hoje",
            // ... outras traduções em português
        }
        // ... outros idiomas se suportados
    }
    ``` 