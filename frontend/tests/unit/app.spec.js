import {mount} from '@vue/test-utils';
import App from '@/App'

const mockRoute = {
  $route: {
    meta: {
      title: 'Dummy Title'
    }
  }
};

test('It should render', () => {
  const wrapper = mount(App, {
    stubs: ['router-link', 'router-view'],
    mocks: {
      ...mockRoute,
      $store: {
        state: {isLoggedIn: true}
      }
    }
  });
  expect(wrapper.html).toBeTruthy();
});

