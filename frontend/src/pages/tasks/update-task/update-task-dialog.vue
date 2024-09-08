<template>
  <q-dialog v-model="dialog">
    <q-card class="q-pa-sm">
      <q-card-section>
        <p class="text-uppercase q-mt-md">Редактирование задачи</p>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <form-data :task="selectedTask" @on-submit="onSubmit" />
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref } from "vue";
import { Loading } from "quasar";

import formData from "./form-data.vue";

import { Task } from "@/api";

const emit = defineEmits(["updateTask"]);

const dialog = ref(false);

const selectedTask = ref(null);

const onSubmit = async (formData) => {
  Loading.show();

  await Task.update(selectedTask.value.id, formData)
    .then((r) => {
      emit("updateTask", r.data);
      hide();
    })
    .catch((e) => {});

  Loading.hide();
};

const show = (task) => {
  selectedTask.value = task;

  dialog.value = true;
};

const hide = () => (dialog.value = false);

defineExpose({ show });
</script>
