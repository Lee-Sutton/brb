import {shallowMount} from '@vue/test-utils';
import Home from '@/views/Home.vue';

describe('Accounts.vue', () => {
    it('renders props.msg when passed', () => {
        const msg = 'new message';
        const wrapper = shallowMount(Home, {
            stubs: ['router-link']
        });
        expect(wrapper.text()).toContain('Create an account to get started')
    });
});
