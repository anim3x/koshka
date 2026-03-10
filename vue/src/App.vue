<script setup>
import CatHeader from './components/CatHeader.vue';
import CatFooter from './components/CatFooter.vue';
import MainArea from './components/MainArea.vue';
</script>

<template>
  <div
    id="layout"
    class="
        h-screen w-[70%] mx-auto
        shadow-3xl
    ">
    <CatHeader />
    <MainArea />
    <CatFooter />
  </div>
</template>