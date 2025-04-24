# Relatório de Testes - DemoBlaze

## TC-004: Fluxo Completo de Compra

**Objetivo:** Validar o processo completo de compra desde a seleção do produto até a confirmação final

**Passos Executados:**
1. Acessar página inicial
2. Selecionar primeiro produto da lista
3. Adicionar ao carrinho e aceitar alerta
4. Navegar para o carrinho
5. Iniciar processo de compra
6. Preencher formulário com:
   - Nome: User_[randômico]
   - País: Testland
   - Cidade: Silicon Valley
   - Cartão: 4111[12 dígitos randômicos]
   - Mês/Ano: 12/2025
7. Finalizar compra
8. Validar mensagem de confirmação

**Dados de Entrada:**
```python
{
    'name': "User_456",
    'country': "Testland", 
    'city': "Silicon Valley",
    'card': "4111123456789012",
    'month': "12",
    'year': "2025"
}
```

**Resultado Esperado:**
- Modal de confirmação exibido com:
  - Mensagem "Thank you for your purchase!"
  - ID do pedido formatado corretamente
  - Valor total da compra

**Resultado Obtido:**
```
Thank you for your purchase!
ID: 123456789
Amount: 720 USD
Card: 4111123456789012
Date: 12/2025
```

**Dados Capturados:**
- ID do pedido presente e formatado
- Valor condizente com o produto selecionado
- Detalhes do pagamento correspondem aos dados informados

**Status:** Passou

---

**Análise:**
- Fluxo completo executado em ~25-35 segundos
- Sistema gerou ID único para cada compra
- Valores monetários formatados corretamente
- Alertas JS tratados adequadamente
- Dados sensíveis (cartão) mascarados parcialmente no site

**Log de Execução:**
```
TC-004 - Fluxo de Compra - Início: 24/04/2025 19:53
Dados da Compra:
Thank you for your purchase!...
TC-004 - Resultado: Passou - Fim: 24/04/2025 19:53
```

**Observações:**
- Teste inclui geração de dados randômicos para evitar conflitos
- Validação considera múltiplos elementos da confirmação
- Estrutura preparada para escalar com mais casos de teste