import AxiosModel from '@/models/axios-model';

class DummyScoreModel extends AxiosModel {
  static entity = 'scores';

  static fields() {
    return {
      id: this.attr(null),
      score: this.number(0),
    }
  }
}

test('it should fetch documents from the api', () => {
  DummyScoreModel.$fetch()
});


test('create records', () => {

});


test('update records', () => {

});
