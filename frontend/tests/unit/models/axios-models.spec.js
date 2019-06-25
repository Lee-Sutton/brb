import AxiosModel from '@/models/axios-model';
import {HOST_URL} from '@/models/axios-model';
import axios from 'axios';

class DummyScoreModel extends AxiosModel {
  static entity = 'scores';

  static fields() {
    return {
      id: this.attr(null),
      score: this.number(0),
    }
  }
}

afterEach(() => {
  jest.resetAllMocks();
});

test('it should fetch documents from the api', async () => {
  const mockStore = {
    insert: jest.fn(),
    entity: 'scores'
  };

  await DummyScoreModel.$fetch.apply(mockStore);
  expect(axios.get).toHaveBeenCalledWith(`${HOST_URL}/api/v1/scores`);
});


test('create records', async () => {
  const record = new DummyScoreModel({
    score: 20
  });

  axios.post.mockResolvedValue(201);
  const result = await DummyScoreModel.$create(record);
  expect(result).toEqual(201);

  expect(axios.post).toHaveBeenCalledWith(
    `${HOST_URL}/api/v1/scores`,
    record.$toJson()
  );
});


test('update records', async () => {
  const record = new DummyScoreModel({
    score: 20,
    id: 1,
  });

  axios.put.mockResolvedValue(201);
  const result = await DummyScoreModel.$update(record);
  expect(result).toEqual(201);

  expect(axios.put).toHaveBeenCalledWith(
    `${HOST_URL}/api/v1/scores/${record.id}`,
    record.$toJson()
  );
});
