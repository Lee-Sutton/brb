import faker from 'faker';
import {RouterLinkStub, shallowMount} from '@vue/test-utils';
import Accounts from '../../../src/components/Accounts.vue';
import flushPromises from 'flush-promises';

const $router = {
    push: jest.fn(),
};

const $store = {
    dispatch: jest.fn(),
};

let wrapper: any;

beforeEach(() => {
    wrapper = shallowMount(Accounts, {
        stubs: {
            RouterLink: RouterLinkStub,
        },
        mocks: {
            $router,
            $store,
        },
    });
    jest.resetAllMocks();
});

test('signup flow', async () => {
    const user = {
        username: faker.internet.userName(),
        email: faker.internet.email(),
        password: faker.internet.password(),
    };

    wrapper.find('[data-cy=username]').setValue(user.username);
    wrapper.find('[data-cy=email]').setValue(user.email);
    wrapper.find('[data-cy=password1]').setValue(user.password);
    wrapper.find('[data-cy=password2]').setValue(user.password);
    wrapper.find('form').trigger('submit');

    expect($store.dispatch).toHaveBeenCalledWith('signup', {
        username: user.username,
        email: user.email,
        password1: user.password,
        password2: user.password,
    });
    await flushPromises();

    // The user is directed back to the home page
    expect($router.push).toHaveBeenCalledWith('home');
});

// test('should allow the user to cancel', function () {
//     const routerStubs = wrapper.findAll(RouterLinkStub);
//     expect(routerStubs.at(0).props().to).toEqual({name: 'home'});
// });
