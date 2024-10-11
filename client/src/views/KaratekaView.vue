<template>
  <div class="about">
    <h1 class="text-4xl text-center my-8">Karateka</h1>
  </div>
  <div class="grid grid-ols-1 md:grid-cols-2 gap-2">
    <div class="flex flex-col rounded-2xl bg-[#ffffff] shadow-xl">
      <div class="flex flex-col p-8">
          <div class="text-2xl font-bold   text-[#374151] pb-6">Ajouté Karateka</div>
          <div class=" text-lg   text-[#374151]">Ajouté un nouveau Karateka.</div>
          <div class="flex justify-end pt-6">
                <button class="bg-[#7e22ce] text-[#ffffff]  font-bold text-base  p-3 rounded-lg hover:bg-purple-800 active:scale-95 transition-transform transform" @click="$router.push('/karateka/create')">Créé</button>
          </div>
      </div>
    </div>
    <div class="flex flex-col rounded-2xl bg-[#ffffff] shadow-xl">
      <div class="flex flex-col p-8">
          <div class="text-2xl font-bold   text-[#374151] pb-6">Modifier Karateka</div>
          <div class=" text-lg   text-[#374151]">Voir liste et modifier un Karateka.</div>
          <div class="flex justify-end pt-6">
            <button class="bg-[#7e22ce] text-[#ffffff]  font-bold text-base  p-3 rounded-lg hover:bg-purple-800 active:scale-95 transition-transform transform" @click="$router.push('/karateka/list')">Voir</button>
          </div>
      </div>
    </div>
  </div>
</template>

<style>

</style>
<script setup lang="ts">
</script>