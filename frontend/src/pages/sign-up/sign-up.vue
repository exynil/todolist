<template>
  <q-layout>
    <q-page-container>
      <q-page class="row justify-center items-center">
        <q-card flat bordered>
          <q-card-section class="bg-blue">
            <h4 class="text-h4 text-white q-my-xl">Регистрация</h4>
          </q-card-section>

          <q-card-section>
            <q-input
              ref="usernameRef"
              v-model.trim="form.username"
              outlined
              lazy-rules="ondemand"
              :rules="[required]"
              type="username"
              label="Пользователь"
              @keydown.enter.prevent="onSignUp"
              :autofocus="true"
            >
              <template #prepend>
                <q-icon name="person" />
              </template>
              <template #append>
                <q-icon name="close" @click="form.username = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <q-input
              ref="passwordRef"
              class="q-mt-sm"
              v-model.trim="form.password"
              outlined
              :type="passwordFieldType"
              lazy-rules="ondemand"
              :rules="[required]"
              label="Пароль"
              @keydown.enter.prevent="onSignUp"
            >
              <template #prepend>
                <q-icon name="lock" />
              </template>
              <template #append>
                <q-icon
                  :name="visibilityIcon"
                  @click="visibility = !visibility"
                  class="cursor-pointer"
                />
                <q-icon name="close" @click="form.password = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <q-input
              ref="password2Ref"
              class="q-mt-sm"
              v-model.trim="form.password2"
              outlined
              :type="passwordFieldType"
              lazy-rules="ondemand"
              :rules="[required]"
              label="Пароль"
              @keydown.enter.prevent="onSignUp"
            >
              <template #prepend>
                <q-icon name="lock" />
              </template>
              <template #append>
                <q-icon
                  :name="visibilityIcon"
                  @click="visibility = !visibility"
                  class="cursor-pointer"
                />
                <q-icon name="close" @click="form.password2 = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <div class="q-mt-md" align="center">
              <q-btn
                size="lg"
                color="blue"
                class="full-width text-white"
                label="Создать"
                @click="onSignUp"
              />
            </div>

            <div class="q-mt-md" align="center">
              <span
                class="text-primary cursor-pointer"
                to="/sign-up"
                @click="$router.push('/log-in')"
              >
                У меня уже есть аккаунт
              </span>
            </div>
          </q-card-section>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, computed } from "vue";
import { required } from "@/utils/validators";
import { Auth } from "@/api";
import { useRouter } from "vue-router";
import { Notify } from "quasar";

const router = useRouter();

const usernameRef = ref(null);
const passwordRef = ref(null);
const password2Ref = ref(null);

const form = ref({
  username: null,
  password: null,
  password2: null,
});

const visibility = ref(false);

const passwordFieldType = computed(() => (visibility.value ? "text" : "password"));

const visibilityIcon = computed(() => (visibility.value ? "visibility_off" : "visibility"));

const onSignUp = async () => {
  usernameRef.value.validate();
  passwordRef.value.validate();
  password2Ref.value.validate();

  if (
    usernameRef.value.hasError ||
    passwordRef.value.hasError ||
    password2Ref.value.hasError
  )
    return;

  if (form.value.password !== form.value.password2) {
    Notify.create({ type: "warning", timeout: 5000, message: "Пароли не совпадают" });
    return;
  }

  const formData = new FormData();
  formData.append("username", form.value.username.toLowerCase());
  formData.append("password", form.value.password);

  await Auth.signup(formData)
    .then((r) => {
      router.push("/log-in");
    })
    .catch((e) => {});
};

document.title = "Регистрация";
</script>
