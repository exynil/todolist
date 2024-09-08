<template>
  <q-form @submit="onSubmit()">
    <div class="row">
      <div class="col-12">
        <p v-required-marker class="text-grey-7 q-mb-none">Название</p>
        <q-input
          dense
          outlined
          v-model.trim="form.title"
          lazy-rules="ondemand"
          :rules="[required, (val) => maxLength(val, 255)]"
        />
      </div>

      <div class="col-12">
        <p class="text-grey-7 q-mb-none">Описание</p>
        <q-input
          dense
          outlined
          v-model.trim="form.description"
          lazy-rules="ondemand"
          autogrow
        />
      </div>
    </div>

    <div class="q-pt-md q-gutter-sm" align="center">
      <q-btn label="Сохранить" type="submit" color="primary" />
      <q-btn flat label="Отменить" v-close-popup />
    </div>
  </q-form>
</template>

<script setup>
import { ref } from "vue";

import { required, maxLength } from "@/utils/validators";

const props = defineProps({
  task: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["onSubmit"]);

const form = ref({
  title: props.task.title,
  description: props.task.description,
});

const onSubmit = async () => {
  const formData = new FormData();

  formData.append("title", form.value.title);
  formData.append("description", form.value.description);

  emit("onSubmit", formData);
};
</script>
