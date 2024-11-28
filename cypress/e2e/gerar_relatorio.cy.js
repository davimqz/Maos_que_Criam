describe('template spec', () => {
    it('o usuario vai ter acesso a relatorios de doacoes distribuidos em ,Data da Doação,Material,Quantidade e Doador ', () => {
      cy.visit('http://127.0.0.1:8000/')
      cy.get('.dropdown > :nth-child(1)').click()
      cy.visit('http://127.0.0.1:8000/relatorio/')

        
    })
      
  })
  