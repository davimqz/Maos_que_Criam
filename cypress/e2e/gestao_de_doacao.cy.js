describe('O gestor de doações adicionará uma doação e tentará ver se a doação está salva no banco de dados', () => {
    it('O administrador conseguirá cadastrar uma doação e ver ela', () => {
  
      cy.visit('http://127.0.0.1:8000')
      cy.get('nav > .cta').click()
      cy.get('#id_username').type('AdmMestre')
      cy.get('#id_password').type('098')
      cy.get('.submit-row > input').click()
      cy.get('.model-doacao > :nth-child(2) > .addlink').click()
      cy.get('#id_doador').select('lucas')
      cy.get('#id_tipo_material').type('plastico')
      cy.get('#id_quantidade').type('2')
      cy.get('#id_produto').type('brinquedo')
      cy.get('.default').click()

    })
    it('O administrador tentará cadastrar uma doação sem preencher um campo e falhará', () => {
  
        cy.visit('http://127.0.0.1:8000')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('AdmMestre')
        cy.get('#id_password').type('098')
        cy.get('.submit-row > input').click()
        cy.get('.model-doacao > :nth-child(2) > .addlink').click()
        cy.get('#id_doador').select('lucas')
        cy.get('#id_tipo_material').type('plastico')
        cy.get('#id_quantidade').type('2')
        cy.get('.default').click()
  
      })
    
    
})