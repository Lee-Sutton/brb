describe('user logs test suite', function () {
    beforeEach(() => {
        cy.resetDb();
        cy.visit('http://localhost:8000');
        cy.seedUser();
    });

    it('should allow the user to create a new log', () => {

    });
});
