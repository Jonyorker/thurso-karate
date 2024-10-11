<template>
  <div class="about">
    <h1 class="text-4xl text-center my-8">Créé Karateka</h1>
  </div>
  <div>
    <div class="mb-4 w-full">
      <label for="first_name">Prénom:</label>
      <input placeholder="Prénom" type="text" id="first_name" v-model="user.first_name" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="last_name">Nom:</label>
      <input placeholder="Nom" type="text" id="last_name"  v-model="user.last_name"  class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="aka_name">nickname:</label>
      <input placeholder="nickname" type="text" id="aka_name" v-model="user.aka_name" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="birthdate">Date de naissance:</label>
      <input placeholder="" type="date" id="birthdate" v-model="user.birth_date" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="belt">Genre:</label>
      <select v-model="user.gender_code" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none">
        <option disabled selected> - </option>
        <option value="MALE">Homme</option>
        <option value="FEMALE">Femme</option>
      </select>
    </div>
    <div class="mb-4 w-full">
      <label for="address">Addresse:</label>
      <input placeholder="123 Chemin Exemple" type="text" id="address" v-model="address.address" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="ville">Ville:</label>
      <input placeholder="Thurso" type="text" id="ville" v-model="address.city" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="postal_code">Code Postal:</label>
      <input placeholder="J0X 3B0" type="text" id="postal_code" v-model="address.postal_code" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="address_type">Type d'addresse:</label>
      <select v-model="address.address_type" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none">
        <option disabled selected> - </option>
        <option value="HOME">principale</option>
        <option value="MOM">mère</option>
        <option value="DAD">père</option>
      </select>
    </div>
    <div class="mb-4 w-full">
      <label for="phone_mom">Télephone Mère:</label>
      <input placeholder="819-985-1234" type="text" id="phone_mom" v-model="user.phone_mom" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="mom_name">Nom Mère:</label>
      <input placeholder="nom de la mère" type="text" id="mom_name" v-model="user.mom_name" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="phone_dad">Télephone Père:</label>
      <input placeholder="819-985-1234" type="text" id="phone_dad" v-model="user.phone_dad" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="dad_name">Nom Père:</label>
      <input placeholder="nom du père" type="text" id="dad_name" v-model="user.dad_name" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none" />
    </div>
    <div class="mb-4 w-full">
      <label for="active">Actif:</label>
      <input placeholder="Prénom" type="checkbox" id="active" v-model="user.active" class="rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none ml-4" />
    </div>
    <div class="mb-4 w-full">
      <label for="belt">Ceinture:</label>
      <select v-model="user.belt" class="w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none">
        <option disabled selected> - </option>
        <option value="WHITE">Blanche</option>
        <option value="WHITE_1">Blanche 1 bar</option>
        <option value="WHITE_2">Blanche 2 bar</option>
        <option value="WHITE_3">Blanche 3 bar</option>
        <option value="YELLOW">Jaune</option>
        <option value="ORANGE">Orange</option>
        <option value="GREEN">Verte</option>
        <option value="BLUE">Bleu</option>
        <option value="BROWN">Brune</option>
        <option value="BLACK_1">Noir</option>
        <option value="BLACK_2">Noir 2 dan</option>
        <option value="BLACK_3">Noir 3 dan</option>

      </select>
    </div>
    <div class="mb-4 w-full">
      <label for="notes">Notes:</label>
      <textarea id="notes" rows="4" v-model="user.notes" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Note..."></textarea>    </div>
    <div class="flex justify-end pt-6">
      <button @click="submit" class="bg-[#7e22ce] text-[#ffffff]  font-bold text-base  p-3 rounded-lg hover:bg-purple-800 active:scale-95 transition-transform transform">Sauvegade</button>
    </div>
  </div>
</template>

<style>

</style>
<script>
export default {
  data() {
    return {
      user: {
        first_name: '',
        last_name: '',
        aka_name: '',
        birth_date: '2000-01-01',
        gender_code: '',
        phone_mom: '',
        phone_dad: '',
        mom_name: '',
        dad_name: '',
        active: true,
        belt: 'WHITE',
        notes: ''
      },
      address: {
          address: '',
          city: '',
          postal_code: '',
          address_type: ''
      },
    }
  },
  methods: {
    submit() {
      console.log(this.user);
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.user)
      };
      const addressRequestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.address)
      };
      fetch('http://127.0.0.1:8000/user', requestOptions)
          .then(response => response.json())
          .then(data => {
            const userId = data.id;

            console.log(userId, '\n');

      fetch('http://127.0.0.1:8000/user/' + userId + '/address', addressRequestOptions)
          .then(response => response.json())})
    }
  }
}
</script>