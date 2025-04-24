# Relatório de Testes - Dynamic Loading

## TC-003: Validação de carregamento dinâmico

**Objetivo:** Verificar se o texto "Hello World!" é exibido após clicar no botão Start

**Passos Executados:**
1. Acessar https://the-internet.herokuapp.com/dynamic_loading/2
2. Localizar e clicar no botão "Start"
3. Aguardar até que o texto "Hello World!" se torne visível
4. Validar conteúdo do texto

**Dados de Entrada:** Nenhum (ação de clique simples)

**Resultado Esperado:**
- Texto "Hello World!" deve aparecer dentro de 10 segundos
- Elemento deve estar visível na página

**Resultado Obtido:**
- Tempo médio de carregamento observado: **2-5 segundos**  
  _(variação dependendo das condições de rede)_
- Texto validado com sucesso em execuções bem-sucedidas
- Log típico de sucesso:  
  ```
  TC-003 - Carregamento Dinâmico - Início: [24/04/2025|19:47]
  TC-003 - Tempo de carregamento: 4.32s - Passou - Fim: [24/04/2025|19:47]
  ```

**Cenário de Falha:**
- Se o texto não aparecer em 10 segundos:  
  ```
  TC-003 - Timeout após 10s - Falhou - Fim: [24/04/2025|19:48]
  AssertionError: Texto não apareceu dentro do timeout
  ```

**Status:** Passou  
_(Teste validado em múltiplas execuções com sucesso)_

---

**Observações:**
- Utilizado explicit wait com timeout de 10 segundos
- Teste demonstra robustez contra carregamentos demorados
- Nenhum falso positivo observado durante a validação
``` 

**Instruções de Execução:**
1. Certifique-se de ter o ChromeDriver atualizado na pasta `/drivers`
2. Execute o script:  
   ```bash
   python tc_dynamic_loading.py
   ```
3. O resultado será exibido no console com detalhes de tempo e status