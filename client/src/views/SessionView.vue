<template>
  <div class="about">
    <h1 class="text-4xl text-center my-8">Session</h1>
  </div>
  <div class="grid grid-cols-2">
    <div class="flex flex-col rounded-2xl w-96 bg-[#ffffff] shadow-xl">
      <div class="flex flex-col p-8">
          <div class="text-2xl font-bold   text-[#374151] pb-6">Crée Session</div>
          <div class=" text-lg   text-[#374151]">Crée une nouvelle session.</div>
          <div class="flex justify-end pt-6">
              <button class="bg-[#7e22ce] text-[#ffffff]  font-bold text-base  p-3 rounded-lg hover:bg-purple-800 active:scale-95 transition-transform transform">Créé</button>
          </div>
      </div>
    </div>
    <div class="flex flex-col rounded-2xl w-96 bg-[#ffffff] shadow-xl">
      <div class="flex flex-col p-8">
          <div class="text-2xl font-bold   text-[#374151] pb-6">Voir et Modifier une Session</div>
          <div class=" text-lg   text-[#374151]">Voir et modifier une session.</div>
          <div class="flex justify-end pt-6">
              <button class="bg-[#7e22ce] text-[#ffffff]  font-bold text-base  p-3 rounded-lg hover:bg-purple-800 active:scale-95 transition-transform transform">Voir</button>
          </div>
      </div>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
<script setup lang="ts">
</script>