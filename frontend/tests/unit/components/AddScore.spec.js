import {mount} from '@vue/test-utils';
import AddScore from '@/components/AddScore';
const $route = {

};

test('it should render', () => {
  const wrapper = mount(AddScore, {
    mocks: {
    }
  });
  expect(wrapper.html()).toBeTruthy();
});
