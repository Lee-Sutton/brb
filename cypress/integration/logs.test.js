describe('user logs test suite', function () {
    const user = {
        username: 'dummyUser',
        password: 'password123',
        email: 'e@e.com',
    };

    beforeEach(() => {
        cy.resetDb();
        cy.visit('/');
        cy.seedUserAndLogin(user);
    });

    it('should allow the user to create a new log', () => {
        cy.get('nav').contains('Logs').click();
        cy.contains('Add Log').should('be.visible');
        cy.get('[data-cy=create-log]').click();

        cy.get('form').within(() => {
            cy.get('#id_content').type('dummy content');
            cy.root().submit();
        });

        cy.get('[data-cy=log-table]').should('be.visible');
    });
});
