
# Relatório de Testes - SauceDemo

## TC-001: Login bem-sucedido

**Objetivo:** Verificar se o login é realizado com sucesso usando credenciais válidas

**Passos Executados:**
1. Acessar https://www.saucedemo.com/
2. Preencher campo usuário com "standard_user"
3. Preencher campo senha com "secret_sauce"
4. Clicar no botão de login

**Dados de Entrada:**
- Usuário: standard_user
- Senha: secret_sauce

**Resultado Esperado:**
- Deve ser redirecionado para a página de produtos (/inventory.html)
- Container de produtos deve ser exibido

**Resultado Obtido:**
- Redirecionamento realizado com sucesso
- Elemento com ID 'inventory_container' encontrado e visível
- Log do teste:  
  ```
  TC-001 - Login válido - Início: [24/04/2025|19:35]
  TC-001 - Resultado: Passou - Fim: [24/04/2025|19:35]
  ```

**Status:** Passou

---

## TC-002: Login mal-sucedido

**Objetivo:** Verificar mensagem de erro com credenciais inválidas

**Passos Executados:**
1. Acessar https://www.saucedemo.com/
2. Preencher campo usuário com "invalid_user"
3. Preencher campo senha com "wrong_password"
4. Clicar no botão de login

**Dados de Entrada:**
- Usuário: invalid_user
- Senha: wrong_password

**Resultado Esperado:**
- Mensagem de erro deve ser exibida:  
  "Epic sadface: Username and password do not match any user in this service"

**Resultado Obtido:**
- Elemento de erro encontrado com texto esperado
- Log do teste:  
  ```
  TC-002 - Login inválido - Início: [24/04/2025|19:35]
  TC-002 - Resultado: Passou - Fim: [24/04/2025|19:35]
  ```

**Status:** Passou

---

**Execução dos Testes:**
- Ambos os casos de teste foram executados com sucesso
- Tempo total de execução: ~8-12 segundos (dependendo da conexão)
- Nenhum erro ou exceção encontrado durante a execução
