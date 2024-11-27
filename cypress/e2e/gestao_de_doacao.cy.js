describe('O gestor de doações adicionará uma doação e tentará ver se a doação está salva no banco de dados', () => {
    it('O administrador conseguirá cadastrar uma doação e ver ela', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('nav > .cta').click()
      cy.get('#id_username').type('tenam')
      cy.get('#id_password').type('1234')
      cy.get('.submit-row > input').click()
      cy.get('.model-doacao > :nth-child(2) > .addlink').click()
      cy.get('#id_doador').select('doador 1')
      cy.get('#id_tipo_material').type('material do tipo xxx')
      cy.get('#id_quantidade')
      cy.get('#id_quantidade').type('5')
      cy.get('#id_produto').type('produto exemplo 1')
      cy.get('.default').click()
      cy.get('#app15-doador > a').click()
      cy.get('.field-__str__ > a').click()
    })

    it('O usuário vai tentar salvar uma doação sem informar o tipo do material', () => {
  
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-doacao > :nth-child(2) > .addlink').click()
        cy.get('#id_doador').select('doador 1')
        cy.get('#id_quantidade')
        cy.get('#id_quantidade').type('5')
        cy.get('#id_produto').type('produto exemplo 1')
        cy.get('.default').click()

    })

    it('O administrador tentará salvar uma doação sem informar o produto doado', () => {
  
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-doacao > :nth-child(2) > .addlink').click()
        cy.get('#id_doador').select('doador 1')
        cy.get('#id_tipo_material').type('material do tipo xxx')
        cy.get('#id_quantidade')
        cy.get('#id_quantidade').type('5')
        cy.get('.default').click()
    })

    it('O administrador tentará salvar uma doação sem informar a quantidade de produtos/materiais doados', () => {
  
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-doacao > :nth-child(2) > .addlink').click()
        cy.get('#id_doador').select('doador 1')
        cy.get('#id_tipo_material').type('material do tipo xxx')
        cy.get('#id_produto').type('produto exemplo 1')
        cy.get('.default').click()
    
    })
    
})