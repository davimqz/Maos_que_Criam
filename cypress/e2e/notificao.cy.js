describe('template spec', () => {
  it('o usuario vai ter acesso a notificacoes de necessidades das doacoes ', () => {
    cy.visit('http://127.0.0.1:8000/')
    cy.get('[href="/necessidades-especificas/"]').click()
      
  })
    
})



