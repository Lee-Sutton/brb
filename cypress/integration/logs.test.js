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
        cy.contains('Create a new log').should('be.visible');
        cy.get('[data-cy=new-log-btn]').click();
    });
});
