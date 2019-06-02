import {Database} from '@vuex-orm/core'
import Score from '@/models/score'

const database = new Database();

database.register(Score, {});

export default database;
