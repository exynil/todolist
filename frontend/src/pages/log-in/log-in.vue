<template>
  <q-layout>
    <q-page-container>
      <q-page class="row justify-center items-center">
        <q-card flat bordered>
          <q-card-section class="bg-blue">
            <h4 class="text-h4 text-white q-my-xl">Вход</h4>
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
              @keydown.enter.prevent="onLogIn"
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
              @keydown.enter.prevent="onLogIn"
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

            <div class="q-mt-md" align="center">
              <q-btn
                size="lg"
                color="blue"
                class="full-width text-white"
                label="Войти"
                @click="onLogIn"
              />
            </div>

            <div class="q-mt-md" align="center">
              <span
                class="text-primary cursor-pointer"
                to="/sign-up"
                @click="$router.push('/sign-up')"
              >
                Создать аккаунт
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

const router = useRouter();

const usernameRef = ref(null);
const passwordRef = ref(null);

const form = ref({
  username: null,
  password: null,
});

const visibility = ref(false);

const passwordFieldType = computed(() => (visibility.value ? "text" : "password"));

const visibilityIcon = computed(() => (visibility.value ? "visibility_off" : "visibility"));

const onLogIn = async () => {
  usernameRef.value.validate();
  passwordRef.value.validate();

  if (usernameRef.value.hasError || passwordRef.value.hasError) return;

  const formData = new FormData();
  formData.append("username", form.value.username.toLowerCase());
  formData.append("password", form.value.password);

  await Auth.login(formData)
    .then((r) => {
      localStorage.setItem("token", r.data.authToken);
      router.push("/");
    })
    .catch((e) => {});
};

document.title = "Вход";
</script>
