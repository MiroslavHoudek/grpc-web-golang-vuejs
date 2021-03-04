<template>
  <q-card inline style="width: 350px; max-width: 90vw">
    <q-card-section>
      <!-- <img src="/statics/img/todo.jpg"> -->
      <q-icon name="cloud" />
      <q-list no-border>
        <q-item>
          <q-item-section>
            <q-btn
              round
              small
              icon="add"
              color="red"
              :disabled="!newTask.trim()"
              @click="addNewTask"
            />
          </q-item-section>
          <q-item-label>
            <q-input
              type="text"
              v-model='newTask'
              placeholder="Add a new task"
              @keyup.enter="addNewTask"
            />
          </q-item-label>
        </q-item>
      </q-list>
    </q-card-section>
    <q-card-section>
      <div>
        <q-list inset-separator no-border>
          <todo-item
            v-for="(task, index) in filteredList"
            :item="task"
            :key="index"
          >
          </todo-item>
        </q-list>
      </div>
    </q-card-section>
    <q-separator />
    <q-card-actions align="center">
      <q-select
        radio
        v-model="selectedFilter"
        :options="filters"
      />
    </q-card-actions>
  </q-card>
</template>

<script>

async function getTodoList () {
  const req = new this.proto.Empty()
  return this.client.getTodoList(req, {})
}

import {
  QCard,
  QCardActions,
  QCardSection,
  QBtn,
  QInput,
  QList,
  QSelect,
  QItem,
  QItemLabel,
  QItemSection
} from 'quasar'

import TodoItem from './TodoItem'

import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  components: {
    QCard,
    QCardActions,
    QCardSection,
    QBtn,
    QInput,
    QList,
    QItem,
    QItemLabel,
    QItemSection,
    QSelect,
    TodoItem
  },
  data () {
    return {
      newTask: '',
      selectedFilter: 'all',
      filters: [
        {
          label: 'All',
          value: 'all'
        },
        {
          label: 'TO-DO',
          value: 'todo'
        },
        {
          label: 'Completed',
          value: 'completed'
        }
      ]
    }
  },
  computed: {
    ...mapState({
      todoList: state => state.todoList.list
    }),
    ...mapGetters('todoList', [
      'incompleteTasks',
      'completedTasks'
    ]),
    filteredList () {
      if (this.selectedFilter === 'all') {
        return this.todoList
      } else if (this.selectedFilter === 'todo') {
        return this.incompleteTasks
      } else if (this.selectedFilter === 'completed') {
        return this.completedTasks
      } else {
        return this.todoList
      }
    }
  },
  methods: {
    ...mapActions('todoList', [
      'addTask'
    ]),
    addNewTask (e) {
      // this.state = getTodoList()
      const res = getTodoList()

      let text = this.newTask.trim()
      if (text) {
        this.addTask(text)
      }
      this.newTask = ''
    }
  }
}
</script>

<style lang="stylus">
</style>
