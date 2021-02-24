<template>
  <q-item
    tag="label"
    @click.prevent
  >
    <q-item-section>
      <q-checkbox
        :value="item.done"
        checked-icon="done"
        unchecked-icon="radio_button_unchecked"
        color="green"
        @change="toggleTask({ task: item })"
      />
    </q-item-section>
    <q-item-label>
      <q-item-section
        label
        v-show="!editing"
        style="cursor: text"
        :class="{ 'task-done': item.done }"
        v-touch-swipe.horizontal="swipeTask"
        @click="inEditMode"
      >
        {{ item.text }}
      </q-item-section>
      <q-input
        ref="taskInput"
        :value="item.text"
        v-show="editing"
        @blur="doneEditing"
        @keyup.enter="doneEditing"
        @keyup.esc="cancelEditing"
      />
    </q-item-label>
    <q-item-section right icon="more_vert">
      <q-menu ref="popover">
        <q-list link>
          <q-item
            @click="inEditMode(); $refs.popover.close()"
          >
            <q-item-label label="Edit" />
          </q-item>
          <q-item
            @click="deleteTask({ task: item }); $refs.popover.close()"
          >
            <q-item-label label="Delete" />
          </q-item>
        </q-list>
      </q-menu>
    </q-item-section>
  </q-item>
  <!-- <li>
    <input type="checkbox" @change="toggleTask({ task: item })">
    <label v-show="!editing" @dblclick="inEditMode">
      {{ item.text }}
    </label>
    <input type="text" v-item-focus="editing" :value="item.text" v-show="editing" @blur="doneEditing" @keyup.enter="doneEditing" @keyup.esc="cancelEditing">

  </li> -->
</template>

<script>
import {
  QCheckbox,
  // QBtn,
  QInput,
  // QField,
  QItem,
  QItemLabel,
  // QItemTile,
  // QItemMain,
  // QItemSide,
  QItemSection,
  TouchSwipe,
  // QPopover,
  QList,
  QMenu
} from 'quasar'
import { mapActions } from 'vuex'

export default {
  components: {
    QCheckbox,
    // QBtn,
    QInput,
    // QField,
    QItem,
    QItemLabel,
    QItemSection,
    // QItemTile,
    // QItemMain,
    // QItemSide,
    // QPopover,
    QList,
    QMenu
  },
  props: ['item'],
  data () {
    return {
      editing: false
    }
  },
  template: '',
  methods: {
    ...mapActions('todoList', [
      'editTask',
      'toggleTask',
      'deleteTask'
    ]),
    inEditMode: function () {
      if (this.item.done) { return }

      this.editing = true
      this.$nextTick(() => {
        this.$refs.taskInput.focus()
        this.$refs.taskInput.select()
      })
    },
    doneEditing (e) {
      const value = e.target.value.trim()
      const task = this.item

      if (!value) {
        this.deleteTask({ task })
      } else if (this.editing) {
        this.editTask({ task: task, newText: value })
        this.editing = false
      }
    },
    cancelEditing: function () {
      this.editing = false
    },
    swipeTask: function ({ evt, direction, duration, distance }) {
      if (this.item.done) {
        return
      }

      const item = this.item
      if (direction === 'right' && distance.x >= 70) {
        this.toggleTask({ task: item })
      }
    }
  },
  directives: {
    TouchSwipe
  }
}
</script>
<style lang="stylus">
  .task-done
    text-decoration line-through
</style>
