describe('template spec', () => {
    it('O administrador vai informar com sucesso o material em falta', () => {
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-necessidade > :nth-child(2) > .addlink').click()
        cy.get('#id_item').type('papelão')
        cy.get('#id_prioridade').select('Alta')
        cy.get('#id_detalhes').type('Detalhes em relação a necessidade do material exemplo teste...')
        cy.get('.default').click()
    })

    it('O administrador não vai fornecer detalhes em relação a necessidade do material e vai tentar salvar', () => {
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-necessidade > :nth-child(2) > .addlink').click()
        cy.get('#id_item').type('papelão')
        cy.get('#id_prioridade').select('Alta')
        cy.get('.default').click()
    })

    it('O administrador não vai informar o material necessário para doação e vai tentar salvar', () => {
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-necessidade > :nth-child(2) > .addlink').click()
        cy.get('#id_prioridade').select('Alta')
        cy.get('#id_detalhes').type('Detalhes em relação a necessidade do material exemplo teste...')
        cy.get('.default').click()
    })

    it('O administrador não vai informar o nivel de necessidade do produto requisitado e vai tentar salvar', () => {
        cy.visit('http://127.0.0.1:8000/')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('tenam')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-necessidade > :nth-child(2) > .addlink').click()
        cy.get('#id_item').type('papelão')
        cy.get('#id_detalhes').type('Detalhes em relação a necessidade do material exemplo teste...')
        cy.get('.default').click()
    })
    
})