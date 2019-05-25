import faker from 'faker';
import {RouterLinkStub, mount} from '@vue/test-utils';
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
    wrapper = mount(Accounts, {
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

    wrapper.find('#id_username').setValue(user.username);
    wrapper.find('#id_email').setValue(user.email);
    wrapper.find('#id_password').setValue(user.password);
    wrapper.find('#id_password_confirm').setValue(user.password);
    wrapper.find('form').trigger('submit');

    expect($store.dispatch).toHaveBeenCalledWith('signup', {
        username: user.username,
        email: user.email,
        password1: user.password,
        password2: user.password,
    });
    await flushPromises();

    // The user is directed back to the home page
    expect($router.push).toHaveBeenCalledWith('/');
});

// test('should allow the user to cancel', function () {
//     const routerStubs = wrapper.findAll(RouterLinkStub);
//     expect(routerStubs.at(0).props().to).toEqual({name: 'home'});
// });
