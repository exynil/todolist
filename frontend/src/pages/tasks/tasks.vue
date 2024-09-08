<template>
  <q-card flat bordered class="bg-grey-1">
    <q-card-section>
      <q-table
        :rows="tasks"
        :columns="columns"
        row-key="name"
        separator="cell"
        :pagination="{ rowsPerPage: 15 }"
        :visible-columns="visibleColumns"
        :wrap-cells="true"
        class="my-sticky-column-table"
      >
        <template #top="props">
          <div class="text-uppercase">Задачи</div>

          <q-space />

          <q-toggle v-model="showId" icon="tag" />

          <q-btn flat round dense icon="add" @click="$refs.createTaskRef.show()" class="q-ml-md">
            <q-tooltip :delay="500"> Добавить </q-tooltip>
          </q-btn>

          <q-btn flat round dense icon="refresh" @click="loadTasks()" class="q-ml-md">
            <q-tooltip :delay="500"> Обновить </q-tooltip>
          </q-btn>

          <q-btn
            flat
            dense
            :icon="props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
            @click="props.toggleFullscreen"
            class="q-ml-md"
          />
        </template>

        <template #body-cell-createdAt="props">
          <q-td key="createdAt" :props="props">
            {{ shortDate(props.row.createdAt) }}
          </q-td>
        </template>

        <template #body-cell-status="props">
          <q-td key="status" :props="props">
            <q-toggle
              color="blue"
              checked-icon="check"
              :false-value="TaskStatus.ACTIVE"
              :true-value="TaskStatus.COMPLETED"
              :modelValue="props.row.status"
              @update:model-value="() => onStatusChange(props.row.id)"
            />
          </q-td>
        </template>

        <template #body-cell-action="props">
          <q-td :props="props">
            <div class="row q-gutter-sm">
              <q-btn-group push>
                <q-btn
                  color="primary"
                  icon-right="edit"
                  no-caps
                  flat
                  dense
                  @click="$refs.updateTaskRef.show(props.row)"
                >
                  <q-tooltip :delay="1000"> Редактировать </q-tooltip>
                </q-btn>
                <q-btn
                  color="negative"
                  icon-right="delete"
                  no-caps
                  flat
                  dense
                  @click="onDeleteTask(props.row.id)"
                >
                  <q-tooltip :delay="1000"> Удалить </q-tooltip>
                </q-btn>
              </q-btn-group>
            </div>
          </q-td>
        </template>

        <template #no-data>
          <div class="full-width row flex-center text-primary q-gutter-sm">
            <span> Нет данных </span>
          </div>
        </template>
      </q-table>
    </q-card-section>
  </q-card>

  <!-- Диалоговое окно добавления задачи -->
  <create-task-dialog ref="createTaskRef" @push-task="pushTask" />

  <!-- Диалоговое окно редактирования задачи -->
  <update-task-dialog ref="updateTaskRef" @update-task="updateTask" />
</template>

<script setup>
import { computed, ref, onMounted } from "vue";

import createTaskDialog from "./create-task/create-task-dialog.vue";
import updateTaskDialog from "./update-task/update-task-dialog.vue";

import { dialogConfirm } from "@/hooks";
import { shortDate } from "@/utils/formatters";

import { TaskStatus } from "@/enums";

import columns from "./columns";

import { Task } from "@/api";

const visibleColumns = computed(() => {
  return columns.filter((c) => c.name !== "id" || showId.value).map((c) => c.name);
});

const tasks = ref([]);
const showId = ref(false);

const pushTask = (task) => tasks.value.push(task);

const updateTask = (updatedTask) => {
  let task = tasks.value.find((t) => t.id === updatedTask.id);
  Object.assign(task, updatedTask);
};

const deleteTask = (taskId) => {
  let index = tasks.value.findIndex((t) => t.id === taskId);
  tasks.value.splice(index, 1);
};

const onDeleteTask = (taskId) => {
  const func = async () => {
    await Task.delete(taskId)
      .then((r) => deleteTask(taskId))
      .catch((e) => {});
  };

  dialogConfirm("Вы действительно хотите удалить?", func);
};

const onStatusChange = async (taskId) => {
  await Task.toggleStatus(taskId)
    .then((r) => {
      let task = tasks.value.find((t) => t.id === taskId);
      task.status = r.data.status;
    })
    .catch((e) => {})
}

const loadTasks = async () => {
  await Task.list()
    .then((r) => (tasks.value = r.data))
    .catch((e) => {});
};

onMounted(loadTasks);

document.title = "Задачи";
</script>
