<template>
  <footer
    class="
      h-[6%]
      bg-[#6dbbe9]
      flex items-center"
  >
    <div class="flex items-center">
      <a
        className="git-link"
        href="https://github.com/anim3x/koshka"
        target="_blank">
        <img
          src="/src/assets/github-ico.png"
          class="w-7 h-7 ml-4">
      </a>
      <span
        class="
      text-white text-xl
      ml-2
    "> 
        koshka v1.1
      </span>
    </div>
    <div class="ml-auto flex items-center">
      <img
        src="/src/assets/pogoda.jpg"
        class="w-8 h-8 mr-2"
      >
      <span
        class="
        text-white text-xl mr-2">
        {{ city }} {{ temp }}°C</span>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '/src/api.js';

const city = ref('');
const temp = ref('');

function getWeather(pos) {
    api.post('/pogoda', {
      latitude: pos.coords.latitude,
      longitude: pos.coords.longitude,
    })
    .then((resp)=>{ 
      // console.log(resp.data['city']);
      city.value = resp.data['city'];
      temp.value = resp.data['temp'];
    });
};

onMounted(() => {
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      // console.log(pos.coords);
      getWeather(pos);
    },
    (error) => {
      console.error('Ошибка получения геолокации:', error.message);
    },
  );
});
</script>