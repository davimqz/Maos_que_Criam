describe('template spec', () => {
  it('o usuario vai ter acesso a um historico de doacoes', () => {
    cy.visit('http://127.0.0.1:8000/')
    cy.get('.dropdown > :nth-child(1)').click()
    cy.visit('http://127.0.0.1:8000/historico-doacoes/')
    cy.scrollTo('bottom');
      
  })
    
})
