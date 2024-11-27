describe('Visualização dos pontos de coleta através do mapa', () => {
    it('O usuário doador, acessará o mapa com pontos de doações', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/mapeamento/"]').click()
      
     
    })
    
  })

  //Não existem casos extra pra esse teste, por isso ta pequeno assim...