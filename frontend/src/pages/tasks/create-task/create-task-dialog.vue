<template>
  <q-dialog v-model="dialog">
    <q-card class="q-pa-sm">
      <q-card-section>
        <p class="text-uppercase">Добавление новой задачи</p>
      </q-card-section>

      <q-card-section>
        <form-data @on-submit="onSubmit" />
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref } from "vue";
import { Loading } from "quasar";

import formData from "./form-data.vue";

import { Task } from "@/api";

const emit = defineEmits(["pushTask"]);

const dialog = ref(false);

const onSubmit = async (formData) => {
  Loading.show();

  await Task.create(formData)
    .then((r) => {
      emit("pushTask", r.data);
      hide();
    })
    .catch((e) => {});

  Loading.hide();
};

const show = () => (dialog.value = true);
const hide = () => (dialog.value = false);

defineExpose({ show });
</script>
